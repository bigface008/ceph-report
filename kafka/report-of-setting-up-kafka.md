# Report of setting up Kafka
- Author 汪喆昊
- Student ID 516030910460

搭建Kafka最便捷的方式是使用已经打包好的[kafka-docker](https://github.com/wurstmeister/kafka-docker)。
步骤如下：
## Install Docker
这没啥好说的。
## Pull Images
下载zookeeper镜像

    sudo docker pull wurstmeister/zookeeper
下载Kafka镜像

    sudo docker pull wurstmeister/kafka
## Install Docker-compose
在shell中执行代码。
```shell
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```
通过以上代码安装docker-compose。
## CLone repo
执行如下代码以克隆仓库，并且进入相应文件夹。
```shell
$ git clone git@github.com:wurstmeister/kafka-docker.git
$ cd kafka-docker
```
## Set arguments
在kafka-docker文件夹内打开文件docker-compose.yml，将**KAFKA_ADVERTISED_HOST_NAME**
修改为自己机器的ip地址。
似乎可以通过命令`docker-compose -f {filename} up`来指定配置文件名。相关的详细信息参见
[文档](https://docs.docker.com/compose/compose-file/)。
## Run Kafka
### Start a cluster
    $ sudo docker-compose up -d
### Add brokers
    $ sudo docker-compose scale kafka=3
### Destroy a cluster
    $ sudo docker-compose stop
## Test Kafka
### Enter docker
使用`sudo docker ps`查看开启的container的列表，选择一个Kafka容器*containter_name*进入：
```shell
$ sudo docker exec -it ${container_name} /bin/bash
$ cd $KAFKA_HOME/bin
```
### Create topic
创建名为test的topic，指定备份数1，分区数1。
```shell
$ ./kafka-topics.sh --create --topic test --zookeeper ${container_name}:2181 --replication-factor 1 --partitions 1
```
### Describe topic
```shell
$ ./kafka-topics.sh --zookeeper ${container_name}:2181 --describe --topic test
```
### Receive topic
```shell
$ kafka-console-consumer.sh --bootstrap-server wurkafka_kafka_1:9092 --from-beginning --topic test
```
以上。