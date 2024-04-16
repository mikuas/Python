"""
客户端
"""

import socket

# 创建socket对象
socket_client = socket.socket()
# 连接到服务器
socket_client.connect(('localhost', 8888))
# 发送消息
# 可通过无限循环保持持续发送消息个服务器
while True:

    send_msg = input('请输入要发送的信息')
    if send_msg == 'exit':
        # 通过特殊标记退出无限循环
        break
    # 消息需要为字节数组(utf8编码)
    socket_client.send(send_msg.encode('utf-8'))
    # 接收返回消息
    recv_data = socket_client.recv(1024)        # 1024是缓冲区大小,一般1024即可
    # recv方法是阻塞的,即不接收到返回消息,就卡在这里等待
    if recv_data.decode('utf-8') == 'exit':
        break
    print(f'服务端回复消息为:{recv_data.decode('utf-8')}')  # 接收的消息需要通过utf-8解码为字符串

# 关闭链接
socket_client.close()






