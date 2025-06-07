import cv2
from service.image_memory import ImageMemory

#  Eliminação de ruídos
# Função para eliminar ruídos em uma imagem usando morfologia matemática
# Esta função aplica uma operação de abertura para remover pequenos ruídos na imagem
def eliminacao_ruidos(memory: ImageMemory):
    """
    Elimina ruídos em uma imagem usando morfologia matemática."""
    
    imagem = memory.getLastEdit()
    
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    
    # Aplica a operação de abertura para eliminar ruídos
    imagem_processada = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, elemento_estruturante)

    memory.addEdit(imagem_processada)