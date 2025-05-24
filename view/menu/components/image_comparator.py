import tkinter as tk
from PIL import Image, ImageTk
import cv2

from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame

class ImageComparator(RoundedFrame):
    def __init__(self, master, app, img_before=None, img_after=None):
        super().__init__(master,
                         bg_color=Configuration.image_comparator_background_color,
                         border_color="black",
                         corner_radius=20,
                         highlightthickness=0)

        self.master = master
        self.app = app
        self.create_widgets()
        self.display_images()

    def create_widgets(self):
        self.container = tk.Frame(self, background="black")
        self.container.pack(fill="both", expand=True, padx=10, pady=10)

        self.container.grid_columnconfigure(0, weight=1, uniform='equal')
        self.container.grid_columnconfigure(1, weight=1, uniform='equal')
        self.container.grid_rowconfigure(0, weight=1)

        self.image_before = tk.Frame(self.container, background="black")
        self.image_before.grid(row=0, column=0, sticky="nsew", padx=2)

        self.image_after = tk.Frame(self.container, background="black")
        self.image_after.grid(row=0, column=1, sticky="nsew", padx=2)

    def show_image(self, frame, image_cv2):
        if image_cv2 is None:
            print("Imagem não carregada!")  # Depuração
            return

        # Converte a imagem BGR (OpenCV) para RGB (PIL)
        image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)

        # Redimensiona para caber no frame, mantendo a proporção
        def update_image():
            frame.update_idletasks()
            w, h = frame.winfo_width(), frame.winfo_height()
            if w > 0 and h > 0:
                # Mantém a largura fixa, ajustando a altura proporcionalmente
                aspect_ratio = image_pil.height / image_pil.width  # Proporção original
                new_height = int(w * aspect_ratio)  # Calcula a nova altura com base na largura

                # Se a altura calculada for maior que o limite do frame, ajuste
                if new_height > h:
                    new_height = h
                    w = int(new_height / aspect_ratio)  # Ajusta a largura para manter a proporção

                # Redimensiona a imagem com as novas dimensões
                image_pil_resized = image_pil.resize((w, new_height), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image_pil_resized)
                label = tk.Label(frame, image=photo)
                label.image = photo  # Guarda referência
                label.pack(expand=False, fill="none", padx=2, pady=2)

        frame.after(100, update_image)

    def display_images(self):
        self.show_image(self.image_before, self.master.app.memory.image_backEdited)
        self.show_image(self.image_after, self.master.app.memory.image_selected)
