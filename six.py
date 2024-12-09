class dairy():
    def __init__(self,farmer_name,address,litre,cost):
        self.farmer_name=farmer_name
        self.address=address
        self.litre=litre
        self.cost=cost
        self.display()

    def display():
        print("farmer name:{self.farmer_name}")
        print("address:{self.address}")
        print("quantity of milk:{self.litre}")
        print("cost per litre:{self.cost}")

d=dairy("shyam","pandharpur",20,60)
P=dairy("Ram","pandharpur",30,60)

d.display()
P.display()
