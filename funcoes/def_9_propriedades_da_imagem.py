import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

def propriedades_da_imagem(imagem):
    
    # Exibe as propriedades da imagem
    propriedades = {
        "altura": imagem.shape[0],
        "largura": imagem.shape[1],
        "canais": imagem.shape[2]
    }
    return propriedades
    


