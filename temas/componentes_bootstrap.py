from datetime import datetime

import ttkbootstrap as ttk
from yt_dlp.utils import datetime_add_months


class Tela:
    def __init__(self, master):
        self.janela = master
        cbt1 = ttk.Checkbutton(self.janela, text='Bolo', style='roundtoggle')
        cbt1.pack()
        cbt2 = ttk.Checkbutton(self.janela, text='Café',
                               style='danger.squaretoggle')
        cbt2.pack()
        lbl = ttk.Label(self.janela, text='Data:', style='inverse-danger')
        lbl.pack()
        den = ttk.DateEntry(self.janela, dateformat='%Y-%m-%d',
                            firstweekday=6, startdate=datetime(2024,12,10),
                            bootstyle='danger')
        den.pack()
        met = ttk.Meter(self.janela, subtext='Velocidade',
                        subtextstyle='warning', bootstyle='warning',
                        interactive=True, stepsize=5, metersize=200)
        met.pack()
        fdg = ttk.Floodgauge(self.janela, mode='determinate', value=0,
                             mask='{}% de tranferência', maximum=100)
        fdg.pack()
        btn1 = ttk.Button(self.janela, text='Start', style='success',
                          command=fdg.start)
        btn1.pack()
        btn2 = ttk.Button(self.janela, text='Stop', style='danger',
                          command=fdg.stop)
        btn2.pack()
        btn3 = ttk.Button(self.janela, text='Step', style='info',
                          command=fdg.step)
        btn3.pack()


janela = ttk.Window(themename="superhero")
app = Tela(janela)
janela.mainloop()