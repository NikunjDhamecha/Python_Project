from treelib import Node, Tree
tree = Tree()


# class category
class Category:
    # class variable
    code_c = 1200

    # constructor
    def __init__(self, name, parent=None):

        self.name = name
        self.parent = parent
        self.code = Category.code_c+1
        Category.code_c += 1
        self.no_of_products = 0
        self.products = []
        self.display_name = self.name
        self.display_name1()

    def display_name1(self):
        temp = self
        while temp.parent is not None:
            self.display_name = f'{temp.parent.name} > {self.display_name}'
            temp = temp.parent

    # display function
    def display(self):

        print("\nCategory --> ", self.name)
        print("Code --> ", self.code)

        print(self.display_name)
        print("No. of products --> ", self.no_of_products)
        if self.no_of_products != 0:
            print("List of products: ")
            for item in self.products:
                print(item.name)


# class product
class Products:
    # class variables
    code_p = 57294

    # constructor
    def __init__(self, name, category, price):
        self.name = name
        self.code = "c-{}".format(Products.code_p+1)
        Products.code_p += 1
        self.price = float(price)
        category.no_of_products += 1
        self.category = category
        category.products.append(self)

    # display function
    def display(self):
        print("\nProduct: ", self.name)
        print("Code: ", self.code)
        print("Category: ", self.category.name)
        print("Price: ", self.price)


# objects of class category
footwear = Category("Footwear")
women = Category("Women", footwear)
shoes = Category("Shoes", women)

vehicle = Category("Vehicle")
car = Category("Cars", vehicle)
scooter = Category("Scooters", vehicle)
automatic = Category("Automatic", car)

gadget = Category("Gadgets")
communication = Category("Communication", gadget)
wristwatch = Category("Wrist watches", gadget)
mobile = Category("Mobiles", communication)

stationary = Category("Stationary Items")
bag = Category("Bags")

list_c = [footwear, women, shoes, vehicle, car, scooter, automatic, gadget, communication, wristwatch,
          mobile, stationary, bag]

list_cat = sorted(list_c, key=lambda item: item.name)

# objects of class products
product1 = Products("Jupiter", scooter, 86200)
product2 = Products("Activa", scooter, 62481)
product3 = Products("Scooty Pep", scooter, 60311)
product4 = Products("Iphone 12", mobile, 50399)
product5 = Products("Samsung s20", mobile, '37345')
product6 = Products("Oppo f15", mobile, 15999)
product7 = Products("Kia", car, 1189248)
product8 = Products("Audi", car, 3869000)
product9 = Products("Mercedes", car, '5174000')
product10 = Products("Titan", wristwatch, 12000)
product11 = Products("Sonata", wristwatch, 6000)
product12 = Products("Apple watch", wristwatch, 29999)
product13 = Products("Flip-flops", shoes, 799)
product14 = Products("Loafers", shoes, 654)
product15 = Products("Heels", shoes, 2699)
product16 = Products("Trimax pen", stationary, 89)
product17 = Products("Scale", stationary, 5)
product18 = Products("Tesla", automatic, 7000000)
product19 = Products("Purse", bag, 899)
product20 = Products("Rack bag", bag, 2099)

list_p = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10,
          product11, product12, product13, product14, product15, product16, product17, product18, product19, product20]


# List of Categories
print("\n")
print("List of Categories")
print("-----------------------------------------")
for i in list_cat:
    i.display()
print("\n\n")

# Sorting of products
print("Sort Price --> Low to High")
print("-----------------------------------------")
list_pro = list(sorted(list_p, key=lambda item: item.price))
for i in list_pro:
    i.display()

print("\n")

print("Sort Price --> High to Low")
print("-----------------------------------------")
y = list(sorted(list_p, key=lambda item: item.price, reverse=True))
for i in y:
    i.display()

print("\n")
'''
# Finding product using code attribute
code = (input("Enter code: "))
flag = 0
for i in Products.list_p:
    if i.code == code:
        flag = 1
        i.display()
        break
if flag == 0:
    print("Entered code does not exist!!")
print("\n")
'''

# hierarchical representation
print("Hierarchical representation")
print("--------------------------------------------------")

tree.create_node("Catalog", 0)
for i in list_c:
    tree.create_node(i.name, i.name, parent=0)
    if i.parent is not None:
        tree.move_node(i.name,i.parent.name)
    for c in i.products:
        tree.create_node(c.name, c.name, parent=i.name)

tree.show()
