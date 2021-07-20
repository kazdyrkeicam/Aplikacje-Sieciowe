import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(('localhost', 1769))
    # while True:
    data = 'policja\r\n\r\n'

    sock.send(data.encode())
    sock.close()

except:
    print('Blad')