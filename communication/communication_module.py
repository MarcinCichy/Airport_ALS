class AirTrafficControlServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port


    async def start_server(self):
        pass

    async def accept_connections(self):
        pass

    async def handle_client(self, client_socket, client_address):
        pass
