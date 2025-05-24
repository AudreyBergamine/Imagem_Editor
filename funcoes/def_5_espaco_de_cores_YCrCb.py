import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem


def espaco_de_cores_YCrCb(imagem):
    
    # Converter a imagem para o espaço de cores YCrCb
    imagemYCrCb = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    
    # Extrair os canais Y, Cr e Cb
    canal_Y, canal_Cr, canal_Cb = cv2.split(imagemYCrCb)
    
    return imagemYCrCb, canal_Y, canal_Cr, canal_Cb