import csv

# #it.calc()
#print(Hello.__dict__) #this will bring all attributes at class level
# # print(it.__dict__)# this will bring all attributes at instance level
# it.apply()   #here the payrate works like what is given which is 0.8
# print(it.price)

# it2.pay_rate = 0.7
# it2.apply()
# print(it2.price) #at first you will see no change because in apply fucntion we are using class name if we use self then see


# for i in Hello.all:
#     print(i.name," ",i.price," ",i.agai)

# print(Hello.all)
#print(Hello.check(10.01))
# print(Hello.all)
# it = Hello("mad",150,400)
# it.instantiate_from_csv()
# print(it.check(100.00))
# print(Hello.all)
# hello1 = Hello("first",500,60)
# hello1.broke = 1
# hello2 = Hello("second",500,70)
# hello2,broke = 1

from bt import bt
from hello import Hello

# first1 = bt("lilo",600,70,6)
# it = Hello("lo",700,80)
# first = bt("kilo",600,70,6)
# print(bt.all)
# print(Hello.all)
# print(first.apply())
# Hello.instantiate_from_csv()
it = bt("hello",750,0,8)
h = Hello("ji",750,0)
it.insert(0.2)
it.apply()
it.dune()
print(it.price)
it.check()
h.check()
# it.check()
# print(it.name)
# it.price = 400
# it.agai = 100
# it.apply()
# print(it.agai)
# print(it.price)
# try:
#     it.name = "leowkebvkjebkjvewv"
# except ValueError as e:
#     print(e)
# print(it.name)
# it.instantiate_from_csv()
# print(Hello.all)
# print(it.check(10.00))

#what is a super method -> super allows us to have access all the attributes and methods of the parent inside the child class


#imp principle of oops -> encapsulation, inheritance, abstraction and polymorphism
# encapsulation is the mechanism of refusing direct access to some of the attributes in a program
#abstraction is the concept which shows only the necessary information and hides the unnecessary information. It also states that you need to hide unnecessary information from the instance
#abstraction is what we called public, private in Cpp
#we have already seen inheritance. Inheritance is about making code reusable across all classes
#polymorphism -> used it by making check function in Hello and then it is used by both bt and Hello -> a single function that knows how to handle different kind of objects