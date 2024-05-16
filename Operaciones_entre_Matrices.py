import tkinter as tk
from tkinter import ttk, simpledialog, messagebox


def Confirmar_Dimensiones(operacion):
    filas_a = simpledialog.askinteger("Matriz No. 1", "Ingrese el Número de Filas de la Matriz No.1:")
    columnas_a = simpledialog.askinteger("Matriz No. 1", "Ingrese el Número de Columnas de la Matriz No.1:")
    filas_b = simpledialog.askinteger("Matriz No. 2", "Ingrese el Número de Filas de la Matriz No.2:")
    columnas_b = simpledialog.askinteger("Matriz No. 2", "Ingrese el Número de Columnas de la Matriz No.2:")

    Add_Paso("\nPaso No.2: Verificación de dimensiones de las matrices")
    if operacion == Multiplicacion_Matrices and columnas_a != filas_b:
        messagebox.showerror("¡ERROR!", "Las Dimensiones no son Compatibles para Operarlas")
        Add_Paso("¡ERROR! Las Dimensiones no son Compatibles para Operarlas")
        return None, None, None, None

    if operacion in [Suma_Matrices, Resta_Matrices] and (filas_a != filas_b or columnas_a != columnas_b):
        messagebox.showerror("¡ERROR!", "Las Dimensiones no son Compatibles para Operarlas")
        Add_Paso("¡ERROR! Las Dimensiones no son Compatibles para Operarlas")
        return None, None, None, None

    return filas_a, columnas_a, filas_b, columnas_b


def Ingreso_Valores_Matriz(parent_frame, filas, columnas, matriz_numero):
    matriz_frame = tk.Frame(parent_frame)
    matriz_frame.pack(side=tk.LEFT, padx=20, pady=10)

    tk.Label(matriz_frame, text=f"Ingreso de Valores de la Matriz No.{matriz_numero}",
             font=("Times New Roman", 14)).pack(pady=10)
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            frame = tk.Frame(matriz_frame)
            frame.pack(padx=5, pady=5)
            tk.Label(frame, text=f"a{i + 1}{j + 1}:").pack(side=tk.LEFT)
            valor_entry = tk.Entry(frame)
            valor_entry.pack(side=tk.LEFT)
            fila.append(valor_entry)
        matriz.append(fila)
    return matriz


def Obtener_Valores_Matriz(matriz):
    valores = []
    for fila in matriz:
        fila_valores = []
        for entry in fila:
            try:
                valor = float(entry.get())
            except ValueError:
                valor = 0
            fila_valores.append(valor)
        valores.append(fila_valores)
    return valores


def Mostrar_Resultado(parent_frame, resultado):
    tk.Label(parent_frame, text="Resultado", font=("Times New Roman", 14)).pack(pady=10)
    for fila in resultado:
        frame = tk.Frame(parent_frame)
        frame.pack(padx=5, pady=5)
        for valor in fila:
            tk.Label(frame, text=str(valor)).pack(side=tk.LEFT, padx=5)


def Operar_Matrices(operacion):
    Limpiar_Ventana()
    Add_Paso("\nPaso No.1: Ingreso de Valores")
    filas_a, columnas_a, filas_b, columnas_b = Confirmar_Dimensiones(operacion)
    if filas_a is None:
        return

    parent_frame = data_frame
    parent_frame.pack_forget()
    parent_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    matriz_frame = tk.Frame(parent_frame)
    matriz_frame.pack(pady=20)

    A = Ingreso_Valores_Matriz(matriz_frame, filas_a, columnas_a, 1)
    B = Ingreso_Valores_Matriz(matriz_frame, filas_b, columnas_b, 2)

    def Calcular_Operacion():
        matriz_a = Obtener_Valores_Matriz(A)
        matriz_b = Obtener_Valores_Matriz(B)
        resultado = operacion(matriz_a, matriz_b)
        if resultado is not None:
            Mostrar_Resultado(resultado_frame, resultado)
            Add_Paso(f"\nPaso No.4: Resultado\n{resultado}")

    ttk.Button(parent_frame, text="Calcular", command=Calcular_Operacion).pack(pady=20)


