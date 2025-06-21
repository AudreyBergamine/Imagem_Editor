import cv2
import numpy as np
from service.image_memory import ImageMemory

# "Splitting" do histograma
# A função split_histogram separa os canais de cor de uma imagem 
# e calcula o histograma para cada canal.
def split_histograma(memory: ImageMemory):
    """
    Separa os canais de cor de uma imagem e calcula o histograma para cada canal.
    Cria uma visualização mostrando os histogramas separados.
    """

    imagem = memory.getLastEdit()

    # Verificar se a imagem é colorida
    if len(imagem.shape) != 3 or imagem.shape[2] != 3:
        raise ValueError("A imagem fornecida não é colorida (esperado 3 canais).")

    # Separar os canais de cor
    B, G, R = cv2.split(imagem)

    # Calcular o histograma para cada canal
    hist_B = cv2.calcHist([B], [0], None, [256], [0, 256]).flatten()
    hist_G = cv2.calcHist([G], [0], None, [256], [0, 256]).flatten()
    hist_R = cv2.calcHist([R], [0], None, [256], [0, 256]).flatten()

    # Normalizar os histogramas para visualização
    hist_B_norm = cv2.normalize(hist_B, hist_B, 0, 200, cv2.NORM_MINMAX)
    hist_G_norm = cv2.normalize(hist_G, hist_G, 0, 200, cv2.NORM_MINMAX)
    hist_R_norm = cv2.normalize(hist_R, hist_R, 0, 200, cv2.NORM_MINMAX)
    
    # Criar imagem para visualização dos histogramas separados
    img_histograma = np.zeros((600, 800, 3), dtype=np.uint8)
    img_histograma.fill(255)  # Fundo branco
    
    # Desenhar os histogramas separados
    # Canal Azul (B)
    for i in range(256):
        altura_B = int(hist_B_norm[i])
        cv2.line(img_histograma, (i + 50, 550), (i + 50, 550 - altura_B), (255, 0, 0), 1)
    
    # Canal Verde (G)
    for i in range(256):
        altura_G = int(hist_G_norm[i])
        cv2.line(img_histograma, (i + 50, 550), (i + 50, 550 - altura_G), (0, 255, 0), 1)
    
    # Canal Vermelho (R)
    for i in range(256):
        altura_R = int(hist_R_norm[i])
        cv2.line(img_histograma, (i + 50, 550), (i + 50, 550 - altura_R), (0, 0, 255), 1)
    
    # Adicionar texto e legendas
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Título principal
    cv2.putText(img_histograma, 'Histograma Separado por Canais - RGB', (50, 30), 
                font, 0.8, (0, 0, 0), 2)
    
    # Eixo X
    cv2.putText(img_histograma, 'Intensidade', (350, 580), 
                font, 0.6, (0, 0, 0), 2)
    
    # Legendas dos canais
    cv2.putText(img_histograma, 'Canal Azul (B)', (50, 80), 
                font, 0.6, (255, 0, 0), 2)
    cv2.putText(img_histograma, 'Canal Verde (G)', (50, 110), 
                font, 0.6, (0, 255, 0), 2)
    cv2.putText(img_histograma, 'Canal Vermelho (R)', (50, 140), 
                font, 0.6, (0, 0, 255), 2)
    
    # Adicionar informações sobre os canais
    cv2.putText(img_histograma, f'Max B: {int(hist_B.max())}', (50, 170), 
                font, 0.5, (255, 0, 0), 1)
    cv2.putText(img_histograma, f'Max G: {int(hist_G.max())}', (50, 190), 
                font, 0.5, (0, 255, 0), 1)
    cv2.putText(img_histograma, f'Max R: {int(hist_R.max())}', (50, 210), 
                font, 0.5, (0, 0, 255), 1)
    
    # Salvar a visualização do histograma na memória
    memory.addEdit(img_histograma)
    
    # Retornar também os dados do histograma
    return hist_R.astype(int).tolist(), hist_G.astype(int).tolist(), hist_B.astype(int).tolist()
    
  