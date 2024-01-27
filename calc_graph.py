import tkinter as tk

# Fonction pour mettre à jour l'affichage
def update_display(value):
    current_text = entry.get()
    new_text = current_text + str(value)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

# Fonction pour évaluer l'expression et afficher le résultat
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erreur")

# Fonction pour effacer l'affichage
def clear_display():
    entry.delete(0, tk.END)

# Création de la fenêtre principale
window = tk.Tk()
window.title("Calculatrice")

# Configuration de l'entrée
entry = tk.Entry(window, width=20, font=("Arial", 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Boutons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 16),
              command=lambda b=button: update_display(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Bouton pour effacer
tk.Button(window, text='C', padx=20, pady=20, font=("Arial", 16), command=clear_display).grid(row=row_val, column=col_val)

# Lancement de la boucle principale
window.mainloop()
