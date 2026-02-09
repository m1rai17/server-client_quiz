import socket

HOST = "127.0.0.1"
PORT = 9999

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

while True:
    data = c.recv(1024).decode()
    if not data:
        break

    print(data, end="")

    if "Your answer (true/false):" in data:
        answer = input()  
        c.send(answer.encode())

c.close()