from time import time

arquivo = open('arquivo.txt', 'r')
pontos_drone = []

tempo_inicial = time()

def lendo_matriz():
    coordens = {}
    i, j = map(int, arquivo.readline().split(' '))
    for l in range(i):
        line = arquivo.readline().split(' ')
        if len(line) == j:
            for colun in range(len(line)):
                if line[colun].find("\n") != -1:
                    line[colun] = line[colun][-2]
                if line[colun] not in '0':
                    coordens[line[colun]] = (l, colun)
    return coordens


def permutacao(coordens, i=0):
    if i == len(coordens):
        pontos_drone.append('R' + "".join(coordens) + 'R')

    for j in range(i, len(coordens)):
            rota = [i for i in coordens]
            rota[i], rota[j] = rota[j], rota[i]
            permutacao(rota, i+1)
    return pontos_drone


def menor_rota(rotas, coordens):
    passos = {}
    limite = 10**4
    menor = str
    for r in rotas:
        custo = 0
        for p in range(len(r)-1):
            custo += abs(coordens[r[p]][0] - coordens[r[p-1]][0]) + abs(coordens[r[p]][1] - coordens[r[p-1]][1])
        t = [i for i in r[1:(len(r)-1)]]
        passos[" ". join(t)] = custo

    for i in passos.items():
        k, q = i
        if q < limite:
            menor = k
            limite = q
    return print(menor)


def implementacao():
    matriz = lendo_matriz()
    return menor_rota(permutacao([p for p in matriz if p != 'R']), matriz)


implementacao()

tempo_final = time()

print(f"\nTempo de execução do algoritmo: {tempo_final - tempo_inicial} segundos.")
