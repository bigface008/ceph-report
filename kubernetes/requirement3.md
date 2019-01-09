# Rquirement 3

沈小洲 5142609052

## Abstract

利用[Report of Requirement 1](./kubernetes/requirement1.md)中搭建的 CI/CD 环境，为Webapp编写`.drone.yml`文件，
通过编写`Dockerfile`在该步骤自动地构建docker镜像

利用[Report of Requirement 2](./kubernetes/requirement2.md)中搭建的Kubernetes，编写`depl.yml`并用 kubectl 命令部署

## Development (Webapp)

最简易的python flask应用 helloworld:
```python
#!/usr/bin/python
#coding: utf-8

import flask
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
    return 'Hello world!'

def main():
    app.run(host='0.0.0.0', port='8000')

if __name__ == '__main__':
    main()
```

## CI/CD

编写`Dockerfile`，基于python镜像，安装flask环境，在entrypoint处运行app:
```
FROM python:2.7
MAINTAINER shenxiaozhou
RUN pip install flask
ENTRYPOINT python main.py
```

在`.drone.yml`中加入publish，构建docker镜像并发布:
```yaml
pipeline:
  ...
  publish:
    image: plugins/docker
    repo: webapp/helloworld
    tags: ${DRONE_TAG=latest}
    dockerfile: Dockerfile
```

自此每个commit被push到github上之后，drone会自动地根据dockerfile构建一个docker镜像，并发布到webapp/helloworld这个repo中

## Deployment

在上一步drone流水线最终将构建的镜像发布到webapp/helloworld上，编写如下`depl.yml`:
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: helloworld-deployment
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: helloworld
    spec:
      containers:
        - name: helloworld
          image: webapp/helloworld:latest
          ports:
            - containerPort: 8000
```

执行
```bash
kubectl apply -f depl.yml
```

就可以将helloworld部署到Kubenetes中
