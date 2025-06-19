import cv2
import numpy as np
from service.image_memory import ImageMemory

def converter_modelos_cor(memory: ImageMemory):
    """
    Mostra um grid 2x2 com a imagem em 4 modelos de cor diferentes.
    """
    img = memory.getLastEdit()
    h, w = img.shape[:2]

    # Modelos de cor
    imagemNC = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imagemNC = cv2.cvtColor(imagemNC, cv2.COLOR_GRAY2BGR)  # Para ficar com 3 canais

    imagemCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    imagemCrCb_vis = cv2.cvtColor(imagemCrCb, cv2.COLOR_YCrCb2BGR)  # Para visualização

    imagemLab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    imagemLab_vis = cv2.cvtColor(imagemLab, cv2.COLOR_LAB2BGR)  # Para visualização

    imagemHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imagemHSV_vis = cv2.cvtColor(imagemHSV, cv2.COLOR_HSV2BGR)  # Para visualização

    # Garantir que todas as imagens tenham o mesmo tamanho
    imagens = [imagemNC, imagemCrCb_vis, imagemLab_vis, imagemHSV_vis]
    imagens = [cv2.resize(im, (w, h)) for im in imagens]

    # Adicionar legendas em cada imagem
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    thickness = 2
    cor_texto = (255, 255, 255)
    cor_sombra = (0, 0, 0)
    offset = 5
    # 1a imagem: Cinza
    cv2.putText(imagens[0], 'Cinza', (20, 40), font, font_scale, cor_sombra, thickness+2, cv2.LINE_AA)
    cv2.putText(imagens[0], 'Cinza', (20, 40), font, font_scale, cor_texto, thickness, cv2.LINE_AA)
    # 2a imagem: YCrCb
    cv2.putText(imagens[1], 'YCrCb', (20, 40), font, font_scale, cor_sombra, thickness+2, cv2.LINE_AA)
    cv2.putText(imagens[1], 'YCrCb', (20, 40), font, font_scale, cor_texto, thickness, cv2.LINE_AA)
    # 3a imagem: LAB
    cv2.putText(imagens[2], 'LAB', (20, 40), font, font_scale, cor_sombra, thickness+2, cv2.LINE_AA)
    cv2.putText(imagens[2], 'LAB', (20, 40), font, font_scale, cor_texto, thickness, cv2.LINE_AA)
    # 4a imagem: HSV
    cv2.putText(imagens[3], 'HSV', (20, 40), font, font_scale, cor_sombra, thickness+2, cv2.LINE_AA)
    cv2.putText(imagens[3], 'HSV', (20, 40), font, font_scale, cor_texto, thickness, cv2.LINE_AA)

    # Montar grid 2x2 na ordem solicitada
    # 1a: imagemNC | 2a: imagemCrCb_vis
    # 3a: imagemLab_vis | 4a: imagemHSV_vis
    topo = np.hstack([imagens[0], imagens[1]])
    baixo = np.hstack([imagens[2], imagens[3]])
    grid = np.vstack([topo, baixo])

    memory.addEdit(grid)
    return grid
