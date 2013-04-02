from plugin_hradio_widget import hradio_widget

db = DAL('sqlite:memory:')
db.define_table('product', Field('color', 'integer'))
db.product.color.requires = IS_EMPTY_OR(IS_IN_SET([(1, 'red'), (2, 'blue'), (3, 'green')])) 

# Inject the horizontal radio widget
db.product.color.widget = hradio_widget
