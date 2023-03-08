from opencv import imread, imwrite, ImreadModes
import numpy as np
from functions import convolute2


def calcular_bordas():
    # Le a imagem
    im = imread("lena_gray.bmp", ImreadModes.IMREAD_GRAYSCALE)

    # Gera as matrizes para a convolucao
    h_kernel = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

    v_kernel = np.array([[-1, -2, -1],
                         [+0, +0, +0],
                         [+1, +2, +1]])

    # Realiza a convolucao
    h_img = convolute2(im, h_kernel)
    v_img = convolute2(im, v_kernel)
    new_img = h_img + v_img

    # Escreve o resultado
    imwrite('test.bmp', new_img)


if __name__ == '__main__':
    calcular_bordas()
