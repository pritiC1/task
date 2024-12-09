import random
class student():
    def __init__(self,name,address,email,f_color,f_game):
        self.name=name
        self.address=address
        self.email=email
        self.f_color=f_color 
        self.f_game=f_game
        self.generate_id()

    def generate_id(self):
        return random.randint(10000,99999)
    

    def display_details(self):
        print("student_name:",{self.name})
        print("address:",{self.address})
        print("email:",{self.email})
        print("f_color:",{self.f_color})
        print("f_game:",{self.f_game})

name=input("enter the student name")
address=input("enter the address: ")
email=input("enter the email:")
f_color=input("enter f_game of student:")
f_game=input("enter the f_game of student:")

stud=student("priti","mahim","pritichaugule44@gmail.com","pink","cricket")
stud.display_details()

