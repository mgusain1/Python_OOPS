import csv
class Hello:
    # def calc(self,price,agai):  #self means that the function is basically passing an instance of its class
    #     print(price+agai)
    pay_rate = 0.8
    all = []
    def calc(self):  #both this and above do the same exact thing
        print(self.price+self.agai)

    # def __init__(self,price,agai):
    #     print(price-agai)

    def __init__(self,name: str,price: int,agai: int): #we can make checks here to make sure that the type of variable matches as required
        #check for validations we use assert statements
        assert price>=0,f"Price {price} must be greater than or equal to 0."
        assert agai>=0,f"Quantity {agai} must be greater than or equal to 0."
        # assigned to self
        #print(price-agai)
        # this line dynamically creates name -> if not used then to give my instance a name i would have had to use it.name = "maddy"
        # Assign to self
        self._name = name #using an underscore so that the attribute becomes restricted and then to change it you have to use setters. if you use double underscore then the attribute becomes totally restricted and cannot be used outside of class
        self._agai = agai
        self._price = price
        Hello.all.append(self)

    def insert(self,val):
        self._price = self._price + val*self._price

    @property
    def agai(self):
        return self._agai

    @agai.setter
    def agai(self,value):
        self._agai = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise ValueError(f"Name '{value}' is too long. Length must be 10 characters or less.")
        self._name = value

    def apply(self): #this can be used too to discount our price
         #self.price = self.price*Hello.pay_rate this will use the one written in class
         self._price = self._price * self.pay_rate # this will use the one we will give

    def __repr__(self): #__repr__ method to display a human-readable representation of the object's state.  without this if you print Hello.all then you will get result in language you wont understand
        return "{} Name {} price {} quantity {} and pay rate {}".format(self.__class__.__name__,self._name,self._price,self._agai,self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls): #this is a class method it cannot be called from instance but only from class
        with open('it.csv','r') as f:
            reader = csv.DictReader(f)
            lis = list(reader)

        for i in lis:
            Hello(
                name = i.get('name'),
                price = int(i.get('price')),
                agai = float(i.get('agai'))
            )

    @staticmethod
    def check(val):
        s = str(val)
        list = s.split('.')
        if int(list[1])<1:
            return True
        else:
            return False

    def timothee(self):
        return "hello Paul"

    def zendaya(self):
        return "hello Chani"

    def dune(self): # this is abstraction hiding all the unecessary ones as timothee and zendya are parts of the process so when the instance calls it only calls dune it doesn't care about what is going on in the entire process
        print(self.timothee())
        print(self.zendaya())

    def check(self):
        print("I am in {} check".format(self.__class__.__name__))

    # decorators are function that you can pre execute before another function
