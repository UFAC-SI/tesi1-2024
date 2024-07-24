import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.escolha = tk.IntVar(value=-1)
        self.rbt_sim = tk.Radiobutton(self.janela, text='Sim',
                                      variable=self.escolha, value=1,
                                      command=self.habilitar)
        self.rbt_sim.pack()
        self.rbt_nao = tk.Radiobutton(self.janela, text='Não',
                                      variable=self.escolha, value=0,
                                      command=self.desabilitar)
        self.rbt_nao.pack()

        self.noticia = tk.IntVar()
        self.cbt_noticia = tk.Checkbutton(self.janela, text='Noticia',
                                          variable=self.noticia,
                                          state='disabled')
        self.cbt_noticia.pack()
        self.btn_mostrar = tk.Button(self.janela, text='Mostrar',
                                     command=self.mostrar)
        self.btn_mostrar.pack()
        self.lbl_mostrar = tk.Label(self.janela)
        self.lbl_mostrar.pack()

    def habilitar(self):
        if self.escolha.get()==1:
            self.cbt_noticia.config(state='normal')

    def desabilitar(self):
        if self.escolha.get()==0:
            self.cbt_noticia.config(state='disabled')
            self.noticia.set(0)
            self.lbl_mostrar.config(text='')

    def mostrar(self):
        if self.noticia.get() == 1:
            self.lbl_mostrar.config(text='Alguma notícia...')




janela = tk.Tk()
app = Tela(janela)
janela.mainloop()