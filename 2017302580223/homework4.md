## 1. `nslookup www.whu.edu.cn`

![1585237173804](homework4/1585237173804.png)

## 2. 作业题

- **P11**

![1585238568909](homework4/1585238568909.png)

~~~
a)是，因为连接数更多，所以链路带宽份额更大
b)是，Bob仍然需要执行并行下载；否则，他将获得比其他四个用户更少的带宽
~~~

- **P12**

![1585237328576](homework4/1585237328576.png)

~~~py
from socket import *
port=12000
server=socket(AF_INET,SOCK_STREAM)
server.bind('',port)
server.listen(1)
while True:
	conn,addr=socket.accept()
	message=server.recv(1024).decode()
	print(message)
~~~

- **P20**

![1585239585348](homework4/1585239585348.png)

~~~
可以定期拍摄本地DNS服务器中DNS缓存的快照，在DNS缓存中出现最频繁的Web服务器就是最流行的服务器。因为如果更多的用户对Web服务器感兴趣，那么DNS请求就会对此感兴趣服务器更频繁地由用户发送。
~~~

