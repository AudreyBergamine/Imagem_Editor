import cv2

# “Splitting” do histograma
# A função split_histogram separa os canais de cor de uma imagem 
# e calcula o histograma para cada canal.
def split_histograma(imagem):
    # Separar os canais de cor
    B, G, R = cv2.split(imagem)
    
    # Calcular o histograma para cada canal
    hist_B = cv2.calcHist([B], [0], None, [256], [0, 256])
    hist_G = cv2.calcHist([G], [0], None, [256], [0, 256])
    hist_R = cv2.calcHist([R], [0], None, [256], [0, 256])
    
    return hist_B, hist_G, hist_R
    
  