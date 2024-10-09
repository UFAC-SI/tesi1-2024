import ttkbootstrap as ttk

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
        btn_cadastrar = ttk.Button(frm_botoes, text='Cadastrar', style='dark')
        btn_cadastrar.grid(row=0, column=0, padx=5, pady=5)
        btn_excluir = ttk.Button(frm_botoes, text='Excluir', style='dark')
        btn_excluir.grid(row=0, column=1, padx=5, pady=5)
        btn_editar = ttk.Button(frm_botoes, text='Editar', style='dark')
        btn_editar.grid(row=0, column=2, padx=5, pady=5)

app = ttk.Window(themename='litera')
Tela(app)
app.mainloop()