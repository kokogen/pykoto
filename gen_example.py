import select
import socket

to_read = {}
to_write = {}
generators = []

def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost',7000))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen()

    while True:
        print('server(): before yield')
        yield ('read', server_socket)
        client_socket, client_addr = server_socket.accept()
        print('Client from {} connected'.format(client_addr))
        generators.append(client(client_socket))



def client(client_socket):
    print('client(): before starting while')
    while True:
        print('client(): before first yield')
        yield ('read', client_socket)
        data = client_socket.recv(1024)
        if not data:
            break
        else:
            print('client(): before second yield')
            yield ('write', client_socket)
            client_socket.send(data.upper())
    client_socket.close()

def loop():
    print('loop(): before starting')
    while any([generators, to_read, to_write]):
        print('loop(): the next loop started')
        while not generators:
            print('loop(): generators is empty')
            ready_to_read, ready_to_write, _ = select.select(to_read, to_write, [], 0.2)
            print('loop(): after select')
            for sock in ready_to_read: generators.append(to_read.pop(sock))
            for sock in ready_to_write: generators.append(to_write.pop(sock))

        print(generators)
        print(to_read)
        print(to_write)

        try:
            gen = generators.pop(0)
            op, sock = next(gen)

            if op == 'read': to_read[sock] = gen
            if op == 'write': to_write[sock] = gen
        except StopIteration:
            print('Done')


generators.append(server())

loop()