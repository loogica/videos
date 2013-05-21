Coopy - Persistência de Objetos
===============================

:date: 2013-04-12 19:00
:tags: python,persistencia,coopy
:category: Videos
:author: Felipe Cruz
:short_description: Coopy é uma ferramenta de persistência de dados Simples, Transparente e Não-Intrusiva que permite
                    com pouco trabalho criar sistemas persistentes para prototipação ou produção. Os dados ficam disponíveis
                    em memória então o desempenho é excelente mesmo assim a durabilidade é garantida entre sessões de uso.

.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/KSVujdM0jyQ?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">


TODO List com Coopy
-------------------

.. code-block:: python

    from coopy.base import init_persistent_system

    class Todo(object):
        def __init__(self):
            self.tasks = []

        def add_task(self, name, desc):
            task = dict(name=name, description=desc)
            self.tasks.append(task)

    todo_list = init_persistent_system(Todo())
    todo_list.add_task("Some Task Name", "Desc")


Testes fáceis?
--------------

.. code-block:: python

    todo_list = Todo()
    todo_list.add_task("Test", "Make Test")

    assert len(todo_list.tasks) == 1


Coopy - Prototipação
--------------------

* Aplicação de URL Shortener em 72 linhas: https://gist.github.com/felipecruz/5367960

Coopy em Produção
-----------------

* Rio bus - http://riobus.loogica.net
* Fonte: https://github.com/loogica/riobus
* 1800 linhas e +36 mil ruas em memória desde 9/2012.
