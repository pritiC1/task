class Travel():
    def __init__(self,location,country,state,airport,f_place,capital,count_of_visited):
        self.location=location
        self.country=country
        self.state=state
        self.airport=airport
        self.f_place=f_place
        self.capital=capital
        self.count_of_visited=count_of_visited
        self.visited()

    def visited(self):
        if self.count_of_visited<=0:
            visited=0
        else:
            visited=visited+1

location=input("enter location where you want to visit:")
country=input("enter country name:")
state=input("enter state:")
airport=input("enter airport location:")
f_place=input("enter famous place:")
capital=input("enter capital:")
count_of_visited=input("enter count of visited places:")

obj=Travel(location,country,state,airport,f_place,capital,count_of_visited)






