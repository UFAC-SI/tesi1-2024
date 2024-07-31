import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x200')
        #exemplo de LabelFrame
        self.frm_left = tk.LabelFrame(self.janela, text='Título',
                                      labelanchor='nw')
        self.frm_left.pack(side=tk.LEFT)
        #self.frm_left.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
        self.frm_right = tk.Frame(self.janela, bg='blue', bd=10)
        #self.frm_right.place(relx=0.51, rely=0.99)
        self.frm_right.pack(side=tk.LEFT)
        #componentes do frm_left
        self.btn1 = tk.Button(self.frm_left, text='Botão 1')
        self.btn1.pack(side=tk.LEFT, padx=10)
        self.btn2 = tk.Button(self.frm_left, text='Botão 2')
        self.btn2.pack(side=tk.LEFT, padx=10)
        # componentes do frm_right
        self.btn3 = tk.Button(self.frm_right, text='Botão 3')
        self.btn3.pack()
        self.btn4 = tk.Button(self.frm_right, text='Botão 4')
        self.btn4.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()