import tkinter as tk

from view.menu.components.IconButton import IconButton
from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame
import os
from funcoes.def_0_abrir_imagem import *
from funcoes.def_1_split_and_merge import *
from funcoes.def_2_separar_canais_RGB import *
from funcoes.def_3_convert_RGB_to_HSV import *
from funcoes.def_4_convert_HSV_to_RGB import *
from funcoes.def_5_espaco_de_cores_YCrCb import *
from funcoes.def_6_espaco_de_cor_LAB import *
from funcoes.def_7_convertendo_em_tons_de_cinza import *
from funcoes.def_8_converter_modelos_cor import *
from funcoes.def_9_propriedades_da_imagem import *
from funcoes.def_10_pegar_cor_de_um_pixel import *
from funcoes.def_11_modificar_cor_de_um_pixel import *
from funcoes.def_12_regiao_de_interesse import *
from funcoes.def_13_redimensionar_imagem import *
from funcoes.def_14_ajuste_de_brilho import *
from funcoes.def_15_ajuste_de_contraste import *
from funcoes.def_16_inverter_cores import *
from funcoes.def_17_negativo_da_imagem import *
from funcoes.def_18_adicionar_imagens import *
from funcoes.def_19_subtrair_imagens import *
from funcoes.def_20_multiplicar_imagens import *
from funcoes.def_21_dividir_imagens import *
from funcoes.def_22_media_de_duas_imagens import *
from funcoes.def_23_filtro_media import *
from funcoes.def_24_filtro_mediana import *
from funcoes.def_25_suavizar_imagem import *
from funcoes.def_26_realcar_imagem import *
from funcoes.def_27_calcular_histograma import *
from funcoes.def_28_calcular_histograma_colorido import *
from funcoes.def_29_binarizar_imagem import *
from funcoes.def_30_equalizar_histograma import *
from funcoes.def_31_quantizar_histograma import *
from funcoes.def_32_split_histograma import *
from funcoes.def_33_stretching_histograma import *
from funcoes.def_34_erosao import *
from funcoes.def_35_dilatacao import *
from funcoes.def_36_abertura import *
from funcoes.def_37_fechamento import *
from funcoes.def_38_abertura_fechamento_tons_cinza import *
from funcoes.def_39_gradiente_morfologico import *
from funcoes.def_40_top_hat import *
from funcoes.def_41_eliminacao_ruidos import *



selecionar_imagem()

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
        self.create_widgets()
    
    def create_widgets(self):
        # Frame interno para conter os widgets
        self.inner_frame = tk.Frame(self, bg=Configuration.side_background_color, width=Configuration.side_menu_width - 20, height=Configuration.side_menu_height - 20)
        self.inner_frame.pack_propagate(False)  # Impede que o frame redimensione automaticamente
        self.create_window(Configuration.side_menu_width // 2, Configuration.side_menu_height // 2, window=self.inner_frame, anchor="center")
        
        # Criando os botões do menu lateral
        self.opcao0 = IconButton(self.inner_frame, 
                    image_path="view/static/images/engrenagem.png", 
                    text="Abrir Imagem", 
                    command=self.show_menu_principal, 
                    background_color="#555", 
                    text_color="white")
        self.opcao0.pack(side="top")
        
        # Criando os botões do menu lateral
        self.opcao1 = IconButton(self.inner_frame, 
                    image_path="view/static/images/engrenagem.png", 
                    text="Escalas de cinza", 
                    command=self.show_menu_principal, 
                    background_color="#555", 
                    text_color="white")
        self.opcao1.pack(side="top")






        
    def show_menu_principal(self):
        pass
    
    def show_editor(self):
        pass