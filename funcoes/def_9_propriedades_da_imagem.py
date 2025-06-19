import cv2
from service.image_memory import ImageMemory
import tkinter as tk
from tkinter import ttk

def propriedades_da_imagem(memory: ImageMemory):
    """
    Exibe as propriedades da imagem em uma janela moderna, com emojis coloridos e layout otimizado.
    """
    imagem = memory.getLastEdit()
    propriedades = [
        ("✔️ Altura", f"{imagem.shape[0]} px"),
        ("✔️ Largura", f"{imagem.shape[1]} px"),
        ("✔️ Canais", f"{imagem.shape[2]}")
    ]

    # Criar janela personalizada sem exibir root
    root = tk.Tk()
    root.withdraw()
    win = tk.Toplevel(root)
    win.title("Propriedades da Imagem")
    win.configure(bg="#232946")
    win.resizable(False, False)
    win.geometry("400x350")
    win.grab_set()

    # Título
    label_titulo = tk.Label(win, text="👽 Propriedades da Imagem", font=("Arial", 16, "bold"), fg="#eebbc3", bg="#232946")
    label_titulo.pack(pady=(20, 10))

    # Frame central para propriedades
    frame_central = tk.Frame(win, bg="#232946")
    frame_central.pack(expand=True)

    # Propriedades centralizadas, mas alinhadas à esquerda a partir do ✔️
    for emoji, valor in propriedades:
        label = tk.Label(frame_central, text=f"{emoji} {valor}", font=("Arial", 15), fg="#b8c1ec", bg="#232946", anchor="w", justify="left")
        label.pack(fill="x", padx=40, pady=6)

    # Mensagem final
    label_final = tk.Label(win, text="✨ Aproveite a edição!✨ \n ", font=("Arial", 13, "italic"), fg="#eebbc3", bg="#232946")
    label_final.pack(pady=(20, 10))

    # Botão fechar super moderno e customizado
    btn_frame = tk.Frame(win, bg="#232946")
    btn_frame.pack(pady=(0, 15))

    def on_enter(e):
        btn_custom.config(bg="#f7c8e0")
    def on_leave(e):
        btn_custom.config(bg="#eebbc3")

    # Função auxiliar para desenhar retângulo arredondado
    def create_rounded_rect(canvas, x1, y1, x2, y2, r=20, **kwargs):
        canvas.create_arc(x1, y1, x1+r*2, y1+r*2, start=90, extent=90, style='pieslice', **kwargs)
        canvas.create_arc(x2-r*2, y1, x2, y1+r*2, start=0, extent=90, style='pieslice', **kwargs)
        canvas.create_arc(x1, y2-r*2, x1+r*2, y2, start=180, extent=90, style='pieslice', **kwargs)
        canvas.create_arc(x2-r*2, y2-r*2, x2, y2, start=270, extent=90, style='pieslice', **kwargs)
        canvas.create_rectangle(x1+r, y1, x2-r, y2, **kwargs)
        canvas.create_rectangle(x1, y1+r, x2, y2-r, **kwargs)

    btn_custom = tk.Canvas(btn_frame, width=130, height=44, bg="#eebbc3", highlightthickness=0, bd=0)
    create_rounded_rect(btn_custom, 2, 2, 128, 42, r=18, fill="#eebbc3", outline="#eebbc3")
    # X grande e colorido
    btn_custom.create_text(38, 22, text="✖", font=("Arial", 22, "bold"), fill="#d72660")
    # Texto 'Fechar'
    btn_custom.create_text(90, 22, text="Fechar", font=("Arial", 13, "bold"), fill="#232946")
    btn_custom.bind("<Button-1>", lambda e: win.destroy())
    btn_custom.bind("<Enter>", on_enter)
    btn_custom.bind("<Leave>", on_leave)
    btn_custom.pack()

    # Centralizar janela na tela
    win.update_idletasks()
    largura = win.winfo_width()
    altura = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (largura // 2)
    y = (win.winfo_screenheight() // 2) - (altura // 2)
    win.geometry(f"{largura}x{altura}+{x}+{y}")

    # Espera a janela ser fechada e destrói o root
    root.wait_window(win)
    root.destroy()
    return propriedades


