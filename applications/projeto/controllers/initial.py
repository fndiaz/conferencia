# coding: utf-8

def show_cliente():
	response.title="Eventos"

	grid = SQLFORM.grid(db.meetme,
		user_signature=False, searchable=True, csv=False, 
		paginate=50, details=False,  
		ignore_rw = True, maxtextlength=36, 
    	)
	return response.render("initial/show_grid.html", grid=grid)

@auth.requires_login()
def show_servidor():
	response.title="Servidores"

	db.args=Servidor.id.readable=False
	grid = SQLFORM.grid(Servidor,
		user_signature=True, searchable=True, csv=False,
		paginate=50, details=False, 
		ignore_rw = True, maxtextlength=26,
		create=auth.has_membership("admin"),
		editable=auth.has_membership("admin"),
		deletable=auth.has_membership("admin"),  
    	links = [lambda row: A('hosts', _class='btn', 
    		_title='ver servidores', 
    		_href=URL("initial", "/servidor_host", 
    		vars=dict(f=row.id, n1='Servidores', p1='show_servidor')))]
		)
	return response.render("initial/show_grid.html", grid=grid)

@auth.requires_login()
def show_distro():
	response.title="Distribuições"

	db.args=Distro.id.readable=False
	db.args=Distro.img.readable=False
	grid = SQLFORM.grid(Distro,
		user_signature=True, searchable=True, csv=False,
		paginate=50, details=False, ignore_rw = True, 
		maxtextlength=26, links_placement='left',
		create=auth.has_membership("admin"),
		editable=auth.has_membership("admin"),
		deletable=auth.has_membership("admin"),  
    	links = [lambda row: A('hosts', 
    		_class='btn', 
    		_title='ver servidores', 
    		_href=URL("initial", "/distro_host", 
    		vars=dict(f=row.id, n1='Distros', p1='show_distro'))), 
    	dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.img) ))))]
		)
	return response.render("initial/show_grid.html", grid=grid)


@auth.requires_login()
def cliente_host():
	filtro = request.vars['f']
	queryset = db(db.cliente.id == filtro)
	rows = queryset.select()
	cliente = rows[0]
	response.title = cliente.nome
	print cliente

	nome_ant1 = request.vars['n1']
	funcao_ant1 = request.vars['p1']
	nome_atual = cliente.nome

	query = ((db.hosts.id_cliente == filtro) & (db.distro.id == db.hosts.id_distro))
	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) ))), 
	 lambda row: A('Detalhes', 
    		      _class='btn', 
    		      _title='Detalhes', 
    		      _href=URL("initial", "/detalhes_nav", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=cliente.nome, 
    		      			n1='Clientes', p1='show_cliente', p='cliente_host'))),
	 lambda row: A('Editar', 
    		      _class='btn', 
    		      _title='Editar', 
    		      _href=URL("initial", "/edit_host", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=cliente.nome, 
    		      		n1='Clientes', p1='show_cliente', p='cliente_host')))]
	db.hosts.id.readable=False
	db.distro.img.readable=False
	
	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, db.distro.img, 
			  db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'hosts.id':   'ID',
			   'hosts.id_cliente': 'Cliente',
               'hosts.id_servidor': 'Servidor',
               'hosts.id_distro': 'Distro',
               'hosts.nome': 'Nome',
	           'hosts.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, searchable=False, maxtextlength=23, links=links, 
						links_placement='left', editable=False, create=False)

	return response.render("initial/show_grid2.html", grid=grid, nome_ant1=nome_ant1, 
						funcao_ant1=funcao_ant1, nome_atual=nome_atual)

