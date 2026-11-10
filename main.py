student=[]
rows=["Name","USN","Dept","Sub1_marks","Sub2_marks","Sub3_marks"]
student.append(rows)

def add_student():
    data=[]
    for i in student[0]:
        val=input(f"Enter student {i} : ").upper()
        data.append(val)
    student.append(data)

def display():  
    if(len(student)==1):
        print("DataBase is empty...")
    else:
        for i in student:
            print(f"|   {i[0]}  |  {i[1]}  |  {i[2]}  |  {i[3]}  |  {i[4]}  |  {i[5]}   ")

def delete_student():
    usn=input("enter the student USN to delete ").upper()
    for i in range(1,len(student)):
        if(student[i][1]==usn):
            print(f" Student with name {student[i][0]} and {usn.upper()} is deleted successfully")
            student.pop(i)
            break
  
def update():
    usn=input("enter the student USN to update ").upper()
    for i in range(1,len(student)):
        if(student[i][1]==usn):
            data=[]
            for j in student[0]:
                val=input(f"Enter the Student {j} to Update : ").upper()
                data.append(val)
            student[i]=data
            print("Updated successfully...")
            break
    
    

print("          Student DataBase           ")
while(1):
    print("     SELECE FROM BELOW OPTIONS    ")
    op=int(input("  1.Insert  2.Display 3.Delete 4.update 5.Exit   : "))
    if(op==1):
        add_student()
    elif(op==2):
        display()
    elif(op==3):
        delete_student()
    elif(op==4):
        update()
    else:
        break;

print("Thank you For using ")