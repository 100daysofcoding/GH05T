#!/bin/bash

# Fonction pour le chiffrement César
caesar_cipher() {
    local text="$1"
    local shift="$2"

    local result=""
    local char

    for (( i=0; i<${#text}; i++ )); do
        char="${text:$i:1}"

        if [[ $char =~ [A-Za-z] ]]; then
            ascii_val=$(printf "%d" "'$char")

            if [[ $char =~ [A-Z] ]]; then
                ascii_val=$(( (ascii_val - 65 + shift) % 26 + 65 ))
            fi

            if [[ $char =~ [a-z] ]]; then
                ascii_val=$(( (ascii_val - 97 + shift) % 26 + 97 ))
            fi

            result+="$(printf \\$(printf "%03o" "$ascii_val"))"
        else
            result+="$char"
        fi
    done

    echo "$result"
}

# Fonction pour le serveur TCP
start_tcp_server() {
    echo "Démarrage du serveur TCP..."
    nc -l -p $TCP_PORT | while IFS= read -r line; do
        decoded_message=$(caesar_cipher "$line" "-3")  # Utilisez un décalage de -3 pour déchiffrer
        echo "Message reçu : $decoded_message"

        # Envoie d'un message chiffré au client
        encrypted_response=$(caesar_cipher "Réponse du serveur" "3")  # Utilisez un décalage de 3 pour chiffrer
        echo "$encrypted_response" | nc -q 1 localhost $TCP_PORT
    done
}

# Fonction pour le serveur UDP
start_udp_server() {
    echo "Démarrage du serveur UDP..."
    nc -lu -p $UDP_PORT | while IFS= read -r line; do
        decoded_message=$(caesar_cipher "$line" "-3")  # Utilisez un décalage de -3 pour déchiffrer
        echo "Message reçu : $decoded_message"

        # Envoie d'un message chiffré au client
        encrypted_response=$(caesar_cipher "Réponse du serveur" "3")  # Utilisez un décalage de 3 pour chiffrer
        echo "$encrypted_response" | nc -u -q 1 localhost $UDP_PORT
    done
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
# Ensuite vous pouvez ecrire n'importe quel texte chiffré par décalage sur le terminal du telnet pour recevoir le message déchiffré

# Dans le deuxième terminal, utilisez nc pour envoyer un message au serveur UDP
# nc -u localhost 9999
# Ensuite vous pouvez ecrire n'importe quel texte chiffré par décalage sur le terminal du netcat pour recevoir le message déchiffré