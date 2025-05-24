import tkinter as tk

from funcoes import def_0_abrir_imagem
from funcoes import def_1_split_and_merge
from funcoes import def_2_separar_canais_RGB
from funcoes import def_3_convert_RGB_to_HSV
from funcoes import def_4_convert_HSV_to_RGB
from funcoes import def_5_espaco_de_cores_YCrCb
from funcoes import def_6_espaco_de_cor_LAB
from funcoes import def_7_convertendo_em_tons_de_cinza
from funcoes import def_8_converter_modelos_cor
from funcoes import def_9_propriedades_da_imagem
from funcoes import def_10_pegar_cor_de_um_pixel
from funcoes import def_11_modificar_cor_de_um_pixel
from funcoes import def_12_regiao_de_interesse
from funcoes import def_13_redimensionar_imagem
from funcoes import def_14_ajuste_de_brilho
from funcoes import def_15_ajuste_de_contraste
from funcoes import def_16_inverter_cores
from funcoes import def_17_negativo_da_imagem
from funcoes import def_18_adicionar_imagens
from funcoes import def_19_subtrair_imagens
from funcoes import def_20_multiplicar_imagens
from funcoes import def_21_dividir_imagens
from funcoes import def_22_media_de_duas_imagens
from funcoes import def_23_filtro_media
from funcoes import def_24_filtro_mediana
from funcoes import def_25_suavizar_imagem
from funcoes import def_26_realcar_imagem
from funcoes import def_27_calcular_histograma
from funcoes import def_28_calcular_histograma_colorido
from funcoes import def_29_binarizar_imagem
from funcoes import def_30_equalizar_histograma
from funcoes import def_31_quantizar_histograma
from funcoes import def_32_split_histograma
from funcoes import def_33_stretching_histograma
from funcoes import def_34_erosao
from funcoes import def_35_dilatacao
from funcoes import def_36_abertura
from funcoes import def_37_fechamento
from funcoes import def_39_gradiente_morfologico
from funcoes import def_38_abertura_fechamento_tons_cinza
from funcoes import def_40_top_hat
from funcoes import def_41_eliminacao_ruidos
from view.menu.components.IconButton import IconButton
from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame
import os
# from funcoes.def_0_abrir_imagem import *
# from funcoes.def_1_split_and_merge import *
# from funcoes.def_2_separar_canais_RGB import *
# from funcoes.def_3_convert_RGB_to_HSV import *
# from funcoes.def_4_convert_HSV_to_RGB import *
# from funcoes.def_5_espaco_de_cores_YCrCb import *
# from funcoes.def_6_espaco_de_cor_LAB import *
# from funcoes.def_7_convertendo_em_tons_de_cinza import *
# from funcoes.def_8_converter_modelos_cor import *
# from funcoes.def_9_propriedades_da_imagem import *
# from funcoes.def_10_pegar_cor_de_um_pixel import *
# from funcoes.def_11_modificar_cor_de_um_pixel import *
# from funcoes.def_12_regiao_de_interesse import *
# from funcoes.def_13_redimensionar_imagem import *
# from funcoes.def_14_ajuste_de_brilho import *
# from funcoes.def_15_ajuste_de_contraste import *
# from funcoes.def_16_inverter_cores import *
# from funcoes.def_17_negativo_da_imagem import *
# from funcoes.def_18_adicionar_imagens import *
# from funcoes.def_19_subtrair_imagens import *
# from funcoes.def_20_multiplicar_imagens import *
# from funcoes.def_21_dividir_imagens import *
# from funcoes.def_22_media_de_duas_imagens import *
# from funcoes.def_23_filtro_media import *
# from funcoes.def_24_filtro_mediana import *
# from funcoes.def_25_suavizar_imagem import *
# from funcoes.def_26_realcar_imagem import *
# from funcoes.def_27_calcular_histograma import *
# from funcoes.def_28_calcular_histograma_colorido import *
# from funcoes.def_29_binarizar_imagem import *
# from funcoes.def_30_equalizar_histograma import *
# from funcoes.def_31_quantizar_histograma import *
# from funcoes.def_32_split_histograma import *
# from funcoes.def_33_stretching_histograma import *
# from funcoes.def_34_erosao import *
# from funcoes.def_35_dilatacao import *
# from funcoes.def_36_abertura import *
# from funcoes.def_37_fechamento import *
# from funcoes.def_38_abertura_fechamento_tons_cinza import *
# from funcoes.def_39_gradiente_morfologico import *
# from funcoes.def_40_top_hat import *
# from funcoes.def_41_eliminacao_ruidos import *


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
        
        # Lista de funções e nomes dos botões
        funcoes = [
            ("Abrir Imagem", def_0_abrir_imagem),
            ("Split and Merge", def_1_split_and_merge),
            ("Separar Canais RGB", def_2_separar_canais_RGB),
            ("RGB para HSV", def_3_convert_RGB_to_HSV),
            ("HSV para RGB", def_4_convert_HSV_to_RGB),
            ("Espaço de Cores YCrCb", def_5_espaco_de_cores_YCrCb),
            ("Espaço de Cor LAB", def_6_espaco_de_cor_LAB),
            ("Tons de Cinza", def_7_convertendo_em_tons_de_cinza),
            ("Converter Modelos de Cor", def_8_converter_modelos_cor),
            ("Propriedades da Imagem", def_9_propriedades_da_imagem),
            ("Pegar Cor de um Pixel", def_10_pegar_cor_de_um_pixel),
            ("Modificar Cor de um Pixel", def_11_modificar_cor_de_um_pixel),
            ("Região de Interesse", def_12_regiao_de_interesse),
            ("Redimensionar Imagem", def_13_redimensionar_imagem),
            ("Ajuste de Brilho", def_14_ajuste_de_brilho),
            ("Ajuste de Contraste", def_15_ajuste_de_contraste),
            ("Inverter Cores", def_16_inverter_cores),
            ("Negativo da Imagem", def_17_negativo_da_imagem),
            ("Adicionar Imagens", def_18_adicionar_imagens),
            ("Subtrair Imagens", def_19_subtrair_imagens),
            ("Multiplicar Imagens", def_20_multiplicar_imagens),
            ("Dividir Imagens", def_21_dividir_imagens),
            ("Média de Duas Imagens", def_22_media_de_duas_imagens),
            ("Filtro Média", def_23_filtro_media),
            ("Filtro Mediana", def_24_filtro_mediana),
            ("Suavizar Imagem", def_25_suavizar_imagem),
            ("Realçar Imagem", def_26_realcar_imagem),
            ("Calcular Histograma", def_27_calcular_histograma),
            ("Histograma Colorido", def_28_calcular_histograma_colorido),
            ("Binarizar Imagem", def_29_binarizar_imagem),
            ("Equalizar Histograma", def_30_equalizar_histograma),
            ("Quantizar Histograma", def_31_quantizar_histograma),
            ("Split Histograma", def_32_split_histograma),
            ("Stretching Histograma", def_33_stretching_histograma),
            ("Erosão", def_34_erosao),
            ("Dilatação", def_35_dilatacao),
            ("Abertura", def_36_abertura),
            ("Fechamento", def_37_fechamento),
            ("Abertura/Fechamento Tons de Cinza", def_38_abertura_fechamento_tons_cinza),
            ("Gradiente Morfológico", def_39_gradiente_morfologico),
            ("Top Hat", def_40_top_hat),
            ("Eliminação de Ruídos", def_41_eliminacao_ruidos),
        ]

        # Função especial para o botão "Abrir Imagem"
        def abrir_imagem_callback():
            def_0_abrir_imagem.selecionar_imagem()
            def_0_abrir_imagem.abrir_imagem()

        for nome, funcao in funcoes:
            if nome == "Abrir Imagem":
                callback = abrir_imagem_callback
            else:
                callback = funcao
            btn = IconButton(
                self.inner_frame,
                image_path="view/static/images/engrenagem.png",
                text=nome,
                command=callback,
                background_color="#555",
                text_color="white"
            )
            btn.pack(side="top", fill="x", pady=2)






        
    def show_menu_principal(self):
        pass
    
    def show_editor(self):
        pass