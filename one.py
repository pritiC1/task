class Student():

    def _init_(self,stud,n):
        for i in range(1,n+1):
            self.first_name=stud[i][0]
            self.middle_name=stud[i][1]
            self.last_name=stud[i][2]
            self.caste=stud[i][3]
            self.category=stud[i][4]
            self.email=stud[i][5]
            self.phone_number=stud[i][6]
            self.dob=stud[i][7]
            self.parent_first_name=stud[i][8]
            self.parent_middle_name=stud[i][9]
            self.parent_last_name=stud[i][10]
            self.parent_p_no=stud[i][11]
            self.parent_email=stud[i][12]
            self.admission_year=stud[i][13]

            self.generate_PRN()

    def generate_PRN(self,stud,i):
        lst=[]
        unique=""
        for i in phone_number:
            if i in phone_number[10:5]:
                unique=unique+i
        PRN=self.admission_year+stud+self.caste+unique
        if PRN is not lst:
            lst.append(PRN)
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

for i in range(1,n+1):

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

dict.setdefault(i,[first_name,middle_name,last_name,caste,category,email,phone_number,dob,parent_first_name,parent_middle_name,parent_last_name,parent_p_no,parent_email,admission_year]  )    


num=Student(dict,n)