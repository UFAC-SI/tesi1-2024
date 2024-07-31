import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Gerenciador Pack')
        self.lbl_red =tk.Label(self.janela, text='Red', bg='red')
        self.lbl_red.pack(fill=tk.BOTH, expand=True)
        self.lbl_green = tk.Label(self.janela, text='Green', bg='green')
        self.lbl_green.pack(fill=tk.BOTH, expand=True)
        self.lbl_blue = tk.Label(self.janela, text='Blue', bg='blue')
        self.lbl_blue.pack(fill=tk.BOTH, expand=True)
        self.lbl_grey_left = tk.Label(self.janela, text='Grey Left', bg='grey')
        self.lbl_grey_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.lbl_grey_right = tk.Label(self.janela, text='Grey Right',
                                       bg='grey')
        self.lbl_grey_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.lbl_black = tk.Label(self.janela, text='Black', bg='black')
        self.lbl_black.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.lbl_cyan = tk.Label(self.janela, text='Cyan', bg='cyan',
                                 fg='black')
        self.lbl_cyan.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.yellow = tk.Label(self.janela, text='Yellow', bg='yellow',
                               fg='black')
        self.yellow.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.lbl_magenta = tk.Label(self.janela, text='Magenta',
                                    bg='magenta', fg='black')
        self.lbl_magenta.pack(fill=tk.BOTH, expand=True)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()