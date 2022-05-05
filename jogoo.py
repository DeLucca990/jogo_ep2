from funções_ep2 import *
from dados_jogo import DADOS, EARTH_RADIUS
#Adicionando países numa lista

lista_paises = []
for continentes in DADOS:
    for pais in DADOS[continentes]:
        lista_paises.append(pais)
#Página Inicial
print(lista_paises)
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

pais=normaliza(DADOS)
pais_rand=sorteia_pais(pais)
while True:
    palpite=str(input('Qual seu palpite:')).lower()
    while palpite not in lista_paises and palpite!='dica' and palpite!='inventario':
        print('País INVÁLIDO')
        palpite=str(input('Qual seu palpite:')).lower()
    if palpite!='dica' and palpite!='inventario' and palpite!='desisto':
        tentaviva_inicial-=1
        print(f'Você tem {tentaviva_inicial} tentativa(s)')
    if palpite=='dica':
        tentaviva_inicial=tentaviva_inicial
        print('Mercado de Dicas')
        print('-'*40)
        print('''
1. Cor da Bandeira  - custa 4 tentativas
2. Letra da capital - custa 3 tentativas
3. Área             - custa 6 tentativas
4. Populção         - custa 5 tentativas
5. Continente       - custa 7 tentativas
0. Sem dica         - custa 0 tentativas''')
        print('-'*40)
        while True:
            escolhe_dica=str(input('Escolha sua opção [0][1][2][3][4][5]:'))
            if escolhe_dica=='1':
                tentaviva_inicial-=4
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='2':
                tentaviva_inicial-=3
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='3':
                tentaviva_inicial-=6
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='4':
                tentaviva_inicial-=5
                print(f'Agora você tem {tentaviva_inicial} tentativa(s)')
                break
            elif escolhe_dica=='5':
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
    elif palpite=='desisto':
        esc_final=str(input('Vai arregar é???[s/n]')).lower()
        if esc_final=='s':
            break
    elif tentaviva_inicial==0:
        print('Meu amigo... tu só pode ter passado no conselho! GAME OVER!!!')
        break 