Estruturas de Dados - Básico - Fundamentos - Parte 1
====================================================

:date: 2012-12-16 14:30
:tags: python,estruturas de dados
:category: Videos
:author: Felipe Cruz
:short_description: Aprenda sobre a parte conceitual das estruturas de dados onde
                    encontramos os protocolos abstratos de Sequências e Mapas.


.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/-XnBF5DCZWQ?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">
 

Sequências e Mapas
------------------

São conjuntos de comportamentos que devem ser obedecidos
integralmente pelos objetos que o implementam.


Sequências
``````````

.. code-block:: python

    lista[indice]

Sequências - Exemplos
``````````````````````

O índice deve ser um número inteiro, começando de 0
e indo até o tamanho da sequência menos 1.

.. code-block:: python

    lista = ["a", "b", "c"]
    assert lista[0] == "a" 
    assert lista.index("c") == 2

Mapas
`````

A chave pode ser qualquer objeto *imutável*.
Chaves do tipo Strings são muito comuns. Pode ser uma tupla também.

Mapas - Exemplos
````````````````

.. code-block:: python

    m = {'key': 'value'}
    assert m['key'] == 'value'
    'key' in mapa
    del mapa['key']


Documentação Oficial
--------------------

* http://docs.python.org/3.3/c-api/abstract.html
* http://docs.python.org/3.3/library/collections.abc.html
