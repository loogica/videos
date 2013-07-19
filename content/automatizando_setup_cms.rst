Automatizando setup do django-cms com fabric
============================================

:date: 2013-07-19 16:00
:tags: python,basico,automatizando,fabric
:category: Videos
:author: Felipe Cruz
:short_description: Como configurar rapidamente um projeto com django-cms usando fabric 
                    e alguns outros recursos templated django, makefiles e curl.

.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/xDTbgzsJIuM?rel=0" frameborder="0" allowfullscreen></iframe>
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

    curl -0 https://raw.github.com/felipecruz/loogica_django_cms_template/master/setup_cms.py > setup_cms.py && python setup_cms.py

.. code-block:: python

    import os
    import sys

    from fabric.operations import local
    from fabric.context_managers import lcd

    TEMPLATE_URL = 'https://github.com/felipecruz/loogica_django_cms_template/archive/master.zip'
    DJANGO_CMD = 'django-admin.py startproject --template={template} {project}'

    if __name__ == "__main__":
        project_name = raw_input('Project name: ')
        path = raw_input('Path to create {0}: '.format(project_name))
        with lcd(path):
            local(DJANGO_CMD.format(project=project_name,
                                    template=TEMPLATE_URL))
            with lcd(project_name):
                local('make dbinitial')
                local('make runserver')
