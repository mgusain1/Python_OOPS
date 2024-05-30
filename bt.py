from hello import Hello
class bt(Hello):
    #all = [] already present in parent class therefore not required here
    def __init__(self,name,price,agai,broken:int):
        #call to super function to access attributes of parent class
        super().__init__(
            name,price,agai
        )

        assert broken >= 0, f"Quantity {broken} must be greater than or equal to 0."
        self.broken = broken
        # assigned to self
        # print(price-agai)
        # bt.all.append(self) # through super we can access it