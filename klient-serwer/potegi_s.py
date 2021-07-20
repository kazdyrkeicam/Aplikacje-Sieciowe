import socket as s
import datetime

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.bind(('localhost', 1769))
sock.listen(5)

# while True:
client, addr = sock.accept()
print("Polaczono: " + addr[0])

while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))

    client.send(str(datetime.datetime.now()).encode('utf-8'))
client.close()
sock.close()