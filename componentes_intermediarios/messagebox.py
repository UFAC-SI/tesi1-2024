import tkinter as tk
from tkinter import messagebox
class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Abrir',
                             command=self.abrir_mensagem)
        self.btn.pack()

    def abrir_mensagem(self):
        messagebox.showinfo('Informação', 'Vc clicou no btn Abrir')
        messagebox.showwarning('Aviso', 'Vc foi avisado')
        messagebox.showerror('Erro', 'Vc me estressou')
        resposta = messagebox.askyesno('Confirmação', 'Deseja continuar?')
        #print(resposta)
        if resposta:
            messagebox.showinfo('Confirmou', 'Informação Confirmada')
        else:
            self.janela.destroy()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()