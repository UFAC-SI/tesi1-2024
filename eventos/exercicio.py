import tkinter as tk
from tkinter.scrolledtext import ScrolledText
class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn_tecla = tk.Button(self.janela, text='Pressione a '
                                                     'qualquer tecla')
        self.btn_tecla.pack()
        self.sct = ScrolledText(self.janela)
        self.sct.pack()
        self.btn_limpa = tk.Button(self.janela, text='Limpar')
        self.btn_limpa.pack()
        self.janela.bind('<Key>', self.teclar)
        self.btn_limpa.bind('<Button-1>', self.limpar)

    def teclar(self, event):
        conteudo = ''
        if event.char == event.keysym:
            conteudo = f'Tecla Normal: {event.char}\n'
        elif len(event.char) == 1:
            conteudo = f'Tecla de pontuação: {event.keysym} --> {event.char}\n'
        else:
            conteudo = f'Tecla especial: {event.keysym}\n'
        self.sct.insert(tk.END, conteudo)

    def limpar(self, event):
        self.sct.delete(0.0, tk.END) #Primeiro indice funciona representando
        # linhas e colunas do scrolledtext, segundo indice é o final

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()