Django incomun
==============

:date: 2012-08-01 18:30
:tags: django
:category: Videos
:status: draft
:short_description: Como inspecionar de Apps e Models

Objetivo
--------

O Objetivo dessa aula é comentar sobre algumas funções do framework Django
que podem ser muito úteis para desenvolvimento de bibliotecas ou ferramentas
relacionadas ao Django.

- Vamos explicar um pouco também sobre a introspeção de Models e como
  investigar e entender os ``Fields``.

- Se você quiser ver o código fonte, essas funções estão no módulo ``django.db.models.loading``

Para usa-las, basta usar

.. code-block:: python

    from django.db.models import get_app, get_apps, \
                                 get_model, get_models, \
                                 register_model

Função get_apps()
~~~~~~~~~~~~~~~~~

Essa função retorna a lista de instâncias dos módulos (não o nome deles apenas)
que estão configurados em ``INSTALLED_APPS``.

.. code-block:: python

    from django.db.models import get_apps
    app_list = get_apps()

Existe uma variação, que é outra função, que recebe o nome de uma app e retorna
a instância dela.

.. code-block:: python

    from django.db.models import get_app
    app = get_app('app_name')

Função get_models(app_instance)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Essa função retorna a lista de classes de uma app Django. O parâmetro é uma
instância de app.

.. code-block:: python

    from django.db.models import get_models, get_app
    app = get_app('app_name')
    models = get_models(app)

