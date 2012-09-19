Mais Python Básico - pt2
========================

:date: 2012-08-30 23:00
:tags: python
:category: Videos
:author: Felipe
:short_description: Executando programas, arquivos fonte etc..

O ideal é ver em 720p HD em fullscreen.

.. raw:: html

    <iframe id="video" width="560" height="315" src="http://www.youtube.com/embed/UB3u5jqB4D8" frameborder="0" allowfullscreen>
    </iframe>

    <script>
        $(document).ready(function() {
            $('#video').fitVids();
        });
    </script>

Executando programas em Python
------------------------------

A maneira mais simples seria chamar o interpretador seguido do nome do programa:

.. code-block:: sh

    $ python meu_programa.py

Uma outra maneira, seria colocar no início do seu arquivo .py:

.. code-block:: shell

    #!/usr/bin/env python

E nos UNIX-like (linux e osx), precisamos dar permissão de execução:

.. code-block:: sh

    chmod +x meu_programa.py

Para finalmente:

.. code-block:: sh

    ./meu_programa.py

Configurando encoding de arquivos fonte
---------------------------------------

PEP 
```
PEP 0263 - [http://www.python.org/dev/peps/pep-0263/]

Como no primeiro video, já comentei sobre unicodes, vou explicar como informar
ao interpretador python que o seu arquivo fonte tem um 'encoding' diferente de
ASCII. A nossa língua (pt-BR) faz muito uso de caracteres que não são representados
no ASCII. Em alguns casos, onde queremos colocar palavras acentuadas em strings
Python precisamos permitir que isso seja aceito.

A forma de fazer isso é informar na primeira linha do seu arquivo fonte o encondig:

.. code-block:: python

    # -*- coding: encoding -*-

Na prática, eu quase sempre uso utf-8:

.. code-block:: python

    # -*- coding: utf-8 -*-

Melhor Ambiente Interativo
--------------------------

Para facilitar os estudos, vamos instalar um ambiente interativo com
mais recursos.

.. code-block:: sh

    $ pip install ipython
    $ ipython

