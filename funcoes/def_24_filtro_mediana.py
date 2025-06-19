import cv2
import numpy as np
from service.image_memory import ImageMemory

def filtro_mediana(memory: ImageMemory):
    """ 
    Aplica um filtro de mediana a uma imagem usando a função otimizada do OpenCV.
    Este filtro substitui cada pixel pelo valor mediano dos pixels vizinhos.
    """
    try:
        # Obtém a imagem atual
        imagem = memory.getLastEdit()
        
        if imagem is None:
            print("Erro: Nenhuma imagem carregada na memória")
            return
        
        # Verifica se a imagem é válida
        if imagem.size == 0:
            print("Erro: Imagem inválida ou vazia")
            return
        
        # Cria uma cópia da imagem para não modificar a original
        imagem_filtrada = imagem.copy()
        
        # Aplica o filtro de mediana usando a função otimizada do OpenCV
        # Usa kernel 3x3 para o filtro de mediana
        kernel_size = 3
        imagem_filtrada = cv2.medianBlur(imagem_filtrada, kernel_size)
        
        # Adiciona a imagem processada à memória
        memory.addEdit(imagem_filtrada)
        
        print("Filtro de mediana aplicado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao aplicar filtro de mediana: {str(e)}")
        print(f"Tipo do erro: {type(e).__name__}")

"""
Exemplo do material da Prof Marcia: 

# Carregue a imagem
imgOriginal = cv2.imread("minhaimagem.jpeg", 0)
# Defina o tamanho da janela para o filtro de mediana
tamanho_da_janela = 3
# Aplicar o filtro de mediana
imgFiltroMediana = cv2.medianBlur(imgOriginal, tamanho_da_janela)
# Salvar a imagem filtrada
cv2.imwrite('imagem_filtrada.jpg', imgFiltroMediana)

"""