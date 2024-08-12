import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        colunas = ['nome', 'email', 'telefone']

        self.tvw_pessoas = ttk.Treeview(self.janela,
                                        show='headings',
                                        columns=colunas,
                                        height=5)
        #cabeçalho
        self.tvw_pessoas.heading(0, text='Nome')
        self.tvw_pessoas.heading('email', text='E-mail')
        self.tvw_pessoas.heading(2, text='Telefone')
        #colunas
        self.tvw_pessoas.column('nome', minwidth=0, width=200)
        self.tvw_pessoas.column('telefone', minwidth=0, width=100)
        #conteúdo
        self.tvw_pessoas.insert('', 'end', values=('Fulano','fulano@ufac.br'))
        self.tvw_pessoas.insert('', 'end', values=('Ciclano', 'fulano@ufac.br'))
        self.tvw_pessoas.insert('', 'end', values=('Beltrano',
                                                   'fulano@ufac.br'))
        self.tvw_pessoas.insert('', 'end', values=('Teste', 'teste@ufac.br',
                                                   '68-99999900'))
        self.tvw_pessoas.insert('', 'end', values=('Teste', 'teste@ufac.br',
                                                   '68-99999900'))
        self.tvw_pessoas.insert('', 'end', values=('Invisível', 'teste@ufac.br',
                                                   '68-99999900'))

        # pai = self.tvw_pessoas.insert('', 'end', text='Pessoas')
        # self.tvw_pessoas.insert(pai, 'end', text='Claudionor')
        # self.tvw_pessoas.insert(pai, 'end', text='Macilon')
        self.tvw_pessoas.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()