import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def selecionar_imagem():
    """
    Abre uma janela para o usuário selecionar uma imagem do computador.

    :return: Caminho para o arquivo da imagem selecionada ou None se nenhuma imagem for selecionada.
    """
    Tk().withdraw()  # Oculta a janela principal do Tkinter
    caminho_imagem = askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    return caminho_imagem





def abrir_imagem(caminho_imagem):
    """
    Abre e exibe uma imagem usando OpenCV.

    :param caminho_imagem: Caminho para o arquivo da imagem.
    """
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print(f"Erro: Não foi possível carregar a imagem em '{caminho_imagem}'. Verifique o caminho.")
        return
    
    # Retornar uma imagem para uso posterior
    return imagem
