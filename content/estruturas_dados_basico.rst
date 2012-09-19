Estruturas de Dados - Básico
============================

:date: 2012-09-09 13:00
:tags: python
:category: Videos
:author: Felipe
:status: draft
:short_description: Estruturas de dados - Básico

Pra onde vamos?
---------------

Se já sabemos manipular, mesmo que de forma simples, números, strings e sabemos
como executar programas Python pela linha de comando, já podemos aprender
coisas que serão muito mais comuns na prática.

Normalmente, os cursos seguem uma linha onde o próximo passo seria continuar
com a parte de fluxo de controle (if, else), loops e depois pra funções.

Aqui, nós vamos aprender um pouco sobre as estururas de dados embutidas
na linguagem Python:

* Listas (list)
* Dicionários (dict)
* Tuplas (tuple)

Uma das chaves pra produtividade de Python e outras linguagens é o suporte
'builtin' (embutido) dessas estruturas de dados. Não é necessário importar
nada, nem declarar Classe alguma pra usa-las.

Listas
``````

Listas são estruturas de dados com tamanho flexível, que em geral, usamos 
representar coleções de objetos. Normalmente queremos acessar os elementos 
por índice ou executar um loop para acessar cada elemento de uma lista 
para realizar uma tarefa.

Em Python, Listas são mutáveis, ou seja, podemos mudar os valores dos
elementos, adicionar ou remover.

A forma de acessar elementos de uma lista, pelo seu índice é usando a 
notação ``[]`` sempre lembrando que oprimeiro índice de uma lista em
Python é 0.

Como sempre, o primero exemplo é um código.

.. code-block:: python

    lista = []
    outra_lista = ['a', 'b', 'c']
    assert 'b' == outra_lista[1]

Essa é a construção mais comum de uma lista. 
Em Python as listas são representadas por colchetes ``[]``
e podem crescer através de operações como ``append()``.

.. code-block:: python

    lista = [1]
    lista.append(2)
    lista == [1, 2]

Uma lista também pode ter encaixada em outra lista.

.. code-block:: python

    lista = [1]
    lista.extend([2, 3])
    lista == [1, 2, 3]

E pra fechar o básico de listas, vamos ver mais algumas
operações e as outras ficam pra aula só de listas.

.. code-block:: python

    # inserir em uma posição
    lista = [1, 2, 3]
    lista.insert(1, 4)
    assert lista == [1, 4, 2, 3]

    # retirar um elemento
    lista = [1, 2, 3]
    lista.remove(2)
    lista == [1, 3]

    # pegar o último elemento, removendo-o da lista
    lista = [1, 2, 3, 4, 5]
    lista.pop() # remove do final e retorna 5
    lista == [1, 2, 3, 4]

    # Se você especificar o índice do elemento, 
    # faz o mesmo com ele ao invés do último
    lista.pop(0) #remove do inicio e retorna 1
    lista == [2, 3, 4]

Listas por padrão, quando percorridas, a ordem de retorno
é a mesma de inserção a não ser que seja ela ordenada ou invertida.

Listas também permitem a troca do valor de uma posição

.. code-block:: python

    lista = [1, 2]
    lista[0] = 3
    lista == [3, 2]


Tuplas
``````

O comportamento:

Tuplas são como listas imutáveis, que tem o tamanho fixo e não podem crescer.

A semântica:

É muito comum pensar em listas apenas como isso, mas em muitos casos, elas
são usadas com uma semântica associada as posições.

.. code-block:: python

    tupla = (1,2)

    # (nome, identidade, email)
    dados_pessoa = ('Nome da Pessoa', 23435, 'email@email.com')

    # Tuplas são imutáveis. Por isso não é possível alterar os elementos
    dados_pessoa[0] = 'Fulano'
    TypeError: 'tuple' object does not support item assignment


A função ``datetime.now()`` retorna uma tupla onde cada posição
contem um dos valores que compões o obejeto ``datetime``

.. code-block:: python

    from datetime import datetime
    datetime.now()
    
    datetime.datetime(2012, 9, 1, 18, 5, 25, 746250)

Dicionários
```````````

Dicionários (dict) são estruturas de acesso por uma chave e não por um índice.
Chave pode ser qualquer objeto imutável, inclusive uma tupla. Números e strings
são imutáveis e são muito comumente usados como chaves de dicionários.

Dada uma chave, podemos inserir, obter e remover o valor associada a ela.

Dicionários podem ser criados usando as chaves ``{}`` ou com a função ``dict()``

Exemplos:

.. code-block:: python

    dicionario = {'chave': 'valor'}

    dicionario[1] = 1
    dicionario['a'] = 'b'

    dicionario == {'chave': 'valor', 'a': 'b', 1: 1}

Uma outra forma de criar dicionários, com a função ``dict()``:

.. code-block:: python

    dicionario = dict(nome='Pessoa', idade=25)
    dicionario == {'idade': 25, 'nome': 'Pessoa'}

Dicionários têm ainda outras facilidades. Seguem alguns exemplos.

Testar se uma chave existe no dicionário:

.. code-block:: python

    dicionario = dict(nome='Pessoa', idade=25)
    assert 'nome' in dicionario

Remover um par chave-valor de um dicionário:

.. code-block:: python

    dicionario = dict(nome='Pessoa', idade=25)
    del dicionario['nome']

    dicionario == {'idade': 25}

Se precisarmos percorrer os items (chave-valor), as chaves ou os
valores de um dicionário, podemos fazer como exibido abaixo:

.. code-block:: python

    >>> dicionario.items()
    [('idade', 25)]
    >>> dicionario.keys()
    ['idade']
    >>> dicionario.values()
    [25]


Documentação Oficial sobre as Estruturas de Dados
`````````````````````````````````````````````````

A documentação oficial do Python é excelente: http://docs.python.org/tutorial/datastructures.html

