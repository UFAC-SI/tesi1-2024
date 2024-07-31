import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x200')
        self.frm_left = tk.LabelFrame(self.janela, text='Título', labelanchor='nw')
        self.frm_left.pack(side=tk.LEFT)
        self.frm_right = tk.Frame(self.janela, bg='blue', bd=10)
        self.frm_right.pack(side=tk.LEFT)
        self.btn1 = tk.Button(self.frm_left, text='Botão 1', command=self.abrir_janela)
        self.btn1.pack(side=tk.LEFT)

    def abrir_janela(self):
        #self.janela.withdraw() #Esconde a janela Tk
        self.janela.iconify()  #Minimiza a janela Tk
        self.toplevel = tk.Toplevel(self.janela)
        self.btn_fechar = tk.Button(self.toplevel, text='Fechar', command=self.fechar_janela)
        self.btn_fechar.pack()
        self.toplevel.grab_set() #Impede a interação com a janela Tk


    def fechar_janela(self):
        self.toplevel.destroy() #Destroi da toplevel
        #self.janela.deiconify() #Exibe a janela Tk, caso tenha usado iconify


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()