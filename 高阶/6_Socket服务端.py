"""
socket

"""

import socket

# 1.创建socket对象
socket_server = socket.socket()

# 2.绑定socket_server到指定IP和地址
"""socket_server.bind((host, port))"""
socket_server.bind(('localhost', 8888))

# 3.服务端开始监听端口
socket_server.listen()  # listen()中类型为整数,表示允许连接数量,超出的会等待,可以不填,不填自动设置一个合理值

# 4.接收客户端连接,获得连接对象
conn, address = socket_server.accept()      # return: tuple
"""conn 客户端和服务器的连接对象        address 客户端的地址信息"""
print(f'接收到了客户端的连接,客户端的信息是:{address}')
# accept方法是阻塞方法,如果没有连接,会卡在当前这一行不向下执行代码
# accept返回的是一个二元元组,可以使用上述形式,用2个变量接收二元元组的2个元素

# 5.客户端连接后,通过recv方法,接收客户端发送的消息
# 可以通过while True无限循环来持续和客户端进行数据交互
while True:
    data: str = conn.recv(1024).decode('UTF-8')
    # recv方法的返回值是字节数组(Bytes),可以通过decode使用UTF-8解码为字符串
    # recv方法的传参是buffsize,缓冲区大小,一般设置为1024即可

# 可以通过判定客户端发来的特殊标记,如exit,来退出无限循环
    if data == 'exit':
        break

    print(f'接收到发来的数据:{data}')
    # 回复客户端
    msg = input('请输入回复信息:').encode('UTF-8')     # encode可以将字符串编码为字符数组对象
# 6.通过conn(客户端当此连接对象),调用send方法可以回复消息
    conn.send(msg)

# 7.conn(客户端当此连接对象)和socket_server对象调用close方法,关闭连接
conn.close()
# 整体停止
socket_server.close()









