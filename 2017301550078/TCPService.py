from socket import * 

serverPort=12000 
serverSocket=socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1) 
while True:
    connSocket,addr = serverSocket.accept()
    sentence = connSocket.recv(1024).decode()
    print(sentence)
    msg = 'HTTP/1.1 200 OK\n\rContent-Type: text/html\n\r\n\r<h1>hello<h1>\n\r'
    connSocket.send(msg.encode())
    connSocket.close()