import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

request = 'GET /html HTTP/1.1'
host, port = 'www.httpbin.org', 80
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A)'
msg = request + '\r\n' + 'Host: ' + host + '\r\n' + 'User-Agent: ' + agent + '\r\n\r\n'

s.connect((host, port))
s.sendall(msg.encode())

header = b''
content = b''

while b'\r\n\r\n' not in header:
    header += s.recv(1)

ContentLength = int((header.split(b'Content-Length:')[1]).split(b'\r\n')[0][1:])

while len(content) < ContentLength:
    content += s.recv(1)

with open('index.html', 'bw') as file:
    file.write(content)
    file.close()

s.close()