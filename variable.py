# number=17
# for i in range(2,number):
#     if number % i==0:
#         print ('this is not prime number')
#         break
# else:
#     print ('this is prime number')

# list=[90,20,34,11,34,98,54]
# output=list[0::2]
# print(output)

# list=[90,20,34,11,34,98,54]
# output=list[1::2]
# print(output[::-1])

# list=[90,20,34,11,34,98,54]
# output=list[0::3]
# print(output)

# list1=[1,1,2,2,3,3,4,5,6]
# output= list(set(list1))
# print(output)

# set={45,87,67,44,23,90,87,12,65}
# print(set)

# set={12,23,45,67,89,90,32,12}
# set.add(32)
# print(set)

# set={43,45,67,12,45,87,10}
# set.add(5)
# print(set)

# set={43,45,67,12,45,87,10}
# set.pop()
# print(set)

# set={43,45,67,12,45,87,10}
# set.copy()
# print(set)

# tuple=(20,34,87,67,12,45,65,90,89,84)
# print(tuple)

# tuple=(20,34,87,67,12,45,65,90,89,84)
# tuple.count(84)
# print(tuple)

# tuple=(20,34,87,67,12,45,65,90,89,84)
# tuple.index(84)
# print(tuple)

# dict={'name':'rahul','address':'pune','rollno':30}
# print(dict)

# dict={'name':'rahul','address':'pune','rollno':30}
# for i in dict.keys():
#     print(i)

# dict={'name':'rahul','address':'pune','rollno':30}
# for i in dict.values():
#     print(i)


# dict={'name':'rahul','address':'pune','rollno':30}
# for i in dict.items():
#     print(i)

# dict={'name':'rahul','address':'pune','rollno':30}
# print(dict['address'])

# dict={'name':'rahul','address':'pune','rollno':30}
# print(dict['name'])

# dict={'name':'rahul','address':'pune','rollno':30}
# dict['address']='latur'
# print(dict)

# dict={'name':'rahul','address':'pune','rollno':30}
# dict['email']='vj@gmail.com'
# print(dict)

# dict={'name':'rahul','address':'pune','rollno':30}
# del dict['address']
# print(dict)

# dict={'name':'rahul','address':'pune','rollno':30}
# del dict['name']
# print(dict)

# student = {
#     'student1': {'name': 'Rahul','address': 'Pune','rollno': 30},
#     'student2': {'name': 'Prerna','address': 'Udgir','rollno': 31}
# }
# print(student)

# dict={
#     'student':{'name':'amit','rollno':30,'address':'pune'},
#     'teacher':{'name':'radha','rollno':99,'address':'mumbai'}
# }
# for emp,details in dict.items():
#     print(emp)

#     for value in details.values():
#         print(value)

# del dict['student']['name']
# print(dict['student'])

# string='software'
# print(string)

# string='software'
# print(string[::-1])

# string='software test'
# output= max(string.split(),key=len)
# print(output)

# string='software test'
# output= min(string.split(),key=len)
# print(output)

# string='software'
# output=sorted(string)
# result=''.join(output)
# print(result)

# string='54673829frtsd%^^&@@*'
# output=''
# for i in string:
#     if i.isalpha():
#         output=output+i
# print(output)        

# string='54673829frtsd%^^&@@*'
# output=''
# for i in string:
#     if i.isalnum():
#         output=output+i
# print(output)  

# string='Hello Software'
# output=''
# for i in string:
#     if i.isupper():
#         output=output+i
# print(output[::-1])

# string='Hello Software'
# output=''
# for i in string:
#     if i.isupper():
#         output=output+i.lower()
#     else:
#         output=output+i.upper()
# print(output[::-1])

# string='softwaretest9156410'
# list=sorted(string) 
# output=''.join(list)
# print(output)

# string='softwaretest9156410'
# alphabet=[]
# numeric=[]
# for i in string:
#     if i.isalpha():
#         alphabet.append(i)
#     else:
#         numeric.append(i)
# output=''.join(sorted(alphabet)+sorted(numeric))
# print(output)

# string='apple','mango','orange','banana','apple'
# duplicate=[]  
# seen=set()
# for i in string:
#     if i in seen:
#         duplicate.append(i)
#     else:
#         seen.add(i)
# output=''.join(duplicate)
# print(output)

# string='banglore'
# dict={}
# output=''
# for i in string:
#     dict[i]=dict.get(i,0)+1
# for k, v in dict.items():
#     output=output+k+str(v)
# print(output)  

# string='12g45hj678hnj98p'
# output=''
# for i in string:
#     if i.isnumeric():
#         x=int(i)
#     else:
#         d=i
#         output=output+x*d
# print(output)

# seen=set()
# seen.add(i)

# result=[]
# result.append(i)

# output=''
# output=output+i
# dict={}
# dict[i]=i

# list=[]
# even=[]
# odd=[]
# for i in range(1,20):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print('Even:',even)
# print('Odd:',odd)

# dict={}
# for i in range(1,20):
#     if i%2==0:
#         dict[i]=i*i
# print(dict)

# string='software768504'
# output=string.removeprefix('software')
# print(output)

# class product:
#     def show(self):
#         print('the name of product',self)
#         print('the price of product',self)

# object=product()
# object.name='mobile'
# object.price=90000
# object.show()

# class product:
#     def __init__(self,name,price,category):
#         self.name=name
#         self.price=price 
#         self.category=category

#         print(self.name)
#         print(self.price)
#         print(self.category)
# j=product('laptop',90000,'electronics')

# class school:
#     def show(self):
#         print(self.name)
#         print(self.address)

# class IIT(school):
#     def display(self):
#         print('welcome to IIT mumbai')
# class college:
#     def display(self):
#         print('welcome to college')
# class IIT(school,college)
#     pass

# obj=IIT()
# obj.name='DEV'
# obj.address='pune'
# obj.show()
# obj.display() 

# class parent1:
#     def show(self):
#         print('this is parent1')
# class parent2:
#     def show(self):
#         print('this is parent2')

# class child(parent1,parent2):
#     def display(self):
#         print('this is child class')
# obj=child()
# obj.show()
# obj.display()

# ##runtime polymorphism

# class product:
#     def show(self):
#         print(self.name)
#         print(self.price)

# class IIT(product):
#     def show(self):
#         print('welcome to IIT')

# obj=IIT()
# obj.name='mobile'
# obj.price=70000
# obj.show()

# class product:
#     def show(self,name=''):
#         print('this is very good product')
#         if name:
#             print('Product name:', name)

# obj=product()
# obj.show()
# obj.show('laptop')

