# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:27:00 2021

@author: DELL
"""

import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
##Crear una instancia de Tkinter
ventana = tk.Tk()
ventana.geometry("700x800") #Tamaño de
ventana
##Añadir color al fondo
ventana.config(bg='#DFDFDF')
##Añadir un título a la ventana
ventana.title("Plan de vuelo")
#--------------------- INPUTS -----------------
#Variables generales para los inputs
fuente_txt = 'calibri 12'
justificacion_txt = 'left'
padding = 5
#./ Fin variables de los inputs
#--------------------- FILA 0 (LABELS) -----------------
lbl_focal = tk.Label(ventana, text="Distancia Focal(mm)")
lbl_ancho_img = tk.Label(ventana, text="Ancho de la imagen(pixel)")
lbl_alto_img = tk.Label(ventana, text="Alto de la imagen(pixel)")
lbl_focal.grid( padx=padding, pady=padding, row=0, column=0)
lbl_ancho_img.grid( padx=padding, pady=padding, row=0, column=1)
lbl_alto_img.grid( padx=padding, pady=padding, row=0, column=2)
#--------------------- FILA 1 (INPUTS) -----------------
txt_focal = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_ancho_img = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_alto_img = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_focal.grid( padx=padding, pady=padding, row=1, column=0)
txt_ancho_img.grid( padx=padding, pady=padding, row=1, column=1)
txt_alto_img.grid( padx=padding, pady=padding, row=1, column=2)
#--------------------- FILA 2 (LABELS) -----------------
lbl_ancho_sensor = tk.Label(ventana, text="Ancho del sensor(mm)")
lbl_alto_sensor = tk.Label(ventana, text="Alto del sensor(mm)")
lbl_altura_vuelo = tk.Label(ventana, text="Altura de vuelo(metros)")
lbl_ancho_sensor.grid( padx=padding, pady=padding, row=2, column=0)
lbl_alto_sensor.grid( padx=padding, pady=padding, row=2, column=1)
lbl_altura_vuelo.grid( padx=padding, pady=padding, row=2, column=2)
#--------------------- FILA 3 (INPUTS) -----------------
txt_ancho_sensor = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_alto_sensor = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_altura_vuelo = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_ancho_sensor.grid( padx=padding, pady=padding, row=3, column=0)
txt_alto_sensor.grid( padx=padding, pady=padding, row=3, column=1)
txt_altura_vuelo.grid( padx=padding, pady=padding, row=3, column=2)
#--------------------- FILA 4 (LABELS) -----------------
lbl_solape_l = tk.Label(ventana, text="Solape logitudinal(%)")
lbl_solape_t = tk.Label(ventana, text="Solape transversal(%)")
lbl_largo_parcela = tk.Label(ventana, text="Largo parcela(m)")
lbl_solape_l.grid( padx=padding, pady=padding, row=4, column=0)
lbl_solape_t.grid( padx=padding, pady=padding, row=4, column=1)
lbl_largo_parcela.grid( padx=padding, pady=padding, row=4, column=2)
#--------------------- FILA 5 (INPUTS) -----------------
txt_solape_l = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_solape_t = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_largo_parcela = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_solape_l.grid( padx=padding, pady=padding, row=5, column=0)
txt_solape_t.grid( padx=padding, pady=padding, row=5, column=1)
txt_largo_parcela.grid( padx=padding, pady=padding, row=5, column=2)
#--------------------- FILA 6 (LABELS) -----------------
lbl_ancho_parcela = tk.Label(ventana, text="Ancho parcela(m)")
lbl_velocidad_vuelo = tk.Label(ventana, text="Velocidad vuelo(m/s)")
lbl_RSI = tk.Label(ventana, text="RCI(mm)")
lbl_ancho_parcela.grid( padx=padding, pady=padding, row=6, column=0)
lbl_velocidad_vuelo.grid( padx=padding, pady=padding, row=6, column=1)
lbl_RSI.grid( padx=padding, pady=padding, row=6, column=2)
#--------------------- FILA 7 (INPUTS) -----------------
txt_ancho_parcela = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_velocidad_vuelo = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_RSI = tk.Entry(ventana, font= fuente_txt, justify= justificacion_txt)
txt_ancho_parcela.grid( padx=padding, pady=padding, row=7, column=0)
txt_velocidad_vuelo.grid( padx=padding, pady=padding, row=7, column=1)
txt_RSI.grid( padx=padding, pady=padding, row=7, column=2)
#--------------------- FILA 10 (VENTANA) ----------------------
out_text = tk.Text(ventana, background="#6c99bb", foreground="white", font= fuente_txt)
out_text.grid(pady=10, padx=10, row = 10, column=0, columnspan=3)

#--------------------- FILA 8 (BTN) -----------------
def calcular_GDS(altura_vuelo, focal, RSI):
    return ( (altura_vuelo * 100) / focal ) * RSI
def calcular_Escala_De_Vuelo(focal, altura_vuelo):
    return (1/((focal/1000)/altura_vuelo))
def calcular_Ancho_Imagen_Terreno(ancho_sensor, escalaDeVuelo):
    return (ancho_sensor * escalaDeVuelo)/1000
def calcular_Alto_Imagen_Terreno(alto_sensor, escalaDeVuelo):
    return (alto_sensor * escalaDeVuelo)/1000
def calcular_Base_Aerea(ancho_img, solape_l):
    return ancho_img * (1 - (solape_l/100))
def calcular_Distancia_Entre_Pasadas(alto_img, solape_t):
    return alto_img * (1 - (solape_t/100))
def calcular_Intervalo_Entre_Fotos(baseAerea, velocidad_vuelo):
    return baseAerea / velocidad_vuelo
def calcular_Numero_De_Pasadas(ancho_parcela, distanciaEntrePasadas):
    return ancho_parcela / distanciaEntrePasadas
def calcular_Fotos_Por_Pasadas(largo_parcela, baseAerea):
    return (largo_parcela/baseAerea) + 1
def calcular_Numero_Fotos_Vuelo(fotosPorPasada, numeroDePasadas):
    return fotosPorPasada * numeroDePasadas
def calcular_Distancia_Vuelo(numeroDePasadas, largo_parcela, ancho_parcela):
    return (numeroDePasadas * largo_parcela) + ancho_parcela
def calcular_Duracion_Vuelo(numeroDeFotosVuelo, intervaloEntreFotos ):
    return ( numeroDeFotosVuelo * intervaloEntreFotos ) / 60
def calcular():
    focal = float(txt_focal.get())
    ancho_img = float(txt_ancho_img.get())
    alto_img = float(txt_alto_img.get())
    ancho_sensor = float(txt_ancho_sensor.get())
    alto_sensor = float(txt_alto_sensor.get())
    altura_vuelo = float(txt_altura_vuelo.get())
    solape_l = float(txt_solape_l.get())
    solape_t = float(txt_solape_t.get())
    largo_parcela = float(txt_largo_parcela.get())
    ancho_parcela = float(txt_ancho_parcela.get())
    velocidad_vuelo = float(txt_velocidad_vuelo.get())
    RSI = float(txt_RSI.get())
    GDS = calcular_GDS(altura_vuelo, focal, RSI)
    escalaDeVuelo = calcular_Escala_De_Vuelo(focal, altura_vuelo)
    anchoImagenTerreno = calcular_Ancho_Imagen_Terreno(ancho_sensor, escalaDeVuelo)
    altoImagenTerreno = calcular_Alto_Imagen_Terreno(alto_sensor, escalaDeVuelo)
    baseAerea = calcular_Base_Aerea(anchoImagenTerreno, solape_l)
    distanciaEntrePasadas = calcular_Distancia_Entre_Pasadas(altoImagenTerreno, solape_t)
    intervaloEntreFotos = calcular_Intervalo_Entre_Fotos(baseAerea, velocidad_vuelo)
    numeroDePasadas = calcular_Numero_De_Pasadas(ancho_parcela, distanciaEntrePasadas)
    fotosPorPasada = calcular_Fotos_Por_Pasadas(largo_parcela, baseAerea)
    numeroDeFotosVuelo = calcular_Numero_Fotos_Vuelo(fotosPorPasada, numeroDePasadas)
    distanciaVuelo = calcular_Distancia_Vuelo(numeroDePasadas, largo_parcela, ancho_parcela)
    duracionDeVuelo = calcular_Duracion_Vuelo(numeroDeFotosVuelo, intervaloEntreFotos )
    out_text.config(state="normal")
    out_text.delete('1.0', tk.END)
    out_text.insert(tk.END, "GDS: {}\n\n".format(GDS))
    out_text.insert(tk.END, "escalaDeVuelo: {}\n\n".format(escalaDeVuelo))
    out_text.insert(tk.END, "anchoImagenTerreno: {}\n\n".format(anchoImagenTerreno))
    out_text.insert(tk.END, "altoImagenTerreno: {}\n\n".format(altoImagenTerreno))
    out_text.insert(tk.END, "baseAerea: {}\n\n".format(baseAerea))
    out_text.insert(tk.END, "distanciaEntrePasadas: {}\n\n".format(distanciaEntrePasadas))
    out_text.insert(tk.END, "intervaloEntreFotos: {}\n\n".format(intervaloEntreFotos))
    out_text.insert(tk.END, "numeroDePasadas: {}\n\n".format(numeroDePasadas))
    out_text.insert(tk.END, "fotosPorPasada: {}\n\n".format(fotosPorPasada))
    out_text.insert(tk.END, "numeroDeFotosVuelo: {}\n\n".format(numeroDeFotosVuelo))
    out_text.insert(tk.END, "distanciaVuelo: {}\n\n".format(distanciaVuelo))
    out_text.insert(tk.END, "duracionDeVuelo: {}\n\n".format(duracionDeVuelo))
    out_text.config(state="disable")
botonDir = tk.Button(text = "Calcular", command = calcular).grid( padx=padding, pady=padding, row = 8 , column = 1 )



##Lanzar el GUI
ventana.mainloop()
