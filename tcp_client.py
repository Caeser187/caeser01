"""
    tcp_
"""

from socket import *

while True:
    #  创建套接字
    sockfd = socket(AF_INET, SOCK_STREAM)  # 默认参数就还是tcp

    # 链接服务端程序
    # server_addr = ("172.40.91.205", 8888)
    server_addr = ("127.0.0.1", 8888)
    sockfd.connect(server_addr)
    while True:
        data = input(">>")
        sockfd.send(data.encode())
        if data == "**":
            break
        msg = sockfd.recv(1024)
        print("Server:", msg)

    sockfd.close()
