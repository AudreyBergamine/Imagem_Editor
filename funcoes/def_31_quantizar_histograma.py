import cv2
import numpy as np
from service.image_memory import ImageMemory

# Quantização ou agrupamento do histograma
def quantizar_histograma(memory: ImageMemory, quantidade_de_cores: int):
    """
    Quantiza as cores de uma imagem usando o algoritmo K-means.
    Este método agrupa as cores com base na sua frequência na imagem,
    criando um resultado com maior impacto visual.
    """
    imagem = memory.getLastEdit()

    # Remodelar a imagem para uma lista de pixels (N_pixels, 3) e converter para float32
    pixels = imagem.reshape((-1, 3))
    pixels = np.float32(pixels)

    # Definir critérios de parada para o K-means e aplicar o algoritmo
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(pixels, quantidade_de_cores, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Converter os centros (as novas cores da paleta) de volta para uint8
    centers = np.uint8(centers)
    
    # Mapear cada pixel original para a sua nova cor (o centro do seu cluster)
    imagem_quantizada_flat = centers[labels.flatten()]
    
    # Remodelar a imagem de volta para as dimensões originais
    imagem_quantizada = imagem_quantizada_flat.reshape(imagem.shape)
    
    memory.addEdit(imagem_quantizada)
