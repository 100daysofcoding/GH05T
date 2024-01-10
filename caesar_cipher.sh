#!/bin/bash

caesar_cipher() {
    local text="$1"
    local shift="$2"

    local result=""
    local char

    for (( i=0; i<${#text}; i++ )); do
        char="${text:$i:1}"

        if [[ $char =~ [A-Za-z] ]]; then
            ascii_val=$(printf "%d" "'$char")

            # Gérer les majuscules
            if [[ $char =~ [A-Z] ]]; then
                ascii_val=$(( (ascii_val - 65 + shift) % 26 + 65 ))
            fi

            # Gérer les minuscules
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

echo "Bienvenue dans l'outil de chiffrement César."

read -p "Veuillez entrer le texte à chiffrer/déchiffrer : " input_text
read -p "Veuillez entrer le décalage : " shift_amount

# Assurez-vous que le décalage est un nombre entier
if ! [[ "$shift_amount" =~ ^[0-9]+$ ]]; then
    echo "Le décalage doit être un nombre entier."
    exit 1
fi

# Choisir entre chiffrement et déchiffrement
echo "Veuillez choisir une option :"
echo "1 - Chiffrer"
echo "2 - Déchiffrer"
read -p "Choix : " choice

case $choice in
    1)
        result=$(caesar_cipher "$input_text" "$shift_amount")
        echo "Texte chiffré : $result"
        ;;
    2)
        # Déchiffrer en utilisant un décalage négatif
        result=$(caesar_cipher "$input_text" "$((0 - shift_amount))")
        echo "Texte déchiffré : $result"
        ;;
    *)
        echo "Option non valide. Veuillez choisir 1 ou 2."
        exit 1
        ;;
esac
