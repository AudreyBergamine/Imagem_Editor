import cv2
from service.image_memory import ImageMemory

def regiao_de_interesse(memory: ImageMemory):
    """ Extrai e exibe uma região de interesse da imagem. """
    
    imagem = memory.getLastEdit()
    
    # Definir a região de interesse (exemplo: linhas 0 a 30, colunas 20 a 50)
    ROI = imagem[0:30, 20:50]
    memory.addEdit(ROI)

    # Removido cv2.imshow para evitar problemas de compatibilidade
    # A região de interesse será exibida na interface principal do editor
    
    # Salvar a região de interesse em um arquivo
    cv2.imwrite("ROI1.png", ROI)
    
    # Retornar a região de interesse
    return ROI

