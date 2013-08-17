Introdução ao AngularJS - 1
===========================

:date: 2013-08-17 18:50
:tags: angularjs,javascript
:category: Videos
:author: Felipe Cruz
:short_description: Introdução sobre o framework AngularJS falando de escopo, controllers
                    e diretivas e explicando os conceitos básicos do framework.

.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/tOsgF7KOvsQ?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">



Arquivos
--------

.. code-block:: html

    <!doctype html>
    <html ng-app>
      <head>
        <title>Angular</title>
        <script src="/angular.min.js"></script>
        <script src="/app.js"></script>
      </head>
      <body>
        <div ng-controller="MeuCtrl">
          <h1>Participar de Lista - {{ nome }}{{ email }}</h1>
          <input type="text" ng-model="email" placeholder="email" />
          <button ng-click="enviar_email()">Assinar</button>
        </div>
      </body>
    </html>


.. code-block:: javascript 

    function MeuCtrl($scope) {
        $scope.email = "seuemail@email.com";
        $scope.nome = "Seu Nome";

        $scope.enviar_email = function() {
            alert($scope.email);
        };
    }



