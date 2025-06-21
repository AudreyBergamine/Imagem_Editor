import cv2
from service.image_memory import ImageMemory
import numpy as np

def calcular_histograma_colorido(memory: ImageMemory):
    """ Calcula o histograma de uma imagem colorida e cria uma visualização. """
    imagem = memory.getLastEdit()

    # Verifica se a imagem é colorida
    if len(imagem.shape) != 3 or imagem.shape[2] != 3:
        raise ValueError("A imagem fornecida não é colorida (esperado 3 canais).")

    # Calcula o histograma para cada canal (B, G, R)
    HB = cv2.calcHist([imagem], [0], None, [256], [0, 256]).flatten()
    HG = cv2.calcHist([imagem], [1], None, [256], [0, 256]).flatten()
    HR = cv2.calcHist([imagem], [2], None, [256], [0, 256]).flatten()

    # Converte para inteiros para retorno
    HR_list = HR.astype(int).tolist()
    HG_list = HG.astype(int).tolist()
    HB_list = HB.astype(int).tolist()

    # Criar visualização do histograma colorido usando OpenCV
    # Normalizar os histogramas para caber na imagem
    hist_B_norm = cv2.normalize(HB, HB, 0, 250, cv2.NORM_MINMAX)
    hist_G_norm = cv2.normalize(HG, HG, 0, 250, cv2.NORM_MINMAX)
    hist_R_norm = cv2.normalize(HR, HR, 0, 250, cv2.NORM_MINMAX)
    
    # Criar imagem para o histograma (425x340 pixels)
    img_histograma = np.zeros((425, 340, 3), dtype=np.uint8)
    img_histograma.fill(255)  # Fundo branco
    
    # Desenhar o histograma para cada canal
    for i in range(256):
        # Canal Azul (B)
        altura_B = int(hist_B_norm[i])
        cv2.line(img_histograma, (i, 399), (i, 399 - altura_B), (255, 0, 0), 1)
        
        # Canal Verde (G)
        altura_G = int(hist_G_norm[i])
        cv2.line(img_histograma, (i, 399), (i, 399 - altura_G), (0, 255, 0), 1)
        
        # Canal Vermelho (R)
        altura_R = int(hist_R_norm[i])
        cv2.line(img_histograma, (i, 399), (i, 399 - altura_R), (0, 0, 255), 1)
    
    # Adicionar texto e legendas
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Título principal
    cv2.putText(img_histograma, 'Histograma Colorido - RGB', (10, 30), 
                font, 0.7, (0, 0, 0), 2)
    
    # Eixo X
    cv2.putText(img_histograma, 'Intensidade', (120, 420), 
                font, 0.5, (0, 0, 0), 1)
    
    # Legendas dos canais
    cv2.putText(img_histograma, 'Vermelho', (10, 50), 
                font, 0.5, (0, 0, 255), 2)
    cv2.putText(img_histograma, 'Verde', (10, 70), 
                font, 0.5, (0, 255, 0), 2)
    cv2.putText(img_histograma, 'Azul', (10, 90), 
                font, 0.5, (255, 0, 0), 2)
    
    # Salvar a visualização do histograma na memória
    memory.addEdit(img_histograma)
    
    # Retornar também os dados do histograma
    return HR_list, HG_list, HB_list
  