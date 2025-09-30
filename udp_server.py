import socket

HOST, PORT = "", 53444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print("UDP server listening on port", PORT)

    data, addr = server.recvfrom(1024)
    print("Server got:", data.decode(errors="ignore"))

    server.sendto(b"Back at you UDP", addr)