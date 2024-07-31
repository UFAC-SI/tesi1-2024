import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Gerenciador Grid')
        self.btn1 = tk.Button(self.janela, text='1')
        self.btn1.grid(row=0, column=1)
        self.btn2 = tk.Button(self.janela, text='2')
        self.btn2.grid(row=1, column=0, columnspan=2)
        self.btn3 = tk.Button(self.janela, text='3')
        self.btn3.grid(row=1, column=1, columnspan=2)
        self.btn4 = tk.Button(self.janela, text='4')
        self.btn4.grid(row=2, column=0)
        self.btn5 = tk.Button(self.janela, text='5')
        self.btn5.grid(row=2, column=1)
        self.btn6 = tk.Button(self.janela, text='6')
        self.btn6.grid(row=2, column=2)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()