import socket
import ssl

HOST, PORT = "127.0.0.4", 1796
#################
SERVER_COMMON_NAME = 'example.com'
SERVER_CERT = 'server.crt'
CLIENT_CERT = 'client.crt'
CLIENT_KEY = 'client.key'
#################

try:
    ######################
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=SERVER_CERT)
    context.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = context.wrap_socket(s, server_side=False, server_hostname=SERVER_COMMON_NAME)
    ######################

    s.connect((HOST,PORT))

    print("Connected")

    value = input("Value: ")

    s.sendall(value.encode() + b'\r\n')

    result = b''
    while b'\r\n' not in result:
        result += s.recv(1)
    result = result.decode()[:-2]

    print(f"Result: {result}")

except socket.error:
    print("Error")
finally:
    s.close()
