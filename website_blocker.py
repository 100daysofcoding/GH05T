import platform
import os
from datetime import datetime, timedelta

# Liste des sites à bloquer
blocked_sites = ["www.facebook.com", "www.twitter.com"]

# Chemin du fichier hosts
hosts_path = ""
system = platform.system()
if system == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif system == "Linux" or system == "Darwin":
    hosts_path = "/etc/hosts"
else:
    print("Système d'exploitation non pris en charge.")
    exit()

# Fonction pour bloquer les sites
def block_websites():
    try:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in blocked_sites:
                if site not in content:
                    file.write("127.0.0.1 " + site + "\n")
            print("Sites bloqués avec succès.")
    except Exception as e:
        print("Erreur :", e)

# Fonction pour débloquer les sites
def unblock_websites():
    try:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in blocked_sites):
                    file.write(line)
            file.truncate()
        print("Sites débloqués avec succès.")
    except Exception as e:
        print("Erreur :", e)

# Exemple d'utilisation
def main():
    block_websites()
    # Attendre 60 secondes (simulant une période de blocage)
    print("Attente...")
    import time
    time.sleep(60)
    unblock_websites()

if __name__ == "__main__":
    main()
