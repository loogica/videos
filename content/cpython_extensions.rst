Python C Extensions
==================================

:date: 2012-08-25 18:30
:tags: c, extensoes
:category: Videos
:status: draft
:author: Felipe

Primeiro passo - Python.h + setup.py
------------------------------------

O primeiro passo pra criar um ambiente de estudos pra criar uma extensão em C
é criar um arquivo .c que inclui Python.h e um arquivo setup.py que descreve
os componentes da extensão.

A versão inicial do setup.py pode ser:

.. code-block:: python

    from distutils.core import setup, Extension

    setup(name="py_c_zmq",
          ext_modules=[Extension("_c_zmq", ['src/pyczmq.c'],
                                           libraries=['zmq'])])

Em detalhes:

* Vamos usar do módulo ``distutils.core`` a função ``setup`` e a classe ``Extension``
* Chamamos setup dando um nome pra esse módulo como primeiro argumento
* Descrevemos o módulo de extensão com nome ``_c_zmq``, uma lista de arquivos fonte
  ``['src/pyczmq.c']`` e a lista de nomes de bibliotecas usadas ``['zmq']``

Se o conteúdo do arquivo ``src/pyczmq.c`` for:

.. code-block:: c 

    #include <Python.h>
    #include <zmq.h>

Feito isso, podemos testar a compilação pela primeira vez:

.. code-block:: sh

    $ python setup.py build
