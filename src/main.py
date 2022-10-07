"""
    1 - O daltonismo é uma condição que possui como principal característica a dificuldade para distinguir o vermelho e o verde e, 
    com menos frequência, o azul e o amarelo. Implemente uma solução, utilizando OpenCV, que leia uma imagem e indique se um daltônico 
    poderá ter dificuldade na identificação das cores vermelho e/ou verde. Uma possível solução para ajudar daltônicos, seria inserir 
    algum rótulo/texto indicando a área que ele poderá dificuldade na identificação. Implemente esta solução na imagem.

    2 - Implemente uma solução que leia um vídeo e rotule/indique o(s) objeto(s) em movimento na cena. 

"""


from question1.main import identifyColors
from question2.main import readVideo


def main():
    readVideo()
    identifyColors()


main()
