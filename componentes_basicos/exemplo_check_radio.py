import tkinter as tk

class Tela:
    def clicou_check(self):
        if self.var_brasil.get() == 1 and self.var_argentina.get() == 0:
            self.lbl_mostrar_check['text'] = 'Nunca Será'
        elif self.var_argentina.get() == 1 and self.var_brasil.get() == 0:
            self.lbl_mostrar_check.config(text='Campeão')
        else:
            self.lbl_mostrar_check.config(text='')

    def clicou_radio(self):
        self.lbl_mostrar_radio.config(text=self.carioca.get())

    def __init__(self, master):
        self.janela = master
        self.var_brasil = tk.IntVar()
        self.var_argentina = tk.IntVar()
        #Botões de check
        self.cbt_brasil = tk.Checkbutton(self.janela,
                                         text='Brasil',
                                         variable=self.var_brasil,
                                         command=self.clicou_check)
        self.cbt_brasil.pack()
        self.cbt_argentina = tk.Checkbutton(self.janela,
                                            text='Argentina',
                                            variable=self.var_argentina,
                                            command=self.clicou_check)
        self.cbt_argentina.pack()
        self.lbl_mostrar_check = tk.Label(self.janela,
                                          foreground='white')
        self.lbl_mostrar_check.pack()
        #Botões de radio
        # valor = [1,2]
        # self.rbt_1 = tk.Radiobutton(self.janela, text='Um',
        #                             value=valor[0],
        #                             selectcolor='red').pack()
        # self.rbt_2 = tk.Radiobutton(self.janela,
        #                             text='Dois',
        #                             value=valor[1],
        #                             selectcolor='red').pack()
        #Automatizar a criação dos botões de radio
        dicionario = {1:'Flamengo', 2:'Vasco', 3:'Botafogo'}
        self.carioca = tk.StringVar()
        for (v, t) in dicionario.items():
            self.rbt = tk.Radiobutton(self.janela, text=t,
                                      selectcolor='red', value=v,
                                      variable=self.carioca,
                                      command=self.clicou_radio).pack()

        self.lbl_mostrar_radio = tk.Label(self.janela)
        self.lbl_mostrar_radio.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()