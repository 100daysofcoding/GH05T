#!/bin/bash

# Fonction pour le chiffrement ROT13
rot13_cipher() {
    local text="$1"
    echo "$text" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
}

# Fonction pour le serveur UDP
start_udp_server() {
    echo "Démarrage du serveur UDP..."
    nc -lu -p $UDP_PORT | while read -r message; do
        decrypted_message=$(rot13_cipher "$message")
        echo "Message chiffré reçu : $decrypted_message"
    done
}

# Port pour le serveur UDP
UDP_PORT=9999

# Démarrer le serveur UDP
start_udp_server
