import cv2
import numpy as np
from service.image_memory import ImageMemory

def calcular_histograma_colorido(memory: ImageMemory):
    """ 
    Calcula o histograma de uma imagem colorida usando a função otimizada do OpenCV.
    Retorna os vetores de histograma para os canais R, G e B.
    """
    try:
        # Obtém a imagem atual
        imagem = memory.getLastEdit()
        
        if imagem is None:
            print("Erro: Nenhuma imagem carregada na memória")
            return None, None, None
        
        # Verifica se a imagem é válida
        if imagem.size == 0:
            print("Erro: Imagem inválida ou vazia")
            return None, None, None
        
        # Verifica se a imagem é colorida
        if len(imagem.shape) != 3:
            print("Erro: A imagem deve ser colorida (3 canais)")
            return None, None, None
        
        # Calcula o histograma para cada canal usando a função otimizada do OpenCV
        # OpenCV usa BGR, então os canais são: 0=B, 1=G, 2=R
        histograma_B = cv2.calcHist([imagem], [0], None, [256], [0, 256])
        histograma_G = cv2.calcHist([imagem], [1], None, [256], [0, 256])
        histograma_R = cv2.calcHist([imagem], [2], None, [256], [0, 256])
        
        # Converte para listas para compatibilidade
        HB = histograma_B.flatten().tolist()
        HG = histograma_G.flatten().tolist()
        HR = histograma_R.flatten().tolist()
        
        # Adiciona os dados do histograma à memória
        histograma_data = {
            "HR": HR,
            "HG": HG,
            "HB": HB
        }
        memory.addEdit(histograma_data)
        
        print("Histograma colorido calculado com sucesso!")
        
        return HR, HG, HB
        
    except Exception as e:
        print(f"Erro ao calcular histograma colorido: {str(e)}")
        print(f"Tipo do erro: {type(e).__name__}")
        return None, None, None
  