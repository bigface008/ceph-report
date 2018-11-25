# Report of testing storage & network

- Author 汪喆昊
- Student ID 516030910460

这次作业里，沈小洲[部署](./report-of-setting-up-kafka.md)了 4 台服务器，服务器公网、
内网 ip 如下：

|         | 服务器 1   | 服务区 2   | 服务器 3   | 服务器 4    |
| ------- | ---------- | ---------- | ---------- | ----------- |
| 内网 ip | 172.17.0.7 | 172.17.0.8 | 172.17.0.9 | 172.17.0.10 |

服务器 1-3 上分别部署了 1 个 zookeeper 实例和 1 个 kafka broker 实例，剩下的一台部署
了 consumer，producer。以下测试均在内网进行。

## Network

参考了[腾讯云的网络性能测试文档](https://cloud.tencent.com/document/product/213/11460)

首先安装 iperf3

```shell
$ sudo apt-get install iperf3
```

### 带宽测试

首先需要一台陪练机向测试机发送信息
测试机

```shell
$ iperf3 -s
```

陪练机

```shell
$ iperf3 -c ${服务器IP地址} -b 2G -t 300 -P ${网卡队列数目}
```

例如

    $ iperf3 -c 10.0.0.1 -b 2G -t 300 -P 8

某次测试的结果（作为证明）

![iperf result](./image/kafka-01.png)

针对本次作业，使用 iperf3，在服务器之间发送数据，测量相应带宽。测试结果如下

|          | 服务器 1  | 服务器 2  | 服务器 3  | 服务器 4  |
| -------- | --------- | --------- | --------- | --------- |
| 服务器 1 | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps |
| 服务器 2 | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps |
| 服务器 3 | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps |
| 服务器 4 | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps | 1.54 Gbps |

由此可大致推测带宽为 **1.54 Gbps**。

### 网络延迟测试

|                      | ping 值 |
| -------------------- | ------- |
| 服务器 1 到 服务器 2 | 0.229 ms |
| 服务器 2 到 服务器 3 | 0.236 ms |
| 服务器 3 到 服务器 1 | 0.238 ms |
| 服务器 4 到 服务器 1 | 0.238 ms |
| 服务器 4 到 服务器 2 | 0.242 ms |
| 服务器 4 到 服务器 3 | 0.240 ms |

## Storage

首先了解两个伪设备

- /dev/null 伪设备，回收站.写该文件不会产生 IO
- /dev/zero 伪设备，会产生空字符流，对它不会产生 IO

可以使用如下命令测试硬盘写速度(表示 每次写入 8k 的数据，执行 300000 次)

```shell
$ time dd if=/dev/zero of=test.dbf bs=8k count=300000 oflag=direct
```

使用如下命令测试硬盘读速度(表示 每次读取 8k 的数据，执行 300000 次)

```shell
$ dd if=test.dbf bs=8k count=300000 of=/dev/null
```

也可以使用`hdparm`命令来测试

```shell
$ hdparm -Tt /dev/sda
```

某次测试的证明

![hdparm result](./image/kafka-00.png)

测试结果如下

|                | 服务器 1        | 服务器 2       | 服务器 3        |
| -------------- | --------------- | -------------- | --------------- |
| Cached Reads   | 10398.03 MB/sec | 9627.82 MB/sec | 10375.77 MB/sec |
| Buffered Reads | 112.10 MB/sec   | 92.72 MB/sec   | 119.96 MB/sec   |

以上。
