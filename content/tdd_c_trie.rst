TDD com C - Criando uma Trie - pt 1
===================================

:date: 2013-05-08 12:00
:tags: testes,unittest,tdd,estrutudas de dados,C
:category: Videos
:author: Felipe Cruz
:short_description: Nesse video exploramos um pouco de TDD com a linguagem C para construir passo a passo uma Trie,
                    que é uma estrutura de dados muito utilizada em buscas de texto.


.. raw:: html

    <p><strong>Ver em Fullscreen/HD</strong><p>

    <div class="videoContent">
    <iframe width="560" height="315" src="http://www.youtube.com/embed/lklNd0vF37k?rel=0" frameborder="0" allowfullscreen></iframe>
    </div>

    <script>
        $(document).ready(function() {
            $('.videoContent').fitVids();
        });
    </script>

    <div class="videoTranscription">

Repositórios
------------

tdd_trie
https://github.com/loogica/tdd_trie

thc
https://github.com/hltbra/thc


Código
------
    
trie.c

.. code-block:: c

    #include <stdlib.h>
    #include <stddef.h>
    #include "trie.h"

    trie_node_t* trie_init (void)
    {
        trie_node_t *trie;
        trie = malloc (sizeof (trie_node_t));
        if (trie == NULL)
            return NULL;
        trie->value = 'R';
        trie->children = malloc (sizeof (trie_node_t) * ALPHABET_SIZE);
        if (trie->children == NULL) {
            free (trie);
            return NULL;
        }

        for (int i = 0; i < ALPHABET_SIZE; i++)
            trie->children[i] = NULL;

        return trie;
    }

trie.h

.. code-block:: c

    #define ALPHABET_SIZE 26

    typedef struct trie_node_s trie_node_t;

    struct trie_node_s {
        char value;
        trie_node_t **children;
    };

    trie_node_t* trie_init (void);


test_trie.c

.. code-block:: c

    #include <stddef.h>
    #include "thc.h"
    #include "../src/trie.h"

    void test_trie_init (void)
    {
        trie_node_t* trie = trie_init ();
        ENSURE (NULL != trie);
        ENSURE ('R' == trie->value);
        ENSURE (NULL != trie->children);

        for (int i = 0; i < ALPHABET_SIZE; i++)
            ENSURE (NULL == trie->children[i]);
    }


tests/test_trie.h

.. code-block:: c

    #ifndef _TEST_TRIE_H
    #define _TEST_TRIE_H
    void test_trie_init (void);
    #endif


tests/suite.c

.. code-block:: c

    #include "thc.h"
    #include "test_trie.h"

    int main (int argc, char *argv[])
    {
        thc_addtest (test_trie_init);
        return thc_run (THC_VERBOSE);
    }

