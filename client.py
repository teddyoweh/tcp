import socket
import threading
from constants import SERVER_IP,SERVER_PORT,CODES


CHOOSE_GAME = '''
=========================

[1] - Create New Room
[2] - Join Room

=========================
'''



class Errors:
    def __init(self):
        pass
    def validate_cg_inpt(self,input):
        if input not in ['1', '2']:
            print('Invalid Choice')
            return False
        else:
            return True
class Room():
    def __init__(self,client):
        self.client = client

    def create(self):
        print("Creating New Room")
        self.client.send_data(CODES['CREATE_ROOM'])
        received_data = self.client.receive_data()
        print(f"Received data from server: {received_data}")
        self.room_code = received_data
    def join(self):
        print("Joining Room")
        code = input('Enter Room Code: ')
        self.client.send_data(f"{CODES['JOIN_ROOM']} {code}")


    


class Game(Errors):
   
    def __init__(self,client):
        self.client= client
        super().__init__()
        self.started = False
        print(CHOOSE_GAME)
        self.room = Room(client)
        cg_inpt = input(">>> ")
        if(self.validate_cg_inpt(cg_inpt)):
            self.started = True
            if(cg_inpt=='1'):
                self.create_new_room()
            elif(cg_inpt=='2'):
                self.join_room()
    def create_new_room(self):
        self.room.create()
    def join_room(self):
        self.room.create()


        
        
        

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server {self.host}:{self.port}")

    def send_data(self, data):
        self.client_socket.sendall(data.encode())

    def receive_data(self):
        return self.client_socket.recv(1024).decode()

    def disconnect(self):
        if self.client_socket:
            self.client_socket.close()

if __name__ == '__main__':
 

    client = TCPClient(SERVER_IP,SERVER_PORT)
    client.connect()

    while True:
        game = Game(client)
        # data = input("Enter data to send to server: ")
        # client.send_data(data)
        # received_data = client.receive_data()
        # print(f"Received data from server: {received_data}")

TCPClient()