import tkinter as tk
from tkinter import ttk, messagebox

from PyQt5.QtWidgets import QMessageBox


class Tela:
    def __init__(self, master):
        self.janela = master
        valores = [10,20,30]
        self.cbx = ttk.Combobox(self.janela, values=valores)
        self.cbx.pack()
        self.lbl = ttk.Label(self.janela)
        self.lbl.pack()
        self.cbx.bind('<<ComboboxSelected>>', self.mostrar)

    def mostrar(self, event):
        self.lbl.config(text=self.cbx.get())
        messagebox.showinfo('Infor', self.cbx.get(), parent=self.janela)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()