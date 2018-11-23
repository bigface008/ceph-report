# Report of setting up Kafka
- Author 汪喆昊
- Student ID 516030910460

搭建Kafka最便捷的方式是使用已经打包好的[kafka-docker](https://github.com/wurstmeister/kafka-docker)。
步骤如下：
## Install Docker
这没啥好说的。
## Install Docker-compose
在shell中执行代码。
```shell
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```
通过以上代码安装docker-compose。
## CLone repo
执行如下代码以克隆仓库
```shell
$ git clone git@github.com:wurstmeister/kafka-docker.git
```
## Run Kafka
### Start a cluster
    $ docker-compose up -d
### Add brokers
    $ docker-compose scale kafka=3
### Destroy a cluster
    $ docker-compose stop

## Set arguments
根据需要在docker-compose.yml中修改相关的变量。不过开始用原来的文件貌似也没啥问题。
通过命令`docker-compose -f {filename} up`来指定相应的的配置文件名。相关的详细信息参见
[文档](https://docs.docker.com/compose/compose-file/)。
