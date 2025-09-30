import socket

HOST, PORT = "127.0.0.1", 53444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    message = b"Hello UDP"
    print("Sending:", message.decode())
    sock.sendto(message, (HOST, PORT))

    data, _ = sock.recvfrom(1024)
    print("Received:", data.decode())