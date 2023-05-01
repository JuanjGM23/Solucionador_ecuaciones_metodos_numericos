import tkinter as tk
from sympy import *
from sympy.abc import x
import random 
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import tkinter.simpledialog as simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
from random import randint,randrange

"""""
 **************************************************************************************************************************************
 *  Nombre Programa:  Solucionador de ecuaciones con interfaz de usuario.                                                             *
 *  Descripcion:      el programa consiste en la creacion de la interfaz de usuario y la integracion de seis metodos                  *
 *                    tanteo, biseccion, regla falsa, Newton Rahpson, secante y Steffensen. Con sus diferentes funcionalidades.       *
 *                                                                                                                                    *
 *  Programador:      Ing. Juan Jose Gañan Monsalve.                                                                                  *
 *  Fecha:            24/04/2023                                                                                                      *                                                                                *
 *  Licencia:         Creative Commons V3.                                                                                            *
 *  Version:          1.0                                                                                                             *
 **************************************************************************************************************************************

"""



# Cramos la ventana principal y pasamos asignamos valores, diseño y demas
root = tk.Tk()
root.geometry("550x610")
etiqueta = tk.Label(root,text="Métodos Numéricos",font=("Arial", 16, "bold") ,bg="#63A8E3")
etiqueta.pack(fill=tk.X)

style = ttk.Style()
# Configurar el estilo de los botones
style.configure("TButton", foreground="black", background="white")

etiqueta = tk.Label(root, text="Ingresa la ecuación a resolver: ",font=("Arial", 14, "bold"))
etiqueta.place(x=15, y=50)

etiqueta = tk.Label(root, text="Selecciona el método por el cual desea resolver la ecuación : ",font=("Arial", 10,))
etiqueta.place(x=15, y=80)

# Crear un frame con color de fondo
frame = tk.Frame(root, bd=2, relief="groove")
frame.pack(padx=10, pady=10)
frame.place(x=11, y=115, width=530, height=85)

root.title("Métodos Numéricos")


# Crear un cuadro de entrada para que el usuario ingrese la ecuación
equation_entry = tk.Entry(root, width=30)
equation_entry.place(x=320, y=53)
equation_entry.configure(cursor="question_arrow")
# Crear una etiqueta para mostrar el resultado de la ecuación
result_label = tk.Label(root, text="")
result_label.pack()

def reiniciar():
    equation_entry.delete(0, tk.END)
    result_label.config(text="")
    if os.path.exists("Informe.pdf"):
        os.remove("Informe.pdf")

# Carga el archivo de icono
icono = Image.open("reiniciar.png")
# Crea una instancia de la imagen con Tkinter
icono_tk = ImageTk.PhotoImage(icono)
Btn_reiniciar = ttk.Button(root, image=icono_tk,command=reiniciar)
Btn_reiniciar.place(x=250, y=150)
Btn_reiniciar.configure(cursor="hand2")


def tanteo():
    # Para caputar u obtener la ecuacion ingresada por el usuario
    equation_str = equation_entry.get()
    if not equation_str:
        messagebox.showwarning("Alerta", "Por favor, ingrese una ecuación.")
        return
    x = Symbol('x')
    # Convertimos  la cadena de texto en una expresion simbolica de Sympy
    f = sympify(equation_str)
    # Definimos los valores iniciales de x
    x0 = random.uniform(-70, 0)
    x1 = random.uniform(0, 70)

    # Definimos la tolerancia
    tolerancia = 1e-6 # esta notacion equivale a 0.00000001
    iteraciones = 0
    # Aplicamos el metodo de tanteo
    while abs(x1 - x0) > tolerancia:
        iteraciones +=1
        x0 = x1
        x1 = float(nsolve(f, x, x0))  

    result_label.config(text=f"Por el método de tanteo, las soluciones aproximadas son: {x1:.1f}\n{iteraciones} iteraciones")                    
    result_label.place(x=110, y=200)

