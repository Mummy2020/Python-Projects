mySentence = "love the color"

color_set = ["red", "blue", "green", "pink", "teal", "black"]

def color_function(name):
    list = []
    for i in color_set:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        list.append(msg)
    return list

list = color_function("Sankung")
for i in list:
    print(i)

def get_name():
    go = True
    while go:
        name = input("what is your name?")
        if name =="":
            print("You need to provide your name!")
        elif name == "Sankung":
            print("Sankung, you are not allowed to use this software")
        else:
            go = False
    list = color_function(name)
    for i in list:
        print(i)

get_name()


def my_function(fname):
    print(fname + " loves to play soccer")

my_function("Sankung")
my_function("Isha")
my_function("Bubacarr")

def multiply(a, b):
    return a * b
print(multiply(5, 4))

my_list = ["orang", "banana", "pineapple", "papaya", "lemon"]
for i in my_list:
    print(i)

my_list.count("pineapple")
my_list.append("mango")
my_list[1] = "jackfruit"
my_list.remove("lemon")
print(my_list)

my_list.sort()
print(my_list)

my_list.count(my_list)
print(my_list)

fname = "Sankung"
lname = "Saidyleigh"
print("Hello {} {}".format(fname,lname))

txt = "For only {price: .2f} dollars!"
print(txt.format(price = 49))

print("binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}".format(4))

x = format(20, "b")
print(x)

def getSum(num1,num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))

getSum(2,4)
