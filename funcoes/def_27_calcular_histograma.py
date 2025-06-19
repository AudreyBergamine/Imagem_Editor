import cv2
import numpy as np
from service.image_memory import ImageMemory

def calcular_histograma(memory: ImageMemory):
    """ 
    Calcula o histograma de uma imagem em tons de cinza usando a função otimizada do OpenCV.
    """
    try:
        # Obtém a imagem atual
        imagem = memory.getLastEdit()
        
        if imagem is None:
            print("Erro: Nenhuma imagem carregada na memória")
            return
        
        # Verifica se a imagem é válida
        if imagem.size == 0:
            print("Erro: Imagem inválida ou vazia")
            return
        
        # Converte para escala de cinza se for colorida
        if len(imagem.shape) == 3:
            imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        else:
            imagem_cinza = imagem
        
        # Calcula o histograma usando a função otimizada do OpenCV
        histograma = cv2.calcHist([imagem_cinza], [0], None, [256], [0, 256])
        
        # Converte para lista para compatibilidade
        vetor_histograma = histograma.flatten().tolist()
        
        # Adiciona o histograma à memória
        memory.addEdit(vetor_histograma)
        
        print("Histograma calculado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao calcular histograma: {str(e)}")
        print(f"Tipo do erro: {type(e).__name__}")
