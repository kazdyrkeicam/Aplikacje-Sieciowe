import socket as s

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.bind(('localhost', 1769))
sock.listen(5)

client, addr = sock.accept()
print("Polaczono: " + addr[0])

while True:
    data = b''
    while b'\r\n\r\n' not in data:
        data += client.recv(1)
    print(data.decode())

    client.close()
sock.close()