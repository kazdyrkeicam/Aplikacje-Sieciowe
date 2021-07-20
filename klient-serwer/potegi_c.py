import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(('localhost', 1769))
    # while True:
    data = 'message'
    sock.send(data.encode('utf-8'))

    data = sock.recv(1024)
    if not data:
        pass
    print('Czas: ' + data.decode('utf-8'))
    sock.close()

except:
    print('Blad')