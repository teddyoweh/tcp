import socket
import argparse
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
 
def main(dir):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
 
    client.connect(ADDR)
    parser = argparse.ArgumentParser(description="File server")
    parser.add_argument("action", help="Action to perform", choices=["add", "list", "fetch"])
    parser.add_argument("file", help="Name of the file to add/fetch")
    args = parser.parse_args()
    print(args.file)
    if args.action == "add":
        file = open(dir, "r")
        data = file.read()
        client.send(dir.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        file.close()
    
        """ Closing the connection from the server. """
        client.close()
 
 
if __name__ == "__main__":
    main('client.py')
 