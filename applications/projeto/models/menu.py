# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('hosts',SPAN('3'),''),XML('&trade;&nbsp;'),
                  _class="brand", _href="principal")
response.title = ' '.join(
    word.capitalize() for word in request.application.split('_'))
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Clientes'), False, URL("initial", "show_cliente"), []),
    (T('Servidores'), False, URL("initial", "show_servidor"), []),
    (T('Distros'), False, URL("initial", "show_distro"), []),
    (T('+host'), False, URL("initial", "interface"), [])
]


DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu2 = [
        (SPAN('Admin', _class='dropdown-toggle'), False, '#', [
            (T('Usuários'), False, URL('projeto', 'manager', 'users')),
            (T('Grupos'), False, URL('projeto', 'manager', 'groups')),
            (T('Membros'), False, URL('projeto', 'manager', 'membership'))
        ]),
        (SPAN('Login', _class='dropdown-toggle'), False, '#', [
        (   T('Logout'), False, URL('initial', 'user', 'logout'))
            ])
    ]
if DEVELOPMENT_MENU: _()


