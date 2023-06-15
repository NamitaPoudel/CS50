from cubes import cube      ## only needed to call cube to access it. Eg: cube(x)
import cubes                ## needs the name of the file to call it. Eg: cubes.cube(x)
import classes, flight
import sys

print("Hello, world")

print("##--------------------Variables--------------------##")
name = input("Name: ")
print("Hello, "+name)
print(f"Hello, {name}")

print("\n##--------------------conditions-------------------##")
n = int(input("Number: "))
if n > 0:
    print("Positive Number.")
elif n < 0:
    print("Negative Number.")
else:
    print("Zero")

print("\n##-----------------------Sequences and Loops------------------##")
##List: sequence of mutable values (modify the list in any way)
##tuple: sequence of immutable values (can't modify the values of tuple)
##sets: collection of unique values (all the values need to be unique)
##dict: collection of key-value pairs (key are unique)

print("#----List-----#")
names = ["Harry", "Ron", "Hermione", "Ginny"]
print(names)
print(names[1])
names.append("Draco")
names.sort()
print(names)

print("#--------Tuple-------#")
coordinatesX = 10.0
cordinatesY = 20.0
cordinate = (10.0, 20.0)


print("#------------Sets---------#")
#Create empty set
s = set()

#add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")

print("#--------Loops--------#")
for i in range(6):
    print(i)
print()
for name in names:
    print(name)
print()
for char in names[0]:
    print(char)

print("#-------Dict-------#")
houses = {"Harry": "Gryffindor", "Draco":"Slytherin"}

#add elements
houses["Hermione"] = "Gryfindor"
print(houses)

print()
print("##----------------Functions-------------#")
def square(n):
    return n*n

for i in range(10):
    print(f"The square of {i} is {square(i)}")
    print(f"The cube of {i} is {cube(i)}")
    print(cubes.cube(i))
    print()

print("##----------------Object Oriented Programming--------------##")
##uses classes.py
p = classes.Point(2,8)
print(p.x)
print(p.y)

fli = flight.Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if fli.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No Avialable Seats for {person}")

print("\n##----------------Decorators-------------##")
def announce(f):
    def wrappper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrappper

@announce
def hello():
    print("Hello, world!  ")

hello()

print("\n##------------Lambda Functions-------------##")
people = [
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Cho", "house":"Ravenclaw"},
    {"name": "Draco", "house":"Slytherin"}
]

people.sort(key=lambda person:person["name"])
print(people)

print("\n##--------Exceptions----------##")
try:
    x=int(input("x: "))
    y=int(input("y: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")