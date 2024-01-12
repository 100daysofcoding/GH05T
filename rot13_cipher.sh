#!/bin/bash

# Fonction pour le chiffrement/déchiffrement ROT13
rot13_cipher() {
    local text="$1"
    echo "$text" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
}

# Afficher le menu
echo "ROT13 Cipher Tool"
echo "[1] Chiffrer le texte"
echo "[2] Déchiffrer le texte"

# Lire le choix de l'utilisateur
read -p "Choisissez une option (1/2): " choice

case $choice in
    1)
        read -p "Entrez le texte à chiffrer : " input_text
        encrypted_text=$(rot13_cipher "$input_text")
        echo "Texte chiffré : $encrypted_text"
        ;;
    2)
        read -p "Entrez le texte à déchiffrer : " input_text
        decrypted_text=$(rot13_cipher "$input_text")
        echo "Texte déchiffré : $decrypted_text"
        ;;
    *)
        echo "Option invalide."
        ;;
esac
