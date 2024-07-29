import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x100')
        lbl1 = tk.Label(self.janela, text='Red qualquer coisa', bg='red')
        lbl1.grid(row=0, column=0)
        self.janela.columnconfigure(1, weight=1)
        self.janela.columnconfigure(2, weight=2)
        self.janela.columnconfigure(3, weight=2)

        lbl2 = tk.Label(self.janela, text='Black', bg='black')
        lbl2.grid(row=1, column=1, columnspan=2, sticky=tk.EW)
        lbl3 = tk.Label(self.janela, text='Yellow Teste column', bg='yellow')
        lbl3.grid(row=2, column=2, rowspan=2)
        lbl3 = tk.Label(self.janela, text='Blue', bg='blue')
        lbl3.grid(row=3, column=3)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()