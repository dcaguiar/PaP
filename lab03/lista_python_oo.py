# lista_python_oo.py
# -----------------------------------------------------------
# Lista de Exercícios de Python - Paradigma Orientado a Objetos
# Cada questão é implementada abaixo como se fosse um arquivo separado.
# -----------------------------------------------------------

import math
from abc import ABC, abstractmethod

# ========================
# Q1 - Classe Ponto2D
# ========================
class Ponto2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distancia(self, outro: 'Ponto2D') -> float:
        return math.sqrt((self.x - outro.x)**2 + (self.y - outro.y)**2)


# ========================
# Q2 - Classe Ponto3D (herda Ponto2D)
# ========================
class Ponto3D(Ponto2D):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z

    def distancia(self, outro: 'Ponto3D') -> float:
        return math.sqrt((self.x - outro.x)**2 + (self.y - outro.y)**2 + (self.z - outro.z)**2)


# ========================
# Q3 - Produto e Pedido
# ========================
class Produto(ABC):
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __repr__(self):
        return f"{self.nome} - R${self.preco:.2f} ({self.estoque} em estoque)"

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int):
        if quantidade > produto.estoque:
            raise ValueError("Estoque insuficiente")
        self.produto = produto
        self.quantidade = quantidade
        produto.estoque -= quantidade

    def subtotal(self):
        return self.quantidade * self.produto.preco

class Pedido:
    def __init__(self):
        self.itens = []0s

    def adicionar_item(self, item: ItemPedido):
        self.itens.append(item)

    def total(self):
        return sum(i.subtotal() for i in self.itens)


# ========================
# Q4 - Agenda e Contato
# ========================
class Contato:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato: Contato):
        self.contatos.append(contato)

    def buscar(self, nome: str):
        return [c for c in self.contatos if nome.lower() in c.nome.lower()]


# ========================
# Q5 - Controle de empréstimo de livros
# ========================
class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.disponivel = True

class Emprestimo:
    def __init__(self, pessoa: Pessoa, livro: Livro):
        if not livro.disponivel:
            raise ValueError("Livro indisponível")
        self.pessoa = pessoa
        self.livro = livro
        livro.disponivel = False

    def devolver(self):
        self.livro.disponivel = True


