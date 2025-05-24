import cv2

def pegar_cor_de_um_pixel(imagem, x, y):
    """
    Retorna a cor de um pixel específico na imagem.

    Args:
        imagem: A imagem carregada (matriz).
        x: Coordenada x do pixel.
        y: Coordenada y do pixel.

    Returns:
        Uma tupla (r, g, b) representando as cores vermelho, verde e azul.
    """
    (b, g, r) = imagem[y, x]
    print(f"Cor do pixel na coordenada ({x}, {y}) -- Vermelho: {r}, Verde: {g}, Azul: {b}")
    return (r, g, b)