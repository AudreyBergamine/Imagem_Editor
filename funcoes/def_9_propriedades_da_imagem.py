import cv2
from service.image_memory import ImageMemory

def propriedades_da_imagem(memory: ImageMemory):
    """
    Obtém as propriedades de uma imagem.
    """

    imagem = memory.getLastEdit()
    
    # Exibe as propriedades da imagem
    propriedades = {
        "altura": imagem.shape[0],
        "largura": imagem.shape[1],
        "canais": imagem.shape[2]
    }
    return propriedades
    


