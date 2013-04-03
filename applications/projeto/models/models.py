usuario = db.define_table("usuario",
      Field("nome", notnull=True, unique=True),
      Field("pin"),
      Field("email"),
      #auth.signature
      format="%(nome)s")


meetme = db.define_table("meetme",
      Field("confno", 'id'), 
      Field("starttime", "datetime"),
      Field("endtime", "datetime"),
      Field("membros_user", 'list:reference usuario'),
      Field("admin_user", 'list:reference usuario'),
      Field('gravacao', "boolean"),
      #primarykey=['confno']
      )


meetme.confno.label = 'Sala'
meetme.starttime.label = 'Início'
meetme.endtime.label = "Fim"
meetme.membros_user.label = "Membros"
meetme.admin_user.label = "Admins"


