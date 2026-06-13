import tkinter as tk
from tkinter import messagebox

class JogoGato:
    def __init__(self, root):
        self.root = root
        self.root.title("Meu Gato Virtual 🐱")
        self.root.geometry("500x450")
        
        # Atributos iniciais
        self.fome = 100
        self.felicidade = 100
        self.energia = 100
        self.posicao_gato = 0  # Para animação de movimento
        self.frame_animacao = 0  # Frame atual da animação
        
        # Canvas para animação
        self.canvas = tk.Canvas(root, width=450, height=150, bg="lightblue", relief="sunken", bd=2)
        self.canvas.pack(pady=10, padx=10)
        
        # Label do gato ASCII com animação
        self.label_gato = tk.Label(root, text=self.gato_literal("happy"), font=("Courier", 12), justify="center")
        self.label_gato.pack(pady=5)
        
        self.label_status = tk.Label(root, text=self.obter_texto_status(), font=("Arial", 11), justify="left")
        self.label_status.pack(pady=5)
        
        # Frame com botões
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)
        
        tk.Button(frame_botoes, text="Alimentar", command=self.alimentar, width=14, bg="#FFB6C1").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Brincar", command=self.brincar, width=14, bg="#87CEEB").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Dormir", command=self.dormir, width=14, bg="#DDA0DD").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Sair", command=self.root.destroy, width=14, bg="#D3D3D3").pack(side=tk.LEFT, padx=5)
        
        # Loop para atualizar animação e status
        self.animar_gato()
        self.atualizar_tempo()

    def obter_texto_status(self):
        return f"Fome: {self.fome}/100\nFelicidade: {self.felicidade}/100\nEnergia: {self.energia}/100"
    
    def gato_literal(self, mood):
        """Retorna um gato ASCII variando conforme humor"""
        if mood == "happy":
            return " /\\_/\\\n( ^.^ )\n > ^ <"
        if mood == "hungry":
            return " /\\_/\\\n( o.o )\n >   <"
        if mood == "sleepy":
            return " /\\_/\\\n( -.- ) z\n  z z"
        if mood == "sad":
            return " /\\_/\\\n( T.T )\n >   <"
        return " /\\_/\\\n( ?.? )\n >   <"
    
    def gato_andando(self, frame):
        """Retorna um gato andando em diferentes frames de animação"""
        frames = [
            "~( ^.^ )~",  # Posição 1
            " ( ^.^ ) ",  # Posição 2
            "~( ^.^ )~"   # Posição 3 (volta ao 1)
        ]
        return frames[frame % 3]

    def atualizar_tela(self):
        """Atualiza status visual conforme estado do gato"""
        self.label_status.config(text=self.obter_texto_status())
        
        if self.fome < 30:
            estado = "hungry"
        elif self.energia < 30:
            estado = "sleepy"
        elif self.felicidade < 30:
            estado = "sad"
        else:
            estado = "happy"
        
        self.label_gato.config(text=self.gato_literal(estado))
    
    def animar_gato(self):
        """Anima o gato andando no canvas"""
        self.canvas.delete("all")
        x = 50 + (self.frame_animacao % 10) * 30
        y = 70
        
        gato = self.gato_andando(self.frame_animacao)
        self.canvas.create_text(x, y, text=gato, font=("Courier", 16))
        
        self.frame_animacao += 1
        self.root.after(150, self.animar_gato)

    def alimentar(self):
        """Alimenta o gato e restaura fome"""
        if self.fome == 100:
            messagebox.showinfo("Info", "O gato já está satisfeito!")
            return
        self.fome = min(100, self.fome + 25)
        self.felicidade = min(100, self.felicidade + 5)
        self.atualizar_tela()

    def brincar(self):
        """Brinca com o gato (consome energia)"""
        if self.energia < 20:
            messagebox.showwarning("Aviso", "O gato está muito cansado para brincar!")
            return
        self.felicidade = min(100, self.felicidade + 25)
        self.energia = max(0, self.energia - 20)
        self.fome = max(0, self.fome - 10)
        self.atualizar_tela()

    def dormir(self):
        """Deixa o gato dormir (restaura energia)"""
        if self.energia == 100:
            messagebox.showinfo("Info", "O gato não está cansado!")
            return
        self.energia = min(100, self.energia + 40)
        self.fome = max(0, self.fome - 15)
        messagebox.showinfo("Zzz...", "O gato dormiu feliz! 😴")
        self.atualizar_tela()

    def atualizar_tempo(self):
        """Atualiza status a cada 2.5 segundos e verifica condição de perda"""
        self.fome = max(0, self.fome - 4)
        self.felicidade = max(0, self.felicidade - 3)
        self.energia = max(0, self.energia - 2)
        
        self.atualizar_tela()
        
        if self.fome == 0:
            messagebox.showinfo("Game Over", "Seu gato morreu de fome! 💔")
            self.root.destroy()
            return
        if self.felicidade == 0:
            messagebox.showinfo("Game Over", "Seu gato fugiu porque está muito triste! 😿")
            self.root.destroy()
            return
        
        self.root.after(2500, self.atualizar_tempo)

# Iniciar o jogo
if __name__ == "__main__":
    janela = tk.Tk()
    jogo = JogoGato(janela)
    janela.mainloop()
