Testes de Unidade (Mocks e Stubs) e Funcionais 
==============================================

:date: 2013-04-24 19:00
:tags: python,testes,unittest,mocks,stubs
:category: Videos
:author: Felipe Cruz
:short_description: Entenda mais sobre testes unitários simples, com mocks e stubs para ter testes unitários mais completos e
                    como essas abordagens se comparam aos testes Funcionais/Integração. Aprenda uma forma simples de utilizar recursos da
                    biblioteca padrão para ter esses diversos tipos de testes em sua aplicação.

.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/He7uY4pyllQ?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">


Meu Review do Vídeo
-------------------

No caso do teste funcional, o ideal(ou talvez certo) seria ter um teste contendo 2 instâncias de Todo
e não apenas o socket cliente. Nesse caso do vídeo acredito que o teste acabou saindo
**incompleto para um teste funcional** mas **completo como teste de integração** porque testa a interação entre 2 componentes distintos
mas não testa se 2 instâncias conectadas se comportam da forma esperada.





Código fonte do Vídeo
---------------------

.. code-block:: python

    import pytest
    import zmq

    class Todo:
        def __init__(self):
            self.tasks = []
            self._context = zmq.Context()
            self._publisher = self._context.socket(zmq.PUB)
            self._publisher.bind('tcp://*:8888')

        def add_task(self, name, detail=None):
            task = dict(name=name, detail=detail)
            self.tasks.append(task)

            try:
                self._publisher.send_pyobj(task)
            except zmq.ZMQError as zmqe:
                raise Exception("Network Error")


    def test_todo_init():
        todo = Todo()

        assert 0 == len(todo.tasks)

    def test_todo_add_task():
        todo = Todo()
        todo.add_task('test todo')

        assert 1 == len(todo.tasks)
        assert dict(name='test todo', detail=None) == todo.tasks[0]

    def test_todo_add_task_mock():
        from unittest.mock import MagicMock
        todo = Todo()
        todo._publisher = MagicMock()
        todo.add_task('test todo')

        message = {"name": 'test todo', "detail": None}
        todo._publisher.send_pyobj.assert_called_with(message)

    def test_todo_add_task_stub():
        from unittest.mock import patch
        todo = Todo()

        def send_pyobj_success_stub(self, data):
            pass

        def send_pyobj_error_stub(self, data):
            raise zmq.ZMQError()

        with patch('zmq.sugar.socket.Socket.send_pyobj', send_pyobj_success_stub):
            todo.add_task('test todo')

        with patch('zmq.sugar.socket.Socket.send_pyobj', send_pyobj_error_stub):
            with pytest.raises(Exception):
                todo.add_task('test todo')

    def test_functional():
        import time
        todo = Todo()
        time.sleep(0.1)

        context = zmq.Context()
        receiver_socket = context.socket(zmq.SUB)
        receiver_socket.connect('tcp://localhost:8888')
        receiver_socket.setsockopt_string(zmq.SUBSCRIBE, "")
        time.sleep(0.1)

        todo.add_task('todo test')
        message = {'detail': None, 'name': 'todo test'}
        time.sleep(0.1)
        assert message == receiver_socket.recv_pyobj(flags=zmq.DONTWAIT)
        
