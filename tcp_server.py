import socket
class WebServer():
   def __init__(self):
      self.tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      self.tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
      self.tcp_server_socket.bind(('',8080))
      self.tcp_server_socket.listen(128)

   def client_request_handler(self,new_socket,port_ip):
      data=new_socket.recv(1024).decode('utf-8')
      datalist=data.split(" ")
      path=datalist[1]
      print(f' we\'re visiting: {path}')
      if path=='/':
         path='/index.html'
      line='HTTP/1.1 200 ok\r\n'
      header='Server: laura\'s server \r\n'
      with open ('html'+path,'rb') as f:
         body= f.read()
      respond=(line+header+'\r\n' ).encode('utf-8')+body
      new_socket.send(respond)
      # new_socket.close()

   def start(self):
      while True:
         new_socket,port_ip = self.tcp_server_socket.accept()
         self.client_request_handler(new_socket,port_ip)
if __name__ == '__main__':
   ws=WebServer()
   ws.start()
