from funções_ep2 import *
from dados_jogo import DADOS, EARTH_RADIUS
from funções_ep2 import haversine
from funções_ep2 import esta_na_lista
from funções_ep2 import adiciona_em_ordem
from distancia import distancia_palpite_pais
#Funções Adicionais

dic_dicas={' dica1':'1. Cor da Bandeira  - custa 4 tentativas',
            'dica2':'2. Letra da capital - custa 3 tentativas',
            'dica3':'3. Área             - custa 6 tentativas',
            'dica4':'4. Populção         - custa 5 tentativas',
            'dica5':'5. Continente       - custa 7 tentativas',
            'dica0':'0. Sem dica         - custa 0 tentativas'}

lista_palpites = []
lista_paises = []
for continentes in DADOS:
    for pais in DADOS[continentes]:
        lista_paises.append(pais)
#Página Inicial

print('='*43)
print('|                                         |')
print('| Bem vindo ao Akinator Reverso de Países |')
print('|                                         |')
print('=======      Design de Software     =======')
print('')
print('Comandos:')
print('    Dica       - Entra no mercado de dicas')
print('    Desisto    - Desiste da rodada')
print('    Inventario - Exibe sua posição')
print('')
print('Um país foi ecolhido, tente adivinhar, e veja se você manja de geografia!!!')
tentaviva_inicial=20
print(f'Você tem {tentaviva_inicial} tentativa(s)')
#Começando o jogo

numero_das_dicas=['0|','1|','2|','3|','4|','5']
numero_das_dicas_str=''.join(numero_das_dicas)
pais=normaliza(DADOS)
pais_rand=sorteia_pais(pais)

while True:
    palpite=str(input('Qual seu palpite:')).lower().strip()
    while palpite not in lista_paises and palpite!='dica' and palpite!='inventario' and palpite!='desisto':
        print('País INVÁLIDO')
        palpite=str(input('Qual seu palpite:')).lower().strip()
    if palpite!='dica' and palpite!='inventario' and palpite!='desisto':
        tentaviva_inicial-=1

        if esta_na_lista(palpite, lista_palpites) == False:
            lista_palpites = adiciona_em_ordem(palpite, distancia_palpite_pais(palpite, pais_rand) , lista_palpites)
        else:
            print('Tu já tentou esse, bixo... acorda, meu irmão!!!')

        for catalogo in lista_palpites:
            print(f'{catalogo[0]} está a {catalogo[1]} km da resposta') 

        print(f'Você tem {tentaviva_inicial} tentativa(s)')
    if palpite=='dica':
        print('Dicas da pulga')
        print('-'*40)
        for k,v in dic_dicas.items():
            print(v)
        print('-'*40)
        while True:
            escolhe_dica=str(input(f'Escolha sua opção [{numero_das_dicas_str}]:'))
            if escolhe_dica=='1':
                if tentaviva_inicial<4:
                    print('Acabou o estoque de dicas, maluco!')
                    break
                tentaviva_inicial-=4
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='2':
                if tentaviva_inicial<3:
                    print('Acabou o estoque de dicas, maluco!')
                    break
                tentaviva_inicial-=3
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='3':
                numero_das_dicas.remove('3|')
                numero_das_dicas_str=''.join(numero_das_dicas)
                if tentaviva_inicial<6:
                    print('Acabou o estoque de dicas, maluco!')
                    break
                del dic_dicas['dica3']
                tentaviva_inicial-=6
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='4':
                numero_das_dicas.remove('4|')
                numero_das_dicas_str=''.join(numero_das_dicas)
                if tentaviva_inicial<5:
                    print('Acabou o estoque de dicas, maluco!')
                    break
                del dic_dicas['dica4']
                tentaviva_inicial-=5
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='5':
                numero_das_dicas.remove('5')
                numero_das_dicas_str=''.join(numero_das_dicas)
                if tentaviva_inicial<7:
                    print('Acabou o estoque de dicas, maluco!')
                    break
                del dic_dicas['dica5']
                tentaviva_inicial-=7
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='0':
                break
            else:
                print('Digite uma dica válida')





    #Final do jogo
    if palpite == pais_rand:
        print('Acertou, danadinho!')
        break
    #if palpite in lista_paises and palpite != pais_rand:
        #dis = 
    elif palpite=='desisto':
        esc_final=str(input('Vai arregar é???[s/n]')).lower()
        if esc_final=='s':
            print(f'Você é péssimo em Geografia!!! O país era: {pais_rand}')
            break
    elif tentaviva_inicial<=0:
        print('Meu amigo... tu só pode ter passado no conselho! GAME OVER!!!')
        break 