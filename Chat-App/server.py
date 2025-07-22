
import socket
import threading

HOST = '127.0.0.1'
PORT = 12350  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = {}

print("🚀 Server is running...")

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                client.close()
                remove(client)

def remove(client):
    if client in clients:
        clients.remove(client)

def handle_client(client):
    try:
        client.send("USERNAME".encode())
        username = client.recv(1024).decode()
        usernames[client] = username
        clients.append(client)

        print(f"✅ {username} joined.")
        broadcast(f"{username} joined the chat!", client)

        while True:
            message = client.recv(1024).decode()
            if message:
                print(f"{username}: {message}")
                broadcast(f"{username}: {message}", client)
            else:
                break
    except:
        pass
    finally:
        client.close()
        remove(client)
        if client in usernames:
            broadcast(f"{usernames[client]} left the chat.")
            del usernames[client]

def receive():
    while True:
        client, addr = server.accept()
        print(f"📥 Connected with {addr}")
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

receive()