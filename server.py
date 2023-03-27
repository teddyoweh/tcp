import socket
import threading
import random
import string
from decorators import debug
from constants import SERVER_IP,SERVER_PORT
from datetime import datetime


class GameStruct:
    
    def __init__(self):
        self.games = {}
    @property
    def new_code(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(5))
 
    def create_room(self,user):
        new_code = self.new_code
        self.games[new_code] = {
            'room': new_code,
            'createdat':str(datetime.now()),
            'players': [
                    {
                    'ip':user[0],
                    'port':user[1]
                    }
            ],
            
        
        }
        return new_code
        
    

        
class TCPServer(GameStruct):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from client {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            if data.decode()=='CR1':
                client_socket.sendall(self.create_room(client_socket.getpeername()).encode())
            print(f"Received data from client {client_socket.getpeername()}: {data.decode()}")
            client_socket.sendall(data)
        client_socket.close()

    def stop(self):
        if self.server_socket:
            self.server_socket.close()

if __name__ == '__main__':
    server = TCPServer(SERVER_IP,SERVER_PORT)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()
    