# Creamos el boton para que el usuario pueda dar clic en la opcion de tanteo
btn_Calcular_Tanteo = ttk.Button(root, text="Tanteo", command=tanteo)
btn_Calcular_Tanteo.place(x=15, y=120)
btn_Calcular_Tanteo.configure(cursor="hand2")


def biseccion():
    # Para caputar u obtener la ecuacion ingresada por el usuario
    equation_str = equation_entry.get()
    if not equation_str:
        messagebox.showwarning("Alerta", "Por favor, ingrese una ecuación.")
        return

    # Convertimos  la cadena de texto en una expresion simbolica de Sympy
    x = Symbol('x')
    f = sympify(equation_str)
    # Definimos los valores iniciales de x
    a = random.uniform(-70, 0)
    b = random.uniform(0, 70)
    tolerancia = 1e-6
    contadorIterar = 0 # Inicializamos contador de iteraciones en cero 0

    while abs(b - a) > tolerancia:
        contadorIterar += 1
        c = (a + b) / 2 # metodo biseccion 
        # Este if nos sirve para actulizar los valores del intervalo
        if f.subs(x, a) * f.subs(x, c) < 0:
            b = c # Si se cumple esta condicion, es porque la raiz se encuentra en el intervalo a-c
            # y actualizamos en el valor de b con c
        else:
            a = c # En caso contrario, la raíz se encuentra en el intervalo c-b por lo que se 
            #actualiza el valor de a con c
         
    result_label.config(text=f"Por el metodo de biseccion, la solución aproximada es: {c:.1f}\n{contadorIterar} iteraciones")
    result_label.place(x=110, y=200)
# Creamos el boton para iniciar el cálculo
btn_Calcular_Bise = ttk.Button(root, text="Bisección", command=biseccion)
btn_Calcular_Bise.place(x=210, y=120)
btn_Calcular_Bise.configure(cursor="hand2")


def reglaFalsa():

    equation = equation_entry.get()
    if not equation:
        messagebox.showwarning("Alerta", "Por favor, ingrese una ecuación.")
        return
    x = Symbol('x')
    f = lambdify(x, equation)

    a = random.uniform(-60, 0)
    b = random.uniform(0, 60)
    tolerancia = 1e-6
    max_iteraciones = 5000
    iteracioness = 0
    
     # Aplicar regla falsa
    while abs(b - a) > tolerancia and iteracioness < max_iteraciones:
        iteracioness += 1
        c = b - (f(b)*(b - a)) / (f(b) - f(a))
        fc = f(c)
        
        if fc == 0:
            # Encontramos la raíz exacta
            break
        elif f(b)*fc < 0:
            # La raíz está en el intervalo [a, c]
            b = c
        else:
            # La raíz está en el intervalo [c, b]
            a = c
        
    result_label.config(text=f"Por el metodo de Regla Falsa, la solución aproximada es: {c:.1f}\n{iteracioness} iteraciones")  
    result_label.place(x=110, y=200)

btn_Calcular_Regla = ttk.Button(root, text="Regla Falsa", command=reglaFalsa)
btn_Calcular_Regla.place(x=295, y=120)
btn_Calcular_Regla.configure(cursor="hand2")




