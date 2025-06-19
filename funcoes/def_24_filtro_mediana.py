import cv2
import numpy as np
from service.image_memory import ImageMemory

# Função para aplicar o filtro mediana 
def filtro_mediana(memory: ImageMemory, tamanho_janela: int = 3):
    """
    Aplica um filtro de mediana a uma imagem usando OpenCV.
    :param memory: Instância de ImageMemory.
    :param tamanho_janela: Tamanho da janela do filtro (deve ser ímpar e >= 3).
    """
    imagem = memory.getLastEdit()

    # Verificações de segurança
    if imagem is None:
        raise ValueError("Nenhuma imagem carregada na memória.")
    if tamanho_janela < 3 or tamanho_janela % 2 == 0:
        raise ValueError("O tamanho da janela deve ser um número ímpar maior ou igual a 3.")
    if imagem.dtype not in [np.uint8, np.uint16]:
        imagem = imagem.astype(np.uint8)
    if min(imagem.shape[0], imagem.shape[1]) < tamanho_janela:
        raise ValueError("A imagem é muito pequena para o tamanho da janela escolhido.")

    imagem_filtrada = cv2.medianBlur(imagem, tamanho_janela)
    memory.addEdit(imagem_filtrada)

"""
Exemplo do material da Prof Marcia: 

# Carregue a imagem
imgOriginal = cv2.imread("minhaimagem.jpeg", 0)
# Defina o tamanho da janela para o filtro de mediana
tamanho_da_janela = 3
# Aplicar o filtro de mediana
imgFiltroMediana = cv2.medianBlur(imgOriginal, tamanho_da_janela)
# Exibe a imagem original e a imagem filtrada
cv2.imshow("Original", imgOriginal)
cv2.imshow("Filtro_mediana", imgFiltroMediana)
# Salvar a imagem filtrada
cv2.imwrite('imagem_filtrada.jpg', imgFiltroMediana)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""