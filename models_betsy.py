from peewee import Model,SqliteDatabase,CharField,ForeignKeyField,IntegerField,DecimalField

# path=r'C:\Uses\Gert Faber\Dropbox\00-WincAcademy\C-SQL\03-Betsy\betsy.db'
path = 'betsy.db'
db =SqliteDatabase(path)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name        = CharField()
    adress      = CharField()
    bill_info   = CharField()
#################################

class Tag(BaseModel):
    name = CharField()


# class Product(BaseModel):
#     name            = CharField()
#     description     = CharField()
#     price_per_unit  = DecimalField(decimal_places=2)
#     stock           = IntegerField()
#     owner           = ForeignKeyField(User)
#     tag             = ForeignKeyField(Tag)
##################################


class Product(BaseModel):
    name            = CharField(index=True)
    description     = CharField()
    price_per_unit  = DecimalField(decimal_places=2)
    stock           = IntegerField()
    owner           = ForeignKeyField(User)
    # tag             = ForeignKeyField(Tag)

class ProductTag(BaseModel):
    product            = ForeignKeyField(Product)
    tag                = ForeignKeyField(Tag)

class Transaction(BaseModel):
    buyer       = ForeignKeyField(User)
    # seller      = ForeignKeyField(User)
    product     = ForeignKeyField(Product)
    quantity    = IntegerField()


def create_tables():
    with db:
        db.create_tables([User, Product, Transaction, Tag, ProductTag])


def print_all_products():
    print('------ print(prod.name, prod.description, prod.price_per_unit, prod.stock, prod.owner)')
    query_all = Product.select()
    for prod in query_all:
        print(prod.id, prod.name, prod.description, prod.price_per_unit, prod.stock, prod.owner)

    
def print_table(Model):
    query_all = Model.select()
    for mod in query_all:
        print(mod.buyer)
