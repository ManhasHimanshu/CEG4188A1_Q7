import socket

HOST, PORT = "127.0.0.1", 53333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    message = b"Hello TCP"

    print("Sending:", message.decode())
    sock.sendall(message)

    reply = sock.recv(1024)
    print("Received:", reply.decode())