def Newton():

    equation = equation_entry.get()
    if not equation:
        messagebox.showwarning("Alerta", "Por favor, ingrese una ecuación.")
        return
    # Definir la función
    x = sp.Symbol('x')
    funcion = sp.sympify(equation_entry.get())
    # Definir la derivada de la función
    derivada = sp.diff(funcion, x)

    # Definir el valor inicial y la tolerancia
    valor_inicial = random.uniform(-10, 10)
    tolerancia = 1e-6

    # Definir el número máximo de iteraciones
    max_iteraciones = 100

    # Definir el contador de iteraciones
    contador = 0

    # Implementar el método de Newton-Raphson
    while abs(funcion.subs(x, valor_inicial)) > tolerancia and contador < max_iteraciones:
        valor_inicial = valor_inicial - funcion.subs(x, valor_inicial) / derivada.subs(x, valor_inicial)
        contador += 1

    # Imprimir el resultado
    if contador == max_iteraciones:
        result_label.config(text=f"El método de Newton-Raphson no converge después de {max_iteraciones} iteraciones.")
    else:
        result_label.config(text=f"Por el metodo de Regla Falsa, la solución aproximada es: {valor_inicial:.1f}\nNúmero de iteraciones: {contador}")
        
    result_label.place(x=110, y=200)
btn_Calcular_Newton = ttk.Button(root, text="Newton-Raphson", command=Newton)
btn_Calcular_Newton.place(x=100, y=120)
btn_Calcular_Newton.configure(cursor="hand2")


def Secante():
    equation = equation_entry.get()
    
    if not equation:
        messagebox.showwarning("Alerta", "Por favor, ingrese una ecuación.")
        return
    x = Symbol('x')
    f = lambdify(x, equation)

    #Generador de puntos de arranque
    from random import random
    while True:
        Xa=-1000*random();Xb=-Xa
        if f(Xa)*f(Xb)<0:
            break
    print('Xa = ',Xa,'     ','Xb = ',Xb)

    #Corriendo el método de la secante
    cont=0
    Xc=Xa-((f(Xa)*(Xa-Xb))/(f(Xa)-f(Xb)))
    while True:
        cont+=1
        if abs(f(Xc))<=1e-6:
            break
        elif f(Xa)*f(Xc)<0:
            Xb=Xc;Xc=Xa-((f(Xa)*(Xa-Xb))/(f(Xa)-f(Xb)))
        else:
            Xa=Xc;Xc=Xa-((f(Xa)*(Xa-Xb))/(f(Xa)-f(Xb)))

    result_label.config(text=f"Por el metodo de Secante, la solución aproximada es: {Xc:.1f}\n{cont} iteraciones")
    result_label.place(x=110, y=200)

btn_Calcular_Secante = ttk.Button(root, text="Secante", command=Secante)
btn_Calcular_Secante.place(x=380, y=120)
btn_Calcular_Secante.configure(cursor="hand2")



def Steffensen():

    equation = equation_entry.get()
    if not equation:
        messagebox.showwarning("Alerta", "Por favor, ingrese una ecuación.")
        return
    
    x = Symbol('x')
    f = lambdify(x, equation)

    #Corriendo el método de la Steffensen varias soluciones
    Soluciones=[]
    Max_Seeds=100
    #Generador de punto de arranque
    i=0
    while i<=Max_Seeds:
        x0=randrange(10)
        x1=x0
        while True:
            if abs(f(x1))<=0.0001:
                break
            else:
                x1=x0-((f(x0)**2)/(f(x0+f(x0))-f(x0)))
                x0=x1
        i+=1
        x0=round(x0, 2)
        if x0 in Soluciones:
            print()
        else:
            Soluciones.append(x0)
            print('Nueva solución encontrada:',x0)       
    result_label.config(text=f"Por el metodo de Steffensen, la solución aproximada es: {Soluciones}\n{i} iteraciones")
    result_label.place(x=110, y=200)

    graficar_soluciones(Soluciones, f)

btn_Calcular_Steffensen = ttk.Button(root, text="Steffensen", command=Steffensen)
btn_Calcular_Steffensen.place(x=460, y=120)
btn_Calcular_Steffensen.configure(cursor="hand2")


def graficar_soluciones(soluciones, f):
    # Convertir las soluciones a una lista de flotantes
    soluciones = [float(sol) for sol in soluciones]
    # Generar un arreglo de puntos x
    x = np.linspace(-30, 30, 1000)
    y = [f(xi) for xi in x]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
    # Agregar marcadores en las posiciones de las soluciones
    for sol in soluciones:
        ax.plot(sol, 0, marker='o', markersize=8, color="red")
    # Mostrar la gráfica
    plt.title("Grafica")
    plt.show()



