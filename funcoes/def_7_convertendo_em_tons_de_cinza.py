import cv2

from service.image_memory import ImageMemory

# Função para converter uma imagem colorida em tons de cinza
def convertendo_em_tons_de_cinza(memory: ImageMemory):
    imagem = memory.getLastEdit()
    
    # Só converte se for colorida (3 canais)
    if len(imagem.shape) == 3 and imagem.shape[2] == 3:
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        memory.addEdit(imagem_cinza)
        memory.update()
    else:
        print("A imagem já está em tons de cinza.")
    
