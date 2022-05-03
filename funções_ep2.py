def normaliza(dic):
    dic_normaliza={}
    dic_valor={}
    for cont,paises in dic.items():
        for pais,espec in paises.items():
            dic_valor=espec
            dic_valor['continente']=cont
            dic_normaliza[pais]=dic_valor
    return dic_normaliza

from random import choice
def sorteia_pais(dic):
    aleato=choice(list(dic))
    return aleato

import math 
def haversine(r,phi1,lam1,phi2,lam2):
    phi1r=math.radians(phi1)
    phi2r=math.radians(phi2)
    lam1r=math.radians(lam1)
    lam2r=math.radians(lam2)
    dentro=(math.sin((phi2r-phi1r)/2))**2 + math.cos(phi1r)*math.cos(phi2r)*(math.sin((lam2r-lam1r)/2))**2
    n_quero=math.asin(math.sqrt(dentro))
    d=2*r*n_quero
    return d 

def adiciona_em_ordem(pais,dis,lista_p):
    esse=[pais,dis]
    final=[]
    if len(lista_p)==0:
        return [esse]
    for i in range(0,len(lista_p)):    
        if lista_p[i][1]>dis:
            lista_p.insert(i,esse)
        if dis>lista_p[len(lista_p)-1][1]:
            lista_p.append(esse) 
    for element in lista_p:
        if element not in final:
            final.append(element)
    return final

def esta_na_lista(pais,lista):
    c=0
    for i in range(0,len(lista)):
        if pais in lista[i][0]:
            c+=1
    if c>=1:
        return True
    else:
        return False 

import random
def sorteia_letra(pala,lista):
    palal=pala.lower()
    proibido=['.', ',', '-', ';', ' ']
    lista_pala=[]
    c=0
    for i in range(0,len(palal)):
        if palal[i] in proibido or palal[i] in lista:
            c+=1
        if palal[i] not in proibido and palal[i] not in lista:
            lista_pala.append(palal[i])
    if c==len(palal):
        return ''
    else:
        escolhido=random.choice(lista_pala)
        return escolhido      
