num = 10
num2 = num + 5

text = "hello"

aList = []
aList.append(1)
aList.append('hello')
aList.append([1,2])


aDict = {}
aDict["hello"] = "world"
aDict["dict"] = {"hello:": "world"}
aDict["list"] = [1, 2]


def f(x):
    return 2*x+3

def sumAll(a, b, c):
    return a + b + c



def OddEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
# print(OddEven(1))
# print(OddEven(2))


def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년이에요')



fruits = ['사과', '배', '감', '귤']

# for fruit in fruits:
#     print(fruit)


fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
	if '배' == fruit:
		count += 1

def CountFruit(name):
    count = 0
    for fruit in fruits:
        if name == fruit:
            count += 1
    return count

# print(CountFruit('사과'))
# print(CountFruit('배'))
# print(CountFruit('수박'))
# print(CountFruit('귤'))


people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for person in people:
    print(person['name'], person['age'])

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return myname, person['age']
    return myname,'해당하는 이름이 없습니다'

print(get_age('bob'))
print(get_age('kay'))