def head(x):
    return x[0]

def tail(x):
    return x[1:]

def init(x):
    return x[:-1]

def last(x):
    return x[-1]

def fib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
# def aux(l1,l2,i):


# def concatlistas(l1,l2):

def tamanhoLista(l1): # Q13
    if (l1 == []):
        return 0
    else:
        return 1 + tamanhoLista(tail(l1))
    

def concatlistas(l1,l2):
    if (l1 == [] and l2 == []):
        return []
    elif (l1 == []):
        return concatlistas(l2,[])
    else:
        return [head(l1)] + concatlistas(tail(l1),l2)

print(concatlistas([1,2],[3,4]))

def pertenceLista(x,lista):
    if (tamanhoLista(lista) == 0):
        return False
    elif (x == head(lista)):
        return True
    else:
        return pertenceLista(x,tail(lista))
    
print(pertenceLista(1,[4,2,3,1]))

def uniaolistas(l1,l2):
    if (l1 == [] and l2 == []):
        return []
    elif (l1 == []):
        return uniaolistas(l2,[])
    elif pertenceLista(head(l1),tail(l1)) or pertenceLista(head(l1),l2):
        return uniaolistas(tail(l1),l2)
    else:
        return [head(l1)] + uniaolistas(tail(l1),l2)

print(uniaolistas([1,2],[3,4,1]))

# Questão 9) Defina uma função que dada uma lista de inteiros e um número n, 
# retorne o total de
# elementos de valor superior a n.

def maioresQue(n,l1): # Q13
    if (l1 == []):
        return 0
    elif (head(l1) > n):
        return 1 + maioresQue(n,tail(l1))
    else:
        return 0 + maioresQue(n,tail(l1))


print(maioresQue(2,[1,2,3]))

# Questão 10) Defina uma função que dada uma lista de inteiros e um número n, 
# retorne outra lista contendo apenas de elementos de valor superior a n. 
# Use a função feita na Q6.

def listaMaiores(l1,n):
    if (l1 == []):
        return []
    elif (head(l1) > n):
        return concatlistas([head(l1)],listaMaiores(tail(l1),n))
    else:
        return listaMaiores(tail(l1),n)
        
print(listaMaiores([1,2,3,4,5,6,7,8,9,10],2))

# Questão 11a) Escreva uma função que inverte o conteúdo de uma lista. Use apenas as funções da
# Q1 e a da Q6: invertelista (“abcd”) = “dcba”.

def invertelista(lista):
    if (lista == []):
        return []
    else:
        return concatlistas(invertelista(tail(lista)),[head(lista)])

print(invertelista([1,2,3]))


# Questão 12) Escreva uma função que receba uma palavra e gere seu palíndromo.
# Ex.:  geraPalindromo (“abcd”) = “abcddcba”.

def geraPalindromo (lista):
    return concatlistas(init(lista),invertelista(lista))

# print(geraPalindromo(list("abc")));
# Questão 14) Escreva a função ehPrimo para verificar se um 
# número dado é primo

def ehPrimoAuxiliar(a,b):
    if b == 1:
        return True
    elif (a % b == 0):
        return False
    else:
        return ehPrimoAuxiliar(a,b-1)

def ehPrimo(n):
    if n == 1:
        return False
    else: 
        return ehPrimoAuxiliar(n,n-1)
    
# Questão 15) Defina a função strip que dadas duas listas, 
# retira da segunda todos os elementos que
# ocorrem na primeira, em qualquer quantidade.        

def strip(l1,l2):
    if (l2 == []):
        return []
    elif pertenceLista(head(l2),l1):
        return strip(l1,tail(l2))
    else:
        return concatlistas([head(l2)],strip(l1,tail(l2)))
    
print(strip([1,2,3],[1,2,3,4]*3))

# Questão 16) Defina a função consoantList que retorna verdadeiro se somente se
# todas as consoantes da segunda lista, incluindo repetições, ocorrem na primeira lista,
# na mesma ordem. # Exemplos:
# ordSublist ("sdd", "saude") -> False
# ordSublist ("sdd", "saudade") -> True

def consoantListAux(l1,l2):
    if (l1 == []):
        return True
    elif l2 == []:
        return False
    elif pertenceLista(head(l1),[head(l2)]):
        return consoantList(tail(l1),tail(l2))
    else:
        return False
    
def consoantList(l1,l2):
    return consoantListAux(strip(list("aeiou"),l1),strip(list("aeiou"),l2))
    
print(consoantList(list("sdd"),list("saude")))

    
    