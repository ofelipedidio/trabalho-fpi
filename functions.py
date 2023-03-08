import numpy as np


# Isso eh muito lento, nao vale a pena otimizar em python, pra acelerar, da pra usar uma biblioteca como "scipy"
def convolute2(matrix: np.ndarray, kernel: np.ndarray):
    k_size = len(kernel)
    m_height, m_width = matrix.shape
    padded = np.pad(matrix, (k_size - 1, k_size - 1))

    output = []
    for i in range(m_height):
        for j in range(m_width):
            output.append(np.sum(padded[i:k_size + i, j:k_size + j] * kernel))

    output = np.array(output).reshape((m_height, m_width))
    return output