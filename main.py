"""
    1 - O daltonismo é uma condição que possui como principal característica a dificuldade para distinguir o vermelho e o verde e, 
    com menos frequência, o azul e o amarelo. Implemente uma solução, utilizando OpenCV, que leia uma imagem e indique se um daltônico 
    poderá ter dificuldade na identificação das cores vermelho e/ou verde. Uma possível solução para ajudar daltônicos, seria inserir 
    algum rótulo/texto indicando a área que ele poderá dificuldade na identificação. Implemente esta solução na imagem.

    2 - Implemente uma solução que leia um vídeo e rotule/indique o(s) objeto(s) em movimento na cena. 

"""
import numpy as np
import cv2 as cv

def main():
    image = cv.imread("paisagem.jfif", cv.IMREAD_COLOR)

    if image is None:
        print("impossivel carregar a imagem!")
        return
    
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, (36, 25, 25), (70, 255,255))

    imask = mask > 0
    green = np.zeros_like(image, np.uint8)
    green[imask] = image[imask]

    cv.imshow("green", green)

    height, width, depth = image.shape
    
    cv.waitKey(0)

main()

