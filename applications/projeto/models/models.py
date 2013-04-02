usuario = db.define_table("usuario",
      Field("nome", notnull=True, unique=True),
      Field("pin"),
      Field("email"),
      #auth.signature
      format="%(nome)s")


meetme = db.define_table("meetme",
      Field("confno", notnull=True, unique=True),
      Field("starttime", "datetime"),
      Field("endtime", "datetime"),
      Field("membros_user", 'list:reference usuario'),
      primarykey=['confno']
      )



