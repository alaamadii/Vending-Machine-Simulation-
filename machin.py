class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def display_information(self):
        print(f"product: {self.name}, Price {self.price}")

class Drink(Product):
    def __init__(self,name,price,volume):
        self.volume = volume
        super().__init__(name,price)
    def display_information(self):
        print(f"Product {self.name}, Price {self.price}, the Volume is {self.volume}")

class Snacks(Product):
    def __init__(self,name, price, calories):
        self.calories = calories
        super().__init__(name,price)
    def display_information(self):
        print(f"Product is {self.name}, Price {self.price}, the calories are {self.calories} ")

class Candy(Product):
    def __init__(self,name, price, flavour):
        self.flavour = flavour
        super().__init__(name, price)
    def display_information(self):
        print(f"Product {self.name}, Price {self.price}, flavour {self.flavour}")



import csv
def load_products(products):
    productss = []
    with open(products, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            type_, name, price, extra = row
            price = float(price)
            if type_ == 'Drink':
                productss.append(Drink(name,price,extra))
            elif type_ =="Snack":
                productss.append(Snacks(name,price,extra))
            elif type_ == "Candy":
                productss.append(Candy(name,price, extra))
    return productss

def get_menu(productss):
    print("Welcome to the vending machine\n plese select what you want:")

    for index,pro in enumerate(productss, start=1):
        print(f'{index}. {pro.__class__.__name__} - {pro.name}')

    choice = int(input('> '))
    print("\nProduct Information")
    productss[choice - 1].display_information()
def colect():
   productss = load_products("products.csv")
   get_menu(productss)

if __name__ == "__main__":
    colect()


