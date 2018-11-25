from __future__ import print_function
import sys
from random import randint
from datetime import datetime
from multiprocessing import Pool

import click
from pykafka import KafkaClient


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def routine(index, message_length, message_count):
    # create kafka client
    client = KafkaClient(hosts="172.17.0.7:21900,172.17.0.8:21900,172.17.0.9:21900")
    # select topic
    topic = client.topics['topic-p-12']

    # initialize stats
    succ = 0
    size = 0
    begin = datetime.utcnow()

    # get a producer and send messages
    with topic.get_sync_producer() as producer:
        for i in range(message_count):
            # message begining with a timestamp and filled by 'x' to message_length
            msg = '%30s' % datetime.utcnow().isoformat()
            msg += 'x' * ((randint(100, 100000) if message_length < 31 else message_length) - 30)
            try:  # send a message
                producer.produce(msg)
            except:  # fail
                pass
            else:  # success
                succ += 1
                size += len(msg)
            # display stats each 10% progress
            if i % (message_count / 10) == 0:
                eprint('[%d] %s -> %d / %d' % (index, begin, succ, message_count))
    end = datetime.utcnow()
    eprint('[%d] %s -> %d / %d -> %s' % (index, begin, succ, message_count, end))
    # return stats result
    return succ, size, begin, end


@click.command()
@click.option('--producers', '-p', default=1, help='Number of concurrent producer. Default 1')
@click.option('--message-length', '-l', default=0, help='Lenth of message, less than 31 for randint(100, 10000). Default 0')
@click.option('--message-count', '-c', default=100, help='How many messages to send. Default 100')
def main(producers, message_length, message_count):
    # create a process pool
    pool = Pool(producers)
    # run producers in different process
    res = [pool.apply_async(routine, (i, message_length, message_count)) for i in range(producers)]

    # do stats
    succ_total = 0
    size_total = 0
    very_begin = None
    very_end = None
    for r in res:
        succ, size, begin, end, = r.get()  # get stats from routines
        succ_total += succ
        size_total += size
        if very_begin is None or very_begin > begin:
            very_begin = begin
        if very_end is None or very_end < end:
            very_end = end

    # print test results
    print('Send messages (succ / total): %d / %d' % (succ_total, producers * message_count))
    if very_begin is not None and very_end is not None:
        duration = (very_end - very_begin).total_seconds()
        print('Time: %d s' % duration)
        print('Messages per second: %.2f' % (succ_total / duration))
        print('Data per second: %.2f KB/s' % (size_total / duration / 1024))


if __name__ == '__main__':
    main()
