from config import get_constants

class AirTrafficControlServer:
    def __init__(self, host=None, port=None):
        constants = get_constants()
        self.host = constants['HOST']
        self.port = constants['PORT']


    async def start_server(self):
        pass

    async def accept_connections(self):
        pass

    async def handle_client(self, client_socket, client_address):
        pass
