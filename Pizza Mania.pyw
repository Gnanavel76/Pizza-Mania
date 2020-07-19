import re
import os
from tkinter import*
from tkinter import messagebox
# Current working directory
cwd = os.getcwd()
os.chdir(cwd)
amount=0
subamount=0
Exc=30
Exp=45
Ext=15
vegs=100
vegm=200
vegr=300
nvegs=150
nvegm=300
nvegr=370
q=""
w=""
def bill1():
    global q,w
    fv="Pizza Mania  Welcomes You"+"\n"+str(E1.get())+"\n"+str(E2.get())+"\n"+str(E3.get())+"\n"+"\n"+"Pizza Details:"+"\n"+q+"\n"+w+'\n'+"Total Amount:\t"+"Rs."+str(amount)
    messagebox.showinfo("Bill",fv)
def bill():
    if re.search(r'^[a-z ]+$',str(E1.get())):
        dl.configure(text="")
        if re.search(r'^(0|91)?[7-9]{1}[0-9]{9}',str(E3.get())) and len(str(E3.get()))==10:
                    dl2.configure(text="")
                    global amount,subamount,q,w
                    if z.get()==1:
                        subamount+=Exc
                        w+="Extra Cheese\t"+"Rs.30"+"\n"
                    if t.get()==1:
                        subamount+=Exp
                        w+="Extra PepperCorn\t"+"Rs.45"+"\n"
                    if d.get()==1:
                        subamount+=Ext
                        w+="Extra Tomato\t"+"Rs.15"+"\n"
                    if x.get()==0 and y.get()==0:
                        messagebox.showinfo("Sorry","Please fill all the details")
                    elif x.get()==0:
                        messagebox.showinfo("Sorry","Please select Veg or Non-Veg")
                    elif x.get()==1:
                        q+="Veg"+"\n"
                        if y.get()==0:
                           messagebox.showinfo("Sorry","Please select the size")
                        elif y.get()==3:
                            q+="Small Size\t\t"+"Rs.100"
                            amount=amount+vegs+subamount
                            bill1()
                        elif y.get()==4:
                            q+="Medium Size\t"+"Rs.200"
                            amount=amount+vegm+subamount
                            bill1()
                        else:
                            q+="Regular Size\t"+"Rs.300"
                            amount=amount+vegr+subamount
                            bill1()
                        amount=0
                        subamount=0
                        q=""
                        w=""
                    elif x.get()==2:
                        q+="Non-Veg"+"\n"
                        if y.get()==0:
                           messagebox.showinfo("Sorry","Please select the size") 
                        elif y.get()==3:
                            q+="Small Size\t\t"+"Rs.150"
                            amount=amount+nvegs+subamount
                            bill1()
                        elif y.get()==4:
                            q+="Medium Size\t"+"Rs.300"
                            amount=amount+nvegm+subamount
                            bill1()
                        else:
                            q+="Regular Size\t"+"Rs.370"
                            amount=amount+nvegr+subamount
                            bill1()
                        amount=0
                        subamount=0
                        q=""
                        w=""
        else:
                    dl2.configure(text="Please Enter correct Mobile!")
    else:
        dl.configure(text="Please Enter correct name!")
win=Tk()
win.title("Pizza Mania")
win.geometry("1350x700")
x=IntVar()
y=IntVar()
z=IntVar()
t=IntVar()
d=IntVar()
img=PhotoImage(file = "final123.png")
img1=PhotoImage(file = "final1.png")
L=Label(win,image=img,width=1360,height=700)
L.pack(fill="both",expand=True)
f=Frame(L,bg="black",width=300,height=360)
f.place(x=100,y=150)
c=Canvas(f,width=280,height=300,bg='black',highlightbackground="black")
c.place(x=10,y=50)
c.create_line(3,135,280,135,fill="white",width=2)
c.create_line(3,208,280,208,fill="white",width=2)
c.create_line(3,280,280,280,fill="white",width=2)
L1=Label(f,image=img1,width=70,height=70)
L1.place(x=115,y=5)
L2=Label(f,text="Customer Details",bg="black",fg="white",font=("calibri",18,"bold"))
L2.place(x=65,y=80)
L3=Label(f,text="Name:",bg="black",fg="white",font=("arial",14,"bold")) #Name Label
L3.place(x=10,y=130)
L4=Label(f,text="Email Id:",bg="black",fg="white",font=("arial",14,"bold")) #Emailid Label
L4.place(x=10,y=203)  
L5=Label(f,text="Mobile No:",bg="black",fg="white",font=("arial",14,"bold")) #MobileNo Label
L5.place(x=10,y=275)
dl=Label(f,width=35,bg="black",fg="white")
dl.place(x=13,y=188)
dl2=Label(f,width=35,bg="black",fg="white")
dl2.place(x=13,y=332)
E1=Entry(f,width=25,font=("arial",14,"bold"),bg="black",fg='white',bd=0,insertbackground="red") #Name Entry
E1.place(x=12,y=160)
E2=Entry(f,width=25,font=("arial",14,"bold"),bg="black",fg='white',bd=0,insertbackground="white") #Email Entry
E2.place(x=13,y=233)
E3=Entry(f,width=25,font=("arial",14,"bold"),bg="black",fg='white',bd=0,insertbackground="white") #Mobile Entry
E3.place(x=13,y=303)
f1=Frame(L,bg="black",width=300,height=250)
f1.place(x=960,y=165)
f2=Frame(L,bg="black",width=300,height=110)
f2.place(x=960,y=400)
L6=Label(f1,text="Pizza Details:",bg="black",fg="white",font=("arial",18,"bold"))
L6.place(x=13,y=5)
r=Radiobutton(f1,text="Veg",bg="black",fg="white",font=("arial",18,"bold"),value=1,variable=x,selectcolor="black") #Radio Button
r.place(x=15,y=50)
r1=Radiobutton(f1,text="Non Veg",bg="black",fg="white",font=("arial",18,"bold"),value=2,variable=x,selectcolor="black") #Radio Button
r1.place(x=160,y=50)
c=Checkbutton(f1,text="Extra Cheese",font=("arial",17,"bold"),bg="black",fg="white",variable=z,selectcolor="black")
c.place(x=15,y=100)
c1=Checkbutton(f1,text="Extra Pepper",font=("arial",17,"bold"),bg="black",fg="white",variable=t,selectcolor="black")
c1.place(x=15,y=150)
c2=Checkbutton(f1,text="Extra Tomato",font=("arial",17,"bold"),bg="black",fg="white",variable=d,selectcolor="black")
c2.place(x=15,y=200)
L7=Label(f2,text="Size:",bg="black",fg="white",font=("arial",18,"bold"))
L7.place(x=13,y=8)
r2=Radiobutton(f2,text="Small",bg="black",fg="white",font=("arial",12,"bold"),variable=y,value=3,selectcolor="black") #Radio Button
r2.place(x=13,y=55)
r3=Radiobutton(f2,text="Medium",bg="black",fg="white",font=("arial",12,"bold"),variable=y,value=4,selectcolor="black") #Radio Button
r3.place(x=100,y=55)
r4=Radiobutton(f2,text="Regular",bg="black",fg="white",font=("arial",12,"bold"),variable=y,value=5,selectcolor="black") #Radio Button
r4.place(x=200,y=55)
b1=Button(L,text="Submit",font=("arial",12,"bold"),bg="red",fg="white",width=10,bd=0,command=bill) #button
b1.place(x=630,y=650)
win.mainloop()
