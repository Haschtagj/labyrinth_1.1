def main():
    server = Server().accept()
    data = server.recv(1024)
    # server.close()
    server_socket = options[data]
    if isinstance(server_socket, str):
        pass
    elif server_socket == options["Game"]:
        server_socket = server_socket()
        server_started = True
        while server_started:
            server_socket.open_to()
            server_socket.accept()
            data = server_socket.recv()
            server_socket.send('5/5')
        server.close()


def main():
    om = OptionsMenu()
    print(om)
    index = om.set_option()
    client = Client()
    client.connect()
    data = om.get_option(index)
    client.send(data)
    client.close()
    time.sleep(0.5)
    server = om.options[data]
    server = server()
    server.connect()
    connected = True
    while connected:
        data = input('>_ ')
        server.send(data)
        if data == '':
            connected = False
        server.recv()
