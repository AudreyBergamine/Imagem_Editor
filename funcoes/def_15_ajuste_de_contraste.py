import cv2
from service.image_memory import ImageMemory

def ajuste_de_contraste(memory: ImageMemory, k):
    # Obter as dimensões da imagem
    linhas, colunas = ImageMemory.shape[:2]
    
    # Criar uma cópia da ImageMemory para edição
    ImageMemory = ImageMemory.copy()
    
    # Ajustar o contraste
    for x in range(linhas):
        for y in range(colunas):
            for c in range(ImageMemory.shape[2]):  # Para cada canal de cor
                valor_original = ImageMemory[x, y, c]
                valor_editado = valor_original + (valor_original * k / 100)
                ImageMemory[x, y, c] = max(0, min(255, int(valor_editado)))  # Garantir valores válidos
    
    return ImageMemory
