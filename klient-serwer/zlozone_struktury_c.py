import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(('localhost', 1769))
    # while True:
    data = (5.5, 'text', 5)
    sock.send(pickle.dumps(data))

    data = sock.recv(1024)
    if not data:
        pass
    print(data.decode('utf-8'))
    sock.close()

except:
    print('Blad')