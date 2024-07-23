import tkinter as tk

class Tela:
    def abrir(self):
        lista = ['Flamengo', 'Vasco', 'Botafogo']
        valores = [i for i in range(1, 13)]
        mes = tk.StringVar()
        self.spb_meses = tk.Spinbox(self.janela, values=valores,
                                    wrap=True, state="readonly",
                                    fg='black', textvariable=mes)
        self.spb_meses.pack()
        dia = tk.StringVar()
        self.scl_dias = tk.Scale(self.janela, from_= 1, to=31,
                                 variable=dia)
        self.scl_dias.pack()

    def __init__(self, master):
        self.janela = master
        self.mnu_barra = tk.Menu(self.janela) #barra
        self.mnu_arquivo = tk.Menu(self.mnu_barra, tearoff=0) #item
        self.mnu_editar = tk.Menu(self.mnu_barra) #item
        self.mnu_barra.add_cascade(label='Arquivo', menu=self.mnu_arquivo) #label
        self.mnu_barra.add_cascade(label='Editar', menu=self.mnu_editar) #label
        self.mnu_arquivo.add_command(label='Salvar') #comandos
        self.mnu_arquivo.add_separator()
        self.mnu_arquivo.add_command(label='Abrir', command=self.abrir)
        self.mnu_editar.add_command(label='Copiar')
        self.mnu_editar.add_command(label='Colar')

        self.janela.config(menu=self.mnu_barra) #adiciona na janela

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
