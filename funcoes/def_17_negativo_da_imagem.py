import cv2
import numpy as np
from service.image_memory import ImageMemory

def negativo_da_imagem(memory: ImageMemory):
    """
    Aplica a transformação negativa a uma imagem de forma otimizada.
    Usa operações vetorizadas para melhor performance.
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
        
        # Cria uma cópia da imagem para não modificar a original
        imagem_negativa = imagem.copy()
        
        # Aplica a transformação negativa usando operação vetorizada
        # Para imagens coloridas (3 canais BGR)
        if len(imagem_negativa.shape) == 3:
            imagem_negativa = 255 - imagem_negativa
        # Para imagens em escala de cinza (1 canal)
        elif len(imagem_negativa.shape) == 2:
            imagem_negativa = 255 - imagem_negativa
        else:
            print("Erro: Formato de imagem não suportado")
            return
        
        # Adiciona a imagem processada à memória
        memory.addEdit(imagem_negativa)
        
        print("Negativo da imagem aplicado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao aplicar negativo da imagem: {str(e)}")
        print(f"Tipo do erro: {type(e).__name__}")

