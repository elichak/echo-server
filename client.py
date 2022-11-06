import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 1234))
print('Соединение установлено!')
sock.send('hello, world!'.encode('utf-8'))
print('Сообщение \n hello, world! \n отправлено!')
data = sock.recv(1024)
sock.close()

print(data)
print('Соединение закрыто!')
