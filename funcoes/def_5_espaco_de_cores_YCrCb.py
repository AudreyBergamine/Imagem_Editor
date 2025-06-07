import cv2

def espaco_de_cores_YCrCb(imagem):
    """ Converte uma imagem para o espaço de cores YCrCb e extrai seus canais. """

    # Converter a imagem para o espaço de cores YCrCb
    imagemYCrCb = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    
    # Extrair os canais Y, Cr e Cb
    canal_Y, canal_Cr, canal_Cb = cv2.split(imagemYCrCb)
    
    return imagemYCrCb, canal_Y, canal_Cr, canal_Cb