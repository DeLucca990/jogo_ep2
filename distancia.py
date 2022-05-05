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

    return haversine(raio, fi1, lan1, fi2, lan2)

print(distancia_palpite_pais('brasil', 'franca'))