import socket
import subprocess
import threading

def handle_client(client_socket):
    # Affiche ce que le client envoie
    request = client_socket.recv(1024)
    print(f"Received: {request.decode()}")

    # Renvoie une réponse
    client_socket.send(b"ACK!")

    # Ferme la connexion avec le client
    client_socket.close()

def start_server(bind_host, bind_port):
    # Crée un objet socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Attache le socket à une interface réseau et un port
    server.bind((bind_host, bind_port))

    # Active le mode écoute
    server.listen(5)
    print(f"[*] Listening on {bind_host}:{bind_port}")

    while True:
        # Attend une connexion entrante
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        # Crée un thread pour gérer le client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def send_command(target_host, target_port, command):
    # Crée un objet socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Se connecte au serveur
    client.connect((target_host, target_port))

    # Envoie la commande
    client.send(command.encode())

    # Reçoit la réponse
    response = client.recv(4096)
    print(response.decode())

def main():
    # Choix entre être serveur ou client
    choice = input("Choose [1] to be a server, [2] to be a client: ")

    if choice == '1':
        # En mode serveur
        bind_host = input("Enter the server bind address (default is 0.0.0.0): ") or "0.0.0.0"
        bind_port = int(input("Enter the server bind port (default is 9999): ") or 9999)
        start_server(bind_host, bind_port)
    elif choice == '2':
        # En mode client
        target_host = input("Enter the target address: ")
        target_port = int(input("Enter the target port: "))
        command = input("Enter the command to send: ")
        send_command(target_host, target_port, command)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
