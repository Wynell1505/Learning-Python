#build a generic addition program
x = 1
y = 2

z = x + y
print(z)

#make the program more versatile, prompt the user for numbers
x = int(input("What's x? "))
y = int(input("What's y? "))
#we're using the + operator, so we have to convert the input to int
print(x + y)

#create the same program using floats
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
print(f"z:,") #this formatting adds a comma after every three digits 

#create a chain on functions that x a number entered by the user
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n*n

main()

#testing how github uploading works
print(1+1)