import socket
import _thread

HOST, PORT = 'localhost', 1772

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (fib(n-1)+fib(n-2))

def one_client(client):
    data = b''
    while b'\r\n\r\n' not in data:
        data += client.recv(1)
    data = data.decode()[:-4]

    response = (str(fib(int(data))) + '\r\n\r\n').encode()
    client.sendall(response)
    client.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    client, addr = s.accept()
    print("Connected: " + addr[0])
    _thread.start_new_thread(one_client, (client, ))

s.close()