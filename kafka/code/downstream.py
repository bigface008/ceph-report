from __future__ import print_function
import sys
from random import randint
from datetime import datetime, timedelta
from dateutil import parser
from time import sleep
from Queue import Empty
from multiprocessing import Pool, Queue, Manager

import click
from pykafka import KafkaClient
from pykafka.common import OffsetType


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def routine(group, index, q):
    # create kafka client
    client = KafkaClient(hosts='172.17.0.7:21900,172.17.0.8:21900,172.17.0.9:21900')
    # select topic
    topic = client.topics['topic-p-12']

    # create a consumer from given group
    consumer = topic.get_balanced_consumer(
        consumer_group='group-%d' % group,
        auto_commit_enable=True,
        zookeeper_connect='172.17.0.7:21800,172.17.0.8:21800,172.17.0.9:21800',
        auto_offset_reset=OffsetType.LATEST,
        reset_offset_on_start=True
    )

    # initialize stats
    begin = None
    end = None
    latency = 0
    count = 0
    size = 0
    min_latency = 999999999
    max_latency = -1

    # timer for display infos every 5 seconds
    timer = datetime.utcnow()
    while True:
        try:
            msg = consumer.consume(block=False)  # try to get a message
        except (SocketDisconnectedError, NoBrokersAvailableError) as e:
            # reconnect
            consumer = topic.get_balanced_consumer(
                consumer_group='mytestgroup',
                auto_commit_enable=True,
                zookeeper_connect='172.17.0.7:21800,172.17.0.8:21800,172.17.0.9:21800'
            )
        except Empty:
            sleep(0.01)
        else:
            if msg is not None:  # got a message
                t_s = len(msg.value)  # size of this message
                try:
                    # get timestamp from the message and calc the latency between send and recv
                    t_l = (datetime.utcnow() - parser.parse(msg.value[:30])).total_seconds()
                except:  # wrong message format
                    import traceback
                    eprint(traceback.format_exc())
                else:
                    latency += t_l  # total latency
                    if min_latency > t_l:  # min_latency
                        min_latency = t_l
                    if max_latency < t_l:
                        max_latency = t_l
                size += t_s  # total size
                count += 1  # count messages

                if begin is None:  # when get the first message
                    begin = datetime.utcnow()
                end = datetime.utcnow()  # when get the last message
            else:
                sleep(0.01)

        # display infos per 5 seconds
        if datetime.utcnow() - timer > timedelta(seconds=5):
            timer = datetime.utcnow()
            eprint('[%d-%d] %5d %10d | %s -> %s | %.3f <%.3f> %.3f' % (
                group, index,
                count, size,
                begin, end,
                min_latency,
                (-1 if begin is None or end is None else latency / (end - begin).total_seconds()),
                max_latency
            ))

        try:
            # quit when get anything from q
            q.get(block=False)
            # return stats result
            return (
                count, size,
                begin, end,
                latency, min_latency, max_latency
            )
        except Empty:
            pass


@click.command()
@click.option('--consumers', '-c', default=1, help='Number of consumers in each group')
@click.option('--groups', '-g', default=1, help='Number of consumer groups')
def main(consumers, groups):
    # create a process pool
    pool = Pool(consumers * groups)
    # create queues for each process to notify them quiting
    m = Manager()
    qs = [[m.Queue() for c in range(consumers)] for g in range(groups)]
    # run consumers
    res = [[pool.apply_async(routine, (g, c, qs[g][c])) for c in range(consumers)] for g in range(groups)]

    eprint('Press enter to stop...')
    raw_input()

    # notify all process to quit
    for qsg in qs:
        for qc in qsg:
            qc.put('something')

    # initialize stats
    count_total = 0
    size_total = 0
    very_begin = None
    very_end = None
    latency_total = 0
    min_latency = 999999999
    max_latency = -1

    eprint('Waiting for consumers returning...')
    # do stats
    for rg in res:
        for rc in rg:
            count, size, begin, end, latency, min_l, max_l = rc.get()
            count_total += count
            size_total += size
            if very_begin is None or (begin is not None and begin < very_begin):
                very_begin = begin
            if very_end is None or (end is not None and end > very_end):
                very_end = end
            latency_total += latency
            if min_l < min_latency:
                min_latency = min_l
            if max_l > max_latency:
                max_latency = max_l

    # print test results
    print('Total messages: %d' % count_total)
    print('Total size: %d bytes' % size_total)
    if very_begin is not None and very_end is not None:
        duration = (very_end - very_begin).total_seconds()
        print('Total time: %.3f s' % duration)
        print('Messages per second: %.2f' % (count_total / duration))
        print('Data per second: %.2f KB/s' % (size_total / duration / 1024))
    if count_total > 0:
        print('Average size: %d bytes' % int(size_total / count_total))
        print('Average latency: %.3f s' % (latency_total / count_total))
    if min_latency < 999999999:
        print('Min latency: %.3f s' % min_latency)
    if max_latency > 0:
        print('Max latency: %.3f s' % max_latency)


if __name__ == '__main__':
    main()
