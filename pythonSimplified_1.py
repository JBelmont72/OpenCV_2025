'''
object  oriented computing
https://www.youtube.com/watch?v=f0TrMH9s-VE&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=1

https://www.youtube.com/watch?v=-LsuiVGO-88&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=3

https://www.youtube.com/playlist?list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv
In this tutorial, we will practice the principles of Object-Oriented Programming and draw a forest of unique tree objects.
We will first create a Tree class and then we will replicate it in different locations, sizes and colours. We will also include a very large degree of randomness in our code, so that each time our program runs - a brand new forest with brand new trees is created
Object Oriented Programming
'''

# class Fruits:
#     def __init__(self):
#         self.Name='Apple'
#         self.color='red'
        
# myFruit = Fruits()
# myFruit.color=('green')
# myFruit.Name=('kiwi')
# print(myFruit.color) 
# print(myFruit.Name) 

# #this one needs work
# class Fruits:
#     def __init__(self,name,clr):
#         self.Name =name
#         self.color =clr
# #myFruit = Fruits('name','clr') 
# # apple = Fruits('apple','red')
# FruitList = ['apple','banana','orange']
# for i in FruitList:
    
    
#     print((i))
# myFruit.Name=('kiwi')
# myFruit.color ='green'
# print("make this Kiwi: ",myFruit.Name)
# print(myFruit.color)
       
# class Fruits():
    
#     #method
#     def __init__(self,name,clr):
#         self.name = name
#         self.color =clr
#     def details(self):
#         print('my '+self.name+' is '+self.color)
    
        
# apple =Fruits('apple','red')
# apple.details()
# kiwi =Fruits('kiwi','green')
# kiwi.details()
# name of object.name of method followed by ()
# the self "keyword"  insures that all the attributes are accessible by all the methodsclass Fruits():
# class Fruits:    
#     #method
#     def __init__(self,name,clr):
#         self.name = name
#         self.color =clr
#     def details(self):
#         print('my '+self.name+' is '+self.color)
#     def expiration(self):
        
#         print('Expires on: '+'03/20/2026')
# apple =Fruits('apple','red')
# apple.details()
# kiwi =Fruits('kiwi','green')
# kiwi.details()
# kiwi.expiration()
# apple.expiration()

# # another way to call a method and add an attribute
# class Fruits:    
#     #method
#     def __init__(self,name,clr):
#         self.name = name
#         self.color =clr
#         self.expiration ='03/20/2026'
#     def details(self):
#         print('my '+self.name+' is '+self.color)
#         print('Expires on: '+self.expiration)
        
        
        
# apple =Fruits('apple','red')
# apple.details()
# kiwi =Fruits('kiwi','green')
# kiwi.details()


# class Fruits:    
#     #method
#     def __init__(self,name,clr,exp):
#         self.name = name
#         self.color =clr
#         self.expiration = exp
#     def details(self):
#         print('my '+self.name+' is '+self.color)
#         print('Expires on: '+self.expiration)
        
# expiration = '03/25/2026'       
# apple =Fruits('apple','red',expiration)
# # here self represents the apple 'Object'
# apple.details()
# kiwi =Fruits('kiwi','green',expiration)
# #here self represents the kiwi object
# kiwi.details()

# class myClass:
#     def __init__(self,a,b):
#         self.abc = a
#         self.deg =b #self.attribute
# ''' init has a rederved name, can't be changed-
# it's where we initialze attributes-
# It's automatically executed with every class instance

# SELF is the object of each instance

# FYI self in Javascript is 'this' and and Class is called a 'constructor'
# function Fruit(name,clr){
#     this.Name =name
#     this.color = clr
# }
# THe above is the python class written as a javascript 'Constructor'
# FUNCTIONS inside a CLass are called METHODS
# and varialbleswith the self. prefix inside Functions are called ATTRIBUTES

# '''
# # lesson 2 python simplified
# class Guitar:
#     def __init__(self):
#         self.strings= 6
#         self.name= 'stratovarious'
#     # def play :  # without the SELF, we create a funstion, NOT a method#
#     #
#  # call a function with '  play() '
#  # call a methid with object name first " object.play()"       
        
