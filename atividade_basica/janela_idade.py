import tkinter as tk
import datetime
class Tela:
    def __init__(self, master):
        self.janela = master
        #dia
        self.dia = tk.IntVar()
        self.spb_dia = tk.Spinbox(self.janela, from_=1, to=31, fg='white',
                                  textvariable=self.dia)
        self.spb_dia.pack()
        #mes
        self.mes = tk.IntVar()
        self.scl_mes = tk.Scale(self.janela, from_=1, to=12, variable=self.mes)
        self.scl_mes.pack()
        #ano
        self.ano = tk.StringVar()
        self.ent_ano = tk.Entry(self.janela, width=5, textvariable=self.ano)
        self.ent_ano.pack()
        self.btn_calcular = tk.Button(self.janela, text='Calcular Idade', command=self.calcular_idade)
        self.btn_calcular.pack()
        self.lbl_idade = tk.Label(self.janela)
        self.lbl_idade.pack()

    def calcular_idade(self):
        dia_nasc = self.dia.get()
        mes_nasc = self.mes.get()
        ano_nasc = int(self.ano.get())
        hoje = datetime.date.today()
        diff_dias = hoje.day - dia_nasc
        diff_meses = hoje.month - mes_nasc
        diff_anos = hoje.year - ano_nasc
        if diff_dias < 0:
            diff_meses -= 1
            diff_dias += 31
        if diff_meses < 0:
            diff_anos -= 1
            diff_meses += 12

        total = diff_anos * 365 + diff_meses * 31 + diff_dias
        resultado = (f'Idade: {diff_anos} anos, {diff_meses} meses e {diff_dias} dias ou {total} dias')
        self.lbl_idade.config(text=resultado)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
