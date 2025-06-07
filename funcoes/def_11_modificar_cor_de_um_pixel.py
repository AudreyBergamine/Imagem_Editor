import cv2
from service.image_memory import ImageMemory
from .def_10_pegar_cor_de_um_pixel import pegar_cor_de_um_pixel

def modificar_cor_de_um_pixel(memory: ImageMemory, coordenadas, nova_cor, verbose=False):
    
    """
    Modifica a cor de um pixel ou região da imagem.

    Args:
        imagem: A imagem a ser editada.
        coordenadas: Tupla ou slice indicando o pixel ou região a ser alterada.
        nova_cor: Tupla representando a nova cor no formato (B, G, R).
        verbose: Booleano para exibir mensagens de depuração.

    Returns:
        A imagem editada.
    """
    # Obtém a imagem atual da memória
    imagem = memory.getLastEdit()
    
    
    # Validação de entrada
    if not (0 <= coordenadas[0] < imagem.shape[0] and 0 <= coordenadas[1] < imagem.shape[1]):
        raise ValueError("As coordenadas estão fora dos limites da imagem.")
    if not (len(nova_cor) == 3 and all(0 <= c <= 255 for c in nova_cor)):
        raise ValueError("A nova cor deve ser uma tupla (B, G, R) com valores entre 0 e 255.")

    cor_original = pegar_cor_de_um_pixel(imagem, coordenadas[0], coordenadas[1])
    if verbose:
        print(f"Cor original do pixel na coordenada {coordenadas} -- Vermelho: {cor_original[0]}, Verde: {cor_original[1]}, Azul: {cor_original[2]}")
        print(f"Nova cor do pixel na coordenada {coordenadas} -- Vermelho: {nova_cor[0]}, Verde: {nova_cor[1]}, Azul: {nova_cor[2]}")

    # Modifica a cor do pixel
    imagem[coordenadas] = nova_cor
    return imagem
