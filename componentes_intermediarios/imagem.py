import tkinter as tk
from PIL import Image, ImageTk
class Tela:
    def __init__(self, master):
        self.janela = master
        #self.img = tk.PhotoImage(file='logo-ufac.png')
        #self.img = self.img.subsample(4,4)
        #Usando a biblioteca PILLOW
        arquivo = Image.open('capivara-ufac.jpg')
        arquivo = arquivo.resize((400,400)) #redimensionando a img
        arquivo = arquivo.reduce(2)

        self.img = ImageTk.PhotoImage(arquivo)
        self.lbl = tk.Label(self.janela, image=self.img)
        self.lbl.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()