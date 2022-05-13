import random 
from funções_ep2 import *
from dados_jogo import DADOS, EARTH_RADIUS
from funções_ep2 import haversine
from funções_ep2 import esta_na_lista
from funções_ep2 import adiciona_em_ordem
from funções_ep2 import sorteia_letra
from distancia import distancia_palpite_pais

repete = 's'

while repete == 's':    

    #Dicionários/Listas adicionadas

    dic_dicas_opcoes={}
    pop = 0
    area_final=0
    cont=0
    letras = []
    restritos = ['.', ',', '-', ';', ' '] 
    cores_bandeira = []
    cores_ditas = []

    dic_dicas={' dica1':'1. Cor da Bandeira  - custa 4 tentativas',
                'dica2':'2. Letra da capital - custa 3 tentativas',
                'dica3':'3. Área             - custa 6 tentativas',
                'dica4':'4. População        - custa 5 tentativas',
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
    print(f'Você tem \033[36m{tentaviva_inicial}\033[m tentativa(s)')

    #Começando o jogo

    numero_das_dicas=['0','|1','|2','|3','|4','|5']
    numero_das_dicas_str=''.join(numero_das_dicas)
    pais=normaliza(DADOS)
    pais_rand=sorteia_pais(pais)

    for continente in DADOS:
        for country in DADOS[continente]:
            if country == pais_rand:
                for tipo,cor in DADOS[continente][country]['bandeira'].items():
                    if cor > 0:
                        if tipo != 'outras':
                            cores_bandeira.append(tipo)

    while True:

    #Selecionando um palpite

        palpite=str(input('Qual seu palpite:')).lower().strip()
        print('')
    #Palpite inválido

        while palpite not in lista_paises and palpite!='dica' and palpite!='dicas' and palpite!='inventario' and palpite!='desisto':
            print('País INVÁLIDO')
            print('')
            palpite=str(input('Qual seu palpite:')).lower().strip()

    #Uma vez que o palpite é válido... 

        if palpite!='dica' and palpite!='dicas' and palpite!='inventario' and palpite!='desisto':
            tentaviva_inicial-=1
            print('Distâncias:')
            if esta_na_lista(palpite, lista_palpites) == False:
                lista_palpites = adiciona_em_ordem(palpite, distancia_palpite_pais(palpite, pais_rand) , lista_palpites)
            else:
                print('\033[36mTu já tentou esse, bixo... acorda, meu irmão!!!\033[m')
            for catalogo in lista_palpites:
                    if 0<catalogo[1]<1000:
                        print(f'\033[32m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                    elif 1000<=catalogo[1]<2000:
                        print(f'\033[33m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                    elif 2000<=catalogo[1]<5000:
                        print(f'\033[34m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                    elif 5000<=catalogo[1]<10000:
                        print(f'\033[35m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                    elif catalogo[1]>=10000:
                        print(f'\033[31m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
            if tentaviva_inicial>10:
                print(f'Você tem \033[36m{tentaviva_inicial}\033[m tentativa(s)')
            if 5<tentaviva_inicial<=10:
                print(f'Você tem \033[33m{tentaviva_inicial}\033[m tentativa(s)')
            if tentaviva_inicial<=5:
                print(f'Você tem \033[31m{tentaviva_inicial}\033[m tentativa(s)')    
            
        #Pedindo e implementando as funções nas dicas...
        
        if palpite=='dica' or palpite=='dicas':
            print('Tá precisando de dicas né...')
            print('-'*40)
            for k,v in dic_dicas.items():
                print(v)
            print('-'*40)
            while True:
                escolhe_dica=str(input(f'Escolha sua opção [{numero_das_dicas_str}]:'))
                if escolhe_dica=='1':
                    if tentaviva_inicial<4:
                        print(f'Tá com alzheimer?? Você só tem \033[31m{tentaviva_inicial}\033[m tentativas, maluco!')
                        break
                    else:
                        if cores_bandeira != []:
                            cor_sorteada = random.choice(cores_bandeira)
                            cores_ditas.append(cor_sorteada)
                            cores_bandeira.remove(cor_sorteada)
                            dic_dicas_opcoes['cores'] = cores_ditas
                            cores_ditas_str=', '.join(cores_ditas)
                            tentaviva_inicial-=4
                        else:
                            print('As cores são só essas mesmo... se não matar agora é leigo!')
                    if tentaviva_inicial>10:
                        print(f'Você tem \033[36m{tentaviva_inicial}\033[m tentativa(s)')
                    if 5<tentaviva_inicial<=10:
                        print(f'Você tem \033[33m{tentaviva_inicial}\033[m tentativa(s)')
                    if tentaviva_inicial<=5:
                        print(f'Você tem \033[31m{tentaviva_inicial}\033[m tentativa(s)')
                    break
                if escolhe_dica=='2':
                    if tentaviva_inicial<3:
                        print(f'Tá com alzheimer?? Você só tem \033[31m{tentaviva_inicial}\033[m tentativas, maluco!')
                        break
                    else:
                        for continente in DADOS:
                            for country in DADOS[continente]:
                                if country == pais_rand:
                                    letras.append(sorteia_letra(DADOS[continente][country]['capital'], restritos))
                                    restritos += letras
                                    dic_dicas_opcoes['letras'] = letras
                                    letras_str=', '.join(letras) 
                    tentaviva_inicial-=3
                    if tentaviva_inicial>10:
                        print(f'Você tem \033[36m{tentaviva_inicial}\033[m tentativa(s)')
                    if 5<tentaviva_inicial<=10:
                        print(f'Você tem \033[33m{tentaviva_inicial}\033[m tentativa(s)')
                    if tentaviva_inicial<=5:
                        print(f'Você tem \033[31m{tentaviva_inicial}\033[m tentativa(s)')
                    break
                if escolhe_dica=='3':
                    numero_das_dicas.remove('|3')
                    numero_das_dicas_str=''.join(numero_das_dicas)
                    if tentaviva_inicial<6:
                        del dic_dicas['dica3']
                        print(f'Tá com alzheimer?? Você só tem \033[31m{tentaviva_inicial}\033[m tentativas, maluco!')
                        break
                    else:
                        for continente in DADOS:
                            for country in DADOS[continente]:
                                if country == pais_rand:
                                    area_final = DADOS[continente][country]['area']
                                    dic_dicas_opcoes['area']=area_final
                    del dic_dicas['dica3']
                    tentaviva_inicial-=6
                    if tentaviva_inicial>10:
                        print(f'Você tem \033[36m{tentaviva_inicial}\033[m tentativa(s)')
                    if 5<tentaviva_inicial<=10:
                        print(f'Você tem \033[33m{tentaviva_inicial}\033[m tentativa(s)')
                    if tentaviva_inicial<=5:
                        print(f'Você tem \033[31m{tentaviva_inicial}\033[m tentativa(s)')
                    break
                if escolhe_dica=='4':
                    numero_das_dicas.remove('|4')
                    numero_das_dicas_str=''.join(numero_das_dicas)
                    if tentaviva_inicial<5:
                        del dic_dicas['dica4']
                        print(f'Tá com alzheimer?? Você só tem \033[31m{tentaviva_inicial}\033[m tentativas, maluco!')
                        break
                    else:
                        for continente in DADOS:
                            for country in DADOS[continente]:
                                if country == pais_rand:
                                    pop = DADOS[continente][country]['populacao']
                                    dic_dicas_opcoes['população'] = pop
                    del dic_dicas['dica4']
                    tentaviva_inicial-=5
                    if tentaviva_inicial>10:
                        print(f'Você tem \033[36m{tentaviva_inicial}\033[m tentativa(s)')
                    if 5<tentaviva_inicial<=10:
                        print(f'Você tem \033[33m{tentaviva_inicial}\033[m tentativa(s)')
                    if tentaviva_inicial<=5:
                        print(f'Você tem \033[31m{tentaviva_inicial}\033[m tentativa(s)')
                    break
                if escolhe_dica=='5':
                    numero_das_dicas.remove('|5')
                    numero_das_dicas_str=''.join(numero_das_dicas)
                    if tentaviva_inicial<7:
                        del dic_dicas['dica5']
                        print(f'Tá com alzheimer?? Você só tem \033[31m{tentaviva_inicial}\033[m tentativas, maluco!')
                        break
                    else:
                        for continente in DADOS:
                            for country in DADOS[continente]:
                                if country == pais_rand:
                                    cont = continente
                                    dic_dicas_opcoes['continente'] = cont
                    del dic_dicas['dica5']
                    tentaviva_inicial-=7
                    if tentaviva_inicial>10:
                        print(f'Você tem \033[36m{tentaviva_inicial}\033[m tentativa(s)')
                    if 5<tentaviva_inicial<=10:
                        print(f'Você tem \033[33m{tentaviva_inicial}\033[m tentativa(s)')
                    if tentaviva_inicial<=5:
                        print(f'Você tem \033[31m{tentaviva_inicial}\033[m tentativa(s)')
                    break
                if escolhe_dica=='0':
                    break
                else:
                    print('Digite uma dica válida')

        #Printando as dicas
        if palpite!='inventario':
            print('Dicas:')
            for tema in dic_dicas_opcoes:
                if dic_dicas_opcoes[tema] == area_final:
                    print(f'- Área: {area_final} km²')
                if dic_dicas_opcoes[tema] == pop:
                    print(f'- População: {pop} habitantes')
                if dic_dicas_opcoes[tema] == cont:
                    print(f'- Continente: {cont}')
                if tema == 'letras':
                    print(f'- Letras da capital: {letras_str}')
                if tema == 'cores':
                    print(f'- Cores da bandeira: {cores_ditas_str}')
            print('')

        #Adiconando o inventário...

        if palpite=='inventario':
            print('='*50)
            print('Este é seu invetário... Que não serve para nada =)')
            print('')
            print('Distâncias:')
            for catalogo in lista_palpites:
                if 0<catalogo[1]<1000:
                    print(f'\033[32m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                elif 1000<=catalogo[1]<2000:
                    print(f'\033[33m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                elif 2000<=catalogo[1]<5000:
                    print(f'\033[34m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                elif 5000<=catalogo[1]<10000:
                    print(f'\033[35m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
                elif catalogo[1]>=10000:
                    print(f'\033[31m{catalogo[0]} está a {catalogo[1]:.3f} km da resposta\033[m')
            print('')
            print('Dicas:')
            for tema in dic_dicas_opcoes:
                if dic_dicas_opcoes[tema] == area_final:
                    print(f'- Área: {area_final} km²')
                if dic_dicas_opcoes[tema] == pop:
                    print(f'- População: {pop} habitantes')
                if dic_dicas_opcoes[tema] == cont:
                    print(f'- Continente: {cont}')
                if tema == 'letras':
                    print(f'- Letras da capital: {letras_str}')
                if tema == 'cores':
                    print(f'- Cores da bandeira: {cores_ditas_str}')
            print('='*50)
            print('')

        #Final do jogo

        if palpite == pais_rand:
            print('Acertou, danadinho!')
            print(f'Você acertou o país com \033[32m{20-tentaviva_inicial}\033[m tentativas')
            break 
        elif palpite=='desisto':
            esc_final=str(input('Vai arregar é???[s/n]:')).lower()
            if esc_final=='s':
                print('')
                print(f'Você é péssimo em Geografia!!! O país era: \033[32m{pais_rand}\033[m')
                break
        elif tentaviva_inicial<=0:
            print('')
            print(f'Meu amigo... tu só pode ter passado no conselho! \033[31mGAME OVER!!!\033[m O país era: \033[32m{pais_rand}\033[m')
            break 

    print('')        
    repete = input('Quer jogar de novo? Ou não consegue???[s/n]:').lower()
print('')
print('Obrigado por jogar!!!')
print('')
print('Até a próxima!!!')
print('')
print('Esse jogo foi criado pelo \033[31mPulga\033[m e pelo \033[34mRafoso\033[m')
