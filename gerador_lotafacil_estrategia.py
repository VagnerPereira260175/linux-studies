import random


contador = 0
while contador < 5: # gera a quantidade de lista selicionadas.
    # Listas iniciais
    lista_numero_inicial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    lista_numero_final = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    # Selecionando números aleatórios
    selecionados_inicial = random.sample(lista_numero_inicial, 6)
    selecionados_final = random.sample(lista_numero_final, 9)

    # Criando a lista resultado
    resultado = selecionados_inicial + selecionados_final
    resultado.sort() # coloca a lista em ordem
    contador += 1