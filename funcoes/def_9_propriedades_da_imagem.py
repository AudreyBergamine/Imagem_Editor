import cv2

def propriedades_da_imagem(imagem):
    
    # Exibe as propriedades da imagem
    propriedades = {
        "altura": imagem.shape[0],
        "largura": imagem.shape[1],
        "canais": imagem.shape[2]
    }
    return propriedades
    


