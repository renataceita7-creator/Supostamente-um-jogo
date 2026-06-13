import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class JogoGato:
    def __init__(self, root):
        self.root = root
        self.root.title("Meu Gato Virtual 🐱")
        self.root.geometry("700x550")
        self.root.configure(bg="#f0f0f0")
        
        # Atributos iniciais
        self.fome = 100
        self.felicidade = 100
        self.energia = 100
        self.frame_animacao = 0
        self.photo_images = []
        
        # Carregar imagem do gato
        self.carregar_sprites()
        
        # Canvas para animação
        self.canvas = tk.Canvas(root, width=600, height=200, bg="lightblue", relief="sunken", bd=2)
        self.canvas.pack(pady=10, padx=10)
        
        # Label de estado do gato (emoji)
        self.label_estado = tk.Label(root, text="😺 Feliz!", font=("Arial", 14), fg="#FF6B6B")
        self.label_estado.pack(pady=5)
        
        self.label_status = tk.Label(root, text=self.obter_texto_status(), font=("Arial", 11), justify="left", bg="#f0f0f0")
        self.label_status.pack(pady=5)
        
        # Frame com botões
        frame_botoes = tk.Frame(root, bg="#f0f0f0")
        frame_botoes.pack(pady=10)
        
        tk.Button(frame_botoes, text="🍖 Alimentar", command=self.alimentar, width=14, bg="#FFB6C1", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="🎾 Brincar", command=self.brincar, width=14, bg="#87CEEB", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="😴 Dormir", command=self.dormir, width=14, bg="#DDA0DD", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="❌ Sair", command=self.root.destroy, width=14, bg="#D3D3D3", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        # Loop para atualizar animação e status
        self.animar_gato()
        self.atualizar_tempo()
    
    def carregar_sprites(self):
        """Carrega ou cria sprites do gato pixel art"""
        caminho_img = r"c:\Users\seque\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1781391453614-aii4r5y6.png"
        
        try:
            # Carregar imagem original
            img = Image.open(caminho_img)
            
            # Redimensionar para melhor visualização
            img = img.resize((600, 200), Image.Resampling.LANCZOS)
            
            # Extrair 3 frames (dividindo a imagem em 3 partes)
            width = img.width // 3
            height = img.height
            
            for i in range(3):
                frame = img.crop((i * width, 0, (i + 1) * width, height))
                frame = frame.resize((150, 150), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(frame)
                self.photo_images.append(photo)
                
            print("✅ Sprites carregados com sucesso!")
            
        except Exception as e:
            print(f"⚠️ Erro ao carregar imagem: {e}")
            print("Usando sprites padrão...")
            self.criar_sprites_padrao()
    
    def criar_sprites_padrao(self):
        """Cria sprites de fallback se a imagem não estiver disponível"""
        from PIL import Image, ImageDraw
        
        for i in range(3):
            img = Image.new('RGB', (150, 150), color='white')
            draw = ImageDraw.Draw(img)
            
            draw.text((50, 60), f"Gato {i+1}", fill='black')
            photo = ImageTk.PhotoImage(img)
            self.photo_images.append(photo)

    def obter_texto_status(self):
        return f"🍗 Fome: {self.fome}/100  |  💖 Felicidade: {self.felicidade}/100  |  ⚡ Energia: {self.energia}/100"
    
    def atualizar_tela(self):
        """Atualiza estado visual conforme situação do gato"""
        self.label_status.config(text=self.obter_texto_status())
        
        if self.fome < 30:
            estado = "😿 Com Fome!"
            cor = "#FF6B6B"
        elif self.energia < 30:
            estado = "😴 Cansado..."
            cor = "#9B59B6"
        elif self.felicidade < 30:
            estado = "😞 Triste..."
            cor = "#E74C3C"
        else:
            estado = "😺 Feliz!"
            cor = "#2ECC71"
        
        self.label_estado.config(text=estado, fg=cor)
    
    def animar_gato(self):
        """Anima o gato texturizado no canvas"""
        self.canvas.delete("all")
        
        if self.photo_images:
            frame_idx = self.frame_animacao % 3
            x = 150 + (self.frame_animacao // 3) % 4 * 100
            
            self.canvas.create_image(x, 100, image=self.photo_images[frame_idx])
        
        self.frame_animacao += 1
        self.root.after(200, self.animar_gato)

    def alimentar(self):
        """Alimenta o gato e restaura fome"""
        if self.fome == 100:
            messagebox.showinfo("Info", "O gato já está satisfeito! 😸")
            return
        self.fome = min(100, self.fome + 25)
        self.felicidade = min(100, self.felicidade + 5)
        messagebox.showinfo("Alimentação", "O gato comeu feliz! 😋")
        self.atualizar_tela()

    def brincar(self):
        """Brinca com o gato (consome energia)"""
        if self.energia < 20:
            messagebox.showwarning("Aviso", "O gato está muito cansado para brincar! 😪")
            return
        self.felicidade = min(100, self.felicidade + 25)
        self.energia = max(0, self.energia - 20)
        self.fome = max(0, self.fome - 10)
        messagebox.showinfo("Brincadeira", "Que divertido! 🎾")
        self.atualizar_tela()

    def dormir(self):
        """Deixa o gato dormir (restaura energia)"""
        if self.energia == 100:
            messagebox.showinfo("Info", "O gato não está cansado! 😸")
            return
        self.energia = min(100, self.energia + 40)
        self.fome = max(0, self.fome - 15)
        messagebox.showinfo("Soninho", "O gato dormiu feliz! 😴💤")
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
