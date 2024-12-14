times = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'RB Bragantino', 'Fortaleza', 'São Paulo',
         'Cruzeiro', 'Internacional', 'Atlhetico-PR', 'Atléico-MG', 'Santos', 'Cuiabá', 'Corinthians', 'Bahia', 'Goiás',
         'Coritiba', 'Vasco', 'América-MG')
primeiros = times[0:5]
ultimos = times[16:]
ordem = sorted(times)
cor = times.index('Corinthians') + 1
print(15*'-=')
print(f'Lista de times do Brasileirão: {times}')
print(15*'-=')
print(f'Os 5 primeiros são {primeiros}')
print(15*'-=')
print(f"Os 4 últimos são {ultimos}")
print(15*'-=')
print(f'Times em ordem alfabética: {ordem}')
print(15*'-=')
print(f'O Corinthians está na {cor}ª posição')