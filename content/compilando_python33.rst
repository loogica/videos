Compilando Python 3.3
=====================

:date: 2012-12-12 15:00
:tags: python,basico,instalacao
:category: Videos
:author: Felipe Cruz
:short_description: Como compilar o código fonte distribuído do Python 3.3.0,
                    criar uma instalação customizada e utilizar o novo binário
                    em um virtualenv.

.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/Dpx6Wfjdhrw?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">



Comandos
--------

.. code-block:: bash

    cd ~
    wget http://python.org/ftp/python/3.3.0/Python-3.3.0.tar.bz2 
    tar -jxvf Python-3.3.0.tar.bz2  
    cd Python-3.3.0/ 
    ./configure --prefix=/home/vagrant/python3.3 
    make -j2 
    make install 
    cd .. 
    ls 
    cd python3.3/ 
    ls 
    bin/python3 
    mkvirtualenv --distribute --python=~/python3.3/bin/python3 py33
