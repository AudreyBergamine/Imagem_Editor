import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from service.image_memory import ImageMemory

def selecionar_imagem():
    """
    Abre uma janela para o usuário selecionar uma imagem do computador.

    :return: Caminho para o arquivo da imagem selecionada ou None se nenhuma imagem for selecionada.
    """
    # Tk().withdraw()  # Oculta a janela principal do Tkinter
    caminho_imagem = askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print("Erro ao abrir a imagem.")
        return None
    return imagem





def abrir_imagem(imagem):
    """
    Abre e exibe uma imagem usando OpenCV.

    :param caminho_imagem: Caminho para o arquivo da imagem.
    """
    cv2.imshow("Imagem", imagem)
    
    
    # Retornar uma imagem para uso posterior
    return imagem
