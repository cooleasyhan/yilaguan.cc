#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'YiHan'
SITENAME = u'YiLaGuan'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['/u01/pelican/plugins/pelican-plugins']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'txt',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('CodeSearch', 'http://www.yilaguan.cc/cs'),
	 ('Tags', 'http://www.yilaguan.cc/tags.html'),
	 ('Archives', 'http://yilaguan.cc/archives.html')
        )
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'pdfs','robots.txt']

##########for buleidea##############


THEME = 'notmyidea'

# Blogroll
LINKS 

# Social widget
SOCIAL

GITHUB_URL = 'https://github.com/cooleasyhan/'

##############for blue idea###########
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