# ========================
# Q6 - Figuras geométricas
# ========================
class Figura(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimetro(self): pass

class Quadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Retangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def perimetro(self):
        return self.a + self.b + self.c

class Circulo(Figura):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2

    def perimetro(self):
        return 2 * math.pi * self.r


# ========================
# Q7 - Conta Bancária
# ========================
class Conta:
    def __init__(self, numero: str, saldo=0.0):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor


# ========================
# Q8 - Sistema Acadêmico
# ========================
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.matriculas = []

    def calcular_cra(self):
        if not self.matriculas:
            return 0
        soma = sum(m.nota for m in self.matriculas)
        return soma / len(self.matriculas)

class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

class Matricula:
    def __init__(self, aluno: Aluno, disciplina: Disciplina, nota: float):
        self.aluno = aluno
        self.disciplina = disciplina
        self.nota = nota
        aluno.matriculas.append(self)


# ========================
# Q9 e Q10 - Lâmpadas
# ========================
class Lampada:
    estados = ["apagada", "meia-luz", "acesa"]

    def __init__(self):
        self.estado = 0

    def troca_de_estado(self):
        self.estado = (self.estado + 1) % len(self.estados)

    def __repr__(self):
        return self.estados[self.estado]

class Lampada4(Lampada):
    estados = ["apagada", "meia-luz", "acesa", "queimada"]


# ========================
# Q11 - Lâmpada com ajuste contínuo
# ========================
class LampadaAjustavel:
    def __init__(self):
        self.luminosidade = 0.0  # 0% a 100%

    def ajustar(self, valor):
        if not (0 <= valor <= 100):
            raise ValueError("Valor fora do intervalo [0,100]")
        self.luminosidade = valor


# ========================
# Q12 - Classe Matriz
# ========================
class Matriz:
    def __init__(self, dados):
        self.dados = dados

    def shape(self):
        return len(self.dados), len(self.dados[0])

    def soma(self, outra: 'Matriz'):
        return Matriz([[self.dados[i][j] + outra.dados[i][j] for j in range(len(self.dados[0]))] for i in range(len(self.dados))])

    def subtrai(self, outra: 'Matriz'):
        return Matriz([[self.dados[i][j] - outra.dados[i][j] for j in range(len(self.dados[0]))] for i in range(len(self.dados))])

    def multiplica_elemento(self, outra: 'Matriz'):
        return Matriz([[self.dados[i][j] * outra.dados[i][j] for j in range(len(self.dados[0]))] for i in range(len(self.dados))])

    def divide_elemento(self, outra: 'Matriz'):
        return Matriz([[self.dados[i][j] / outra.dados[i][j] for j in range(len(self.dados[0]))] for i in range(len(self.dados))])

    def multiplica(self, outra: 'Matriz'):
        lin, col = len(self.dados), len(outra.dados[0])
        return Matriz([[sum(self.dados[i][k] * outra.dados[k][j] for k in range(len(outra.dados))) for j in range(col)] for i in range(lin)])


# ========================
# Q13 - Quadrado Mágico
# ========================
class QuadradoMagico:
    def __init__(self, matriz: Matriz):
        self.matriz = matriz
        if not self._eh_quadrado_magico():
            raise ValueError("A matriz não é um quadrado mágico.")

    def _eh_quadrado_magico(self):
        m = self.matriz.dados
        n = len(m)
        soma = sum(m[0])
        for i in range(n):
            if sum(m[i]) != soma or sum(m[j][i] for j in range(n)) != soma:
                return False
        if sum(m[i][i] for i in range(n)) != soma or sum(m[i][n-i-1] for i in range(n)) != soma:
            return False
        elementos = [x for linha in m for x in linha]
        return len(set(elementos)) == n*n


# ========================
# Q14 - Solução Sudoku
# ========================
class SolucaoSudoku:
    def __init__(self, matriz: Matriz):
        self.matriz = matriz
        if not self._valida():
            raise ValueError("Solução inválida de Sudoku.")

    def _valida(self):
        m = self.matriz.dados
        for i in range(9):
            if len(set(m[i])) != 9 or len(set(m[j][i] for j in range(9))) != 9:
                return False
        for bi in range(0, 9, 3):
            for bj in range(0, 9, 3):
                bloco = [m[i][j] for i in range(bi, bi+3) for j in range(bj, bj+3)]
                if len(set(bloco)) != 9:
                    return False
        return True


# ========================
# Q15 - Algoritmo de Ordenação
# ========================
class Sorter:
    @staticmethod
    def bubble_sort(lst):
        n = len(lst)
        arr = lst.copy()
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


# ========================
# Q16 - Time de Futebol e Jogador
# ========================
class Jogador:
    def __init__(self, nome, numero, posicao):
        self.nome = nome
        self.numero = numero
        self.posicao = posicao  # goleiro, defensor, meio, atacante

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.titulares = []
        self.reservas = []

    def adicionar_jogador(self, jogador: Jogador, titular=True):
        if any(j.numero == jogador.numero for j in self.titulares + self.reservas):
            raise ValueError("Número de jogador repetido.")
        if titular and len(self.titulares) < 11:
            self.titulares.append(jogador)
        elif not titular and len(self.reservas) < 12:
            self.reservas.append(jogador)
        else:
            raise ValueError("Limite atingido.")

    def formacao(self):
        defensores = len([j for j in self.titulares if j.posicao == "defensor"])
        meias = len([j for j in self.titulares if j.posicao == "meio"])
        atacantes = len([j for j in self.titulares if j.posicao == "atacante"])
        return f"{defensores}-{meias}-{atacantes}"


# ========================
# Q17 - Árvore Genealógica
# ========================
class PessoaArvore:
    def __init__(self, nome, pai=None, mae=None):
        self.nome = nome
        self.pai = pai
        self.mae = mae


# ========================
# Q18 - Integração Numérica (Regra do Trapézio)
# ========================
class IntegradorTrapezio:
    def __init__(self, func):
        self.func = func

    def calcular(self, a, b, n):
        h = (b - a) / n
        soma = 0.5 * (self.func(a) + self.func(b))
        for i in range(1, n):
            soma += self.func(a + i * h)
        return soma * h


# ========================
# Q19 - Criptografia ROT13
# ========================
class Criptografia:
    @staticmethod
    def codificaRot13(texto: str) -> str:
        resultado = []
        for ch in texto:
            if 'a' <= ch <= 'z':
                resultado.append(chr((ord(ch) - 97 + 13) % 26 + 97))
            elif 'A' <= ch <= 'Z':
                resultado.append(chr((ord(ch) - 65 + 13) % 26 + 65))
            else:
                resultado.append(ch)
        return ''.join(resultado)

    @staticmethod
    def decodificaRot13(texto: str) -> str:
        return Criptografia.codificaRot13(texto)


# ========================
# Q20 - Autômato Finito (reconhece (a|b)*abb)
# ========================
class AutomatoABB:
    def __init__(self):
        self.estado = 0

    def transicao(self, simbolo: str):
        if self.estado == 0:
            if simbolo == 'a': self.estado = 1
            elif simbolo == 'b': self.estado = 0
        elif self.estado == 1:
            if simbolo == 'a': self.estado = 1
            elif simbolo == 'b': self.estado = 2
        elif self.estado == 2:
            if simbolo == 'a': self.estado = 1
            elif simbolo == 'b': self.estado = 3
        elif self.estado == 3:
            if simbolo == 'a': self.estado = 1
            elif simbolo == 'b': self.estado = 0

    def reconhecer(self, cadeia: str) -> bool:
        self.estado = 0
        for c in cadeia:
            if c not in ('a', 'b'):
                return False
            self.transicao(c)
        return self.estado == 3
