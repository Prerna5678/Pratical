

class product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name= name
        self.price = price

class shopping_cart():
    def __init__(self):
        self.items={}
        

    def add_to_cart(self,product,quntity=1):
        if product_id in  self.items:
            self.items[product_id][quntity] += quntity
        
        else:
            self.item[product_id][]



        