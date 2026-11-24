import random
from enum import Enum

class Marca(Enum):
    Livre = 1
    Parede = 2
    Visitado = 3
    Beco = 4

def cria():
    n = 15
    labir = [[
    Marca.Livre for i in range(n)
] for j in range(n)]

    for i in range(n):
        labir[0][i] = Marca.Parede #Esquerda        
        labir[n][i] = Marca.Parede #Direita
        labir[i][0] = Marca.Parede #Cima
        labir[i][n] = Marca.Parede #Baixo

    for i in range(1, n-1):
        for j in range(1, n-1):
            if random.randrange(3) == 0:
                labir[i][j] = Marca.Parede
            else:
                labir[i][j] = Marca.Livre

    labir [2,2] = Marca.Livre
    labir [n-1,n] = Marca.Livre
    return labir