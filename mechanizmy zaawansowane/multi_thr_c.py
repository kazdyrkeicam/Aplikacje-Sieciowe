import socket

HOST, PORT = 'localhost', 1772

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

print("Input value: ")
number = input()

s.sendall(number.encode() + b'\r\n\r\n')

data = b''
while b'\r\n\r\n' not in data:
    data += s.recv(1)
data = data.decode()[:-4]

print("Fibb: " + data)

s.close()