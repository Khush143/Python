from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="python_mwf_10_30"
        )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get=="":
        msg.showinfo("Insert Status","All fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")
        msg.showinfo("Insert Status","Data Inserted Successfully")

def search_deta():
    if e_id.get()=="":
        msg.showinfo("Search Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from student where id%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        for i in row:
            e_fname.insert(0,i[1])
            e_lname.insert(0,i[2])
            e_email.insert(0,i[3])
            e_number.insert(0,i[4])
        conn.close()
            
            

root=Tk ()


root.geometry("400x550")
root.title("My Tkinter Example")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Arile",10))
l_id.place(x=50,y=50)

l_fname=Label(root,text="Firse name",font=("Arile",10))
l_fname.place(x=50,y=120)

l_lname=Label(root,text="Last name",font=("Arile",10))
l_lname.place(x=50,y=190)

l_email=Label(root,text="Email",font=("Arile",10))
l_email.place(x=50,y=260)

l_mobile=Label(root,text="Mobile",font=("Arile",10))
l_mobile.place(x=50,y=330)

e_id=Entry(root)
e_id.place(x=220,y=50)

e_fname=Entry(root)
e_fname.place(x=220,y=120)

e_lname=Entry(root)
e_lname.place(x=220,y=190)

e_email=Entry(root)
e_email.place(x=220,y=260)

e_mobile=Entry(root)
e_mobile.place(x=220,y=330)

insert=Button(root,text="INSERT",font=("Arial",14),fg="white",bg="black",command=insert_data)
insert.place(x=50,y=400)

search=Button(root,text="SEARCH",font=("Arial",14),fg="white",bg="black",command=search_deta())
search.place(x=250,y=400)

update=Button(root,text="UPDATE",font=("Arial",14),fg="white",bg="black")
update.place(x=50,y=470)

delate=Button(root,text="DELATE",font=("Arial",14),fg="white",bg="black")
delate.place(x=250,y=470)





