import cv2

def negativo_da_imagem(imagem):
    # Obtém as dimensões da imagem
    linhas, colunas = imagem.shape[:2]
        
    # Aplica a transformação negativa
    for x in range(linhas):
        for y in range(colunas):
            imagem[x, y] = 255 - imagem[x, y]
    
    return imagem



    
