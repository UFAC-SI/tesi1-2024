import threading
import time
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
v = tk.IntVar()
parou = 0


def thread():
    global parou
    parou = 0
    th = threading.Thread(target=iniciar)
    th.start()
def parar():
    global parou
    parou = 1
def reiniciar():
    parar()
    v.set(0)
    lbl.config(text='0%')

def iniciar():
    global v
    valor = 0
    if v.get() > 0:
        valor = v.get()
    for i in range(valor, 101):
        if parou == 1:
            break
        v.set(i)
        lbl.config(text=f"{prb['value']}%")
        time.sleep(0.05)

prb = ttk.Progressbar(janela, mode='determinate', maximum=100, variable=v, length=200)
prb.grid(row=0, column=0, columnspan=3)
lbl = tk.Label(janela, text='0%')
lbl.grid(row=0, column=3)
btn_start = tk.Button(janela, text='Start', command=thread).grid(row=1, column=0)
btn_stop = tk.Button(janela, text='Stop', command=parar).grid(row=1, column=1)
btn_restart = tk.Button(janela, text='Restart', command=reiniciar)
btn_restart.grid(row=1, column=2)
janela.mainloop()