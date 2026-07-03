# Demo 1 - Functions

def greet(name, message="Hello"):
    return f"{message}, {name}"

def add(*numbers):
    return sum(numbers)

def details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print(greet("Imthiyas"))
print(greet("Imthiyas", "Welcome"))

print("addition of 10+20+30=",add(10, 20, 30))

details(Name="Imthiyas", Course="AI & DS")