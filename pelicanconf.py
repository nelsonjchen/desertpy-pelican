#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""Primary configuration file for DesertPy Pelican Site"""

AUTHOR = u'DesertPy Pythonistas'
SITENAME = u'DesertPy'
SITEURL = 'https://desertpy.com'

PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = u'en'

# Additional main menue items
MENUITEMS = [('Discord Chat <i class="fas fa-external-link-alt"></i>', 'https://discord.gg/ch7TPCx')]

# Blogroll
LINKS = []

# Social widget
SOCIAL = []

ARTICLE_PATHS = ['posts', 'meetup_posts_gen']

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = False
PAGE_PATHS = ['pages']

# Add page titles here if you don't want them linked to automatically
EXCLUDED_PAGES = ['Web Chat']

# this should be true for dev purposes otherwise you don't see your specified
# css, uh, I think
RELATIVE_URLS = True
GOOGLE_ANALYTICS = 'UA-39513587-1'
THEME = "themes/desertpyidea"

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
