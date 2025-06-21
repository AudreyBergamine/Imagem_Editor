import cv2
import numpy as np
from service.image_memory import ImageMemory

def calcular_histograma(memory: ImageMemory):
    """ Calcula o histograma de uma imagem em tons de cinza e cria uma visualização. """
    
    imagem = memory.getLastEdit()

    # Converter para tons de cinza se a imagem for colorida
    if len(imagem.shape) == 3:
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        imagem_cinza = imagem

    # Calcular o histograma usando OpenCV (mais eficiente)
    histograma = cv2.calcHist([imagem_cinza], [0], None, [256], [0, 256])
    
    # Converter para lista de inteiros
    vetor_histograma = histograma.flatten().astype(int).tolist()

    # Criar visualização do histograma usando OpenCV
    # Normalizar o histograma para caber na imagem
    hist_norm = cv2.normalize(histograma, histograma, 0, 400, cv2.NORM_MINMAX)
    
    # Criar imagem para o histograma (400x256 pixels)
    img_histograma = np.zeros((425, 340, 3), dtype=np.uint8)
    img_histograma.fill(255)  # Fundo branco
    
    # Desenhar o histograma
    for i in range(256):
        altura = int(hist_norm[i])
        cv2.line(img_histograma, (i, 399), (i, 399 - altura), (0, 0, 0), 1)
    
    # Adicionar texto
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_histograma, 'Histograma - Tons de Cinza', (10, 30), 
                font, 0.7, (0, 0, 0), 2)
    cv2.putText(img_histograma, 'Intensidade', (100, 390), 
                font, 0.5, (0, 0, 0), 1)
    
    # Salvar a visualização do histograma na memória
    memory.addEdit(img_histograma)
    
    # Retornar também os dados do histograma
    return vetor_histograma
