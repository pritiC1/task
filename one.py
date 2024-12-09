class Student():

    def __init__(self,stud,n):
        
            self.first_name=stud[0]
            self.middle_name=stud[1]
            self.last_name=stud[2]
            self.caste=stud[3]
            self.category=stud[4]
            self.email=stud[5]
            self.phone_number=stud[6]
            self.dob=stud[7]
            self.parent_first_name=stud[8]
            self.parent_middle_name=stud[9]
            self.parent_last_name=stud[10]
            self.parent_p_no=stud[11]
            self.parent_email=stud[12]
            self.admission_year=stud[13]

            self.generate_PRN()

    def generate_PRN(self,stud):
        list=[]
        unique = self.phone_number[-6:]
        PRN=self.admission_year+stud+self.caste+unique
        if PRN is not list:
            list.append(PRN)
        print(PRN)
        self.admit()


    def admit(self):
        print(" admission successfull!!")
        self.department()


    def department(self):
        print(" 1)CSE 2)ENTC 3)civil 4)mechanical 5) Electrical ")
        ch=input("enter your choice")
        if ch==1:
            print("welcome in the CSE department")
        elif ch==2:
            print("Welcome in ENTC Department") 
        elif ch==3:
            print("welcome in civil department")
        elif ch==4:
            print("welcome in mechanical department")
        elif ch==5:
            print("welcome in electrical department")
    def courses(self):
        print("\n1.maths \n2.mechanical \n3.civil")
        ch=int(input("enter the choice:"))
        if(ch==1):
            print("maths selected successfully")
        elif(ch==2):
            print("civil selected successfully")
        elif(ch==3):
            print("mechanical selected successfully")
        else:
            print("course is not selected")
            
            
    
n=input("enter no.of student enrolled:")
dict={}

for i in range(n):

    first_name=input("enter the first name:")
    middle_name=input("enter middle name:")
    last_name=input("enter last name:")
    caste=input("enter caste:")
    category=input("enter category:")
    email=input("enter email:")
    phone_number=input("enter phone_number:")
    dob=input("enter date of birth:")
    parent_first_name=input("enter parent first name:")
    parent_middle_name=input("enter parent_middle_name:")
    parent_last_name=input("enter parent_last_name:")
    parent_p_no=input("enter parent phone no:")
    parent_email=input("enter parent email:")
    admission_year=input("admission_year")

obj=Student(first_name,middle_name,last_name,caste,category,email,phone_number,dob,parent_first_name,parent_middle_name,parent_last_name,parent_p_no,parent_email,admission_year )    


