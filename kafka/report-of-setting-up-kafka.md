# Report of setting up Kafka
- Author 汪喆昊
- Student ID 516030910460

搭建Kafka最便捷的方式是使用已经打包好的docker。
步骤如下：
### Install docker-compose
在shell中执行代码

    $ sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    $ sudo chmod +x /usr/local/bin/docker-compose
通过以上代码安装docker-compose。
### Modify arguments
根据需要修改
