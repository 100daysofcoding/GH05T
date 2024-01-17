import paramiko

def remote_command_execution(hostname, port, username, password, command):
    # Création d'une instance SSHClient
    client = paramiko.SSHClient()

    # Chargement des clés par défaut
    client.load_system_host_keys()

    # Auto-ajout des clés de l'hôte
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connexion au serveur SSH
        client.connect(hostname, port=port, username=username, password=password)

        # Exécution de la commande distante
        stdin, stdout, stderr = client.exec_command(command)

        # Affichage de la sortie de la commande
        print("Output:")
        print(stdout.read().decode())

        # Affichage des erreurs
        if stderr:
            print("Errors:")
            print(stderr.read().decode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Fermeture de la connexion SSH
        client.close()

def main():
    # Paramètres de connexion
    hostname = input("Enter the remote hostname or IP address: ")
    port = int(input("Enter the SSH port (default is 22): ") or 22)
    username = input("Enter the SSH username: ")
    password = input("Enter the SSH password: ")

    # Commande à exécuter
    command = input("Enter the command to execute remotely: ")

    # Exécution de la commande à distance
    remote_command_execution(hostname, port, username, password, command)

if __name__ == "__main__":
    main()
