import tkinter as tk
from tkinter import messagebox
import Memoria_Facil

def abrir_seleccion_memoria():
    ventana_principal.withdraw()
    abrir_seleccion_dificultad()

def abrir_seleccion_dificultad():
    seleccion = tk.Toplevel()
    seleccion.title('Selecciona Dificultadd')
    seleccion.geometry('300x400')
    seleccion.resizable(False, False) 


    etiqueta = tk.Label(seleccion, text='Elige una dificultad', font=('Times New Roman', 16))
    etiqueta.pack(pady=20)

    btn_facil = tk.Button(seleccion, text='Fácil', font=('Arial', 14),
                          command=lambda: [seleccion.destroy(), abrir_memoria_facil()])
    btn_facil.pack(pady=10)
    btn_normal = tk.Button(seleccion, text='Normal', state='disabled')
    btn_normal.pack()
    btn_dificil = tk.Button(seleccion, text='Difícil', state='disabled')
    btn_dificil.pack()

def abrir_memoria_facil():
    Memoria_Facil.main(ventana_principal)  

ventana_principal = tk.Tk()
ventana_principal.title('Juegos')
ventana_principal.geometry('400x300')
ventana_principal.resizable(False, False)

titulo = tk.Label(ventana_principal, text='Selecciona un juego', font=('Times New Roman', 18))
titulo.pack(pady=20)

btn_memoria = tk.Button(ventana_principal, text='Juego de Memoria', font=('Times New Roman', 14),
                        width=20, command=abrir_seleccion_memoria)
btn_memoria.pack(pady=10)

btn_otro_juego1 = tk.Button(ventana_principal, text='Juego 2 (futuro)', state='disabled', width=20)
btn_otro_juego1.pack(pady=5)

btn_otro_juego2 = tk.Button(ventana_principal, text='Juego 3 (futuro)', state='disabled', width=20)
btn_otro_juego2.pack(pady=5)

ventana_principal.mainloop()
