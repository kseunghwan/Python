from math import *

phrase = "Giarffe Academy"

print(len(phrase))

print(str(10 /3))
print(pow(10, 3))
print(max(10, 3))
print(min(10, 3))
print(round(10.3))
print(floor(4.5))
print(ceil(8.5))

age = input("Enter your age: ")
print(age)

num1 = input ("Enter a number 1 : ")
num2 = input ("Enter a number 2 : ")
result = int(num1) + int(num2)

print(result)

color = input("Enter a color")
plural_noun = input("Enter a plural_noun")
celebrity = input("Enter a celebrity")

print("Roses are "+ color)
print(plural_noun+" are blue")
print("I love " + celebrity)

friends = ["kevin", "Karen", "Jim", "Oscar", "Tem"]
lucky_numbers = [4, 8, 10, 12, 15, 87, 26, 42]

print(friends[-2:])

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(2, "Kelly")
print(friends)

friends.remove("Tem")
print(friends)

print(friends.index("Oscar"))

print(friends.count("Tem"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()

print(friends2)

friends.clear()
print(friends)

coordinates = (4, 5)
"""
coordinates[1] = 10 -> tuple error
"""
print(coordinates[1])

coordinates = [(4, 5), (6, 9), (80, 55)]

"""
function
"""

def Hope(name, age):
    print("Hello User " + name + ", you are " + str(age))


Hope("LiLi", 24)
Hope("Steve", 45)
Hope("Kim", 70)

def cube(num):
    return num*num*num

print(cube(3))

def cube(num):
    return num*num*num
    """
    앞에 return이 있기에 뒤에 있는 프린트는 실행관문을 거치지않음
    """
    print("code")

result = cube(4)
print(result)


is_male = True

if is_male:
    print("You are a male")

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = True
is_tall = True

if is_male or is_tall:
    print("you are a male")
else:
    print("you neither male nor tall")

is_male = False
is_tall = True

if is_male or is_tall:
    print("you are a male")
else:
    print("you neither male nor tall")

is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a male")
else:
    print("you neither male nor tall")

is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and are not a tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))
print(max_num(3,40,5))
print(max_num(300,40,5))

def max_num(num1, num2, num3):
    if num1 != num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 != num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))
print(max_num(3,40,5))
print(max_num(300,40,5))

num1 = float(input("Enter first number: "))
op = float(input("Enter operator: "))
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("End")

"""
Dictionaries
"""
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Dec","Not a valid Key"))

friends_max = ["jim", "Karen", "Kevin"]
for index in range(10):
    print(index)


for index in range(3, 10):
    print(index)

for index in range(len(friends_max)):
    print(friends_max[index])

"""
Exponent Function
"""
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return  result

print(raise_to_power(3, 2))

number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)

def translate(phrase):
    translation = ""
   #초기화
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
        return translation

print(translate(input("Enter a phrase")))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
        return translation

print(translate(input("Enter a phrase")))

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
        return translation

print(translate(input("Enter a phrase")))


#Try/Except
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

