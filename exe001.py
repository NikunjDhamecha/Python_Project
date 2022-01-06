class category:
    code_c = 100

    def __init__(self, name):
        self.name = name
        self.code = category.code_c + 1
        category.code_c += 1
        self.no_of_products = 0

    def display_category_information(self):
        print('Category Name: ', self.name)
        print('Category Code:', self.code)
        print('Number of Products:', self.no_of_products)


class Product:
    code_p = 300

    def __init__(self, name, category, price):
        self.name = name
        self.code = Product.code_p + 1
        Product.code_p += 1
        self.category = category.name
        self.price = price
        category.no_of_products += 1

    def Product_Diaplay(self):
        print("Product :", self.name, "code: ", self.code, "category: ", self.category, "Price: ", self.price)


cobj1 = category('Electronic')
cobj2 = category('BeautyCare')
cobj3 = category('Stationary')



pobj1 = [Product('mobile', cobj1, 1500),
         Product('TV', cobj1, 30000),
         Product('Laptop', cobj1, 75000),
         Product('Fridge', cobj1, 30000),
         Product('Shampoo', cobj2, 500),
         Product('Conditioner', cobj2, 750),
         Product('Pen', cobj3, 10),
         Product('Book', cobj3, 50),
         Product('Pencil', cobj3, 5),
         Product('Eraser', cobj3, 3)]

for x in pobj1:
    x.Product_Diaplay()
cobj1.display_category_information()
cobj2.display_category_information()
cobj3.display_category_information()

print("\n")
print("Ascending order.....")
x = (sorted(pobj1, key=lambda x: x.price))
for i in x:
    i.Product_Diaplay()

print("\n")
print("Decending Order......")
x = (sorted(pobj1, key=lambda x: x.price,reverse=True))
for i in x:
    i.Product_Diaplay()



codenumber = int(input("Enter Product Code:"))
y = [x for x in pobj1 if x.code == codenumber]
for i in y:
    i.Product_Diaplay()




