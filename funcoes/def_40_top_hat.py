import cv2
import numpy as np
from service.image_memory import ImageMemory

#  Realça objetos brilhantes em fundos escuros
#  e objetos escuros em fundos claros.
#  O operador Top Hat é útil para destacar objetos que são mais brilhantes do que o fundo.
def top_hat(memory: ImageMemory, kernel_size=(25, 25)):
    """ Aplica o operador morfológico Top Hat a uma imagem. """
    
    imagem = memory.getLastEdit()
    
    # Verificar se há uma imagem na memória
    if imagem is None:
        raise ValueError("Nenhuma imagem carregada na memória.")
    
    # Verificar se a imagem é válida
    if imagem.size == 0:
        raise ValueError("A imagem está vazia.")
    
    # Converter para uint8 se necessário
    if imagem.dtype != np.uint8:
        imagem = imagem.astype(np.uint8)
    
    # Verificar se o kernel_size é válido
    if kernel_size[0] < 1 or kernel_size[1] < 1:
        raise ValueError("O tamanho do kernel deve ser maior que zero.")
    
    # Verificar se a imagem é grande o suficiente para o kernel
    if imagem.shape[0] < kernel_size[0] or imagem.shape[1] < kernel_size[1]:
        raise ValueError("A imagem é muito pequena para o tamanho do kernel escolhido.")
    
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    
    # Aplica o operador morfológico Top Hat
    imagem_processada = cv2.morphologyEx(imagem, cv2.MORPH_TOPHAT, elemento_estruturante)

    # Verificar se a operação foi bem-sucedida
    if imagem_processada is None:
        raise RuntimeError("Falha ao aplicar a operação de Top Hat morfológico.")

    # Salvar o resultado na memória
    memory.addEdit(imagem_processada)