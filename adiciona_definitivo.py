from dados_jogo import DADOS, EARTH_RADIUS
from funções_ep2 import haversine
import math

def distancia_palpite_pais(palpite, pais):
    for continente in DADOS:
        for country in DADOS[continente]:
            if country == palpite:
                fi1 = DADOS[continente][country]['geo']['latitude']
                lan1 = DADOS[continente][country]['geo']['longitude']   
            if country == pais:
                fi2 = DADOS[continente][country]['geo']['latitude']
                lan2 = DADOS[continente][country]['geo']['longitude']    
    
    raio = EARTH_RADIUS

    return (f'{(haversine(raio, fi1, lan1, fi2, lan2)/1000):.3f}')

def adiciona_em_ordem(pais, dist, lista):
    if lista == []:
        return [[pais, dist]]
    
    lista_atualizada = []
    i = 0
    n = len(lista)

    if lista == []:
        return [pais, dist]

    while i < n:
        if lista[i][1] > dist:
            lista_atualizada.append([pais, dist])
            dist = lista[n-1][1]
        lista_atualizada.append(lista[i])
        i += 1

    return lista_atualizada

def esta_na_lista(pais, lista):
    i = 0
    n = len(lista)

    while i < n:
        if pais == lista[i][0]:
            return True
        i += 1

    return False

lista_palpites = [['china', 2855], ['italia', 6146]]
palpite = 'india'
pais_rand = 'russia'

if esta_na_lista(palpite, lista_palpites) == False:
    lista_palpites = adiciona_em_ordem(palpite, distancia_palpite_pais(palpite, pais_rand) , lista_palpites)
else:
    print('Tu já tentou esse, bixo... acorda, meu irmão!!!')

for catalogo in lista_palpites:
    print(f'{catalogo[0]} está a {catalogo[1]} km da resposta') 