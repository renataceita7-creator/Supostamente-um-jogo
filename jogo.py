import tkinter as tk
from tkinter import messagebox

class JogoGato:
    def __init__(self, root):
        self.root = root
        self.root.title("Meu Gato Virtual 🐱")
        self.root.geometry("300x350")
        
        # Atributos iniciais
        self.fome = 100
        self.felicidade = 100
        self.energia = 100
        
        # Elementos da Interface
        self.label_gato = tk.Label(root, text="🐱\n¡Miau! Estou feliz!", font=("Arial", 24))
        self.label_gato.pack(pady=20)
        
        self.label_status = tk.Label(root, text=self.obter_texto_status(), font=("Arial", 12))
        self.label_status.pack(pady=10)
        
        # Botões
        tk.Button(root, text="Alimentar", command=self.alimentar, width=15).pack(pady=5)
        tk.Button(root, text="Brincar", command=self.brincar, width=15).pack(pady=5)
        tk.Button(root, text="Dormir", command=self.dormir, width=15).pack(pady=5)
        
        # Loop para diminuir os status com o tempo
        self.atualizar_tempo()

    def obter_texto_status(self):
        return f"Fome: {self.fome}/100\nFelicidade: {self.felicidade}/100\nEnergia: {self.energia}/100"

    def atualizar_tela(self):
        self.label_status.config(text=self.obter_texto_status())
        
        # Mudar o emoji/estado dependendo da situação
        if self.fome < 30:
            self.label_gato.config(text="😿\nEstou com muita fome!")
        elif self.energia < 30:
            self.label_gato.config(text="😴\nEstou com sono...")
        else:
            self.label_gato.config(text="🐱\n¡Miau! Estou bem!")

    def alimentar(self):
        self.fome = min(100, self.fome + 20)
        self.atualizar_tela()

    def brincar(self):
        if self.energia > 20:
            self.felicidade = min(100, self.felicidade + 20)
            self.energia = max(0, self.energia - 15)
        else:
            messagebox.showwarning("Aviso", "O gato está cansado demais para brincar!")
        self.atualizar_tela()

    def dormir(self):
        self.energia = min(100, self.energia + 30)
        self.fome = max(0, self.fome - 10)
        self.atualizar_tela()

    def atualizar_tempo(self):
        # Diminui os status a cada 3 segundos
        self.fome = max(0, self.fome - 5)
        self.felicidade = max(0, self.felicidade - 5)
        self.energia = max(0, self.energia - 3)
        
        self.atualizar_tela()
        
        # Verificar Game Over
        if self.fome <= 0 or self.felicidade <= 0:
            messagebox.showinfo("Fim de Jogo", "Você não cuidou bem do gatinho e ele fugiu! 💔")
            self.root.destroy()
            return
            
        # Agenda a próxima perda de pontos para daqui a 3000 milissegundos (3 segundos)
        self.root.after(3000, self.atualizar_tempo)

# Iniciar o jogo
if __name__ == "__main__":
    janela = tk.Tk()
    jogo = JogoGato(janela)
    janela.mainloop()