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
    
    def reporte_general(self):
        if os.path.isfile(archivo_csv):
            df = pd.read_csv(archivo_csv)
            reporte_general = (df[['Nombre','Eficiencia_final','Estado']])
            return reporte_general

    def reporte_individual(self):
        archivo_existe = os.path.isfile('operarios.csv')
        if not archivo_existe:
            messagebox.showwarning("Error", "No existen datos")
        else:
            operario_buscado = simpledialog.askstring("Nombre a buscar","Ingrese el nombre del operario")            
            return operario_buscado
        
class DataAnalyzer():
    def __init__(self, df):
        self.df = df

    def correlation_matrix(self):
        return self.df.corr()
        
class CantidadesAnalyzer(DataAnalyzer):
    def __init__(self, df):
        super().__init__(df)
        self.cantidades_cols = ['Cantidad_pan_frances','Cantidad_pan_queso','Cantidad_croissant']
    
    def describe_numericas(self):
        descr_numericas = self.df[self.cantidades_cols].describe()
        return descr_numericas
    
    def graficas_generales(self):
        plt.close('all')
        #Referencia plt.close: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
        plt.figure(figsize=(15,6))

        plt.subplot(1, 2, 1)
        corr_cantidades = self.df[self.cantidades_cols].corr()
        sns.heatmap(corr_cantidades, annot=True, cmap='coolwarm')
        plt.title('Matriz de Correlación')
        plt.xticks(rotation=13)
       
        plt.subplot(1, 2, 2)
        estado_counts = self.df['Estado'].value_counts()
        plt.pie(estado_counts, labels = estado_counts.index)
        plt.title("Grafico torta")
        plt.show()

class EstadisticasAnalyzer(DataAnalyzer):
    def graficas_individuales(self,cantidades,complejidades,eficiencias):
        plt.close('all')
        #Referencia plt.close: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
        plt.figure(figsize=(13,5))

        tipos_panes = ["Pan francés", "Pan de queso", "Croissant"]
        plt.subplot(1, 3, 1)
        plt.bar(tipos_panes,cantidades,)
        plt.title("Producción del operario por pan")
        plt.ylabel("Cantidad producida")
        plt.yticks(rotation=90)
        plt.xticks(rotation=20)

        plt.subplot(1, 3, 2)
        tipos_panes = ["Pan francés", "Pan de queso", "Croissant"]
        plt.bar(tipos_panes,complejidades, color="Green")
        plt.title("Nivel de complejidad del operario por pan")
        plt.ylabel("Nivel de complejidad")
        plt.yticks(rotation=90)
        plt.xticks(rotation=20)

        plt.subplot(1, 3, 3)
        tipos_panes = ["Pan francés", "Pan de queso", "Croissant"]
        plt.bar(tipos_panes,eficiencias, color="Orange")
        plt.title("Eficiencia del operario por pan")
        plt.ylabel("Eficiencia")
        plt.yticks(rotation=90)
        plt.xticks(rotation=20)
        plt.show()