#!/bin/bash

# Fonction pour le serveur TCP
start_tcp_server() {
    echo "Démarrage du serveur TCP..."
    nc -l -p $TCP_PORT
}

# Fonction pour le serveur UDP
start_udp_server() {
    echo "Démarrage du serveur UDP..."
    nc -lu -p $UDP_PORT
}

# Port pour le serveur TCP
TCP_PORT=4444

# Port pour le serveur UDP
UDP_PORT=9999

# Afficher le menu
echo "[1] TCP chat server"
echo "[2] UDP chat server"

# Lire le choix de l'utilisateur
read -p "Choisissez un serveur (1/2): " choice

case $choice in
    1)
        start_tcp_server
        ;;
    2)
        start_udp_server
        ;;
    *)
        echo "Choix invalide."
        ;;
esac

# Comment verifier le code ?

# Ouvrez deux terminaux distincts

# Dans le premier terminal, utilisez telnet pour envoyer un message au serveur TCP
# telnet localhost 4444
# Ensuite vous pouvez ecrire n'importe quel texte d'un cote pour le voir de l'autre cote

# Dans le deuxième terminal, utilisez nc pour envoyer un message au serveur UDP
# nc -u localhost 9999
# Ensuite vous pouvez ecrire n'importe quel texte d'un cote pour le voir de l'autre cote