import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.ts = ttk.Style() #instância que define os temas
        temas = self.ts.theme_names()#os nomes dos temas
        self.tema = tk.StringVar()
        self.combobox = ttk.Combobox(self.janela, textvariable=self.tema,
                                     values=temas)
        self.combobox.pack()
        self.combobox.bind('<<ComboboxSelected>>', self.alterar_tema)
        self.btn = ttk.Button(self.janela, text='Teste de Tema').pack()

    def alterar_tema(self, event):
        self.ts.theme_settings(self.tema.get(), {"TButton" :{"configure": {
            "background": 'red'}}})
        self.ts.theme_use(self.tema.get())
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()