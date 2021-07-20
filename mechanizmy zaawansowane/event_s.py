import socket
import select
import _thread as thr
import queue


def fib_thr(n, socket):
    result = fib(n)
    outputs.append(socket)
    output_queue[socket].put(result)

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (fib(n-1)+fib(n-2))

HOST, PORT = 'localhost', 1796

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

inputs = [sock]
outputs = []

output_queue = {}

print("Server running...")

while True:
    input, output, error = select.select(inputs, outputs, [], 0)

    for current in input:

        if current is sock:
            client, addr = sock.accept()
            print("Connected: " + addr[0])

            inputs.append(client)

            output_queue[client] = queue.Queue()

        else:
            data = b''
            while b'\r\n' not in data:
                data += current.recv(1)
            data = data.decode()[:-2]

            thr.start_new_thread(fib_thr, (int(data), current))

    for current in output:
        if not output_queue[current].empty():
            result = output_queue[current].get_nowait()

            current.sendall(str(result).encode() + b'\r\n')

            if current in inputs:
                inputs.remove(current)
            if current in outputs:
                outputs.remove(current)

            current.close()
sock.close()
