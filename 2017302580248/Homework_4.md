nslookup www.whu.edu.cn

Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>nslookup www.whu.edu.cn
服务器:  UnKnown
Address:  192.168.3.1

非权威应答:
名称:    www.whu.edu.cn
Addresses:  2001:250:4001:1::1001
          202.114.64.200

P23

a. Suppose that the server sends the F-bit file to the clients in parallel, and the sending rate is u_s/N. at the same time, the client is also downloading the file. Because u_s/N<=d_min. so clients can download files at u_s/N rate. Time spent is t = F/(u_s/N) = NF/u_s

b. Suppose that the server sends the F-bit file to the clients in parallel. at the same time, the client is also downloading the file at rate d_min. Because u_s/N>=d_min. so server can send files at d_min rate. Time spent is t = F/d_min.

c. from a and b we can get:
if u_s/N<=d_min then NF/u_s>=F/d_min so t=NF/u_s
if u_s/N>=d_min then NF/u_s<=F/d_min so t=F/d_min
combine the two conditions we can get the conclusion:
Minimum distribution time:
t = max{F/d_min,NF/u_s}



P29: Answer

It is not necessary to change UDPServer.py.

For  socket in UDPClient,  port number is 5432. 

For  socket in UDPServer,  port numbers is 12000.

port number for UDPClient is unknown and  port number for UDPServer is 12000.