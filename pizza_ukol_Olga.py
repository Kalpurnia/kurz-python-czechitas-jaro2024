#  rodičovská třída Item 

class Item:
    def __init__(self, name, price):
        self.name=name
        self.price=price 
    def __str__(self): 
        return f"položka{self.name} stojí {self.price}"
        

# dceřiná třída Pizza 

class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name,price)
        self.ingredients = ingredients

        """tady jsem si dovolila oproti zadání pojmenovat atribut "extra_ingedinet",
        protože jinak se mi to pletlo se slovníkem "ingredinent" 
        a zadání o chápu tak, že se jedná o novou ingredienci, která k základnímu složení pizzy nepatří, čili že 
        nikdo si nemůže objednat ingedienci, která už v základní verzi je (například nelze chcít jako exra ingredineci neco, 
        co už v základní verzi je, jen další dávku - větší množství)? """
    def add_extra(self, extra_ingredient, quantity, price_per_ingredient):
        self.ingredients[extra_ingredient] = quantity
        self.price +=price_per_ingredient
        
    def __str__(self): 
        return f"Vaše pizza {self.name} má tyto ingedinence: {self.ingredients} a stojí celkem {self.price} Kč." 


class Drink(Item): 
    def __init__(self, name, volume, price):
        super().__init__(name, price)
        self.volume=volume
    def __str__(self):
        return f"nápoj {self.name} v objemu {self.volume} ml  stojí {self.price} Kč"
    
drink_1 =Drink("Fanta", 250, 40)




pizza_1 = Pizza("Prosciutto", 190, {"rajčata": 200, "mozzarella":150,"šunka":100})
pizza_1.add_extra("žampiony", 100, 30)

print(pizza_1)
print (drink_1)


"""tady přidávám do seznamu všech položek v objednávce názvy položek funkcí 
proto jsem oproti dadání nedala all_items jako parametr ve funci  __init__
oproti zadání volím název all_items, protože když se moc věcí jmenuje stejně,
přestávám se v tom orientovat: """

class Order: 
    def __init__(self, customer_name, delivery_address, status = "Nová"): #předpokládám, 
        # že každá objednávka je na začátku nová, že se nikdy nezadávají ex post -  když už jsou doručené 
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.all_items = []
        self.status = status 

    def add_items_name(self,items):  
        for item in items: 
            self.all_items.append(item.name)

    def mark_delivered(self):
        self.status = "Doručená"

    def __str__(self):
        return f"Objednávka pro {self.customer_name} na adresu {self.delivery_address} obsahuje tyto položky {self.all_items} a je ve stavu {self.status}." 

order_1 = Order("Olga Hubíková", "U vodojemu 15")
order_1.add_items_name([pizza_1, drink_1])

print(order_1) 


class Delivery_Person: 
    def __init__(self, name, phone_number, current_order, available=True): 
        self.name=name 
        self.phone_number = phone_number 
        self.available = available 
        self.current_order = current_order 

    def assign_order(self, new_order): 
        if self.available: 
            self.current_order=new_order
            self.available = False 
            

    def complete_delivery(self, status): 
        if status == "delivered":
            self.available=True
            self.current_order= None 

    def __str__(self): 
        return f"Doručovatel {self.name}, tel. {self.phone_number}, aktuální dostupnost: {self.available}, aktuální objednávka :{self.current_order}" 
        
delivery_person_1 = Delivery_Person ("Samuel Elanius", "776 235 698", "žádná")
print (delivery_person_1)

delivery_person_1.assign_order(order_1)
print (delivery_person_1)

delivery_person_1.complete_delivery("delivered")
print(delivery_person_1)
        






        