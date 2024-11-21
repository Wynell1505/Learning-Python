#prompt user for name, assuming they enter text
name = input("What's your full name? ") 
print ("Hello,", name)

#recreate the first program using an f-string
name = input("What's your name? ")
print(f"Hello, {name}")

#make it grammatically correct
name=input("What's your name? ").strip().title()
print(f"Hello, {name}")

#create a function hello() 
def hello(name):
    print("Hello,", name)

name = input("What's your name? ").strip().title()
hello(name)

#create a chain of functions
def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(name="world"): #the ="world" covers the case if the user enters nothing
    print("Hello,", name)

main()