@auth.requires_login()
def servidor_host():
	filtro = request.vars['f']
	queryset = db(db.servidor.id == filtro)
	rows = queryset.select()
	servidor = rows[0]
	response.title = servidor.nome

	nome_ant1 = request.vars['n1']
	funcao_ant1 = request.vars['p1']
	nome_atual = servidor.nome	

	db.distro.img.readable=False
	db.hosts.id.readable=False
	query = ((db.hosts.id_servidor == filtro) & (db.distro.id == db.hosts.id_distro))

	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) ))), 
	 lambda row: A('Detalhes', 
    		      _class='btn', 
    		      _title='Detalhes', 
    		      _href=URL("initial", "/detalhes_nav", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=servidor.nome, 
    		      		n1='Servidores', p1='show_servidor', p='servidor_host'))),
	 lambda row: A('Editar', 
    		      _class='btn', 
    		      _title='Editar', 
    		      _href=URL("initial", "/edit_host", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=servidor.nome, 
    		      		n1='Servidores', p1='show_servidor', p='servidor_host')))]

	fields = (db.hosts.id, db.hosts.id_cliente, db.hosts.id_distro, db.distro.img, 
				db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'hosts.id':   'ID',
			   'hosts.id_cliente': 'Cliente',
               'hosts.id_servidor': 'Servidor',
               'hosts.id_distro': 'Distro',
               'hosts.nome': 'Nome',
	           'hosts.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, searchable=False, maxtextlength=23, links=links, 
						links_placement='left', editable=False, create=False)

	return response.render("initial/show_grid2.html", grid=grid, nome_ant1=nome_ant1, 
						funcao_ant1=funcao_ant1, nome_atual=nome_atual)

@auth.requires_login()
def distro_host():
	filtro = request.vars['f']
	queryset = db(db.distro.id == filtro)
	rows = queryset.select()
	distro = rows[0]
	response.title = distro.nome

	nome_ant1 = request.vars['n1']
	funcao_ant1 = request.vars['p1']
	nome_atual = distro.nome	
	
	db.hosts.id.readable=False
	db.distro.img.readable=False
	query = ((db.hosts.id_distro == filtro) & (db.distro.id == db.hosts.id_distro))
	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) ))), 
	 lambda row: A('Detalhes', 
    		      _class='btn', 
    		      _title='Detalhes', 
    		      _href=URL("initial", "/detalhes_nav", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=distro.nome, 
    		      		n1='Distros', p1='show_distro', p='distro_host'))),
	 lambda row: A('Editar', 
    		      _class='btn', 
    		      _title='Editar', 
    		      _href=URL("initial", "/edit_host", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=distro.nome, 
    		      		n1='Distros', p1='show_distro', p='distro_host')))]

	fields = (db.hosts.id, db.hosts.id_cliente, db.hosts.id_servidor, db.distro.img, 
			  db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'hosts.id':   'ID',
				'hosts.id_cliente': 'Cliente',
               'hosts.id_servidor': 'Servidor',
               'hosts.id_distro': 'Distro',
               'hosts.nome': 'Nome',
	           'hosts.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, searchable=False, maxtextlength=23, links=links, 
						links_placement='left', editable=False, create=False)

	return response.render("initial/show_grid2.html", grid=grid, nome_ant1=nome_ant1, 
						funcao_ant1=funcao_ant1, nome_atual=nome_atual)

def detalhes_nav():
	#detalhes
	filtro = request.vars['f'] #id_host
	id_cliente = request.vars['c'] #id_cliente
	nome_ant = request.vars['n'] #nome (asterisk ou agronelli ou debian)
	nome_ant1 = request.vars['n1'] #nome (servidores ou clientes ou distros)
	funcao_ant = request.vars['p'] #funcao(host_servidores)
	funcao_ant1 = request.vars['p1'] #funcao(show_servidores)
	

	query = ((db.hosts.id == filtro) & (db.hosts.id_cliente == db.cliente.id)
	 	    & (db.hosts.id_servidor == db.servidor.id) 
	 	    & (db.hosts.id_distro == db.distro.id)) 
	detalhes = db.hosts(query)
	
	
	return response.render("initial/detalhes_host.html", detalhes=detalhes, 
				id_cliente=id_cliente, funcao_ant=funcao_ant, funcao_ant1=funcao_ant1, 
				nome_ant=nome_ant, nome_ant1=nome_ant1, filtro=filtro)


