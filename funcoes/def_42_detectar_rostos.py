import cv2
import numpy as np
from service.image_memory import ImageMemory

def detectar_rostos(memory: ImageMemory):
    """
    Detecta rostos em uma imagem usando o classificador Haar Cascade do OpenCV.
    Desenha retângulos ao redor dos rostos detectados.
    """
    
    imagem = memory.getLastEdit()
    
    # Converter a imagem para escala de cinza para detecção
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Carregar o classificador Haar Cascade para detecção de rostos
    # O OpenCV já inclui classificadores pré-treinados
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    # Se não conseguir carregar o classificador, tentar caminho alternativo
    if face_cascade.empty():
        # Tentar carregar do diretório de dados do OpenCV
        import os
        opencv_data_path = os.path.join(cv2.__file__.replace('__init__.py', ''), 'data')
        cascade_path = os.path.join(opencv_data_path, 'haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Detectar rostos na imagem
    rostos = face_cascade.detectMultiScale(
        imagem_cinza,
        scaleFactor=1.1,  # Fator de redução da imagem
        minNeighbors=5,   # Número mínimo de vizinhos
        minSize=(30, 30), # Tamanho mínimo do rosto
        maxSize=(300, 300) # Tamanho máximo do rosto
    )
    
    # Criar uma cópia da imagem para desenhar os retângulos
    imagem_com_rostos = imagem.copy()
    
    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in rostos:
        # Desenhar retângulo verde ao redor do rosto
        cv2.rectangle(imagem_com_rostos, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Adicionar texto "Rosto" acima do retângulo
        cv2.putText(imagem_com_rostos, 'Rosto', (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Adicionar informação sobre o número de rostos detectados
    num_rostos = len(rostos)
    if num_rostos > 0:
        texto_info = f"Rostos detectados: {num_rostos}"
        cv2.putText(imagem_com_rostos, texto_info, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(imagem_com_rostos, "Nenhum rosto detectado", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Adicionar a imagem processada à memória
    memory.addEdit(imagem_com_rostos)
    
    # Retornar informações sobre a detecção
    coordenadas_list = []
    for (x, y, w, h) in rostos:
        coordenadas_list.append([int(x), int(y), int(w), int(h)])
    
    return {
        "num_rostos": num_rostos,
        "coordenadas": coordenadas_list,
        "imagem_processada": imagem_com_rostos
    } 