import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master):
        self.janela = master
        hino = """
        Uma vez Flamengo,
        Sempre Flamengo,
        Flamengo sempre eu ei de ser,
        É o meu maior prazer,
        Vê-lo brilhar,
        Seja na terra, seja no mar,
        Vencer, vencer, vencer....
        """
        self.scr_musica = tk.Scrollbar(self.janela)
        self.txt_musica = tk.Text(self.janela,
                                  height=4,
                                  #width=40,
                                  yscrollcommand=self.scr_musica.set)
        self.txt_musica.pack(side=tk.LEFT, fill=tk.BOTH)
        self.txt_musica.insert(tk.END, hino)
        self.scr_musica.config(command=self.txt_musica.yview)
        self.scr_musica.pack(side=tk.RIGHT, fill=tk.Y)

        self.txt_scrolledtext = (ScrolledText(self.janela))
        self.txt_scrolledtext.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()