class college():
    def __init__(self,name,location,status,branches,seats):
        self.name=name
        self.location=location
        self.status=status
        self.branches=branches
        self.seats=seats
        self.display()

    def display(self):
        print("collage_name:",{self.name})
        print("location:",{self.location})
        print("status:",{self.status})
        print("branches:",{self.branches})
        print("seats:",{self.seats})
        

    
name=input("enter collage_name:")
location=input("enter collage location:")
status=input("enter collage status:")
branches=input("enter branches:")
seats=input("seats:")

obj=college(name,location,status,branches,seats)