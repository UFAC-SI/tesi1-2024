import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText
class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Abrir Arquivo')
        self.btn.bind('<Button-1>', self.abrir_arquivo)
        self.btn.pack()
        self.sct = ScrolledText(self.janela)
        self.sct.pack()
        self.btn_salvar = tk.Button(self.janela, text='Salvar')
        self.btn_salvar.pack()
        self.btn_salvar.bind('<Button-1>', self.salvar_arquivo)

    def salvar_arquivo(self, event):
        #pegar o conteúdo
        linhas = self.sct.get(0.0, tk.END)
        #escolher o local para salvar
        tipos = (('Texto', '.txt'), ('Python', '.py'))
        nome_arquivo = fd.asksaveasfilename(filetypes=tipos)
        #preencher o arquivo
        with open(nome_arquivo, 'w') as arq:
            arq.write(linhas)

    def abrir_arquivo(self, event):
        tipos = (('Texto', '.txt'), ('Python', '.py'), ('Todos', '.*'))
        #nome_arquivo = fd.askopenfilename(initialdir="/home/limeira", filetypes=tipos)
        #mb.showinfo('Informação', nome_arquivo)
        arquivo = fd.askopenfile(initialdir='/home/limeira', filetypes=tipos)
        with open(arquivo.name, 'r') as arq:
            for linha in arq:
                self.sct.insert(tk.END, linha)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()