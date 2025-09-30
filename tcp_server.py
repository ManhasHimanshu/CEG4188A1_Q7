import socket

HOST, PORT = "", 53333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print("TCP server listening on port", PORT)

    conn, addr = server.accept()
    with conn:
        print("Connection from:", addr)
        data = conn.recv(1024)
        print("Server got:", data.decode(errors="ignore"))

        conn.sendall(b"Back at you TCP")