#Librerias:
import pandas as pd
import matplotlib.pyplot as plt 
#Para visualizacion de datos
import os
import seaborn as sns
#Para importar clases especificas de la libreria
from tkinter import messagebox, simpledialog
#Math y Random
import random as rd
import csv

archivo_csv = "operarios.csv"
df = None

class ManejoUsuarios():
    def registrar_entrada(self):
        nombre_operario = simpledialog.askstring("Nombre","Ingrese el nombre del operario")
        while True:
            cant_frances = simpledialog.askinteger("Cantidad Pan francés","Ingrese cuantas unidades de pan francés produjó")
            cant_queso = simpledialog.askinteger("Cantidad Pan queso","Ingrese cuantas unidades de pan de queso produjó")
            cant_cross = simpledialog.askinteger("Cantidad croissants","Ingrese cuantas unidades de croissants produjó")
            
            if cant_frances >= 0 and cant_frances <= 500:
                if cant_queso >= 0 and cant_queso <= 500:
                    if cant_cross >= 0 and cant_cross <= 500:
                        break
            else:
                messagebox.showwarning("Error", "Ingrese solo valores entre 0 y 500")
                continue
    
        comp_frances = round(rd.uniform(1.0,1.5),2)
        comp_queso = round(rd.uniform(1.0,1.5),2)
        comp_cross = round(rd.uniform(1.0,1.5),2)
        
        efic_frances = round(cant_frances*comp_frances)
        efic_queso = round(cant_queso*comp_queso)
        efic_cross = round(cant_cross*comp_cross)

        eficiencia = round(sum([efic_frances,efic_queso,efic_cross])/sum([comp_frances,comp_queso,comp_cross]))
        
        if eficiencia >= 300:
            estado = "Cumple"
        else:
            estado = "No cumple"

        operario = {
        'Nombre': nombre_operario,
        'Eficiencia_final': eficiencia,
        'Estado': estado,
        'Cantidad_pan_frances': cant_frances,
        'Cantidad_pan_queso': cant_queso,
        'Cantidad_croissant': cant_cross,
        'Complejidad_pan_frances': comp_frances,
        'Complejidad_pan_queso': comp_queso,
        'Complejidad_croissant': comp_cross,
        'Eficiencia_pan_frances': efic_frances,
        'Eficiencia_pan_queso': efic_queso,
        'Eficiencia_croissant': efic_cross
        }
    
        # Verificar si ya existe el archivo
        archivo_existe = os.path.isfile(archivo_csv)

        with open(archivo_csv, 'a', newline='') as f:
            escritor = csv.DictWriter(f, fieldnames=operario.keys())
            if not archivo_existe:
                escritor.writeheader()
            escritor.writerow(operario)

