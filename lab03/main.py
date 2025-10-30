# 1. Escreva uma função ‘head’ que retorna o primeiro elemento de uma lista
def head(list):
    if list == []: return []
    return list[0]
# 2. Escreva uma função ‘tail’ que retorna toda a lista, exceto o primeiro elemento
def tail(list):
    if list == []: return []
    return list[1:]
# 3. Escreva uma função ‘init’ que retorna toda a lista, exceto o último elemento
def init(list):
    if list == []: return []
    return list[:-1]
# 4. Escreva uma função ‘last’ que retorna o último elemento de uma lista
def last(list):
    if list == []: return []
    return list[-1]
# 5. A sequência de Fibonacci é dada pela seguinte série: 0 1 1 2 3 5 8 13 ... 
# Em termos matemáticos, a sequência de Fibonacci pode ser definida através da seguinte relação de recorrência:
# 𝒇(𝒏) = {𝟎, 𝒏=𝟎
#        1 = 𝒏=1
#        f(n-1) + f(n-2)
def fib(n):
    if n == 0: return 0
    return fib() + fib()

#
#
#
#
#
#
#
#
#
#
#