import tkinter as tk
from functools import partial
import importlib

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

# Lista de funções e nomes amigáveis (até def_42)
FUNCOES = [
    ("Abrir Imagem", "def_0_abrir_imagem", "selecionar_imagem"),
    ("Split and Merge", "def_1_split_and_merge", "split_and_merge"),
    ("Separar Canais R", "def_2_separar_canais_RGB", "separar_canal_R"),
    ("Separar Canais G", "def_2_separar_canais_RGB", "separar_canal_G"),
    ("Separar Canais B", "def_2_separar_canais_RGB", "separar_canal_B"),
    ("RGB para HSV", "def_3_convert_RGB_to_HSV", "convert_RGB_to_HSV"),
    ("HSV para RGB", "def_4_convert_HSV_to_RGB", "convert_HSV_to_RGB"),
    ("Espaço de Cores YCrCb", "def_5_espaco_de_cores_YCrCb", "espaco_de_cores_YCrCb"),
    ("Espaço de Cor LAB", "def_6_espaco_de_cor_LAB", "espaco_de_cor_LAB"),
    ("Tons de Cinza", "def_7_convertendo_em_tons_de_cinza", "convertendo_em_tons_de_cinza"),
    ("Converter Modelos de Cor", "def_8_converter_modelos_cor", "converter_modelos_cor"),
    ("Propriedades da Imagem", "def_9_propriedades_da_imagem", "propriedades_da_imagem"),
    ("Pegar Cor de um Pixel", "def_10_pegar_cor_de_um_pixel", "pegar_cor_de_um_pixel"),
    ("Modificar Cor de um Pixel", "def_11_modificar_cor_de_um_pixel", "modificar_cor_de_um_pixel"),
    ("Região de Interesse", "def_12_regiao_de_interesse", "regiao_de_interesse"),
    ("Redimensionar Imagem", "def_13_redimensionar_imagem", "redimensionar_imagem"),
    ("Ajuste de Brilho", "def_14_ajuste_de_brilho", "ajuste_de_brilho"),
    ("Ajuste de Contraste", "def_15_ajuste_de_contraste", "ajuste_de_contraste"),
    ("Inverter Cores", "def_16_inverter_cores", "inverter_cores"),
    ("Negativo da Imagem", "def_17_negativo_da_imagem", "negativo_da_imagem"),
    ("Adicionar Imagens", "def_18_adicionar_imagens", "adicionar_imagens"),
    ("Subtrair Imagens", "def_19_subtrair_imagens", "subtrair_imagens"),
    ("Multiplicar Imagens", "def_20_multiplicar_imagens", "multiplicar_imagens"),
    ("Dividir Imagens", "def_21_dividir_imagens", "dividir_imagens"),
    ("Média de Duas Imagens", "def_22_media_de_duas_imagens", "media_de_duas_imagens"),
    ("Filtro Média", "def_23_filtro_media", "filtro_media"),
    ("Filtro Mediana", "def_24_filtro_mediana", "filtro_mediana"),
    ("Suavizar Imagem", "def_25_suavizar_imagem", "suavizar_imagem"),
    ("Realçar Imagem", "def_26_realcar_imagem", "realcar_imagem"),
    ("Calcular Histograma", "def_27_calcular_histograma", "calcular_histograma"),
    ("Histograma Colorido", "def_28_calcular_histograma_colorido", "calcular_histograma_colorido"),
    ("Binarizar Imagem", "def_29_binarizar_imagem", "binarizar_imagem"),
    ("Equalizar Histograma", "def_30_equalizar_histograma", "equalizar_histograma"),
    ("Quantizar Histograma", "def_31_quantizar_histograma", "quantizar_histograma"),
    ("Split Histograma", "def_32_split_histograma", "split_histograma"),
    ("Stretching Histograma", "def_33_stretching_histograma", "stretching_histograma"),
    ("Erosão", "def_34_erosao", "erosao"),
    ("Dilatação", "def_35_dilatacao", "dilatacao"),
    ("Abertura", "def_36_abertura", "abertura"),
    ("Fechamento", "def_37_fechamento", "fechamento"),
    ("Abertura/Fechamento Tons de Cinza", "def_38_abertura_fechamento_tons_cinza", "abertura_fechamento_tons_cinza"),
    ("Gradiente Morfológico", "def_39_gradiente_morfologico", "gradiente_morfologico"),
    ("Top Hat", "def_40_top_hat", "top_hat"),
    ("Eliminação de Ruídos", "def_41_eliminacao_ruidos", "eliminacao_ruidos"),
    ("Detectar Rostos", "def_42_detectar_rostos", "detectar_rostos"),
]

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
        # Corrigir acesso ao app
        app = getattr(self.master, 'app', None)
        if app is None:
            app = getattr(self.master.master, 'app', None)
        if app is None:
            print("Erro: não foi possível acessar o app.")
            return
        app.trocar_tela('menu_principal')

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

        # Botões dinâmicos para cada função
        for idx, (nome, modulo, funcao) in enumerate(FUNCOES, 1):
            try:
                mod = importlib.import_module(f"funcoes.{modulo}")
                func = getattr(mod, funcao)
            except Exception as e:
                func = None
            def make_callback(f):
                return lambda: self._executar_funcao(f) if f else None
            btn = IconButton(
                self.inner_frame,
                image_path="view/static/images/engrenagem.png",
                text=f"{idx:02d} - {nome}",
                command=make_callback(func),
                background_color="#555",
                text_color="white"
            )
            btn.pack(side="top", fill="x", padx=5, pady=2)

    def _executar_funcao(self, func):
        # Corrigir acesso ao app
        app = getattr(self.master, 'app', None)
        if app is None:
            app = getattr(self.master.master, 'app', None)
        if app is None:
            print("Erro: não foi possível acessar o app.")
            return
        func(app.memory)
        app.trocar_tela('menu_principal')

    def show_menu_principal(self):
        pass

    def show_editor(self):
        pass
