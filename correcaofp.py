import math
import tkinter as tk

def capacitancia_correcao_fator_potencia():
    tensao = float(entry_tensao.get())
    corrent = float(entry_corrent.get())
    frequencia = float(entry_frequencia.get())
    fator_potencia_corrigido = float(entry_fator_potencia_corrigido.get())
    potencia_real = tensao * corrent
    potencia_aparente = potencia_real / fator_potencia_corrigido
    potencia_reativa = math.sqrt(potencia_aparente ** 2 - potencia_real ** 2)
    q_corrigido = potencia_reativa
    q = q_corrigido + (potencia_aparente * math.sin(math.acos(fator_potencia_corrigido)))
    c = (1000000 * q) / (2 * math.pi * frequencia * tensao ** 2)
    label_resultado.config(text=f"Capacitância necessária: {c:.2f} uF")

janela = tk.Tk()
janela.title("Cálculo de Capacitor")

label_tensao = tk.Label(janela, text="Tensão de trabalho (V):")
label_tensao.pack()

entry_tensao = tk.Entry(janela)
entry_tensao.pack()

label_corrent = tk.Label(janela, text="Potencia (A):")
label_corrent.pack()

entry_corrent = tk.Entry(janela)
entry_corrent.pack()

label_frequencia = tk.Label(janela, text="Frequência (Hz):")
label_frequencia.pack()

entry_frequencia = tk.Entry(janela)
entry_frequencia.pack()

label_fator_potencia_corrigido = tk.Label(janela, text="Fator potencia desejado (fP):")
label_fator_potencia_corrigido.pack()

entry_fator_potencia_corrigido = tk.Entry(janela)
entry_fator_potencia_corrigido.pack()

botao_calcular = tk.Button(janela, text="Calcular", command=capacitancia_correcao_fator_potencia)
botao_calcular.pack()

label_resultado = tk.Label(janela)
label_resultado.pack()

janela.mainloop()