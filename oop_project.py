class Item:

    #class attribute ,it is accesible to all objects
    pay_rate=0.8  #payrate after after 20 percent disccount
    all=[] # all is used to keep track of all instance of this class.

    '''price:int  denotes price parameter belongs to int class ,quanity=0 acts as default parameter \n
       if no argument is passed from object and also it denotes that quantity belongs to int class bcz it is assigned with integer '''

    def __init__(self,price:int ,name:str,quantity=0): 

        # running validation to the recived input 
        assert price>=0,f" this price {price} is less than zero" # similar to exception handling by printing the error in a descriptive way
        assert quantity>=0,f" this price {quantity} is less than zero" 

        self.price=price
        self.name=name
        self.quantity=quantity
        Item.all.append(self)    

    def total_price(self):
        return self.price*self.quantity   
    
    def price_after_discount(self):
        return self.price*self.pay_rate     
    '''  here self.pay_rate checks for self instance(object) atrribute value,if it is not present it takes the value of class atrribute
     generally  atrributes that is common for all objects or instances is declaed as class attribute and atrributes which are dynamic and object 
     speccific like {discount} in our example is object specfic is declared as object/instance attribute'''

    def __repr__(self):
        return f"item({self.name},{self.price},{self.quantity})"  
    '''__str and __repr are used to return the objects in readable friendly format ,useful while debugging'''




# item_1=Item(100,"phone",5)
# item_2=Item(200,"laptop",3)
# item_1.pay_rate=0.7   # instance attribute-

# print(item_1.price_after_discount())   #item_1 takes pay_rate=0.7 ,bcz it is defined as instance attribute,which overrides class atrribute.
# print(item_2.price_after_discount())   #item_2 takes payrate=0.8 ,bcz it dosent have instance atrribute defined hence takes class attribute value.


item1 = Item( 100,"Phone", 1)
item2 = Item(1000,"Laptop", 3)
item3 = Item(10,"Cable", 5)
item4 = Item(50,"Mouse", 5)
item5 = Item( 75,"Keyboard", 5)

# for i in Item.all:
#     print(f"{i.price}:{i.name}")  # to print items storde in a clas atribute called all

print(Item.all)  #  this calls __str method by default ,and __repr as fallback if __str is not defined