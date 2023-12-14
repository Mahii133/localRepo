class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
def greet(customer):
    if customer.gender == 'Male':
        print("Hello", customer.name, 'Sir')
    else:
        print("Hello", customer.name, "ma'am")

cust = Customer("Nitish", "Male")  # Assuming Nitish is Male
print(cust.name)

greet(cust)

class Customer:
    def __init__(self, name):
        self.name = name
    
def greet(customer):
    print(id(customer))
    customer.name = 'Nitesh'
    print("Hello", customer.name)
    print(id(customer))

cust = Customer("Ankita") 
print(id(cust))

greet(cust)
print(cust.name)

def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1 = [1,2,3,4,5]
print(id(L1))
print(L1)

change(L1[:]) #cloning outer list will not change it's safe. we can use tuple instead,"[:]" remove this and see the magic

print(L1)