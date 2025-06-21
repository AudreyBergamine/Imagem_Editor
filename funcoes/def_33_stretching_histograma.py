import cv2
import numpy as np
from service.image_memory import ImageMemory

def stretching_histograma(memory: ImageMemory):
    """
    Aplica o stretching de histograma a uma imagem.
    Expande o contraste da imagem para usar toda a faixa de valores disponível.
    """
    
    imagem = memory.getLastEdit()

    # Verificar se há imagem
    if imagem is None:
        raise ValueError("Nenhuma imagem encontrada na memória.")

    # Converter para escala de cinza se for imagem colorida
    if len(imagem.shape) == 3:
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        imagem_cinza = imagem.copy()

    # Obter os valores mínimo e máximo dos pixels da imagem
    min_val = float(imagem_cinza.min())
    max_val = float(imagem_cinza.max())

    # Verificar se há variação na imagem (evitar divisão por zero)
    if min_val == max_val:
        # Se não há variação, retornar a imagem original
        memory.addEdit(imagem)
        return imagem

    # Aplicar o stretching
    imagem_stretched = ((imagem_cinza - min_val) / (max_val - min_val)) * 255
    
    # Garantir que os valores estejam no intervalo [0, 255]
    imagem_stretched = np.clip(imagem_stretched, 0, 255)
    
    # Converter para uint8
    imagem_resultado = imagem_stretched.astype(np.uint8)
    
    # Salvar o resultado na memória
    memory.addEdit(imagem_resultado)
    
    return imagem_resultado