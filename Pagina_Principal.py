import tkinter as tk
from tkinter import ttk
import Operaciones_entre_Matrices
import Matriz_Inversa
import Determinante_de_una_Matriz
import Rango_de_una_Matriz
import Cifrado_por_Matrices
import Cadenas_de_Markov
import Operaciones_con_Vectores


def Click(Nombre_Boton):
    if Nombre_Boton == "Operaciones entre Matrices":
        Operaciones_entre_Matrices.Ventana_Operaciones_entre_Matrices(window)

    elif Nombre_Boton == "Matriz Inversa":
        Matriz_Inversa.Ventana_Matriz_Inversa(window)

    elif Nombre_Boton == "Determinante de una Matriz":
        Determinante_de_una_Matriz.Ventana_Determinante_de_una_Matriz(window)

    elif Nombre_Boton == "Rango de una Matriz":
        Rango_de_una_Matriz.Ventana_Rango_de_una_Matriz(window)

    elif Nombre_Boton == "Cifrado por Matrices":
        Cifrado_por_Matrices.Ventana_Cifrado_por_Matrices(window)

    elif Nombre_Boton == "Cadenas de Markov":
        Cadenas_de_Markov.Ventana_Cadenas_de_Markov(window)

    elif Nombre_Boton == "Operaciones con Vectores":
        Operaciones_entre_Matrices.Ventana.Operaciones_con_Vectores


window = tk.Tk()
window.title("Álgebra Lineal")
window.geometry("414x890")

style = ttk.Style(window)
style.theme_use('alt')

style.configure('TButton', font=("Times New Roman", 15, "bold"), padding=12, borderwidth=4, relief="groove")
style.map('TButton',
          background=[('active', '#DBB6EE'), ('!active', '#7F4CA5')],
          foreground=[('active', 'white'), ('!active', 'white')])

titulo_label = tk.Label(window, text="Álgebra Lineal", font=("Times New Roman", 20, "bold"), bg=window.cget('background'))
titulo_label.pack(pady=(40, 30))

Botones = [
    "Operaciones entre Matrices",
    "Matriz Inversa",
    "Determinante de una Matriz",
    "Rango de una Matriz",
    "Cifrado por Matrices",
    "Cadenas de Markov",
    "Operaciones con Vectores"
]

for ds in Botones:
    button = ttk.Button(window, text=ds, style='TButton', command=lambda ds=ds: Click(ds))
    button.pack(fill='x', padx=50, pady=(7, 7))

window.mainloop()