import socket

if __name__ == '__main__':
    tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client_socket.connect(('127.0.0.1',8000))
    tcp_client_socket.send('hello'.encode(encoding='gbk'))

    content= tcp_client_socket.recv(1024).decode('gbk')
    print(f'server return msg is : {content}')
    tcp_client_socket.close()

