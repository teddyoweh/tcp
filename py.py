import socket
import threading

# function to handle incoming messages
def handle_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            print(data)
        except:
            break

# get user input and send to other client
def send_messages(sock):
    while True:
        message = input()
        sock.sendall(message.encode())

# create socket and connect to other client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8000))

# start threads to handle incoming messages and send messages
receive_thread = threading.Thread(target=handle_messages, args=(sock,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(sock,))
send_thread.start()

# wait for threads to finish (should never happen)
receive_thread.join()
send_thread.join()

# close socket
sock.close()
