import socket

def main():
    host = "127.0.0.1"
    port = 7007

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("[*] Listening on %s:%d" % (host, port))
    conn, addr = s.accept()
    print("[*] Connection from: %s:%d" % (addr[0], addr[1]))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("[*] Received: %s" % data)
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    main()
