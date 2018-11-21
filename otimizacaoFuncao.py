import numpy as np
import matplotlib.pyplot as plt


N = 100
d = 2
F = 0.5
CR = 0.9
GeracaoMax = 500
G = []
Melhor = []

def fit(x):
    ac = 0
    for i in x:
        ac = ac + i**2 - 10*np.cos(2*i*np.pi)
    return ac + 10 * d

x = np.zeros((N,d),dtype=np.float64)
for i in range(N):
    for j in range(d):
        x[i][j] = np.random.uniform(-5.12,5.12)

G.append(x)

k = 0
while k < GeracaoMax:

    # Sorteio
    r1 = x[np.random.random_integers(0,N-1)]
    r2 = x[np.random.random_integers(0,N-1)]
    r3 = x[np.random.random_integers(0,N-1)]

    # Mutação
    v = np.zeros(d,dtype=np.float64)
    for i in range(d):
        v[i] = r1[i] + F * (r2[i] - r3[i])

    # Crossover
    u = np.zeros((N,d),dtype=np.float64)
    for i in range(N):
        c = 0
        for j in range(d):
            random = np.random.uniform(0,1)
            if random <= CR:
                u[i][j] = v[j]
            else:
                u[i][j] = x[i][j]
                c += 0
        if c == 0:
            s = np.random.random_integers(0,d-1)
            u[i][s] = x[i][s]

    # Criando uma nova geração
    sel = []
    for i in range(N):
        if fit(u[i]) < fit(x[i]):
            sel.append(u[i])
        else:
            sel.append(x[i])
        
    k += 1
    x = sel

    G.append(sel)

menor = x[0]
for i in x:
    if fit(i) <= fit(menor):
        menor = i

grafico = [[],[]]
g = 0
for i in range(GeracaoMax+1):
    menor = G[i][0]
    for j in G[g]:
        if fit(j) <= fit(menor):
            menor = j
    grafico[1].append(fit(j))
    grafico[0].append(g)
    g += 1

plt.plot(grafico[0],grafico[1],'go')
plt.axis([0,GeracaoMax+1,min(grafico[1]), max(grafico[1])])
plt.show()

print('MELHOR INDIVÍDUO: {}'.format(menor))

    