AST Básico - Demonstração
=========================

:date: 2013-03-04 19:00
:tags: python,basico,ast
:category: Videos
:author: Felipe Cruz
:short_description: Esse vídeo é uma demonstração prática de como usar o módulo de ASTs para criar um código em tempo de execução,
                    compila-lo e executa-lo.


.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/0jvlEUIaxJQ?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">


Código utilizado na demonstração
--------------------------------

.. code-block:: python

    import ast
    atribuicao = ast.Assign(
        targets=[ast.Name(id="minha_var",
                          ctx=ast.Store())],
        value=ast.Str(s="meu_valor"))
    meu_mod = ast.Module(body=[atribuicao])
    meu_mod_corrigido = ast.fix_missing_locations(meu_mod)
    code = compile(meu_mod_corrigido, "", "exec")
    exec code
    print(minha_var)


Mais Leitura
------------

* Doc. Oficial: http://docs.python.org/3.3/library/ast.html 
* http://eli.thegreenplace.net/2009/02/16/abstract-vs-concrete-syntax-trees/
