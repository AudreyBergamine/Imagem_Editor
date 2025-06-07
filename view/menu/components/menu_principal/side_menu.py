import tkinter as tk
from functools import partial

from funcoes import def_0_abrir_imagem
from funcoes.def_1_split_and_merge import split_and_merge
from funcoes import def_2_separar_canais_RGB
from funcoes.def_7_convertendo_em_tons_de_cinza import convertendo_em_tons_de_cinza
from funcoes.def_3_convert_RGB_to_HSV import convert_RGB_to_HSV
from funcoes.def_4_convert_HSV_to_RGB import convert_HSV_to_RGB

from service.image_memory import ImageMemory
from view.menu.components.IconButton import IconButton
from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame


class Side_menu(RoundedFrame):
    def __init__(self, master):
        super().__init__(master,
                         bg_color=Configuration.side_background_color,
                         border_color="black",
                         corner_radius=20,
                         width=Configuration.side_menu_width,
                         height=Configuration.side_menu_height,
                         highlightthickness=0)

        self.master = master
        self.pack_propagate(False)
        self.create_widgets()
        
    def update(self):
        self.master.app.trocar_tela('menu_principal')

    def create_widgets(self):
        largura_menu = max(Configuration.side_menu_width, 200)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.inner_frame = tk.Frame(self, bg=Configuration.side_background_color)
        self.window_id = self.create_window((0, 0), window=self.inner_frame, anchor="nw", width=largura_menu)

        def on_configure(event):
            self.configure(scrollregion=self.bbox("all"))
            self.itemconfig(self.window_id, width=self.winfo_width())

        self.inner_frame.bind("<Configure>", on_configure)

        def _on_mousewheel(event):
            self.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.bind_all("<MouseWheel>", _on_mousewheel)

        # Botão: Abrir Imagem
        def abrir_imagem_callback(memory: ImageMemory):
            image = def_0_abrir_imagem.selecionar_imagem()
            memory.addImage(image)
            memory.update()
            self.update()

        btn_abrir_0 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="Abrir Imagem",
            command=lambda: abrir_imagem_callback(self.master.app.memory),
            background_color="#555",
            text_color="white"
        )
        btn_abrir_0.pack(side="top", fill="x", padx=5, pady=2)

        # Botão: Split and Merge
        btn_split_merge_1 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="Split and Merge",
            command=lambda: self._executar_funcao(split_and_merge),
            background_color="#555",
            text_color="white"
        )
        btn_split_merge_1.pack(side="top", fill="x", padx=5, pady=2)

        # Botão: Separar Canal R
        btn_canal_r_2_1 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="Separar Canais R",
            command=lambda: self._executar_funcao(def_2_separar_canais_RGB.separar_canal_R),
            background_color="#555",
            text_color="white"
        )
        btn_canal_r_2_1.pack(side="top", fill="x", padx=5, pady=2)

        # Botão: Separar Canal G
        btn_canal_g_2_2 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="Separar Canais G",
            command=lambda: self._executar_funcao(def_2_separar_canais_RGB.separar_canal_G),
            background_color="#555",
            text_color="white"
        )
        btn_canal_g_2_2.pack(side="top", fill="x", padx=5, pady=2)

        # Botão: Separar Canal B
        btn_canal_b_2_3 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="Separar Canais B",
            command=lambda: self._executar_funcao(def_2_separar_canais_RGB.separar_canal_B),
            background_color="#555",
            text_color="white"
        )
        btn_canal_b_2_3.pack(side="top", fill="x", padx=5, pady=2)

        # Botão: Tons de Cinza
        btn_convert_RGB_to_HSV_3 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="RGB para HSV",
            command=lambda: self._executar_funcao(convert_RGB_to_HSV),
            background_color="#555",
            text_color="white"
        )
        btn_convert_RGB_to_HSV_3.pack(side="top", fill="x", padx=5, pady=2)
       
        btn_convert_HSV_to_RGB_4 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="HSV para RGB",
            command=lambda: self._executar_funcao(convert_HSV_to_RGB),
            background_color="#555",
            text_color="white"
        )
        btn_convert_HSV_to_RGB_4.pack(side="top", fill="x", padx=5, pady=2)
      
        btn_espaco_cores_Y = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="HSV para RGB",
            command=lambda: self._executar_funcao(),
            background_color="#555",
            text_color="white"
        )
        btn_espaco_cores_Y.pack(side="top", fill="x", padx=5, pady=2)

        # Botão: Tons de Cinza
        btn_cinza_7 = IconButton(
            self.inner_frame,
            image_path="view/static/images/engrenagem.png",
            text="Tons de Cinza",
            command=lambda: self._executar_funcao(convertendo_em_tons_de_cinza),
            background_color="#555",
            text_color="white"
        )
        btn_cinza_7.pack(side="top", fill="x", padx=5, pady=2)

        
        
    def _executar_funcao(self, func):
        func(self.master.app.memory)
        self.master.app.trocar_tela('menu_principal')

    def show_menu_principal(self):
        pass

    def show_editor(self):
        pass
