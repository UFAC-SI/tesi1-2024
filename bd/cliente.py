from tkinter import messagebox

import ttkbootstrap as ttk

from bd.crud import Crud


class Tela():
    def __init__(self, master):
        self.janela = master
        colunas = ('id', 'nome', 'cpf', 'email')
        self.tvw = ttk.Treeview(self.janela, columns=colunas, height=5, show='headings', style='dark')
        self.tvw.grid()
        #Cabeçalho
        self.tvw.heading('id', text='ID')
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.heading('email', text='E-mail')
        #Colunas
        self.tvw.column('id', minwidth=30, width=30)
        self.tvw.column('nome', minwidth=200, width=200)
        self.tvw.column('cpf', minwidth=100, width=100)
        self.tvw.column('email', minwidth=300, width=300)

        #Barra de rolagem
        scb = ttk.Scrollbar(self.janela, orient=ttk.VERTICAL, command=self.tvw.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.tvw.config(yscrollcommand=scb.set)
        #Botões
        frm_botoes = ttk.Frame(self.janela)
        frm_botoes.grid(row=1, column=0)
        btn_cadastrar = ttk.Button(frm_botoes, text='Cadastrar',
                                   style='dark', command=self.cadastrar_cliente)
        btn_cadastrar.grid(row=0, column=0, padx=5, pady=5)
        btn_excluir = ttk.Button(frm_botoes, text='Excluir', style='dark')
        btn_excluir.grid(row=0, column=1, padx=5, pady=5)
        btn_editar = ttk.Button(frm_botoes, text='Editar', style='dark')
        btn_editar.grid(row=0, column=2, padx=5, pady=5)
        self.crud = Crud()
        self.atualizar_treeview()

    def cadastrar_cliente(self):
        def confirmar_cadastro():
            nome = ent_nome.get()
            cpf = ent_cpf.get()
            email = ent_email.get()
            sql = f"""INSERT INTO cliente (nome, cpf, email) 
                      VALUES ('{nome}', '{cpf}', '{email}');"""
            if nome == '' or cpf == '' or email == '':
                messagebox.showwarning('Aviso', 'Todos os campos são '
                                                'obgrigatórios!',
                                       parent=self.top_cadastrar)
            else:
                if self.crud.insert(sql) == 1:
                    messagebox.showinfo('Info', 'Cliente inserido com sucesso!')
                    self.atualizar_treeview()
                else:
                    messagebox.showwarning('Aviso', 'Cliente não inserido.')
                self.top_cadastrar.destroy()


        self.top_cadastrar = ttk.Toplevel()
        self.top_cadastrar.grab_set()
        lbl_nome = ttk.Label(self.top_cadastrar, text='Nome:')
        lbl_nome.grid(row=0, column=0)
        lbl_cpf = ttk.Label(self.top_cadastrar, text='CPF:')
        lbl_cpf.grid(row=1, column=0)
        lbl_email = ttk.Label(self.top_cadastrar, text='Email:')
        lbl_email.grid(row=2, column=0)
        ent_nome = ttk.Entry(self.top_cadastrar)
        ent_nome.grid(row=0, column=1)
        ent_cpf = ttk.Entry(self.top_cadastrar)
        ent_cpf.grid(row=1, column=1)
        ent_email = ttk.Entry(self.top_cadastrar)
        ent_email.grid(row=2, column=1)
        btn_salvar = ttk.Button(self.top_cadastrar, text='Salvar',
                                command=confirmar_cadastro)
        btn_salvar.grid(row=3, column=1)


    def atualizar_treeview(self):
        #Limpa os dados do treeview
        linhas = self.tvw.get_children()
        for linha in linhas:
            self.tvw.delete(linha)
        #Carrega os dados do banco no treeview
        sql = "SELECT * FROM cliente;"
        dados = self.crud.get(sql) #Lista de tuplas
        for cliente in dados:
            self.tvw.insert('', 'end', values=cliente)

app = ttk.Window(themename='litera')
Tela(app)
app.mainloop()