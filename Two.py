import random as rd

class farmer():

    def __init__(self,name,age,address,farm_location,acres,workers,income,expense):
        self.name=name
        self.age=age
        self.address=address
        self.farm_location=farm_location
        self.acres=acres
        self.workers=workers
        self.income=income
        self.expense=expense

        self.generate_farm_id()
    
    def generate_farm_id(self):
        return rd.randint(10000,99999)


    def profit(self):
        if(income>expense):
            return self.income-self.expense

        
        




    def display_details(self):
        print("farmer name:{self.name}")
        print("age:{self.age}")
        print("address:{self.address}")
        print("farm_location:{self.farm_location}")
        print("acres:{self.acres}")
        print("workers:{self.worrkers}")
        print("income:{self.income}")
        print("expense:{self.expense}")




name=input("enter farmer name:")
age=input("enter farmer age:")
address=input("enter address:")
farm_location=input("enter farm location:")
acres=input("enter area of the farm:")
workers=input("enter the no of workers in farm:")
income=input("enter income:")
expense=input("enter expense:")

farmer_info=farmer(name,age,address,farm_location,acres,workers,income,expense)
farmer_info.display_details()