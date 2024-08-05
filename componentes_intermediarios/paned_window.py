import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.pwd_left = tk.PanedWindow(self.janela, showhandle=True, bd=10,
                                                                     bg='red')
        self.lbl_left = tk.Label(self.pwd_left, text='Left')
        self.pwd_right = tk.PanedWindow(self.janela, orient=tk.VERTICAL, bd=5,
                                                                    bg='green')
        self.lbl_right = tk.Label(self.pwd_right, text='Right')
        self.lbl_right2 = tk.Label(self.pwd_right, text='Right 2')

        self.pwd_left.add(self.lbl_left)
        self.pwd_right.add(self.lbl_right)
        self.pwd_right.add(self.lbl_right2)
        self.pwd_left.add(self.pwd_right)
        self.pwd_left.pack(fill=tk.BOTH, expand=True)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()