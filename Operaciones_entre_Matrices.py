import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

def Crear_Matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = simpledialog.askfloat("Ingreso", f"Ingrese el elemento ({i+1}, {j+1}):", parent=new_window)
            fila.append(valor)
        matriz.append(fila)
    return matriz

def Confirmar_Dimensiones():
    filas_a = simpledialog.askinteger("Matriz No. 1", "Ingrese el Número de Filas de la Matriz No.1:")
    columnas_a = simpledialog.askinteger("Matriz No. 1", "Ingrese el Número de Columnas de la Matriz No.1:")
    filas_b = simpledialog.askinteger("Matriz No. 2", "Ingrese el Número de Filas de la Matriz No.2:")
    columnas_b = simpledialog.askinteger("Matriz No. 2", "Ingrese el Número de Columnas de la Matriz No.2:")

    if columnas_a != filas_b:
        messagebox.showerror("¡ERROR!", "Las dimensiones no son compatibles para multiplicación.")
        return None, None, None, None
    return filas_a, columnas_a, filas_b, columnas_b

def Ingreso_Valores_Matriz(filas, columnas, new_window, matriz_numero):
    tk.Label(new_window, text=f"Ingreso de Valores de la Matriz No.{matriz_numero}", font=("Arial", 14)).pack()
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            tk.Label(new_window, text=f"a{i+1}{j+1}:").pack()
            valor_entry = tk.Entry(new_window)
            valor_entry.pack()
            fila.append(valor_entry)
        matriz.append(fila)
    return matriz

def Operar_Matrices(new_window, operacion):
    filas_a, columnas_a, filas_b, columnas_b = Confirmar_Dimensiones()
    if filas_a is None:
        return

    A = Ingreso_Valores_Matriz(filas_a, columnas_a, new_window, 1)
    B = Ingreso_Valores_Matriz(filas_b, columnas_b, new_window, 2)
    
def Suma_Matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        messagebox.showerror("¡ERROR!", "Las Matrices deben tener las mismas Dimensiones para la Suma")
        return None
    resultado = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return resultado

def Resta_Matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        messagebox.showerror("¡ERROR!", "Las Matrices deben tener las mismas Dimensiones para la Resta")
        return None
    resultado = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return resultado

def Multiplicacion_Matrices(A, B):
    if len(A[0]) != len(B):
        messagebox.showerror("¡ERROR!", "Las Dimensiones no son Compatibles para hacer la Multiplicación")
        return None
    resultado = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return resultado

def Producto_Punto(A, B):
    if len(A) == 1 and len(B) == 1 and len(A[0]) == len(B[0]):
        return sum(A[0][i] * B[0][i] for i in range(len(A[0])))
    else:
        messagebox.showerror("¡ERROR!", "Las matrices no son vectores de igual dimensión para producto punto.")
        return None

def Limpiar_Ventana():
    for widget in new_window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text="")

def Operar_Matrices(operacion):
    filas_a = simpledialog.askinteger("Matriz No. 1", "Ingrese el Número de Filas de la Matriz No.1:")
    columnas_a = simpledialog.askinteger("Matriz No. 1", "Ingrese el Número de Columnas de la Matriz No.1:")
    A = Crear_Matriz(filas_a, columnas_a)
    filas_b = simpledialog.askinteger("Matriz No. 2", "Ingrese el Número de Filas de la Matriz No.2:")
    columnas_b = simpledialog.askinteger("Matriz No. 2", "Ingrese el Número de Columnas de la Matriz No.2:")
    B = Crear_Matriz(filas_b, columnas_b)

    resultado = operacion(A, B)
    if resultado is not None:
        messagebox.showinfo("Resultado", f"El resultado es:\n{resultado}")

def Ventana_Operaciones_entre_Matrices(master):
    global new_window
    new_window = tk.Toplevel(master)
    new_window.title("Operaciones entre Matrices")
    new_window.geometry("950x650")

    titulo_label = tk.Label(new_window, text="OPERACIONES ENTRE MATRICES", font=("Times New Roman", 20, "bold"))
    titulo_label.pack(pady=(40, 50), anchor='n')

    button_frame = tk.Frame(new_window, width=414)
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=50)
    button_frame.pack_propagate(False)

    data_frame = tk.Frame(new_window)
    data_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    frame = tk.Frame(new_window)
    frame.pack(side=tk.LEFT, fill=tk.Y)

    ttk.Button(frame, text="Suma de Matrices", command=lambda: Operar_Matrices(Suma_Matrices)).pack(pady=10, fill=tk.X)
    ttk.Button(frame, text="Resta de Matrices", command=lambda: Operar_Matrices(Resta_Matrices)).pack(pady=10, fill=tk.X)
    ttk.Button(frame, text="Multiplicación de Matrices", command=lambda: Operar_Matrices(Multiplicacion_Matrices)).pack(pady=10, fill=tk.X)
    ttk.Button(frame, text="Producto Punto de Matrices", command=lambda: Operar_Matrices(Producto_Punto)).pack(pady=10, fill=tk.X)
    ttk.Button(frame, text="Limpiar Ventana", command=Limpiar_Ventana).pack(pady=10, fill=tk.X)

