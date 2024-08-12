import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Tela:
    def mostrar(self):
        messagebox.showinfo('Informação', self.d.get())

    def __init__(self, master):
        self.janela = master
        self.d = tk.StringVar()
        dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
        self.cbx_dias = ttk.Combobox(self.janela,
                                     values=dias,
                                     state='readonly',
                                     textvariable=self.d)
        self.cbx_dias.current(6)
        #self.cbx_dias.set('Dias da Semana')
        self.cbx_dias.pack()
        self.btn_mostrar = ttk.Button(self.janela, text='Mostrar',
                                      command=self.mostrar)
        self.btn_mostrar.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()