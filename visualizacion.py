#Para interfaz
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
#Dataframes
import pandas as pd
#Para graficas
import matplotlib.pyplot as plt
import os 
#Importo la clase y el archivo_csv
from funciones import archivo_csv
from funciones import ManejoUsuarios

procesos = ManejoUsuarios()

def nuevo_operario():
    procesos.registrar_entrada()


#Ventana:
ventana = tk.Tk()
ventana.title("Visualización de los datos")
ventana.geometry()

#Botones:
boton_añadir = tk.Button(ventana, text="Nuevo operario", bg="#C0E5F7", command=nuevo_operario)
boton_añadir.grid(row=0, column=0)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)

ventana.mainloop()