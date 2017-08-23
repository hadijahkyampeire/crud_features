#from Flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/shoppinglist.db'
#db = SQLAlchemy(app)


class ShoppingList(object):
    def __init__(self, name_field, budget_field, user):
        #set a primary key for this list self.id = True
        self.name=name_field
        self.budget=budget_field
        self.shoppinglist_items={}
        self.user_id = user
        

    def view_shoppinglist(self):
        return self.shoppinglist_items

    def edit(self,name,quantity):
        self.name=name
        self.quantity=quantity
        return True

    def add_item(self,name):
        list_item=item(name)
        self.shoppinglist_items[name]=list_item

    def edit_item(self,item,name):
        temp=item
        del self.shoppinglist_items[item.name]
        temp.name=name
        self.shoppinglist_items[name]=temp
        return temp.show_info()

    def delete_item(self,name):
        if name and name in self.shoppinglist_items:
            del self.shoppinglist_items[name]
            return True
        else:
            return False

    def view_item(self,name):
        if name in self.shoppinglist_items:
            item=self.shoppinglist_items[name]
            return item.show_info()

class Item(object):
    def __init__(self, name, quantity, shoplist_id):
        self.name = name
        self.quantity = quantity
        self.list_id = shoplist_id #setting the foreign key of list in the items data


class User(object):

    def __init__(self, email_address, first_name, last_name, my_password):
        #self.id = primary key 
        self.email = email_address
        self.firstname = first_name
        self.lastname = last_name
        self.password = my_password

