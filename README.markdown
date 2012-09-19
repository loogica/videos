# How to install

First, update the theme submodule

```sh
pip -r requirements.txt
git submodule init
git submodule update
```

## Create a Blog post

Create an rst file inside `content` folder.

You must specify a header like this:

```
:date: 2012-09-09 13:00
:tags: python
:category: Videos
:author: Felipe
:status: draft
:short_description: Estruturas de dados - Básico
```

The `:status: draft` is optional.
