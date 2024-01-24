import tkinter as tk
from time import strftime

# Fonction pour mettre à jour l'heure
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)  # Met à jour toutes les 1000 ms (1 seconde)

# Configuration de l'interface graphique
root = tk.Tk()
root.title('Digital Clock')

# Étiquette pour afficher l'heure
lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl.pack(anchor='center')

# Lancement de la fonction time
time()

# Lancement de l'interface graphique
root.mainloop()
