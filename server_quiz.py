import socket
import random

HOST = "127.0.0.1"
PORT = 9999

# questions, right answer
questions = [
    ("Congestion collapse means that the network improves throughput as load increases. (true/false)", "false"),
    ("TCP slow start increases the congestion window exponentially. (true/false)", "true"),
    ("During TCP congestion avoidance, the congestion window grows exponentially. (true/false)", "false"),
    ("In fast recovery, TCP immediately enters slow start after duplicate ACKs. (true/false)", "false"),
    ("The transport layer provides communication between applications, while the network layer provides host-to-host delivery. (true/false)", "true"),
    ("Forwarding and routing are two key network layer functions. (true/false)", "true"),
    ("The transport layer determines the physical path packets take through the network. (true/false)", "false"),
    ("FIFO, priority scheduling, and round-robin are examples of scheduling policies. (true/false)", "true"),
    ("IP fragment reassembly is performed only at the final destination host. (true/false)", "true"),
    ("A subnet consists of hosts that share the same network prefix. (true/false)", "true"),
    ("NAT allows multiple devices to share a single public IP address. (true/false)", "true"),
    ("Subnetting increases the number of required public IP addresses. (true/false)", "false"),
    ("In decentralized routing, routers use only neighbor information. (true/false)", "true"),
    ("A distributed routing algorithm works without any information exchange. (true/false)", "false"),
    ("Link-state routing requires routers to have a full map of the network. (true/false)", "true"),
    ("Distance-vector routing usually converges faster than link-state. (true/false)", "false"),
    ("UDP provides no retransmission or recovery of lost packets. (true/false)", "true")
]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Server is listening...")

while True:
    communication_socket, address = server.accept()
    print(f"Connected with: {address}\n")
    score = 0
    total = len(questions)
    # random order of questions
    quiz_questions = questions[:]
    random.shuffle(quiz_questions)

    communication_socket.send(
        f"Welcome to the Quiz! There are {total} questions.\n".encode()
    )

    for index, (question, correct_answer) in enumerate(quiz_questions, start=1):
        q_text = f"Q{index}: {question}\nYour answer (true/false): "
        communication_socket.send(q_text.encode())
        # answer from client
        answer = communication_socket.recv(1024).decode().strip().lower()
        correct_answer = correct_answer.strip().lower()

        if answer == correct_answer:
            score += 1
            feedback = "Correct!\n\n"
        else:
            feedback = f"Incorrect. The correct answer is {correct_answer}.\n\n"

        communication_socket.send(feedback.encode())

    # final score
    result = f"Quiz finished! Your score: {score} / {total}\n"
    communication_socket.send(result.encode())

    communication_socket.close()
    print(f"Connection with {address} ended.\n")
