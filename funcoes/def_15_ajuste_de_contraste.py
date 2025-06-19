import cv2
import numpy as np
from service.image_memory import ImageMemory

def ajuste_de_contraste(memory: ImageMemory, k):
    """
    Ajusta o contraste de uma imagem multiplicando cada pixel por um fator k.
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
        
        # Converte para float para cálculos precisos
        imagem_float = imagem_ajustada.astype(np.float32)
        
        # Aplica o ajuste de contraste usando operação vetorizada
        # Fórmula: pixel + (pixel * k / 100)
        fator = k / 100.0
        imagem_ajustada = np.clip(imagem_float + (imagem_float * fator), 0, 255).astype(np.uint8)
        
        # Adiciona a imagem processada à memória
        memory.addEdit(imagem_ajustada)
        
        print(f"Contraste ajustado com sucesso! (valor: {k})")
        
    except Exception as e:
        print(f"Erro ao ajustar contraste: {str(e)}")
        print(f"Tipo do erro: {type(e).__name__}")
