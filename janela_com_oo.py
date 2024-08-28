import tkinter as tk

class TelaPrincipal:
    def __init__(self, m):
        self.janela = m
        self.janela.geometry('300x500')
        self.janela.title("Janela com Orientação a Objetos")
        

j = tk.Tk() #instância de Tk
app = TelaPrincipal(j) #instância da nossa classe
j.mainloop()

