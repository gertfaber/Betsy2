import os

def populate_betsy():


    def delete_database():
        # path = r'C:\Users\Gert Faber\Dropbox\00-WincAcademy\C-SQL\03-Betsy\betsy.db'
        path = 'betsy.db'

        if os.path.exists(path):
            os.remove(path)

    delete_database()


    import models_betsy
    import peewee
    # from typing import List

    models_betsy.create_tables()

    User1 = models_betsy.User.create(name='User_name1', adress='Adress_user1', bill_info='Bill_info_user1') 
    User2 = models_betsy.User.create(name='User_name2', adress='Adress_user2', bill_info='Bill_info_user2') 
    User3 = models_betsy.User.create(name='User_name3', adress='Adress_user3', bill_info='Bill_info_user3') 
    User4 = models_betsy.User.create(name='User_name4', adress='Adress_user4', bill_info='Bill_info_user4') 
    User5 = models_betsy.User.create(name='User_name5', adress='Adress_user5', bill_info='Bill_info_user5') 

    Tag1 = models_betsy.Tag.create(name='Tag_name1') 
    Tag2 = models_betsy.Tag.create(name='Tag_name2') 
    Tag3 = models_betsy.Tag.create(name='Tag_name3') 
    Tag4 = models_betsy.Tag.create(name='Tag_name4') 
    Tag5 = models_betsy.Tag.create(name='Tag_name5') 

    # Product1 = models_betsy.Product.create(name='Product_name1',            description='Product_Description1', price_per_unit=1.50, stock=10, owner=1, tag=1) 
    # Product2 = models_betsy.Product.create(name='Product_name2 Sweater',    description='Product_Description2', price_per_unit=2.50, stock=20, owner=2, tag=2) 
    # Product3 = models_betsy.Product.create(name='Product_name3',            description='Product_Description3', price_per_unit=3.50, stock=30, owner=3, tag=3) 
    # Product4 = models_betsy.Product.create(name='Product_name4 sweater',    description='Product_Description4', price_per_unit=4.50, stock=40, owner=4, tag=4) 
    # Product5 = models_betsy.Product.create(name='Product_name5',            description='Product_Description5', price_per_unit=5.50, stock=50, owner=5, tag=5) 

    # Product6 = models_betsy.Product.create(name='Product_name6',            description='Product_Description6', price_per_unit=5.60, stock=60, owner=1, tag=3) 
    # Product7 = models_betsy.Product.create(name='Product_name7',            description='Product_Description7', price_per_unit=5.70, stock=70, owner=2, tag=4) 
    ############################
    Product1 = models_betsy.Product.create(name='cheese',   description='nice taste', price_per_unit=1.50, stock=10, owner=1) 
    Product2 = models_betsy.Product.create(name='Sweater',  description='nice color', price_per_unit=2.50, stock=20, owner=2) 
    Product3 = models_betsy.Product.create(name='laptop',   description='Product_Description3: bla bla', price_per_unit=3.50, stock=30, owner=3) 
    Product4 = models_betsy.Product.create(name='sweater',  description='Product_Description4: bla bla', price_per_unit=4.50, stock=40, owner=4) 
    Product5 = models_betsy.Product.create(name='mobile',   description='Product_Description5: bla bla', price_per_unit=5.50, stock=50, owner=5) 

    Product6 = models_betsy.Product.create(name='mobile',   description='Product_Description6: bla bla', price_per_unit=5.60, stock=60, owner=1) 
    Product7 = models_betsy.Product.create(name='sweater',  description='Product_Description7:', price_per_unit=5.70, stock=70, owner=2)

    ProductTag1 = models_betsy.ProductTag.create(product=1,  tag=1) 
    ProductTag1 = models_betsy.ProductTag.create(product=1,  tag=2) 
    ProductTag1 = models_betsy.ProductTag.create(product=2,  tag=1) 
    ProductTag2 = models_betsy.ProductTag.create(product=2,  tag=4) 
    ProductTag3 = models_betsy.ProductTag.create(product=3,  tag=3) 
    ProductTag4 = models_betsy.ProductTag.create(product=4,  tag=4) 
    ProductTag5 = models_betsy.ProductTag.create(product=5,  tag=5) 
    ProductTag6 = models_betsy.ProductTag.create(product=7,  tag=4) 
    ProductTag7 = models_betsy.ProductTag.create(product=8,  tag=5)

 


    Transaction1 = models_betsy.Transaction.create(buyer=4, product=1, quantity=5) 
    Transaction2 = models_betsy.Transaction.create(buyer=5, product=2, quantity=5) 




if __name__ == "__main__":
    populate_betsy()