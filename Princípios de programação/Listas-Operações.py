# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:34:51 2021

@author: Bessa-PC
"""

#Listas em python são sequencias ordenadas em que os elementos são sempre 
    #associados a um índice os quais sempre iniciam em zeromercado

mercado = ['ações', 'opções', 'futuro', 'dólar', 'ouro', 'criptomoedas']

print("mercado = " + str(mercado))

#Mostrando dados da lista
print('-'*20 + ' Dados da lista ' + '-'*20)

    #Primeiro elemento: nome[0]
print("\nO primeiro elemento: mercado[0] = ", mercado[0])

    #Último elemento: nome[-1]
print("\nO último elemento: mercado[-1] = ", mercado[-1])    

    #Total de elementos: len(nome)
print("\nO total de elementos: len(mercado) = ", len(mercado))

    #Fatiamentos: nome[de:até]
print("\nOs elementos de 0 a 2 são: mercado[0:3] = ", mercado[0:3])   
print("Os elementos de 2 a 4 são: mercado[2:5] = ", mercado[2:5])   

    #Busca em listas: 'x' in nome, retorna true ou false
acao = 'ações' in mercado
print("\n'ações' está em mercado: 'ações' in mercado = ", acao)
acao2 = 'Petrobras' in mercado
print("\n'Petrobras' está em mercado: 'Petrobras' in mercado = ", acao2)

    #Alterando um elemento da lista: nome[i] = 'x'
mercado[2] = 'commodity'
print("\nAlterando o valor do índice 2 para 'commodity'': mercado[2] = ", mercado[2])
    #Alterando vários elementos da lista: nome[de:até] = ['x',...,'z']
mercado[0:2] = ['tesouro', 'títulos']
print("\nAlterando os valores dos índices de 0 a 2 para ['tesouro', 'títulos']: mercado[0:2] = ", mercado[0:2])

print('-'*20 + ' Operações com listas ' + '-'*20)
#Operações com listas
    #nome.append(x): Adiciona o elemento x à lista "nome"
print("\nA operação mercado.append('comprar') resulta em:")
mercado.append('comprar')
mercado.append('dólar')
print('\tmercado = ' + str(mercado))

    #nome.extend(y): Insere a lista y no final da lista "nome"
print("\nA operação mercado.extend(['Petrobras', 'BB', 'Vale']) resulta em:")
mercado.extend(['Petrobras', 'BB', 'Vale'])
print('\tmercado = ' + str(mercado))    

    #nome.sort(key=None,Reverse = False): ORdena em ordeme crescente ou alfabética a lista "nome"
print("\nA operação mercado.sort() resulta em:")
mercado.sort()
print('\tmercado = ' + str(mercado))    

    #nome.sort(key=str.casefold): ORdena em ordeme alfabética a lista "nome" sem distinção de Maiúscula e minúscula
print("\nA operação mercado.sort(key=str.casefold) resulta em:")
mercado.sort(key=str.casefold)
print('\tmercado = ' + str(mercado))        

    #nome.count(x): Conta o número de ocorrências de x na lista "nome"
print("\nA operação mercado.count('dolar') resulta em:")
print('\tdólar = ' + str(mercado.count('dólar')))    

    #nome.insert(pos, x): Insere um elemento x na posição "pos" da lista "nome"
print("\nA operação mercado.insert(2, 'Fundo de Investimentos') resulta em:")
mercado.insert(2, 'Fundo de Investimentos')
print('\tmercado = ' + str(mercado))    

    #nome.reverse(): Ordena inversamente a lista "nome"
print("\nA operação mercado.reverse() resulta em:")
mercado.reverse()
print('\tmercado = ' , mercado)    

    #nome.index(x): Retorna o valor do índice do elemento x da lista "nome"
print("\nA operação mercado.index('Petrobras') resulta em:")
print('\tPosição de "Petrobras" = ' + str(mercado.index('Petrobras') + 1))  
  
    #nome.pop(i): Remove e retorna o valor enconrado na posição "i" da lista "nome"
print('\nA operação obj = mercado.pop(1) resulta em')
obj = mercado.pop(1)
print('\tobj = ', obj)
    #nome.remove(x): Remove um elemento x da lista "nome"
print("\nA operação mercado.remove('ouro') resulta em:")
mercado.remove('ouro')
print('\tmercado = ' + str(mercado))  
  
    #nome.clear(): Remove todos os elementos da lista "nome"
print("\nA operação mercado.clear() resulta em:")
mercado.clear()
print('\tmercado = ' + str(mercado))

print('-'*20 + ' Operações com elementos das listas ' + '-'*20)
#Operações com elementos das listas

ibov = ['PETR4', 'BBAS3', 'USIM5', 'GGBR4', 'VALE3']

print(ibov)

    #ibov[2:4]: do elemento de índice 2 ao índice 3
print("\ndo elemento de índice 2 ao índice 3: ibov[2:4] = ", ibov[2:4])

    #ibov[1:]: do elemento de índice 1 até o último elemento
print("\ndo elemento de índice 1 até o último elemento: ibov[1:] = ", ibov[1:])

    #ibov[:3]: do elemento inicial até o elemento de índice 2(pois 3-1 = 2)
print("\ndo elemento inicial até o elemento de índice 2: ibov[:3] = ", ibov[:3])

    #ibov[0:5:2] do elemento inical ao último saltando de 2 em 2
print("\ndo elemento inical ao último saltando de 2 em 2: ibov[:5:2] = ", ibov[0:5:2])   
 
    #ibov[-3:]: seleciona os 3 últimos elementos da lista
print("\nseleciona os 3 últimos elementos da lista: ibov[-3:] = ", ibov[-3:])

    #ibov[:-3]: seleciona os 2 primeros elementos da lista (pois -(3-1))
print("\nseleciona os 3 últimos elementos da lista: ibov[:-3] = ", ibov[:-3])