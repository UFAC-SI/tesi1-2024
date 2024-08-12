import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Cadastro de Funcionários')
        self.menu_barra = tk.Menu(self.janela)
        self.menu_cadastro = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(menu=self.menu_cadastro, label='Cadastro')
        self.menu_cadastro.add_command(label='Funcionário',
                                       command=self.cadastrar)
        self.janela.config(menu=self.menu_barra)

    def cadastrar(self):
        self.top_cadastro = tk.Toplevel(self.janela)
        self.lbl_nome = ttk.Label(self.top_cadastro, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        self.ent_nome = ttk.Entry(self.top_cadastro)
        self.ent_nome.grid(row=0, column=1)
        self.lbl_doc = ttk.Label(self.top_cadastro, text='Doc:')
        self.lbl_doc.grid(row=1, column=0)
        self.ent_doc = ttk.Entry(self.top_cadastro)
        self.ent_doc.grid(row=1, column=1)
        self.btn_confirmar = ttk.Button(self.top_cadastro, text='Confirmar',
                                        command=self.confirmar)
        self.btn_confirmar.grid(row=2, column=0, columnspan=3, sticky=tk.EW)
        #Tabela
        colunas = ['id', 'nome', 'doc']
        self.tvw_func = ttk.Treeview(self.top_cadastro, columns=colunas,
                                     show='headings')
        #Cabeçalho
        self.tvw_func.heading('id', text='ID')
        self.tvw_func.heading('nome', text='NOME')
        self.tvw_func.heading('doc', text='DOCUMENTO')
        #Colunas
        self.tvw_func.column('id', width=25)
        self.tvw_func.column('nome', width=200)
        self.tvw_func.column('doc', width=100)
        self.tvw_func.grid(row=3, column=0, columnspan=2)
        self.contador=0

        #Barra de Rolagem
        self.scb_barra = ttk.Scrollbar(self.top_cadastro,
                                       command=self.tvw_func.yview)
        self.scb_barra.grid(row=3, column=2, sticky=tk.NS)
        self.tvw_func.config(yscrollcommand=self.scb_barra.set)

    def confirmar(self):
        self.contador += 1
        #self.tvw_func.insert(id_pai, posição da linha na tabela, valores)
        self.tvw_func.insert('', 'end', values=(self.contador,
                                                self.ent_nome.get(),
                                                self.ent_doc.get()))


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()