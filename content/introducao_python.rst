Introdução prática
==================

:date: 2012-09-01 18:30
:tags: python 
:category: Videos
:status: draft
:author: Felipe
:short_description: Um primeiro contato com o interpretador Python.

O ideal é ver em 720p HD em fullscreen.

.. raw:: html

    <iframe id="video" width="560" height="315" src="http://www.youtube.com/embed/A3MnTdpe9u8" frameborder="0" allowfullscreen>
    </iframe>

    <script>
        $(document).ready(function() {
            $('#video').fitVids();
        });
    </script>

Conteúdo do video em texto
--------------------------

Esse é um guia textual da introdução prática a linguagem Python.

Primeiros passos
----------------

Modo Interativo:

.. code-block:: sh

    $ python

Pasando Argumentos:

.. code-block:: sh

    $ python meu_programa.py arg1 arg2

Recebendo no programa meu_programa.py:

.. code-block:: python

    import sys
    lista_argumentos = sys.argv
    print(lista_argumentos)

Usando o arquivo criado na etapa anterior:

.. code-block:: sh

    $ python meu_programa.py teste
    ['meu_programa.py', 'teste']
    

Números
-------

Inteiros
~~~~~~~~

Divisão de inteiros retorna inteiro arredondado para baixo.

.. code-block:: pycon

    >>> 1
    1
    >>> 7/2
    3


Pontos Flutuantes
~~~~~~~~~~~~~~~~~

Misturar inteiros e floats converte o inteiro pra float.

.. code-block:: pycon

    >>> 7.0
    7.0
    >>> 7.0/2
    3.5

Complexos
~~~~~~~~~

.. code-block:: pycon

    >>> (1+3j)
    (1+3j)
    >>> (1+3j).imag
    3.0
    >>> (1+3j).real
    1.0

Strings
-------

Formas de criar
~~~~~~~~~~~~~~~

.. code-block:: pycon

    >>> st = "uma string"
    >>> print st
    uma string
    >>> st = 'uma string'
    >>> print st
    uma string
    >>> st = "uma 'string'"
    >>> print st
    uma 'string'
    >>> st = 'uma "string"'
    >>> print st
    uma "string"
    >>> st = """
    ... string formatada
    ...        formatada
    ... """
    >>> print st

    string formatada
           formatada

    >>> 


Operações básicas
~~~~~~~~~~~~~~~~~

.. code-block:: pycon

    >>> st = "hello "      
    >>> st2 = "world"
    >>> print(st + st2)
    hello world
    >>> print((st + st2) * 3)
    hello worldhello worldhello world
    >>> a = "a"
    >>> print a * 10
    aaaaaaaaaa
    >>> 

Acesso aos dados
~~~~~~~~~~~~~~~~

.. code-block:: pycon

    >>> st = "uma string"
    >>> st[0]
    'u'
    >>> st[1]
    'm'
    >>> st[0:2]
    'um'
    >>> st[0:3]
    'uma'
    >>> st[-1]
    'g'
    >>> st[-3:]
    'ing'
    >>> st[:-3]
    'uma str'
    >>> 


Imutabilidade e criação de novas strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

String em Python são imutáveis. Podemos apenas criar strings a partir de outras,
nunca muda-las.

.. code-block:: pycon

    >>> st = "uma string"
    >>> st[2] = " "
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    >>> # uma forma, seria converter a string pra bytearray,
    >>> # mudar a posicao desejada e converter de volta para
    >>> # string
    >>> def troca_letra(palavra, posicao, letra_nova):
    ...     nova_palavra = bytearray(palavra)
    ...     nova_palavra[posicao] = letra_nova
    ...     return str(nova_palavra)
    ...
    >>> print(troca_letra("uma string", 2, " "))
    ... um  string


Unicode
~~~~~~~

Na série 2.x
~~~~~~~~~~~~

* Strings ``str`` e unicodes ``unicode`` são diferentes. 
* Bytes ``bytes`` e strings ``str`` são a mesma coisa.

.. code-block:: pycon

    >>> unicode_st = u"hello\u0020World"
    >>> print(unicode_st)
    hello World
    >>> type(unicode_st)
    <type 'unicode'>
    >>> unicode_st == "hello world"
    False
    >>> type("hello world")
    <type 'str'>
    >>> print(unicode_st.encode('utf-8'))
    hello World
    >>> type(unicode_st.encode('utf-8'))
    <type 'str'>
    >>> bytes == str
    True
    >>> 


Python 3
~~~~~~~~

* Strings e Unicodes são a mesma coisa.
* Quando necessário, converter uma String para array de bytes, usar ``unicode.encode('codec')``.

.. code-block:: pycon

    >>> unicode_str = u"hello\u0020world"
    >>> print(unicode_str)
    hello world
    >>> unicode_str == "hello world"
    True
    >>> type(unicode_str)
    <class 'str'>
    >>> type("hello world")
    <class 'str'>
    >>> print(unicode_str.encode('utf-8'))
    b'hello world'
    >>> unicode_str.encode('utf-8') == \
        bytearray("hello world", "utf-8")
    True

Colocando em prática
--------------------

Se você seguiu essa introdução mas não tinha um console python disponível,
pode praticar nesse console de python 2.7 do pessoal do PythonAnyWhere

.. raw:: html

    <iframe
      style="width: 640px; height: 480px; border: none;"
      name="embedded_python_anywhere"
      src="https://www.pythonanywhere.com/embedded/">
    </iframe>


