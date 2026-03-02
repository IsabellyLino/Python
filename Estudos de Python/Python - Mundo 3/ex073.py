'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Corinthians', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Goiás', 'Vasco', 'São Paulo', 'Internacional', 'Ceará', 'Coritiba', 'Botafogo', 'Athletico-PR', 'Cuiabá', 'Avaí', 'Chapecoense')
print('Os 5 primeiros times são:')
print(times[0:5])
print('Os últimos 4 colocados são:')
print(times[-4:])
print('Times em ordem alfabética:')
print(sorted(times))
print('O time da Chapecoense está na posição:')
print(times.index('Chapecoense') + 1)   
