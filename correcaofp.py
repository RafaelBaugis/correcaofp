import math
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Potência Ativa
        self.potencia_ativa_label = tk.Label(self)
        self.potencia_ativa_label["text"] = "Potência Ativa (kW):"
        self.potencia_ativa_label.pack(side="top")

        self.potencia_ativa_entry = tk.Entry(self)
        self.potencia_ativa_entry.pack(side="top")

        # Tensão
        self.tensao_label = tk.Label(self)
        self.tensao_label["text"] = "Tensão (V):"
        self.tensao_label.pack(side="top")

        self.tensao_entry = tk.Entry(self)
        self.tensao_entry.pack(side="top")

        # Corrente
        self.corrente_label = tk.Label(self)
        self.corrente_label["text"] = "Corrente (A):"
        self.corrente_label.pack(side="top")

        self.corrente_entry = tk.Entry(self)
        self.corrente_entry.pack(side="top")

        # Frequência
        self.frequencia_label = tk.Label(self)
        self.frequencia_label["text"] = "Frequência (Hz):"
        self.frequencia_label.pack(side="top")

        self.frequencia_entry = tk.Entry(self)
        self.frequencia_entry.pack(side="top")

        # Botão Calcular
        self.calcular_button = tk.Button(self)
        self.calcular_button["text"] = "Calcular"
        self.calcular_button["command"] = self.calcular_fator_de_potencia
        self.calcular_button.pack(side="top")

    def calcular_fator_de_potencia(self):
        potencia_ativa = float(self.potencia_ativa_entry.get())
        tensao = float(self.tensao_entry.get())
        corrente = float(self.corrente_entry.get())
        frequencia = float(self.frequencia_entry.get())

        pf = abs(math.cos(math.atan(potencia_ativa / (tensao * corrente))))
        
        s = abs(tensao * corrente) / 1000
        
        q = math.sqrt(abs(s ** 2 - potencia_ativa ** 2))
        
        qc = q - potencia_reativa(0.95 * potencia_ativa, s)
        
        c = abs((1000000000 * qc) / (2 * math.pi * frequencia * tensao ** 2))

        resultado_texto = "Fator de Potência: {:.3f}\n".format(pf)
        
        resultado_texto += "Potência Aparente: {:.3f} kVA\n".format(s)
        
        resultado_texto += "Potência Reativa: {:.3f} kVAR\n".format(q)
        
        resultado_texto += "Capacitância do Capacitor: {:.3f} uF".format(c)

        resultado_window = tk.Toplevel(self.master)

        resultado_label = tk.Label(resultado_window, text=resultado_texto)
        
        resultado_label.pack()

def potencia_reativa(potencia_ativa, s):
    return math.sqrt(abs(s ** 2 - potencia_ativa ** 2))

root = tk.Tk()
app = Application(master=root)
app.mainloop()
