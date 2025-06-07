import cv2
from service.image_memory import ImageMemory

def pegar_cor_de_um_pixel(memory: ImageMemory, x, y):
    
    """
    Retorna a cor de um pixel específico na imagem.

    Args:
        imagem: A imagem carregada (matriz).
        x: Coordenada x do pixel.
        y: Coordenada y do pixel.

    Returns:
        Uma tupla (r, g, b) representando as cores vermelho, verde e azul.
    """
    imagem = memory.getLastEdit()
    
    # Verifica se as coordenadas estão dentro dos limites da imagem
    if 0 <= x < imagem.shape[1] and 0 <= y < imagem.shape[0]:
        (b, g, r) = imagem[y, x]
        print(f"Cor do pixel na coordenada ({x}, {y}) -- Vermelho: {r}, Verde: {g}, Azul: {b}")
        return (r, g, b)
    else:
        print(f"Coordenadas ({x}, {y}) estão fora dos limites da imagem.")
        return None