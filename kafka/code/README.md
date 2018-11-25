# Kafka集群性能测试程序

## upstream

```
$ python upstream.py [-c INTEGER] [-l INTEGER] [-p INTEGER]
```

`-l` 每个消息的长度(Byte)

`-c` 一次测试中每个producer发送多少消息

`-p` producer的数量

这个程序会创建`p`个进程，每个进程创建一个producer，各向Kafka集群发送`c`个长度为`l`的消息，消息中包含发送时的时间戳。
所有消息发送完毕后，会输出统计信息，包括成功发送的消息数、总用时(s)、平均每秒发送消息数、平均每秒发送数据量(KB/s)

## downstream

```
$ python downstream.py [-c INTEGER] [-g INTEGER]
```

`-c` consumer的数量

`-g` consumer group的数量

这个程序会创建`c` x `g`个进程，每个进程创建一个consumer，从Kafka集群接收消息，记录下接收的第一个消息的时间和最后一个消息的时间，在使用者按下回车后结束并输出统计信息，包括收到的消息总数、收到的数据总大小(Byte)、收到所有消息的用时(s)、平均每秒接收的消息数、平均每秒接收的数据量(KB/s)、消息的平均长度(Byte)、每条消息收到距离发送的平均/最小/最大延迟(s)

## about me

Author: Shen Xiaozhou
Student ID: 5142609052
