import mysql.connector as a

con=a.connect(host="localhost",user="root",password="Tritiya12345@",database="university")

def ast():
   
    a=input("enter the roll no of the student::")

    b=input("enter the name of the student::")

    z=input("enter the semester::")

    d=input("enter the section of the student::")

    e=input("enter the address of the student::")

    f=input("enter the phoneno of the student::")

    data=(a,b,z,d,e,f)

    sql='insert into student values(%s,%s,%s,%s,%s,%s)'

    c=con.cursor()

    c.execute(sql,data)

    con.commit()

    print("data entered successfully")

    print(">---------------------------------------------------------------------------------------------------------<")



def dsec():

    cl=input("enter the section to get student list:::")

    data=(cl,)

    sql="select*from student where section =%s"

    c=con.cursor()

    c.execute(sql,data)

    d=c.fetchall()

    for i in d:

        print("rollno:",i[0])

        print("name:",i[1])

        print("semester:",i[2])

        print("section:",i[3])

        print("address:",i[4])

        print("phoneno:",i[5])

        print(">----------------------------------------------------<")

    print("data shown successfully")

    print(">---------------------------------------------------------------------------------------------------------<")
 
def rst():

    a=input("enter the section::")

    n=input("enter the roll no of the student you want to remove::")

    data=(a,n)

    sql='delete from student where section=%s and rollno=%s'

    c=con.cursor()

    c.execute(sql,data)

    con.commit()

    print("data removed successfully")

    print(">---------------------------------------------------------------------------------------------------------<")

def abstu():

    a=input("enter the date::")

    z=input("enter the rollno::")

    b=input("enter the name of the student::")

    e=input("enter the section of the student::")

    d=input("attendance(present or absent)::")

    data=(a,z,b,e,d)

    sql='insert into stu_attendance values(%s,%s,%s,%s,%s)'

    c=con.cursor()

    c.execute(sql,data)

    con.commit()

    print("data entered successfully")

    print(">---------------------------------------------------------------------------------------------------------<")

    print()


 

def datt():

    cl=input("enter the section to get student_attendance list:::")

    data=(cl,)

    sql="select*from stu_attendance where section =%s"

    c=con.cursor()

    c.execute(sql,data)

    d=c.fetchall()

    for i in d:

        print("date:",i[0])

        print("rollno:",i[1])

        print("name:",i[2])

        print("section:",i[3])

        print("attendance:",i[4])

        print(">----------------------------------------------------<")

    print("data displayed successfully")

    print(">---------------------------------------------------------------------------------------------------------<")

    print()


 

def stf():

    a=input("enter the roll no of the student::")

    b=input("enter the name of the student::")

    z=input("enter the section ::")

    d=input("enter fees_paid(yes/no)::")

    data=(a,b,z,d)

    sql='insert into stu_fees values(%s,%s,%s,%s)'

    c=con.cursor()

    c.execute(sql,data)

    con.commit()

    print("data entered successfully")

    print(">---------------------------------------------------------------------------------------------------------<")

    print()


   

def dfees():

    cl=input("enter the section to get student_fees list:::")

    data=(cl,)

    sql="select*from stu_fees where section =%s"

    c=con.cursor()

    c.execute(sql,data)

    d=c.fetchall()

    for i in d:

        print("rollno:",i[0])

        print("name:",i[1])

        print("section:",i[2])

        print("fees_status:",i[3])

        print(">----------------------------------------------------<")

    print("data displayed successfully")

    print(">---------------------------------------------------------------------------------------------------------<")

    print()

   

   
   
from tkinter import *
root=Tk()


thelabel= Label(root,text='CHITKARA UNIVERSITY INSTITUTE OF ENGINEERING AND TECHNOLOGY '  ,fg='white',bg='black',font=( 24))
thelabel.grid(row=1, columnspan=5)

label_1=Label(root, text='Department', font=(16))
label_2=Label(root, text='Year',font=(16))
entry_1=Entry(root,font=(16))
entry_2=Entry(root,font=(16))
label_3=Label(root, text='Section Name',font=(16))
entry_3=Entry(root,font=(16))

label1=Label(root)
label1.grid(row=2)
label1=Label(root)
label1.grid(row=3)
label1=Label(root)
label1.grid(row=6)

label_1.grid(row=5,column=0)
label_2.grid(row=7,column=0)
entry_1.grid(row=5,column=1)
entry_2.grid(row=7,column=1)
label_3.grid(row=9,column=0)
entry_3.grid(row=9,column=1)

label1=Label(root)
label1.grid(row=8)

thelabel= Label(root,text='DASHBOARD                                                  '  ,fg='black',bg='yellow',font=( 30))
thelabel.grid(row=12)

label1=Label(root)
label1.grid(row=10)
label1=Label(root)
label1.grid(row=11)
label1=Label(root)
label1.grid(row=13)

button1=Button(root,text='ADD STUDENT DATA                      ',fg='red',bg='white',command =ast,font=(12))
button2=Button(root,text='DISPLAY STUDENT DATA             ',fg='red' ,bg='white',command =dsec,font=(12))
button3=Button(root,text='REMOVE STUDENT DATA               ',fg='red',bg='white',command=rst,font=(12))
button4=Button(root,text='STUDENT ATTENDANCE                ' ,fg='blue',bg='white',command=abstu,font=(12), )


button1.grid()
button2.grid()
button3.grid()
button4.grid()

button1=Button(root,text='DISPLAY STUDENT ATTENDANCE ',fg='blue',bg='white',command =datt,font=(12))
button2=Button(root,text='STUDENT FEES                               ',fg='green' ,bg='white',command =stf,font=(12))
button3=Button(root,text='DISPLAY STUDENT FEES               ',fg='green',bg='white',command=dfees,font=(12))


button1.grid()
button2.grid()
button3.grid()


root.mainloop()

