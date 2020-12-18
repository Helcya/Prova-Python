#   Crie um programa que leia o nome de varios jogadores e quantas partidas eles jogaram.
#   Depois vai ler a quantidade de gols feitos em cada partida e o total de gols.
#   No final, tudo isso será guardado em um dicionário e apresentado no final. incluindo
#   um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Crie um programa que leia o nome de n jogadores, 
# o time que joga, 
# a quantidade de partidas que eles jogaram, 
# a quantidade de gols feitos em cada partida e 
# o total de gols. 
# Essas informações serão armazenadas em um dicionário. 
# O programa apresentará no final todas as informações dos jogadores e 
# um ranking com os top 3 com mais gols.

quantidade_gols = list()
jogador = dict()
time = list()

while True:
    jogador['Nome'] = str(input('Nome do Jogador:')).strip()
    partidas = int(input(f'Digite a quantidade de partidas jogadas por {jogador["Nome"]}:'))

    if partidas > 0:
        for i in range(0, partidas):
            quantidade_gols.append(int(input(f'Quantos gols na {i+1}º partida?')))
        jogador['Gols'] = quantidade_gols[:]
        jogador['Total'] = sum(quantidade_gols)
    time.append(jogador.copy())

    while True:
        escolha = str(input('Deseja Inserir outro Jogador? [S/N]')).upper().strip()[0]
        if escolha in 'SN':
            jogador.clear()
            quantidade_gols.clear()
            break
        print('Opção inválida.')
    if escolha == 'Não':
        print(' ')
        print(f'{"Cod":<5}{"NOME":<10}{"Total":<10}{"Gols":<10}')
        for i, j in enumerate(time):
            print(f'{i:<5}{j["Nome"]:<10}{j["Total"]:<10}{j["Gols"]}')
        indices = sorted(range(len(quantidade_gols)), key=lambda i: quantidade_gols[i], reverse=True)
        print('TOP 3:')
        print(indices[0],indices[1],indices[2])
        print(' ')
