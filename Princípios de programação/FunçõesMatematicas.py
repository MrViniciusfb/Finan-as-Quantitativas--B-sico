# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:12:37 2021

@author: Bessa-PC
"""

x = 5
y = 10
b = 3

#As funções padrões do python são:
    # Soma: x + y
print('Soma: x + y = ', x+y)
    # Subtração: x -y
print('Subtração: x - y = ', x-y) 
    # Multiplicação: x*y
print('Multiplicação: x * y = ', x*y)
    # Divisão: x/y
print('Divisão: x/y = ', x/y)
    # Potenciação: x**y
print('Potenciação: x**y = ', x**y)
    # Resto: x % y
print('Resto: x % y = ', x%y)

print("="*50 + "\nUtilizando a biblioteca math\n")
#Caso se queira funções mais complexas deve-se usar a biblioteca math
import math
#Funções logarítimicas e exponenciais
    #math.exp(x): retorna euler elevado a x
print('\tPotencia com Euler: e**x = ', math.exp(x)) 
   
    #math.log(x): retorna o logaritmo de x na base euler
print('\tLogaritmo de x na base e: log(x) = ', math.log(x))    
    
    #math.log2(x): retorna o logaritmo de x na base 2
print('\tLogaritmo de x na base 2: log2(x) = ', math.log2(x))
     
    #math.log10(x): retorna o logaritmo de x na base 10
print('\tLogaritmo de x na base 10: log10(x) = ', math.log10(x))   
  
    #math.log(x, b): retorna o logaritmo de x na base b, apenas se b for
        #diferente de 2 ou 10
print('\tLogaritmo de x na base b: logb(x) = ', math.log(x, b))  

    #math.pow(x, y): retorna x elevado a y
print('\tPotenciação: x**y = ', math.pow(x, y))
    
    #math.sqrt(x): retorna a raiz quadrada de x
print('\tRaiz quadrada: sqrt(x) = ', math.sqrt(x))
 
#Funções trigonometricas
print("\nEstas funções trionometricas são dadas em radianos")
    #math.cos(x): retorna o cosseno de x:
print('\tO cosseno de x: cos(x) = ', math.cos(x))

    #math.acos(x): retorna o arco cosseno de x:
print('\tO arco cosseno de x: acos(x/y) = ', math.acos(x/y))

    #math.sin(x): retorna o seno de x:
print('\tO seno de x: sin(x) = ', math.sin(x))

    #math.asin(x): retorna o arco seno de x:
print('\tO arco seno de x: asin(x/y) = ', math.asin(x/y))

    #math.tan(x): retorna a tangente de x:
print('\tA tangente de x: tan(x) = ', math.tan(x))

    #math.atan(x): retorna o arco tangente de x:
print('\tA arco tangente de x: atan(x) = ', math.atan(x))

    #math.degrees(x): converte o ângulo x de radianos para graus
print('\tO angulo em graus vale: gras(x) = ', math.degrees(x))

    #math.radians(x): converte o ângulo x de graus para radianos
print('\tO angulo em radianos vale: rad(x) = ', math.radians(x))

    #math.hypot(x,y): retorna a norma do vetor dado por x e y na origem
print('\tO vetor norma centrado na origem x,y: hypot(x,y) = ', math.hypot(x,y))

#Contantes matemáticas
print('='*50 + "\nConstantes:")

    #math.e: retorna o número de Euler
print('\tO numero de Euler: e = ', math.e)

    #math.pi: Retorna o valor de pi
print('\tO valor de pi: pi = ', math.pi)