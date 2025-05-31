import cv2
import numpy as np

# Função para aplicar o filtro mediana 
def filtro_mediana(imagem):
    
    # Obter dimensões da imagem
    linhas, colunas = imagem.shape
    # Criar uma cópia da imagem para armazenar a imagem filtrada
    imagem_filtrada = np.zeros_like(imagem)
    
    # Percorrer cada pixel da imagem (ignorando as bordas)
    for x in range(1, linhas - 1):
        for y in range(1, colunas - 1):
            # Criar um vetor para armazenar os valores da vizinhança 3x3
            vetor = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    vetor.append(imagem[x + i, y + j])
            
            # Ordenar o vetor
            vetor.sort()
            
            # Atribuir o valor mediano ao pixel central
            imagem_filtrada[x, y] = vetor[4]  # Posição central do vetor ordenado
    
    return imagem_filtrada

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