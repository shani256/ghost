
def subtract(x,y):
    return x - y

def add(x,y):
    return x + y

def divide(x,y):
    return x/y

def multiply(x,y):
     return x*y

print("operations")
print("a.subtract")
print("b.add a number")
print("c.divide a number")
print("d.multiply a number")

choice =input("please enter a choice(a/b/c/d):")
num_1 = float(input("Please enter the first number :"))
num_2 = float(input("Please enter the second number :"))  

if choice == 'a':  
   print(num_1, "-",num_2, "=", subtract(num_1,num_2))

elif choice == 'b':
    print(num_1, "+",num_2, "=", add(num_1,num_2))

elif choice == 'c':
    print(num_1, "/" ,num_2, "=", divide(num_1,num_2))

elif choice =='d':
    print(num_1, "*" , num_2, "=", multiply(num_1, num_2))


else:
    print("Invalid input")
    
    
    
    
    
    