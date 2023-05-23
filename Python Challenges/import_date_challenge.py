import datetime #This is importing the datetime module

y = datetime.datetime.now()#This variable sets the date to the current date
print(y.year) #This prints out the year
print(y.strftime("%A"))#This prints the day of the week           

import random #This imports the random module

print(random.randrange(10, 55))#This prints out the random number between 10 and 55

num1 = 12
key = False

if num1 == 12:
    if key:
        print("num1 is equal to twelve and they have the key!")
    else:
        print("num1 is equal to twelve and they DO NOT have the key")
elif num1 < 12:
    print("num1 is less than twelve!")
else:
    print("num1 is NOT equal to twelve!")

A = 25
B = 35
if A > B:
    print("A is greater than B")
elif A < B:
    print("A is less than B")
else:
    print("A is not greater than B")

print(bool("hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

X =67
print(isinstance(X, bool))

i = 0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1

i = 0
while i < 10:
    print("{} iteration through the loop.".format(i))
    i += 1
    

i = 5
while i < 10:
    print(i)
    if (i == 7):
        break
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("i is no longer less than 5")

i = 0
for i in range(10):
    print(i)
    if (i == 5):
        continue
    i += 1

animals = ("dog", "goat", "donkey", "horse")
for x in animals:
    if x == "donkey":
        continue
    print(x)

mySentence = "I love the color"

color_set = ["red", "blue", "green", "pink", "teal", "black"]

def color_function():
    for i in color_set:
        print("{} {}".format(mySentence,i))

color_function()

             
    
