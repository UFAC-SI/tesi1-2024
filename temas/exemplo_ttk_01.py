import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Window #Importação necessária no sistema Windows
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn1 = ttk.Button(self.janela, text='Botão 1', bootstyle=SUCCESS)
        self.btn1.pack()
        self.btn2 = ttk.Button(self.janela, text='Botão 2',
                               bootstyle="info-outline")
        self.btn2.pack()
#A criação da janela deve ser realizada com a classe Window da biblioteca TTKbootstrap
janela = ttk.Window(themename="superhero")#tk.Tk()
app = Tela(janela)
janela.mainloop()