def edit_host():
    form = SQLFORM(db.hosts, request.vars['f'], submit_button='Editar', fields = ['id_cliente', 'id_servidor', 'id_distro', 'servicos',
				'if1', 'ip1', 'masc1', 'obs1', 'if2', 'ip2', 'masc2', 'obs2',
				'if3', 'ip3', 'masc3', 'obs3', 'if4', 'ip4', 'masc4', 'obs4',
				'nome', 'ip_chegada', 'porta_ssh', 'gateway', 'rotas', 'obs_gerais'],
				labels = {'id_cliente':'Cliente', 'id_servidor':'Servidor', 'id_distro':'Distro',
				'if1':'Interface 1', 'ip1':'IP', 'masc1':'Máscara', 'obs1':'Obs',
				'if2':'Interface 2', 'ip2':'IP', 'masc2':'Máscara', 'obs2':'Obs',
				'if3':'Interface 3', 'ip3':'IP', 'masc3':'Máscara', 'obs3':'Obs',
				'if4':'Interface 4', 'ip4':'IP', 'masc4':'Máscara', 'obs4':'Obs'})

    if form.process().accepted:
       response.flash = 'Editado com sucesso'
    elif form.errors:
       response.flash = 'Ops, algo não está correto'
    else:
       response.flash = 'Edite os dados do host'

    return response.render("initial/show_form.html", form=form, id_cliente = request.vars['c'], 
    				nome_ant = request.vars['n'], nome_ant1 = request.vars['n1'], 
    				funcao_ant = request.vars['p'], funcao_ant1 = request.vars['p1'])


@auth.requires_login()
def interface():
	#adicionar
    form = SQLFORM(db.hosts, submit_button='Adicionar', 
    			fields = ['id_cliente', 'id_servidor', 'id_distro', 'servicos',
				'if1', 'ip1', 'masc1', 'obs1', 'if2', 'ip2', 'masc2', 'obs2',
				'if3', 'ip3', 'masc3', 'obs3', 'if4', 'ip4', 'masc4', 'obs4',
				'nome', 'ip_chegada', 'porta_ssh', 'gateway', 'rotas', 'obs_gerais'], 
				labels = {'id_cliente':'Cliente', 'id_servidor':'Servidor', 'id_distro':'Distro',
				'if1':'Interface 1', 'ip1':'IP', 'masc1':'Máscara', 'obs1':'Obs',
				'if2':'Interface 2', 'ip2':'IP', 'masc2':'Máscara', 'obs2':'Obs',
				'if3':'Interface 3', 'ip3':'IP', 'masc3':'Máscara', 'obs3':'Obs',
				'if4':'Interface 4', 'ip4':'IP', 'masc4':'Máscara', 'obs4':'Obs'})
   
    if form.process().accepted:
    	host = request.vars
    	email(host)
    	response.flash = 'Inserido com sucesso'		
    elif form.errors:
       response.flash = 'Ops, algo não está correto'
    else:
       response.flash = 'Insira os dados do novo host'
    return response.render("initial/show_form2.html", form=form)

def about():
	filtro = request.vars['f']
	query = ((db.hosts.id_servidor == filtro) & (db.distro.id == db.hosts.id_distro))
	fields = (db.hosts.id, db.hosts.id_cliente, db.hosts.id_distro, db.distro.img, 
				db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, maxtextlength=23, searchable=True, editable=False, create=False)

	return response.render("initial/teste.html", grid=grid,)

def user():
	#if request.args(0) == 'register':
    #    	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	return response.render("initial/user.html", user=auth())

def register():
	return auth.register()

def login():
        return auth.login()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)


def principal():
	response.title="Usuários"

	grid = SQLFORM.grid(db.usuario,
		user_signature=False, searchable=True, csv=False, 
		paginate=50, details=False,  
		ignore_rw = True, maxtextlength=36, 
    	)
	return response.render("initial/show_grid.html", grid=grid)

	
def detalhes_clean():
	filtro = request.vars['f'] #id_host
		

	query = ((db.hosts.id == filtro) & (db.hosts.id_cliente == db.cliente.id)
	 	    & (db.hosts.id_servidor == db.servidor.id) 
	 	    & (db.hosts.id_distro == db.distro.id)) 
	detalhes = db.hosts(query)

	
	return response.render("initial/detalhes_host_clean.html", detalhes=detalhes)

def email(host):
	if auth.has_membership('voip'):
		mail.send(
			to="fndiaz02@gmail.com",
			subject="host adicionado",
			message="<html>Um novo host foi adicionado pelo usuário %s <br>nome: %s <br>vpn: %s<br><br>É preciso fazer a instalação do client zabbix e bacula</html>" % (auth.user.first_name, host.nome, host.ip_chegada,)
			)
	elif auth.has_membership('internet'):
		mail.send(
			to="fernando@ad2.com.br",
			subject="host adicionado",
			message="<html>Um novo host foi adicionado pelo usuário %s <br>nome: %s <br>vpn: %s<br><br>É preciso fazer a instalação do client zabbix e bacula</html>" % (auth.user.first_name, host.nome, host.ip_chegada,)
			)
