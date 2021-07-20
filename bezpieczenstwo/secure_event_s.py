import socket
import select
import _thread as thr
import queue

import ssl


def fibbo_thr(n, socket):
    result = fibbo(n)
    outputs.append(socket)
    socket_output_queue[socket].put(result)

def fibbo(n):
    if n <= 1:
        return n
    else:
        return (fibbo(n-1) + fibbo(n-2))


HOST, PORT = '127.0.0.4', 1796

########################################
SERVER_CERT = 'server.crt'
SERVER_KEY = 'server.key'
CLIENT_CERT = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=SERVER_CERT, keyfile=SERVER_KEY)
context.load_verify_locations(cafile=CLIENT_CERT)

########################################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

# list of sockets to watch input and output events
inputs = [s]
outputs = []

# socket output map socket -> queue
socket_output_queue = {}

print("Server running...")

try:
    while True:
        i, o, e = select.select(inputs, outputs, [], 0)

        # check for input sockets ready
        for curr_socket in i:
            # input socket is s (server) - accept new client
            if curr_socket is s:
                client, addr = s.accept()
                print("Connected: " + addr[0])

############################
                client = context.wrap_socket(client, server_side=True)
############################
                inputs.append(client)

                # create output queue
                socket_output_queue[client] = queue.Queue()
            # input socket is not s - any client sent data
            else:
                # receive number
                data = b''
                while b'\r\n' not in data:
                    data += curr_socket.recv(1)
                data = data.decode()[:-2]

                thr.start_new_thread(fibbo_thr, (int(data),curr_socket))

        # check for output sockets ready
        for curr_socket in o:
            if not socket_output_queue[curr_socket].empty():
                result = socket_output_queue[curr_socket].get_nowait()
                curr_socket.sendall(str(result).encode() + b'\r\n')

                if curr_socket in inputs:
                    inputs.remove(curr_socket)

                if curr_socket in outputs:
                    outputs.remove(curr_socket)

                curr_socket.close()
except socket.error:
    print("Error")
finally:
    s.close()
