#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Felipe"
SITENAME = u"loogica blog"
SITEURL = 'http://loogica.net/blog'

STATIC_URL = ""

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'
LOCALE = 'pt_BR'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
#LINKS =  (('Python.org', 'http://python.org'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/felipejcruz', 'icon-twitter'),
          ('Github', 'http://github.com/felipecruz', 'icon-github'),)

DEFAULT_PAGINATION = 4

SUMMARY_MAX_LENGTH = (10)

PDF_GENERATOR = False

DATE_FORMAT = {
    'pt': '%d/%m/%Y'
}
DEFAULT_DATE_FORMAT = ('%d/%m/%Y')

DISPLAY_PAGES_ON_MENU = True

TWITTER_USERNAME = 'felipejcruz'
GITHUB_URL = 'http://github.com/felipecruz'
GOOGLE_ANALYTICS = 'UA-1152054-2'

#THEME = 'svbtle/'
THEME = 'loogica_template/'
MEDIA_URL = './theme/'
