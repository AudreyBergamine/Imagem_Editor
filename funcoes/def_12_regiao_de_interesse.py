import cv2

def regiao_de_interesse(imagem):
    
    # Definir a região de interesse (exemplo: linhas 0 a 30, colunas 20 a 50)
    ROI = imagem[0:30, 20:50]
    
    # Exibir a região de interesse
    cv2.imshow("Região de Interesse", ROI)
    
    # Salvar a região de interesse em um arquivo
    cv2.imwrite("ROI1.png", ROI)
    
    # Retornar a região de interesse
    return ROI

