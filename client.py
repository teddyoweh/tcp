import socket
import hashlib
def main():
    host = "127.0.0.1"
    port = 7007

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ")
    message=  hashlib.md5(message.encode()).hexdigest()
    print(message)
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print("Received from server: " + data)
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    main()