def Suma_Matrices(A, B):
    pasos.append("\nPaso No.3: Sumar las Posiciones Correspondientes de cada Matriz")
    resultado = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            pasos.append(f"{A[i][j]} + {B[i][j]} = {resultado[i][j]}")
    return resultado


def Resta_Matrices(A, B):
    pasos.append("\nPaso No.3: Restar las Posiciones Correspondientes de cada Matriz")
    resultado = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            pasos.append(f"{A[i][j]} - {B[i][j]} = {resultado[i][j]}")
    return resultado


def Multiplicacion_Matrices(A, B):
    pasos.append("\nPaso No.3: Multiplicar las Matrices")
    resultado = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            suma = " + ".join([f"{A[i][k]}*{B[k][j]}" for k in range(len(B))])
            pasos.append(f"({suma}) = {resultado[i][j]}")
    return resultado


def Producto_Punto(A, B):
    pasos.append("\nPaso No.3: Calcular el Producto Punto")
    if len(A) == 1 and len(B) == 1 and len(A[0]) == len(B[0]):
        resultado = sum(A[0][i] * B[0][i] for i in range(len(A[0])))
        suma = " + ".join([f"{A[0][i]}*{B[0][i]}" for i in range(len(A[0]))])
        pasos.append(f"({suma}) = {resultado}")
        return [[resultado]]
    else:
        messagebox.showerror("¡ERROR!", "Las matrices no son vectores de igual dimensión para producto punto.")
        pasos.append("¡ERROR! Las matrices no son vectores de igual dimensión para producto punto.")
        return None


def Limpiar_Ventana():
    for widget in data_frame.winfo_children():
        widget.destroy()
    for widget in resultado_frame.winfo_children():
        widget.destroy()
    Limpiar_Pasos()


def Limpiar_Pasos():
    global pasos
    pasos = []


def Add_Paso(texto):
    pasos.append(texto)


def Mostrar_Pasos():
    pasos_window = tk.Toplevel(new_window)
    pasos_window.title("Pasos de la Operación")

    for paso in pasos:
        tk.Label(pasos_window, text=paso, font=("Times New Roman", 12)).pack(anchor='w')


def Ventana_Operaciones_entre_Matrices(master):
    global new_window, data_frame, resultado_frame, pasos
    pasos = []
    new_window = tk.Toplevel(master)
    new_window.title("Operaciones entre Matrices")

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    new_window.geometry(f"{screen_width}x{screen_height}")

    titulo_label = tk.Label(new_window, text="OPERACIONES ENTRE MATRICES", font=("Times New Roman", 20, "bold"))
    titulo_label.pack(pady=(40, 20), anchor='n')

    button_frame = tk.Frame(new_window, width=414)
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=50)
    button_frame.pack_propagate(False)

    data_frame = tk.Frame(new_window)
    data_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    resultado_frame = tk.Frame(new_window)
    resultado_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    ttk.Button(button_frame, text="Suma de Matrices", command=lambda: Operar_Matrices(Suma_Matrices)).pack(pady=10,
                                                                                                           fill=tk.X)
    ttk.Button(button_frame, text="Resta de Matrices", command=lambda: Operar_Matrices(Resta_Matrices)).pack(pady=10,
                                                                                                             fill=tk.X)
    ttk.Button(button_frame, text="Multiplicación de Matrices",
               command=lambda: Operar_Matrices(Multiplicacion_Matrices)).pack(pady=10, fill=tk.X)
    ttk.Button(button_frame, text="Producto Punto de Matrices", command=lambda: Operar_Matrices(Producto_Punto)).pack(
        pady=10, fill=tk.X)
    ttk.Button(button_frame, text="Mostrar Pasos", command=Mostrar_Pasos).pack(pady=10, fill=tk.X)
    ttk.Button(button_frame, text="Limpiar Todo", command=Limpiar_Ventana).pack(pady=10, fill=tk.X)

