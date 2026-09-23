# class school:
#     def __init__(self):
#         self.__name = "DAV"    #private data
#         self.__address = "pune"   #private data

#         print(self.__name)
#         print(self.__address)

# obj=school()

# class school:
#     def __init__(self):
#         self.__name = "Delhi public school"    #protected data
#         self.__address = "Mumbai"   #protected data

#         print(self.__name)
#         print(self.__address)

# obj=school()

# class school:
#     def __init__(self):
#         self.__name = "Delhi public school"    #public data
#         self.__address = "Mumbai"   #public data

#         print(self.__name)
#         print(self.__address)

# obj=school()

# class mobileinfo():
#     def __init__(self):
#         self._name=''

#     def getname(self):
#         return self._name

#     def setname(self,name):
#         self._name=name
#         print(self._name)

# obj=mobileinfo()
# obj.getname()
# obj.setname('mobile')

from abc import ABC, abstractmethod

class product(ABC):
    @abstractmethod
    def display(self):
        pass

class IIT(product):
    def display(self):
        print('welcome to IIT mumbai')

class car(IIT):
    def display(self):
        print('this is acar')

obj=IIT()
obj.display()

obj=car()
obj.display()

from abc import ABC, abstractmethod

class product(ABC):
    @abstractmethod
    def show(self):
        pass

class IIT(product):
    def show(self):
        print('welcome to IIT mumbai')

class car(IIT):
    def show(self):
        print('welcome to car')

obj=IIT()
obj.show()

obj=car()
obj.show()

string = 'engineering674563'
numbers = ''.join(sorted(char for char in string if char.isdigit()))
letters = ''.join(sorted(char for char in string if char.isalpha()))
print(numbers + letters)


string = 'engineering674563'
alpha='' 
num=''
for i in string:
    if i.isalpha():
        alpha+=i
    else:
        if i.isnumeric():
            num+=i
            print(num+alpha)
            print(alpha+num)
output = ''.join(sorted(string))
print(output)