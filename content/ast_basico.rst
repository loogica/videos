AST Básico
==========

:date: 2013-02-15 16:00
:tags: python,basico,ast
:category: Videos
:author: Felipe Cruz
:short_description: Representação de código em árvore. Podemos converter código em AST e converter uma AST
                    criada programaticamente em código executavel. Podemos obter informações de um código e
                    até modifica-lo. Aprender ASTs é uma forma de se tornar um melhor programador.


.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/l2B8jLmVYqw?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">


Motivação para aprender
-----------------------

* Ter mais consciência do código.
* Obter informações do código.
* Modificar/Gerar código.

Conceito - Statements 
---------------------

Um Statement é uma instrução a ser executada.

.. code-block:: python

    name = "loogica"

    def my_func():
        pass

Conceito - Expressions
----------------------

Uma Expression retorna um valor.

.. code-block:: python

    a + b
    (1, 2, 3)
    nome is None

Statements + Expressions
------------------------

.. code-block:: python

    soma_simples = 1 + b

    if nome is None:
        pass


Dissecando - Statements
-----------------------

.. code-block:: python

    name = "loogica"

* Atribuição           
* Do valor "loogica"
* Na variável "name"

Dissecando - Statements
-----------------------

.. code-block:: python

    name = "loogica"

    Assign(targets=[Name(id='name',
                         ctx=Store())],
           value=Str(s='teste'))

Experimentando
--------------

.. code-block:: python

    import ast
    source = "name = 'loogica'"
    ast.dump(ast.parse(source))

Dissecando Expressions
----------------------

.. code-block:: python

    a + b

* Operação binária de Soma
* Termo a
* Termo b

Dissecando Expressions
----------------------

.. code-block:: python

    a + b

    Expr(value=BinOp(left=Name(id='a', ctx=Load()),
                     op=Add(),
                     right=Name(id='b', ctx=Load())))

Experimentando - pt2
--------------------

.. code-block:: python

    import ast
    source = "a + b"
    ast.dump(ast.parse(source))


Mais Leitura
------------

* Doc. Oficial: http://docs.python.org/3.3/library/ast.html 
* http://eli.thegreenplace.net/2009/02/16/abstract-vs-concrete-syntax-trees/
