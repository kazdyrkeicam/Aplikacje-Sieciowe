import socket

serv = input()
addr = socket.gethostbyname(serv)

try:
for port in range(1,1025):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = sock.connect_ex((addr, port))
if res == 0:
print("PORT {}".format(port))
sock.close()

except socket.error:
print ("Couldn't connect to server")
