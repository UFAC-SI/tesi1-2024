import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        lbl1 = tk.Label(self.janela, text='Label 1', bg='red')
        lbl1.place(x=10, y=10)
        lbl2 = tk.Label(self.janela, text='Label 2', bg='blue')
        lbl2.place(x=10, y=35)
        lbl3 = tk.Label(self.janela, text='Label 3', bg='yellow')
        lbl3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()