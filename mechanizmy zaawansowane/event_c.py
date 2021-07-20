import socket

HOST, PORT = "127.0.0.4", 1796

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

value = input("Value: ")

sock.sendall(value.encode() + b'\r\n')

result = b''
while b'\r\n' not in result:
    result += sock.recv(1)
result = result.decode()[:-2]

print(f"Result: {result}")

sock.close()