def generar_informe():
    equation_str = equation_entry.get()
    if not equation_str:
        messagebox.showwarning("Error", "Por favor, ingrese una ecuación para generar el informe.")
        return

    f = sympify(equation_str)
    x = np.linspace(-30,30,1000).astype(float)
    # Evaluamos la función en los puntos de x
    y = [float(f.subs(Symbol('x'), xi)) for xi in x]
    # Realizamos la creacion de la figura y el eje de la gráfica
    fig, ax = plt.subplots()
    # Para graficar la función
    ax.plot(x, y)

    solucion_str = result_label.cget("text").split(": ")[1].split("\n")[0]
    solucion_str = solucion_str.strip('[]') # Elimina los corchetes del inicio y del final
    solucion = float(solucion_str)


    ax.axvline(x=solucion, color='r')
    ax.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
    ax.plot(solucion, 0, marker='o', markersize=8, color="red")
    # Guardamos la figura como un archivo PNG temporal
    plt.title("Grafica")
    plt.savefig("temp.png")
    # Crear el archivo PDF y configurar el tamaño de la página
    c = canvas.Canvas("Informe.pdf", pagesize=letter)
    c.drawString(50,750, "Informe: Resultados de Métodos Numéricos")
    c.drawString(50,700, f"Ecuación: {equation_str}")
    c.drawString(50, 680, f"Solución encontrada: {format(solucion, '.1f')}")
    # Agregar la imagen de la gráfica
    c.drawImage("temp.png", 50, 350, width=500, height=300)
    c.save()
    os.remove("temp.png")
    messagebox.showinfo("Informe generado", "Informe generado exitosamente.")



def graficar():
    # Obtener la ecuación ingresada por el usuario
    equation_str = equation_entry.get()
    if not equation_str:
        messagebox.showwarning("Error", "Por favor, ingrese una ecuación para graficar.")
        return
    # Convertimos la cadena de texto en una expresión simbolica de Sympy
    f = sympify(equation_str)
    x = np.linspace(-30,30,1000).astype(float)
    # Evaluamos la función en los puntos de x
    y = [float(f.subs(Symbol('x'), xi)) for xi in x]
    fig, ax = plt.subplots()
    # Para graficar la función
    ax.plot(x, y)

    solucion = result_label.cget("text").split(": ")[1].split("\n")[0]
    solucion = solucion.strip('[]')
    solucion = float(solucion)

    ax.axvline(x=solucion, color='r')
    ax.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
    ax.plot(solucion, 0, marker='o', markersize=8, color="red")
    # Mostrar la gráfica
    plt.title("Grafica")
    plt.show()



Btn_Pdf = ttk.Button(root, text="Generar informe en PDF", command=generar_informe)
Btn_Pdf.place(x=210, y=540)
Btn_Pdf.configure(cursor="hand2")

Btn_graficar = ttk.Button(root, text="Graficar", command=graficar)
Btn_graficar.place(x=240, y=500)
Btn_graficar.configure(cursor="hand2")

# Crear el objeto PhotoImage
imagen = tk.PhotoImage(file="imagen.png").subsample(2)
# Crear una etiqueta y mostrar la imagen en ella
etiqueta_imagen = tk.Label(root, image=imagen)
etiqueta_imagen.pack()
etiqueta_imagen.place(x=100, y=240)


def Salir():
    if messagebox.askokcancel("Salir", "¿Quieres abandonar el programa?"):
        root.destroy()

btn_salir = ttk.Button(root, text="Salir", command=Salir)
btn_salir.place(x=240, y=580)
btn_salir.configure(cursor="hand2")


# Iniciamos el loop principal de la ventana
root.mainloop()



