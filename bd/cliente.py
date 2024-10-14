from tkinter import messagebox

import ttkbootstrap as ttk

from bd.crud import Crud


class Tela():
    def __init__(self, master):
        self.janela = master
        colunas = ('id', 'nome', 'cpf', 'email')
        self.tvw = ttk.Treeview(self.janela, columns=colunas, selectmode='browse', height=5, show='headings', style='dark')
        self.tvw.grid(row=0, column=0)
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

        self.ent_pesquisar = ttk.Entry(self.janela)
        self.ent_pesquisar.grid(row=1, column=0, columnspan=2)
        #Botões
        frm_botoes = ttk.Frame(self.janela)
        frm_botoes.grid(row=2, column=0)
        btn_cadastrar = ttk.Button(frm_botoes, text='Cadastrar',
                                   style='dark', command=self.cadastrar_cliente)
        btn_cadastrar.grid(row=0, column=0, padx=5, pady=5)
        btn_excluir = ttk.Button(frm_botoes, text='Excluir', style='dark', command=self.excluir_cliente)
        btn_excluir.grid(row=0, column=1, padx=5, pady=5)
        btn_editar = ttk.Button(frm_botoes, text='Editar', style='dark', command=self.editar_cliente)
        btn_editar.grid(row=0, column=2, padx=5, pady=5)
        btn_pesquisar = ttk.Button(frm_botoes, text='Pesquisar', style='dark', command=self.pesquisar_cliente)
        btn_pesquisar.grid(row=0, column=3)
        self.termo = self.ent_pesquisar.get()
        # if termo == '':
        #     self.sql_atualiza = f"SELECT * FROM cliente;"
        # else:
        #     self.sql_atualiza = f"SELECT * FROM cliente WHERE nome LIKE '%{termo}%'"
        self.crud = Crud()
        self.atualizar_treeview()

    def pesquisar_cliente(self):
        #termo = self.ent_pesquisar.get()
        # if termo == '':
        #     self.sql_atualiza = f"SELECT * FROM cliente;"
        # else:
        #     self.sql_atualiza = f"SELECT * FROM cliente WHERE nome LIKE '%{termo}%'"
        self.atualizar_treeview()

    def editar_cliente(self):
        def confirmar_edicao():
            nome = ent_nome.get()
            cpf = ent_cpf.get()
            email = ent_email.get()
            if nome == '' or cpf == '' or email == '':
                messagebox.showwarning('Aviso', 'Fala que tá errado!')
            else:
                sql = f"""UPDATE cliente SET nome='{nome}', cpf='{cpf}', email='{email}'
                          WHERE id={tupla_id}
                       """
                if self.crud.update(sql) == 1:
                    messagebox.showinfo('Info', 'Cliente editado com sucesso!')
                    self.top_editar.destroy()
                    self.ent_pesquisar.delete('0', 'end')
                    self.atualizar_treeview()

        tupla = self.tvw.selection()
        dados = self.tvw.item(tupla, 'values')
        tupla_id = dados[0]
        self.top_editar = ttk.Toplevel()
        self.top_editar.grab_set()
        lbl_nome = ttk.Label(self.top_editar, text='Nome:')
        lbl_nome.grid(row=0, column=0)
        lbl_cpf = ttk.Label(self.top_editar, text='CPF:')
        lbl_cpf.grid(row=1, column=0)
        lbl_email = ttk.Label(self.top_editar, text='Email:')
        lbl_email.grid(row=2, column=0)
        ent_nome = ttk.Entry(self.top_editar)
        ent_nome.insert('end', dados[1])
        ent_nome.grid(row=0, column=1)
        ent_cpf = ttk.Entry(self.top_editar)
        ent_cpf.insert('end', dados[2])
        ent_cpf.grid(row=1, column=1)
        ent_email = ttk.Entry(self.top_editar)
        ent_email.insert('end', dados[3])
        ent_email.grid(row=2, column=1)
        btn_salvar = ttk.Button(self.top_editar, text='Salvar',
                                command=confirmar_edicao)
        btn_salvar.grid(row=3, column=1)

    def excluir_cliente(self):
        tupla = self.tvw.selection()
        id = self.tvw.item(tupla, 'values')[0]
        nome = self.tvw.item(tupla, 'values')[1]
        sql = f'DELETE FROM cliente WHERE id={id};'
        confirma = messagebox.askyesno('Confirmação',
                                       f'Confirma a exclusão do cliente: {nome}?')
        if confirma:
            if self.crud.delete(sql) == 1:
                messagebox.showinfo('Info', 'Cliente excluído.')
                self.ent_pesquisar.delete('0', 'end')
                self.atualizar_treeview()
        # if len(tupla) != 1:
        #     messagebox.showwarning('Aviso', 'Selecione apenas um cliente!')
        # else:
        #     id = self.tvw.item(tupla, 'values')[0]
        #     nome = self.tvw.item(tupla, 'values')[1]
        #     sql = f'DELETE FROM cliente WHERE id={id};'
        #     confirma = messagebox.askyesno('Confirmação', f'Confirma a exclusão do cliente: {nome}?')
        #     if confirma:
        #         if self.crud.delete(sql) == 1:
        #             messagebox.showinfo('Info', 'Cliente excluído.')
        #             self.atualizar_treeview()

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
                    self.ent_pesquisar.delete('0', 'end')
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
        self.termo = self.ent_pesquisar.get()
        self.sql_atualiza = f"SELECT * FROM cliente WHERE nome LIKE '%{self.termo}%'"
        #Limpa os dados do treeview
        linhas = self.tvw.get_children()
        for linha in linhas:
            self.tvw.delete(linha)
        #Carrega os dados do banco no treeview
        #sql = "SELECT * FROM cliente;"
        dados = self.crud.get(self.sql_atualiza) #Lista de tuplas
        for cliente in dados:
            self.tvw.insert('', 'end', values=cliente)

app = ttk.Window(themename='litera')
Tela(app)
app.mainloop()