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
from funciones import CantidadesAnalyzer
from funciones import EstadisticasAnalyzer

procesos = ManejoUsuarios()

def nuevo_operario():
    procesos.registrar_entrada()

def general_reporte():
    reporte_general = procesos.reporte_general()
    archivo_existe = os.path.isfile(archivo_csv)
    
    if not archivo_existe:
        mensaje = "No hay registros disponibles"

        text_area.delete("1.0",tk.END)
        text_area.insert(tk.END, mensaje)

        text_area2.delete("1.0",tk.END)
        text_area2.insert(tk.END, mensaje)
        
        text_area3.delete("1.0",tk.END)
        text_area3.insert(tk.END, mensaje)
    else:
        df = pd.read_csv(archivo_csv)
        numeric = CantidadesAnalyzer(df)
        
        text_area.delete("1.0",tk.END)
        text_area.insert(tk.END, reporte_general.to_string(index=True))

        reporte_describe1 = numeric.describe_numericas()
        promedio_eficiencia = f"Promedio de eficiencias: {round((sum(df['Eficiencia_final']))/len(df['Eficiencia_final']))}"
        
        text_area2.delete("1.0",tk.END)
        text_area2.insert(tk.END, reporte_describe1)
        
        text_area3.delete("1.0",tk.END)
        text_area3.insert(tk.END, promedio_eficiencia)

def graficas_generales(): 
        archivo_existe = os.path.isfile(archivo_csv)
        
        if not archivo_existe:
            messagebox.showwarning("Error", "Aún no hay datos")
        else:
            df = pd.read_csv(archivo_csv)
            general_reporte()
            cant = CantidadesAnalyzer(df)      
            cant.graficas_generales()

def individual_reporte():
    archivo_existe = os.path.isfile(archivo_csv)
    if not archivo_existe:
        mensaje = "No hay registros disponibles"
        text_area4.delete("1.0",tk.END)
        text_area4.insert(tk.END, mensaje)
    else:
        while True:
            df = pd.read_csv(archivo_csv)
            operario_buscado = procesos.reporte_individual()
            try:
                indice = df[df['Nombre'] == operario_buscado].index[0]
                df_individual = pd.DataFrame([df.loc[indice].to_dict()])
                estats = EstadisticasAnalyzer(df)

                reporte_individual = (df_individual[['Nombre','Eficiencia_final','Estado']])
                reporte_individual2 = ""
                reporte_individual2 += f"Total panes producidos: {df_individual[['Cantidad_pan_frances','Cantidad_pan_queso','Cantidad_croissant']].values.sum()}\n"
                reporte_individual2 += f"Promedio de complejidad: {round((df_individual[['Complejidad_pan_frances','Complejidad_pan_queso','Complejidad_croissant']].values.sum()/3),1)}\n"                

                text_area4.delete("1.0",tk.END)
                text_area4.insert(tk.END, reporte_individual)                                                                                                                                                                                                                                                                                                                           
                
                text_area5.delete("1.0",tk.END)
                text_area5.insert(tk.END, reporte_individual2)

                cantidades = [sum(df_individual['Cantidad_pan_frances']),sum(df_individual['Cantidad_pan_queso']),sum(df_individual['Cantidad_croissant'])] 
                complejidades = [sum(df_individual['Complejidad_pan_frances']),sum(df_individual['Complejidad_pan_queso']),sum(df_individual['Complejidad_croissant'])] 
                eficiencias = [sum(df_individual['Eficiencia_pan_frances']),sum(df_individual['Eficiencia_pan_queso']),sum(df_individual['Eficiencia_croissant'])]

                estats.graficas_individuales(cantidades,complejidades,eficiencias)
                break
            except:
                messagebox.showwarning("Error", "No existe ese usuario")
                continue
def cerrar():
    plt.close('all')
    #Referencia plt.close: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
    ventana.destroy()
    #Referencia .destroy(): https://www-geeksforgeeks-org.translate.goog/how-to-close-a-tkinter-window-with-a-button/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc


#Ventana:
ventana = tk.Tk()
ventana.title("Visualización de los datos")
ventana.geometry()

#Botones:
boton_añadir = tk.Button(ventana, text="Nuevo operario", bg="#C0E5F7", command=nuevo_operario)
boton_añadir.grid(row=0, column=0)

boton_general = tk.Button(ventana, text="Actualizar/Graficas", bg="#C0E5F7", command=graficas_generales)
boton_general.grid(row=0, column=1)

boton_individual = tk.Button(ventana, text="Reporte individual", bg="#C0E5F7",command=individual_reporte)
boton_individual.grid(row=0, column=2)

boton_salir = tk.Button(ventana, text="Salir", bg="#C33A3A", command=cerrar)
boton_salir.grid(row=3, column=0)

#Text areas:
tk.Label(ventana, text="Reporte\ngeneral").grid(row=1, column=0)
text_area = ScrolledText(ventana, width= 70, height= 15)
text_area.grid(row=1, column=1)

tk.Label(ventana, text="Estadisticas\nrelevantes").grid(row=2, column=0)
text_area2 = ScrolledText(ventana, width= 70, height= 15)
text_area2.grid(row=2, column=1)

text_area3 = ScrolledText(ventana, width= 70, height= 0)
text_area3.grid(row=3, column=1)

text_area4 = ScrolledText(ventana, width= 50, height= 15)
text_area4.grid(row=1, column=2)

text_area5 = ScrolledText(ventana, width= 50, height= 15)
text_area5.grid(row=2, column=2)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)

general_reporte()

ventana.mainloop()