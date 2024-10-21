import tkinter as tk

janela = tk.Tk()

frame = tk.Frame(janela)
btn = tk.Button(janela, text='Centro')
btn.pack()
#Primeira forma
#janela.eval('tk::PlaceWindow . center')

frame.pack()
#Segunda forma
w = 600 #janela.winfo_reqwidth()
h = 300 #janela.winfo_reqheight()
ws = janela.winfo_screenwidth()
hs = janela.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
#print(w, h, x, y)
janela.geometry('%dx%d+%d+%d' % (w, h, x, y))

janela.mainloop()