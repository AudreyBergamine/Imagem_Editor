import cv2
import numpy as np
from service.image_memory import ImageMemory

def ajuste_de_brilho(memory: ImageMemory, k):
    """ 
    Ajusta o brilho de uma imagem adicionando um valor k a cada pixel.
    Versão otimizada usando operações vetorizadas.
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
        imagem_ajustada = imagem.copy()
        
        # Aplica o ajuste de brilho usando operação vetorizada
        # Adiciona k a todos os pixels e limita entre 0 e 255
        imagem_ajustada = np.clip(imagem_ajustada.astype(np.int16) + k, 0, 255).astype(np.uint8)
        
        # Adiciona a imagem processada à memória
        memory.addEdit(imagem_ajustada)
        
        print(f"Brilho ajustado com sucesso! (valor: {k})")
        
    except Exception as e:
        print(f"Erro ao ajustar brilho: {str(e)}")
        print(f"Tipo do erro: {type(e).__name__}")
