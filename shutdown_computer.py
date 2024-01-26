import os
import platform

def shutdown_computer()
    system = platform.system()

    try
        if system == Windows
            os.system(shutdown s t 1)  # Arrêt de l'ordinateur sous Windows
        elif system == Linux or system == Darwin
            os.system(sudo shutdown now)  # Arrêt de l'ordinateur sous Linux ou macOS
        else
            print("Système d'exploitation non pris en charge.")
    except Exception as e
        print(Erreur , e)

if __name__ == __main__
    shutdown_computer()
