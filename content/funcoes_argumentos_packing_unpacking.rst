Funções e Argumentos - Packing & Unpacking
==========================================

:date: 2013-03-15 12:00
:tags: python,basico,funcoes,argumentos,packing,unpacking
:category: Videos
:author: Felipe Cruz
:short_description: Python tem o recurso de packing e unpacking para facilitar a declaração e chamada
                    de funções que se utiliza das próprias estruturas de dados básicas como listas/tuplas
                    e dicionário para implementa-las.

.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/8NfkgtytnLM?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">


Argumentos por posição
----------------------

.. code-block:: python

    def funcao(arg1):
        print(arg1)

    funcao("loogica")
    >>> "loogica"


Argumentos por nome
-------------------


.. code-block:: python

    def funcao(meu_arg="padrao"):
        print(meu_arg)

    funcao()
    >>> "padrao"
    

Argumentos por nome
-------------------


.. code-block:: python

    def funcao(meu_arg="padrao"):
        print(meu_arg)
    
    funcao(meu_arg="loogica")
    >>> "loogica"

Argumentos por nome
-------------------


.. code-block:: python

    def funcao(meu_arg="padrao"):
        print(meu_arg)

    funcao("loogica")
    >>> "loogica"

Packing
-------

Motivação: Praticidade


.. code-block:: python

    from datetime import date
    # date signature (year,month,day)
    d = (2013, 3, 15)
    date(d[0], d[1], d[2])
    >>> datetime.date(2013, 3, 15)

Packing
-------

.. class:: center, huge

    CHATO!

Packing
-------

.. class:: center, huge

    MAS....

Packing
-------

.. class:: center, huge

    Python é LEGAL! :)

Packing
-------

Se eu já tenho os argumentos numa lista ou tupla
que por algum motivo já foi calculado..


.. code-block:: python

    from datetime import date
    # date signature (year,month,day)
    d = (2013, 3, 15)
    date(*d)
    >>> datetime.date(2013, 3, 15)


Packing
-------

* Se a lista/tupla tiver mais elementos que o número de argumentos: TypeError


Packing
-------


.. code-block:: python

    class Usuario(object):
        def __init__(self, atv=True,
                           adm=False):
            self.atv = atv
            self.adm = adm

Packing
-------

Normal


.. code-block:: python

    usuario = Usuario(atv=False,
                      adm=True)


Packing
-------

Verboso


.. code-block:: python

    config = {"atv": False,
              "adm": True}

    Usuario(atv=config.get('atv'),
            adm=config.get('adm'))


Packing
-------

Melhor


.. code-block:: python

    config = {"atv": False,
              "adm": True}

    usuario = Usuario(**config)

Packing
-------

* Par chave->valor dos dicts tem que casar com
  assinatura do método.


Unpacking
---------


.. code-block:: python

    def funcao(*args):
        arg1 = args[0]
        arg2 = args[1]
        resto = args[2:]
        print(arg1)
        print(arg2)
        print(resto)

Unpacking
---------


.. code-block:: python

    funcao(*[1,2])
    1
    2
    ()

Unpacking
---------


.. code-block:: python

    funcao(*[1,2,3])
    1
    2
    (3,)

Unpacking
---------


.. code-block:: python

    funcao(*[1,2,3,4])
    1
    2
    (3, 4)


Unpacking
---------


.. code-block:: python

    def funcao(**kwargs):
        print(kwargs)

Unpacking
---------


.. code-block:: python

    funcao(**dict(nome="teste"))
    {'nome': 'teste'}


Unpacking
---------


.. code-block:: python

    funcao(**dict())
    {}

Mais Leitura
------------

* Doc. Oficial: http://docs.python.org/2/tutorial/controlflow.html#arbitrary-argument-lists
