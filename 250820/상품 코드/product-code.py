product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product: 
    def __init__(self, name, code):
        self.name = name
        self.code = code 
    

product1 = Product("codetree",50)
product2 = Product(product_name, product_code)

print("product",product1.code,"is",product1.name)
print("product",product2.code,"is",product2.name)
