import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import abrir_imagem, selecionar_imagem

def adicionar_imagens(memory: ImageMemory):
    """
    Adiciona duas imagens pixel a pixel e retorna a imagem resultante.
    """
    
    imagem = memory.getLastEdit()
    
    # Abrir a segunda imagem
    img2 = selecionar_imagem()

    # Verificar se as imagens foram carregadas corretamente
    if imagem is None or img2 is None:
        raise ValueError("Uma ou ambas as imagens não foram carregadas corretamente.")

    # Garantir que as imagens tenham o mesmo tamanho e número de canais
    if imagem.shape != img2.shape:
        img2 = cv2.resize(img2, (imagem.shape[1], imagem.shape[0]))
        if len(imagem.shape) != len(img2.shape):
            if len(imagem.shape) == 2:
                img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            elif len(imagem.shape) == 3 and len(img2.shape) == 2:
                img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

    # Realizar a adição das imagens
    img_resultado = cv2.add(imagem, img2)

    # Retornar a imagem resultante
    memory.addEdit(img_resultado)
