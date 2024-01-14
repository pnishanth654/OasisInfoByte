import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == "quit":
                print(f"{username} has left the chat.")
                broadcast(f"{username} has left the chat.", client_socket)
                remove_client(client_socket)
                break
            print(f"{username}: {message}")
            # broadcast(f"{username}: {message}", client_socket)  # Comment out this line
        except Exception as e:
            print(f"Error handling client {username}: {e}")
            remove_client(client_socket)
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting to a client: {e}")
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def server_broadcast():
    while True:
        message = input("User: ")
        target_username = input("Target username: ")
        target_client = find_client_by_username(target_username)
        if target_client:
            target_client.send(f"Server: {message}".encode('utf-8'))
        else:
            print(f"User {target_username} not found.")

def find_client_by_username(username):
    for client_socket, client_username in connected_clients.items():
        if client_username == username:
            return client_socket
    return None

# Server configuration
HOST = '127.0.0.1'
PORT = 5555

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []
connected_clients = {}  # Keep track of connected clients and their usernames

print(f"Server listening on {HOST}:{PORT}")

# Start the server_broadcast thread
broadcast_thread = threading.Thread(target=server_broadcast)
broadcast_thread.start()

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Get the username from the client
    username = client_socket.recv(1024).decode('utf-8')
    clients.append(client_socket)
    connected_clients[client_socket] = username  # Store the client socket and username

    # Broadcast the new user joining
    broadcast(f"{username} has joined the chat.", client_socket)

    # Create a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()