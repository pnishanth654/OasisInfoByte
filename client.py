import socket
import threading

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send():
    while True:
        try:
            message = input("Type a message: ")
            client_socket.send(message.encode('utf-8'))
            if message.lower() == "quit":
                break
        except Exception as e:
            print(f"Error sending message: {e}")
            break

# Client configuration
HOST = '127.0.0.1'
PORT = 5555

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Get the username from the user
try:
    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))
except Exception as e:
    print(f"Error sending username: {e}")
    client_socket.close()

# Create threads for sending and receiving messages
receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

# Start the threads
receive_thread.start()
send_thread.start()