# myGuitar = Guitar()
# print(myGuitar.strings) 
# print(myGuitar.name)       
# # NEXT
# class Guitar:
#     def __init__(self):
#         self.strings= 6
#         self.name= 'stratovarious'
#         self.play()     # this calls the method below   
#     def play(self):
#         print(' There is a house of the rising sun.')
# myGuitar = Guitar()
# print(myGuitar.strings) 
# print(myGuitar.name)

# myGuitar = Guitar()
# print(myGuitar.strings) 
# print(myGuitar.name)       
# # NEXT
# print(' next example')

# class Guitar:
#     def __init__(self,st):
#         self.strings= st
#         self.name= 'stratovarious'
#         self.play()     # this calls the method below   
#     def play(self):
#         print(' There is a house of the rising sun.')
# # both of the next two commands worked tochange strings to 10
# myGuitar = Guitar(10)     # this calls the play function and changes the first attribute
# #myGuitar.strings = 10 # this does not call the play function

# print(myGuitar.strings) 
# print(myGuitar.name)
# myGuitar.strings= 20
# print(myGuitar.strings)

# INHERIANCE
# class Guitar:
#     def __init__(self,st):
#         self.strings= st
#         self.name= 'stratovarious'
#         self.play()     # this calls the method below   
#     def play(self):
#         print(' There is a house of the rising sun.')
# # both of the next two commands worked tochange strings to 10
# myGuitar = Guitar(10)     # this calls the play function and changes the first attribute
# #myGuitar.strings = 10 # this does not call the play function

# print(myGuitar.strings) 
# print(myGuitar.name)
# myGuitar.strings= 20
# print(myGuitar.strings)

# class ElectricGuitar(Guitar):
#     pass
# myGuitar=ElectricGuitar(30) # i needed to put in an attribute value because I have it in the --init-- method
# # if only self in the Guitar __init__ I would have just had myGuitar=ElectricGuitar()   "
# print("let me try this: ",myGuitar.strings) # output  'let me try this:  30'

class Guitar():
    def __init__(self,st,model) :
        self.strings = st
        self.model= model
        self.play()
        
    def play(self):
        print('Hear this,my favorite model is ',self.model)
myGuitar = Guitar(7,'Stratocastor') # this is essential to pass values to the --init--
myGuitar.play() # this printed the same as above but needed the above to pass values to the attributes
print(myGuitar.strings) 
print(myGuitar.model)
myGuitar.strings=20 
print(myGuitar.strings)   
class ElectricGuitar(Guitar):       #inheritance, thook the parent class and passe dit into the child class
    pass
myElecGuitar =Guitar(10,'Jimmi Hendrix Reconstruction')
print(myElecGuitar.strings)
myElec= ElectricGuitar(14,'Judson\'s')
myElec.play()


# class Electric(Guitar):
#     def Play_Louder(self):
#         print(' Pam pam pam pam pam'.upper())
        
# myElecGuitar =Guitar(10,'Jimmi Hendrix Reconstruction')
# myElec= Electric(14,'Judson\'s')
# print(myElec.strings)  
# myElec.Play_Louder()    # i have to remember to put self in the 'def Play_Louder(self:)  '
######## want to change a parameter in the child class from what was in the parent class
# class Electric(Guitar):
#     def __init__(self, st, model):
#         super().__init__(st, model)
#         self.strings = 8
#     def Play_Louder(self):
#         print(' Pam pam pam pam pam'.upper())
        
# myElecGuitar =Guitar(10,'Jimmi Hendrix Reconstruction')
# myElec= Electric(14,'Judson\'s')
# print(myElec.strings)  
# myElec.Play_Louder()  

class Electric(Guitar):
    def __init__(self, st, model):
        super().__init__(st, model)
        self.strings = 8
    def Play_Louder(self):
        print(' Pam pam pam pam pam'.upper())
        
myElecGuitar =Guitar(10,'Jimmi Hendrix Reconstruction')
myElec= Electric(14,'Judson\'s')
print(myElec.strings)
  
myElec.Play_Louder()
print(myGuitar.strings)
print(myElec.strings) 
print(myElecGuitar.strings)
