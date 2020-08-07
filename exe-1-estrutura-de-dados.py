# -*- coding: utf-8 -*-

""" 
Pilhas são estruturas de dados em que só é possível
inserir um novo elemento no final da pilha e
só é possível remover um elemento do final da pilha.

Em Python utilizamos listas como se fossem pilhas.
O último elemento a ser inserido é sempre o primeiro elemento
a ser removido.
https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/pilhas
"""

from collections import deque
pilha = [1, 1, 12, 3, 5]
#print(f'Pilha: {pilha}')

pilha.append(8)
#print(f'Inserindo um elemento: {pilha}')

pilha.pop()
#print(f'Removendo um elemento: {pilha}')

"""
Implementando uma pilha como estrutura encadeada. A pilha possui um topo
e cada elemento faz referência ao elemento anterior.
"""
class Nodo:
    """Esta classe representa um nodo de uma estrutura encadeada."""

    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da fila"""

        # Cria um novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha
        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo
        self.topo = novo_nodo

    def remove(self):
        """Remove o elemento que está no topo da pilha."""

        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

# Cria uma pilha vazia
pilha = Pilha()
#print(f'Pilha vazia" {pilha}')

# Insere elementos na pilha
for i in range(5):
    pilha.insere(i)
    #print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

while pilha.topo != None:
    pilha.remove()
    #print("Removendo elemento que está no topo da pilha: ", pilha)

"""
Filas são estruturas de dados em que só é possível inserir
um novo elemento no final da fila e só é possível remover
um elemento do início. Filas seguem um protocolo em que o 
primeiro a entrar é o primeiro a sair.

Podemos implementar fiilas usando listas e a biblioteca deque.
https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/filas
"""

"""
http://turing.com.br/pydoc/2.7/tutorial/datastructures.html#usando-listas-como-filas
"""

fila = deque(["Eric", "John", "Michael"])
fila.append("Terry")  # Terry Chega
fila.append("Graham")  # Graham chega
fila.popleft()  # O primeiro a chegar parte [Eric]
fila.popleft()  # O segundo a chegar parte [John]
# print(fila) ## O resto da fila, em ordem de chegada

"""
Implementando filas com estruturas encadeadas. 
Inserções ocorrem no final da fila e remoções ocorrem no começo.
São dois ponteiros: um para o começo da fila e outro para o final.
Eses ponteiros permitem inserções e remoções com custo constante.
https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/filas
"""

class Nodo:
    """Esta classe representa um nodo de uma estrutura duplamente encadeada."""

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""

        # Cria um novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_dado)

        # Insere em uma fila vazia
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            # Faz com que o novo nodo seja o último da fila.
            self.ultimo.proximo = novo_nodo

            # Faz com que o último da fila referencie o novo nodo.
            self.ultimo = novo_nodo

    def remove(self):
        """Remove o último elemento da fila"""

        assert self.primeiro != None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo

        if(self.primeiro) == None:
            self.ultimo = None

fila = Fila()
#print("Fila vazia: ", fila)

# Insere elementos na fila
for i in range(5):
    fila.insere(i)
    #print("Insere o valor {0} no final da fila: {1}".format(i, fila))

while fila.primeiro != None:
    fila.remove()
    #print("Removendo elemento que está no começo da fila: ", fila)

"""
O que o statement else faz em um loop (note que o 'else' está identado com o 'for')
"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

"""
O statement else quando usado em um loop trata o retorno false da
condicão estabelecida dentro do for. 
"""