# -*- coding: utf-8 -*-

import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt


# Parametros
N = 100             # Numero de individuos de uma população
CR = 0.9             # Taxa de crossover
F = 0.5              # Constante de multação
GeracaoMax = 5
k = 0

d = 2                # Tamanho de cada individuo

# Função Rastrigin
def fit(x):
    ac = 0
    for i in range(d):
        ac = ac + x[i]**2 - np.cos(2*x[i]*np.pi)
    return 10 + ac

# Primeira população
x = np.zeros((N,d), dtype=np.float64)
for i in range(N):
    for j in range(d):
        x[i][j] = np.random.uniform(-5.12,5.12)

# Gerações
G = []
G.append(x)
    
v = []
u = []
for i in range(d):
    v.append(0)
    u.append(0)

while k < GeracaoMax:
    
    # Sorteio de 3 elementos da GERAÇÃO
    r = []
    for i in range(3):
        r.append(np.random.random_integers(0,N-1))

    for i in range(3):
        r[i] = G[k][r[i]]


    # Multação
    for i in range(d):
        v[i] = r[0][i] + F * (r[1][i] - r[2][i])
    
    # Crossover
    count = 0
    for i in range(d):
        # u : TRIAL
        random = np.random.uniform(0,1)
        if random <= CR:
            u[i] = v[i]
        else:
            u[i] = x[i]
            count += 1
        if count == 0:
            s = np.random.random_integers(0,d-1)
            u[s] = x[s]

    
    print(u)
    break