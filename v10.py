import tkinter
import tkinter.messagebox
from tkinter import  *
import smtplib
import center_tk_window
from PIL import ImageTk,Image
import random as rd
import datetime 
from datetime import date,datetime
import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="keerti")
cur=con.cursor()
cur = con.cursor(buffered=True) 
cur.execute("create database if not exists hello")
cur.execute("use hello")

                                                                       ######### TABLES ##########
#doctor registrating table
cur.execute("create table if not exists docreg"
            "("
            "name varchar(30),"
            "username varchar(20) primary key,"
            "age varchar(3),"
            "gender varchar(2),"
            "phone varchar(10),"
            "password varchar(20),"
            "specialisation varchar(40))")

#patient registration table
cur.execute("create table if not exists patientreg"
            "("
            "pat_username varchar(30) primary key,"
            "pat_password varchar(30),"
            "name char(20),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")

#patient appointment
cur.execute("create table if not exists apt"
            "("
            "pat_app_no int primary key,"
            "patient_username varchar (20),"
            "patient_name varchar(20),"
            "doctor_name varchar(20),"
            "patient_age varchar(3),"
            "patient_gender varchar(1),"
            "app_date DATE,"
            "app_time varchar (10),"
            "patient_problem varchar(100),"
            "suggestions varchar (300))")

#for emergency appointment
cur.execute("create table if not exists emergency"
            "("
            "pat_emer_no int,"
            "pat_name varchar(30),"
            "apt_date varchar (30),"
            "apt_time varchar (30),"
            "problem varchar (120))")

                                                                       ##############################



def funcs(x):
    x.destroy()

                                                                            
                                                                        ###########DOCTOR############
    
# showing whether the doctor should login or delete their info
def doc():
    global e1,e2
    root1=Toplevel()
    root1.geometry("600x600")
    root1.title('Hospital Management - DOCTOR') # used for change of title
    photo = PhotoImage(file ="hospital favicon.png")# used for favicon image
      #to center tkinter window
    center_tk_window.center(root1,root1)
    center_tk_window.center_on_parent(root1,root1)
    center_tk_window.center_on_screen(root1)
           ###############
    root1.iconphoto(False,photo)# used for favicon image
       #used for adding image
    canvas = Canvas(root1,width = 300,height = 200) 
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("hmd1.png"))
    canvas.create_image(15,15,anchor = NW,image=img)
            #############
    label=Label(root1,text="DOCTOR",font='arial 23 bold',bg="white")
    label.pack()
    img1 = ImageTk.PhotoImage(Image.open("doclogin.png"))
    l1 = Label(root1,text="Login",font="arial 18 bold",bg = "light blue")
    l1.place(x=115,y=380)

    img2 = ImageTk.PhotoImage(Image.open("delete1.png"))
    l2 = Label(root1,text="Delete",font="arial 18 bold",bg = "light blue")
    l2.place(x=413,y=380)

    img3 = ImageTk.PhotoImage(Image.open("exit2.png"))
    l3 = Label(root1,text="Exit",font="arial 18 bold",bg = "light blue")
    l3.place(x=275,y=520)
    
    b1=Button(root1,text="LOGIN",font="arial 20 bold",image=img1,relief = RAISED,command=lambda:[doc_login(root1)])
    b2=Button(root1,text="DELETE",font="arial 20 bold",image=img2,relief = RAISED,command=lambda:[del_doc(root1)])
    b3=Button(root1,text="Exit",font='arial 20 bold',image=img3,relief = RAISED,command=lambda:[funcs(root1)])

    b1.place(x=100,y=270)
    b2.place(x=400,y=270)
    b3.place(x=250,y=420)
    root1.configure(bg="light blue")
    root1.resizable(False,False)
    root1.mainloop()

#getting username and password for doctor login
def doc_login(rt1):
    global e3,e4
    funcs(rt1)
    root2=Toplevel()
    root2.geometry("350x300")
    root2.title('Hospital Management - DOCTOR LOGIN')# used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon image
    root2.iconphoto(False,photo)#used for favicon image
          #to center tkinter window
    center_tk_window.center(root2,root2)
    center_tk_window.center_on_parent(root2,root2)
    center_tk_window.center_on_screen(root2)
                ##########
    label=Label(root2,text="LOGIN",font='arial 25 bold',bg="lightblue")
    label.pack()
    l1=Label(root2,text="USERNAME",bg="light blue")
    l1.place(x=30,y=80)
    e3=tkinter.Entry(root2)
    e3.place(x=120,y=80)
    l2=Label(root2,text="PASSWORD",bg="light blue")
    l2.place(x=30,y=120)
    e4=tkinter.Entry(root2)
    e4.place(x=120,y=120)
    b1=Button(root2,text="SUBMIT",height=1,width=6,command=lambda:[doc_login_ins(root2)])
    b1.place(x=150,y=190)
    root2.configure(bg="light blue")
    root2.resizable(False,False)
    root2.mainloop()

#after loging in the doc will get their appointment list
def doc_login_ins(rt2):
    #e3 and e4 is wat we get from doc login
    global e3, e4
    p1=e3.get()
    p2=e4.get()
    funcs(rt2)
    cur.execute('select * from docreg where username = (%s)',(p1,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH USERNAME AVAILABLE")
    else:
        dat = list(dat[0])
        doc_name = dat[0]
        pass1 = dat[5]
        if pass1 == p2:
            doc_ins(doc_name)
        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")

#DOCTOR PORTAL
def doc_ins(doc_name):
    root23 = Toplevel()
    root23.geometry("600x600")
    root23.title('Hospital Management - doctor portal')#used for change of title
    photo = PhotoImage(file = "hospital favicon.png")#used for favicon
    root23.iconphoto(False,photo)#used for favicon
             #to center tkinter window
    center_tk_window.center(root23,root23)
    center_tk_window.center_on_parent(root23,root23)
    center_tk_window.center_on_screen(root23)
              ################
    img = ImageTk.PhotoImage(Image.open("docportal.png"))
    label1 = Label(root23,text='login',image = img)
    label1.pack()

    img1 = ImageTk.PhotoImage(Image.open("appointments1.jpg"))
    l1 = Label(root23,font="arial 16 bold",text ="Appointments",bg="light blue")
    l1.place(x=40,y=350)

    img2 = ImageTk.PhotoImage(Image.open("accapp.png"))
    l2 = Label(root23,font="arial 16 bold",text ="Accepted\nAppointments",bg="light blue")
    l2.place(x=380,y=348)

    img3 = ImageTk.PhotoImage(Image.open("exit3.png"))
    l3 = Label(root23,font="arial 16 bold",text ="Exit",bg="light blue")
    l3.place(x=255,y=510)
    
    label = Label(root23, text="DOCTOR PORTAL", font="arial 25 bold")
    b1 = Button(root23,image=img1,relief=RAISED, command=lambda:[doc_decision(doc_name,root23)])
    b2 = Button(root23, image= img2,relief=RAISED,command=lambda:[accepted_list(doc_name,root23)])
    b3 = Button(root23,image=img3,relief=RAISED,command=lambda:[funcs(root23)])
    label.pack()
    b1.place(x=70,y=240)
    b2.place(x=400,y=238)
    b3.place(x=230,y=400)
    root23.configure(bg="light blue")
    root23.resizable(False,False)
    root23.mainloop()

#accept and decline - appointment waiting list for doctors
def doc_decision(doc_name,rt23):
    funcs(rt23)
    root3 = Toplevel()
    root3.geometry("800x500")
       #to center tkinter window
    center_tk_window.center(root3,root3)
    center_tk_window.center_on_parent(root3,root3)
    center_tk_window.center_on_screen(root3)
            ############
    root3.title('Hospital Management - appointment pendings')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root3.iconphoto(False,photo)#used for favicon
    cur.execute("SELECT * FROM apt WHERE doctor_name =(%s) ORDER BY app_date,app_time",(doc_name,))
    data = cur.fetchall()
    for i in range(len(data)):
        data[i] = list(data[i])
    frame = Frame(root3,height=500,width=800,bg="light blue")
    frame.pack()
    pat_name = Label(root3,text = 'Patient\nName',font='arial 14 bold',bg="light blue")
    pat_name.place(x = 100,y = 20)
    pat_age = Label(root3,text = 'Patient\nAge',font='arial 14 bold',bg="light blue")
    pat_age.place(x = 200,y = 20)
    pat_gen = Label(root3,text = 'Patient\nGender',font='arial 14 bold',bg="light blue")
    pat_gen.place(x = 300,y = 20)
    date = Label(root3,text = 'Date',font='arial 14 bold',bg="light blue")
    date.place(x = 400,y = 20)
    time = Label(root3,text = 'Time',font='arial 14 bold',bg="light blue")
    time.place(x = 500,y = 20)
    y_cor = 100
    ycord = doc_apt_lst(data, y_cor, root3)
    b = Button(root3, text = 'OK', command=lambda:[funcs(root3),doc_ins(doc_name)])
    b.place(x = 400, y = ycord)
    root3.configure(bg="light blue")
    root3.resizable(False,False)
    root3.mainloop()

#accept and decline - appointment waiting list for doctors - recurring fuction 
def doc_apt_lst(lst, y_cor, rt3):
    if len(lst) == 0:
        return y_cor
    else:
        sublst = lst[0]
        if sublst[9] == '':
            l3 = Label(rt3,text = sublst[2],bg="light blue")
            l5 = Label(rt3,text = sublst[4],bg="light blue")
            l6 = Label(rt3,text = sublst[5],bg="light blue")
            l7 = Label(rt3,text = sublst[6],bg="light blue")
            l8 = Label(rt3,text = sublst[7],bg="light blue")
            b1 = Button(rt3,text='Accept',command=lambda:[doc_accepted(sublst[0], sublst[3], rt3)])
            b2 = Button(rt3,text='Decline',command=lambda:[doc_declined(sublst[0], sublst[3], rt3)])
            l3.place(x = 100,y = y_cor)
            l5.place(x = 200,y = y_cor)
            l6.place(x = 300,y = y_cor)
            l7.place(x = 400,y = y_cor)
            l8.place(x = 500,y = y_cor)
            b1.place(x = 600,y = y_cor)
            b2.place(x = 670,y = y_cor)
            y_cor += 40
        list1 = []
        for i in range(len(lst)):
            if i > 0:
                list1.append(lst[i])
        y_cor = doc_apt_lst(list1, y_cor, rt3)
        return y_cor

#updating sql querry if doctor accepted the appointment
def doc_accepted(app_no, doc_name, rt3):
    querry = "UPDATE apt SET suggestions = 'accepted' WHERE pat_app_no = '"+str(app_no)+"'"
    cur.execute(querry)
    con.commit()
    doc_decision(doc_name,rt3)

#updating sql querry as 'declined' if doctor doesnt accept the appointment
def doc_declined(app_no, doc_name, rt3):
    querry = "UPDATE apt SET suggestions = 'declined' WHERE pat_app_no = '"+str(app_no)+"'"
    cur.execute(querry)
    con.commit()
    doc_decision(doc_name,rt3)

# doctor accepted appointment list
def accepted_list(doc_name,rt23):
    funcs(rt23)
    root24 = Toplevel()
    root24.geometry("800x500")
       #to center tkinter window
    center_tk_window.center(root24,root24)
    center_tk_window.center_on_parent(root24,root24)
    center_tk_window.center_on_screen(root24)
          ################
    root24.title('Hospital Management - accepted list')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root24.iconphoto(False,photo)#used for favicon
    cur.execute("SELECT * FROM apt WHERE doctor_name =(%s) ORDER BY app_date,app_time",(doc_name,))
    data = cur.fetchall()
    for i in range(len(data)):
        data[i] = list(data[i])
    frame = Frame(root24,height=500,width=800,bg="light blue")
    frame.pack()
    pat_name = Label(root24,text = 'Patient\nName',font='arial 14 bold',bg="light blue")
    pat_name.place(x = 100,y = 20)
    pat_age = Label(root24,text = 'Patient\nAge',font='arial 14 bold',bg="light blue")
    pat_age.place(x = 200,y = 20)
    pat_gen = Label(root24,text = 'Patient\nGender',font='arial 14 bold',bg="light blue")
    pat_gen.place(x = 300,y = 20)
    date = Label(root24,text = 'Date',font='arial 14 bold',bg="light blue")
    date.place(x = 400,y = 20)
    time = Label(root24,text = 'Time',font='arial 14 bold',bg="light blue")
    time.place(x = 500,y = 20)
    y_cor = 100
    ycord = doc_acc_lst(data, y_cor, root24)
    b = Button(root24, text = 'OK', command=lambda:[funcs(root24),doc_ins(doc_name)])
    b.place(x = 400, y = ycord)
    root24.resizable(False,False)
    root24.configure(bg="light blue")
    root24.mainloop()

#doctor accepted list - recurring function
def doc_acc_lst(lst, y_cor, rt24):
    if len(lst) == 0:
        return y_cor
    else:
        sublst = lst[0]
        if sublst[9] == 'accepted':
            l3 = Label(rt24,text = sublst[2],bg="light blue")
            l5 = Label(rt24,text = sublst[4],bg="light blue")
            l6 = Label(rt24,text = sublst[5],bg="light blue")
            l7 = Label(rt24,text = sublst[6],bg="light blue")
            l8 = Label(rt24,text = sublst[7],bg="light blue")
            b1 = Button(rt24,text='Accept',command=lambda:[doc_suggestion(sublst[0], sublst[3], rt24)])
            l3.place(x = 100,y = y_cor)
            l5.place(x = 200,y = y_cor)
            l6.place(x = 300,y = y_cor)
            l7.place(x = 400,y = y_cor)
            l8.place(x = 500,y = y_cor)
            b1.place(x = 600,y = y_cor)
            y_cor += 40
        list1 = []
        for i in range(len(lst)):
            if i > 0:
                list1.append(lst[i])
        y_cor = doc_acc_lst(list1, y_cor, rt24)
        return y_cor

#doctor suggestion part
def doc_suggestion(app_no, doc_name, rt24):
    global doc_dec
    funcs(rt24)
    root25 = Toplevel()
          #to center tkinter window
    center_tk_window.center(root25,root25)
    center_tk_window.center_on_parent(root25,root25)
    center_tk_window.center_on_screen(root25)
              ##########
    root25.title('Hospital Management - suggestions')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root25.iconphoto(False,photo)#used for favicon
    label1 = Label(root25,text="SUGGESTIONS",font="arial 18 bold",bg="light blue")
    label1.pack()
    frame1 = Frame(root25,height=200,width=300,bg="light blue")
    frame1.pack()
    doc_dec = tkinter.Entry(root25)
    doc_dec.place(x=50,y=100)
    b = Button(root25,text="OK",command=lambda:[suggestion_sql(app_no, doc_name, root25)])
    b.place(x=50,y=150)
    root25.configure(bg="light blue")
    root25.resizable(False,False)
    root25.mainloop()

# suggestions sql part
def suggestion_sql(app_no, doc_name, rt25):
    global doc_dec
    suggestion = doc_dec.get()
    querry = "UPDATE apt SET suggestions = '"+suggestion+"' WHERE pat_app_no = '"+str(app_no)+"'"
    cur.execute(querry)
    con.commit()
    accepted_list(doc_name,rt25)

#for deleting doctor ,getting username and password
def del_doc(rt1):
    global e5,e6
    funcs(rt1)
    root4 = Toplevel()
    root4.geometry("500x400")
        #to center tkinter window
    center_tk_window.center(root4,root4)
    center_tk_window.center_on_parent(root4,root4)
    center_tk_window.center_on_screen(root4)
            ##############
    root4.title('Hospital Management - delete doctor details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root4.iconphoto(False,photo)#used for favicon
    label=Label(root4,text="DELETE DOCTOR DETAILS",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root4,height=300,width=300,bg="light blue")
    frame.pack()
    l1=Label(root4,text="USERNAME",bg="light blue")
    l1.place(x=30,y=100)
    e5=tkinter.Entry(root4)
    e5.place(x=100,y=100)
    l2=Label(root4,text="PASSWORD",bg="light blue")
    l2.place(x=30,y=150)
    e6=tkinter.Entry(root4)
    e6.place(x=100,y=150)    
    b1=Button(root4,text='Submit',command=lambda:[delete_doc(root4)])
    b1.place(x=150,y=280)
    root4.configure(bg="light blue")
    root4.resizable(True,True)
    root4.mainloop()

#deleting the doctor info
def delete_doc(rt4):
    global e5,e6
    p3=e5.get()
    p4=e6.get()
    funcs(rt4)
    cur.execute('select * from docreg where username=(%s)',(p3,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH DOCTOR FOUND")
    else:
        dat = list(dat[0])
        pass1 = dat[5]
        if pass1 == p4:
            cur.execute("Delete from docreg where username=(%s)",(p3,))
            con.commit()
            pass2 = dat[0]
            querry = "UPDATE apt SET suggestions = 'declined' WHERE doctor_name = '"+str(pass2)+"'"
            cur.execute(querry)
            con.commit()
            tkinter.messagebox.showwarning("DELETED SUCCESFULLY",'DELETED')
            
        else:
            tkinter.messagebox.showwarning("ERROR", "WRONG PASSWORD \n INTRUDER!!!!!")

                                                                      ######HOSPITAL######
            
            
#getting the values of hospital username and password
def hosp_login():
    global e7,e8
    root6 = Toplevel()
    root6.geometry("400x300")
          #to center tkinter window
    center_tk_window.center(root6,root6)
    center_tk_window.center_on_parent(root6,root6)
    center_tk_window.center_on_screen(root6)
           ###########
    root6.title('Hospital Management - hospital login')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root6.iconphoto(False,photo)#used for favicon
    label=Label(root6,text="LOGIN",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root6,height=200,width=300,bg="light blue")
    frame.pack()
    l1=Label(root6,text="USERNAME",bg="light blue")
    l1.place(x=30,y=50)
    e7=tkinter.Entry(root6)
    e7.place(x=100,y=50)
    l2=Label(root6,text="PASSWORD",bg="light blue")
    l2.place(x=30,y=100)
    e8=tkinter.Entry(root6)
    e8.place(x=100,y=100)
    b4=Button(root6,text="SUBMIT",command=lambda:[abc(root6)])
    b4.place(x=70,y=150)
    root6.configure(bg="light blue")
    root6.resizable(True,True)
    root6.mainloop()

# if the login USERNAME IS 'dhakhosp' AND PASSWORD IS '123456' then it shows hospital portal, else show warning message 
def abc(r6):
    global e7,e8
    p5= e7.get()
    p6= e8.get()
    if p5=="dhakhosp" and p6=="123456":
        ins_hosp(r6)
    else:
        tkinter.messagebox.showwarning("INVALID",'INTRUDER !!!!')
        
# IF THE LOGIN DETAILS ARE CORRECT , THEN IT SHOWS HOSPITAL PORTAL        
def ins_hosp(r6):
    funcs(r6)
    root7 = Toplevel()
    root7.geometry("800x650")
       #to center tkinter window
    center_tk_window.center(root7,root7)
    center_tk_window.center_on_parent(root7,root7)
    center_tk_window.center_on_screen(root7)
            ############
    root7.title('Hospital Management - hospital portal')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root7.iconphoto(False,photo)#used for favicon
          # used for adding image
    canvas = Canvas(root7,width = 275,height = 200)
    canvas.place(x=250,y=250)
    img = ImageTk.PhotoImage(Image.open("hmh 1.jpg"))
    canvas.create_image(20,20,anchor = NW,image=img)
             ############
    check = 'hospital'

    img1 = ImageTk.PhotoImage(Image.open("patreg2.png"))
    l1 = Label(root7,text="Patient\nRegistration",font="arial 14 bold",bg = "light blue")
    l1.place(x=80,y=200)

    img2 = ImageTk.PhotoImage(Image.open("docreg.jpg"))
    l2 = Label(root7,text="Doctor\nRegistration",font="arial 14 bold",bg = "light blue")
    l2.place(x=335,y=200)

    img3 = ImageTk.PhotoImage(Image.open("listofdoctors1.jpg"))
    l3 = Label(root7,text="List of\ndoctors",font="arial 14 bold",bg = "light blue")
    l3.place(x=605,y=200)

    img4 = ImageTk.PhotoImage(Image.open("appointments3.png"))
    l4 = Label(root7,text="Appointments",font="arial 14 bold",bg = "light blue")
    l4.place(x=75,y=335)

    img5 = ImageTk.PhotoImage(Image.open("apptable.png"))
    l5 = Label(root7,text="Appointment table",font="arial 14 bold",bg = "light blue")
    l5.place(x=55,y=453)

    img6 = ImageTk.PhotoImage(Image.open("modifypat2.png"))
    l6 = Label(root7,text="Modify\npatient",font="arial 14 bold",bg = "light blue")
    l6.place(x=100,y=571)

    img7 = ImageTk.PhotoImage(Image.open("modifydoc.png"))
    l7 = Label(root7,text="Modify\ndoctor",font="arial 14 bold",bg = "light blue")
    l7.place(x=355,y=571)

    img8 = ImageTk.PhotoImage(Image.open("deldoc.jpg"))
    l8 = Label(root7,text="Delete doctor",font="arial 14 bold",bg = "light blue")
    l8.place(x=585,y=335)#612,571

    img9 = ImageTk.PhotoImage(Image.open("delpat.jpg"))
    l9 = Label(root7,text="Delete patient",font="arial 14 bold",bg = "light blue")
    l9.place(x=585,y=453)#585,453

    img10 = ImageTk.PhotoImage(Image.open("exit5.png"))
    l10 = Label(root7,text="Exit",font="arial 14 bold",bg = "light blue")
    l10.place(x=620,y=571)
    
    label=Label(root7,text="HOSPITAL PORTAL",font="arial 30 bold",bg='white')
    b1=Button(root7,text="PATIENT\nREGISTRATION",font="arial 16 bold",image=img1,relief=RAISED,command = lambda:[pat_reg(root7,check)])
    b2=Button(root7,text="DOCTOR\nREGISTRATION",font="arial 18 bold",image=img2,relief=RAISED,command = lambda:[doc_reg(root7)])
    b3=Button(root7,text="LIST OF\nDOCTORS",font="arial 18 bold",image=img3,relief=RAISED,command = lambda:[lst_doc(root7,check)])
    b4=Button(root7,text="   APPOINTMENT   ",font='arial 18 bold',image=img4,relief=RAISED, command = lambda:[apoint(root7, check)])
    b5=Button(root7,text="APPOINTMENT TABLE",font="arial 18 bold",image=img5,relief=RAISED,command = lambda:[apo_lst(root7)])
    b6=Button(root7,text="MODIFY\nPATIENT",font='arial 18 bold',image=img6,relief=RAISED,command = lambda:[mod_sub_pat(root7,check)])
    b7=Button(root7,text="MODIFY\nDOCTOR",font='arial 18 bold',image=img7,relief=RAISED,command = lambda:[mod_sub_doc(root7)])
    b8=Button(root7,text="DELETE\nDOCTOR",font='arial 18 bold',image=img8,relief=RAISED,command = lambda:[dele_doc_hosp(root7)])
    b9=Button(root7,text="DELETE\nPATIENT",font='arial 18 bold',image=img9,relief=RAISED,command = lambda:[dele_pat(root7)])
    b10=Button(root7,text="EXIT",font='arial 18 bold',image=img10,relief=RAISED,command = lambda:[funcs(root7)])

    label.pack()
    b1.place(x=100,y=120)
    b2.place(x=355,y=120)
    b3.place(x=610,y=120)
    b4.place(x=100,y=262)
    b5.place(x=100,y=380)
    b6.place(x=100,y=498)
    b7.place(x=355,y=498)
    b8.place(x=610,y=262)
    b9.place(x=610,y=380)
    b10.place(x=610,y=498)
    root7.configure(bg="light blue")
    root7.resizable(False,False)
    root7.mainloop()

#REGISTRATION PART OF PATIENT
def pat_reg(rt7,check):
    global a2,a3,a4,a5,a6,a7,a8
    funcs(rt7)
    root8 = Toplevel()
    root8.geometry("600x600")
        #to center tkinter window
    center_tk_window.center(root8,root8)
    center_tk_window.center_on_parent(root8,root8)
    center_tk_window.center_on_screen(root8)
             #########
    root8.title('Hospital Management - patient registration')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root8.iconphoto(False,photo)#used for favicon
    label=Label(root8,text="PATIENT REGISTER",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root8,height=500,width=500,bg="light blue")
    frame.pack()
    l2=Label(root8,text="USERNAME",bg="light blue")
    l2.place(x=10,y=170)
    a2=tkinter.Entry(root8)
    a2.place(x=150,y=170)
    l3=Label(root8,text="PASSWORD",bg="light blue")
    l3.place(x=10,y=210)
    a3=tkinter.Entry(root8)
    a3.place(x=150,y=210)
    l4=Label(root8,text="NAME",bg="light blue")
    l4.place(x=10,y=250)
    a4=tkinter.Entry(root8)
    a4.place(x=150,y=250)
    l5=Label(root8,text="AGE",bg="light blue")
    l5.place(x=10,y=290)
    a5=tkinter.Entry(root8)
    a5.place(x=150,y=290)
    l6=Label(root8,text="GENDER M/F",bg="light blue")
    l6.place(x=10,y=330)
    a6=tkinter.Entry(root8)
    a6.place(x=150,y=330)
    l7=Label(root8,text="PHONE NUMBER",bg="light blue")
    l7.place(x=10,y=370)
    a7=tkinter.Entry(root8)
    a7.place(x=150,y=370)
    l8=Label(root8,text="BLOOD GROUP",bg="light blue")
    l8.place(x=10,y=410)
    a8=tkinter.Entry(root8)
    a8.place(x=150,y=410)
    b1=Button(root8,text="SUBMIT",command = lambda:[entry_pat(root8,check)])
    b1.place(x=250,y=450)
    root8.configure(bg="light blue")
    root8.resizable(False,False)
    root8.mainloop()

#inserting the registration values is sql
def entry_pat(rt8,check):
    global a2,a3,a4,a5,a6,a7,a8
    p2=a2.get()
    p3=a3.get()
    p4=a4.get()
    p5=a5.get()
    p6=a6.get()
    p7=a7.get()
    p8=a8.get()
    cur.execute("SELECT * FROM patientreg WHERE pat_username=(%s)",(p2,))
    data = cur.fetchall()
    if len(data) == 0:
        cur.execute('insert into patientreg values(%s,%s,%s,%s,%s,%s,%s)',(p2,p3,p4,p5,p6,p7,p8,))
        con.commit()
        s=("registration is successfully done")
        tkinter.messagebox.showinfo("PATIENT", s)
        if check == 'patient':
            funcs(rt8)
            patient()
        else:
            ins_hosp(rt8)
    else:
        tkinter.messagebox.showwarning("USERNAME TAKEN","Sorry this username is already taken try a different one")
        pat_reg(rt8,check)

#REGISTRATION PART OF DOCTOR
def doc_reg(rt7):
    global x2,x3,x4,x5,x6,x7,x8
    funcs(rt7)
    root9= Toplevel()
    root9.geometry("600x600")
      #to center tkinter window
    center_tk_window.center(root9,root9)
    center_tk_window.center_on_parent(root9,root9)
    center_tk_window.center_on_screen(root9)
            ###########
    root9.title('Hospital Management - doctor registration')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root9.iconphoto(False,photo)#used for favicon
    label=Label(root9,text="DOCTOR REGISTER",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root9,height=500,width=500,bg="light blue")
    frame.pack()
    l2=Label(root9,text="NAME",bg="light blue")
    l2.place(x=10,y=170)
    x2=tkinter.Entry(root9)
    x2.place(x=150,y=170)
    l3=Label(root9,text="USERNAME",bg="light blue")
    l3.place(x=10,y=210)
    x3=tkinter.Entry(root9)
    x3.place(x=150,y=210)
    l4=Label(root9,text="PASSWORD",bg="light blue")
    l4.place(x=10,y=250)
    x4=tkinter.Entry(root9)
    x4.place(x=150,y=250)
    l5=Label(root9,text="GENDER M/F",bg="light blue")
    l5.place(x=10,y=290)
    x5=tkinter.Entry(root9)
    x5.place(x=150,y=290)
    l6=Label(root9,text="PHONE NUMBER",bg="light blue")
    l6.place(x=10,y=330)
    x6=tkinter.Entry(root9)
    x6.place(x=150,y=330)
    l7=Label(root9,text="AGE",bg="light blue")
    l7.place(x=10,y=370)
    x7=tkinter.Entry(root9)
    x7.place(x=150,y=370)
    l8=Label(root9,text="SPECIALISATION",bg="light blue")
    l8.place(x=10,y=410)
    x8=tkinter.Entry(root9)
    x8.place(x=150,y=410)
    b1=Button(root9,text="SUBMIT",command = lambda:[entry_doc(root9)])
    b1.place(x=250,y=450)
    root9.configure(bg="light blue")
    root9.resizable(False,False)
    root9.mainloop()

#inserting the registration values is sql 
def entry_doc(rt9):
    global x2,x3,x4,x5,x6,x7,x8
    p2=x2.get()
    p3=x3.get()
    p4=x7.get()
    p5=x5.get()
    p6=x6.get()
    p7=x4.get()
    p8=x8.get()
    cur.execute("SELECT * FROM docreg WHERE username=(%s)",(p3,))
    data = cur.fetchall()
    if len(data) == 0:
        cur.execute('insert into docreg values(%s,%s,%s,%s,%s,%s,%s)',(p2,p3,p4,p5,p6,p7,p8,))
        con.commit()
        s=("registration is successfully done")
        tkinter.messagebox.showinfo("DOCTOR",s)
        ins_hosp(rt9)
    else:
        tkinter.messagebox.showwarning("USERNAME TAKEN","Sorry this username is already taken try a different one")
        doc_reg(rt9)

#LIST OF DOCTORS AND THEIR SPECIALIZATION
def lst_doc(rt7,check):
    funcs(rt7)
    root10 = Toplevel()
    root10.geometry("600x600")
       #to center tkinter window
    center_tk_window.center(root10,root10)
    center_tk_window.center_on_parent(root10,root10)
    center_tk_window.center_on_screen(root10)
            #############
    root10.title('Hospital Management - list of doctors')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root10.iconphoto(False,photo)#used for favicon
    label = Label(root10,text="LIST OF DOCTORS AND THEIR SPECIALISATION",font="arial 20 bold",bg="light blue")
    cur.execute("SELECT * FROM docreg")
    data = cur.fetchall()
    lst_name = []
    lst_spec = []
    for i in range(len(data)):
        data[i] = list(data[i])
    frame = Frame(root10,height=500,width=500,bg="light blue")
    frame.pack()
    l = Label(root10,text = 'Doctor name',font='arial 18 bold',bg="light blue")
    l.place(x = 50,y = 50)
    l0 = Label(root10,text = 'Specalization',font='arial 18 bold',bg="light blue")
    l0.place(x = 250,y = 50)
    y_cor = 100
    ycord = lst_dis(data, y_cor, root10)
    if check == 'patient':
        b = Button(root10, text="Close", command = lambda:[funcs(root10),pat_ins()])
        b.place(x = 150, y = ycord)
    else:
        b = Button(root10, text="Close", command = lambda:[ins_hosp(root10)])
        b.place(x = 150, y = ycord)
    root10.configure(bg="light blue")
    root10.resizable(True,True)
    root10.mainloop()

# append the list of doctor tkinter window as per sql
def lst_dis(lst, y_cor, r10):
    if len(lst) == 0:
        return y_cor
    else:
        sublst = lst[0]
        l1 = Label(r10,text = sublst[0],bg="light blue")
        l2 = Label(r10,text = sublst[6],bg="light blue")
        l1.place(x = 50,y = y_cor)
        l2.place(x = 250,y = y_cor)
        list_name = []
        list_spec = []
        y_cor += 40
        list1 = []
        for i in range(len(lst)):
            if i > 0:
                list1.append(lst[i])
        y_cor = lst_dis(list1, y_cor, r10)
        return y_cor

# getting username and password so that they can modify
def mod_sub_doc(rt7):
    global e9,e10
    funcs(rt7)
    root12 = Toplevel()
    root12.geometry("400x400")
      #to center tkinter window
    center_tk_window.center(root12,root12)
    center_tk_window.center_on_parent(root12,root12)
    center_tk_window.center_on_screen(root12)
           ##############
    root12.title('Hospital Management - modify doctor details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root12.iconphoto(False,photo)#used for favicon
    label=Label(root12,text="MODIFICATION",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root12,height=300,width=300,bg="light blue")
    frame.pack()
    l1=Label(root12,text="USER NAME",bg="light blue")
    l1.place(x=10,y=130)
    e9=tkinter.Entry(root12)
    e9.place(x=100,y=130)
    l2=Label(root12,text="PASSWORD",bg="light blue")
    l2.place(x=10,y=150)
    e10=tkinter.Entry(root12)
    e10.place(x=100,y=150)
    b1=Button(root12,text='Submit',command=lambda:[modify_doc(root12)])
    b1.place(x=100,y=190)
    root12.configure(bg="light blue")
    root12.resizable(True,True)
    root12.mainloop()

#asking what details to be modified
def modify_doc(rt12):
    global e9,e10,e11
    p1=e9.get()
    p2=e10.get()
    funcs(rt12)
    cur.execute('select * from docreg where username=(%s)',(p1,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH DOCTOR FOUND")
    else:
        dat = list(dat[0])
        pass1 = dat[5]
        if pass1 == p2:
            root13 = Toplevel()
            root13.geometry("500x500")
                 #to center tkinter window
            center_tk_window.center(root13,root13)
            center_tk_window.center_on_parent(root13,root13)
            center_tk_window.center_on_screen(root13)
                   #############
            root13.title('Hospital Management - modify doctor details')#used for change of title
            photo = PhotoImage(file ="hospital favicon.png")#used for favicon
            root13.iconphoto(False,photo)#used for favicon
            label=Label(root13,text="MODIFY",font="arial 25 bold",bg="light blue")
            label.pack()
            frame=Frame(root13,height=500,width=500,bg="light blue")
            frame.pack()
            l1=Label(root13,text="Choose number to modify: 1.Name \n 2.Username \n 3.Password \n 4.Age \n 5.Gender \n 6.Phone \n 7.Specialization ",bg="light blue")
            l1.place(x=10,y=130)
            e11=tkinter.Entry(root13)
            e11.place(x=220,y=170)
            b1=Button(root13,text="Submit",command=lambda:[mod_all_doc(root13,p1)])
            b1.place(x=250,y=210)
            root13.configure(bg="light blue")
            root13.resizable(True,True)
            root13.mainloop()
        else:
            tkinter.messagebox.showwarning("ERROR","NO DATA FOUND")

#asking the new detail that has to be modified
def mod_all_doc(rt13,p1):
    global e11
    x=e11.get()
    x = int(x)
    funcs(rt13)
    if x == 1:
        beta = "New name"
    elif x == 2:
        beta = "New username"
    elif x == 3:
        beta = "New password"
    elif x == 4:
        beta = "New age"
    elif x == 5:
        beta = "New gender"
    elif x==6:
        beta= "New phone no"
    elif x==7:
        beta= "Update specialisation"
    root14 = Toplevel()
    root14.geometry("400x400")
          #to center tkinter window
    center_tk_window.center(root14,root14)
    center_tk_window.center_on_parent(root14,root14)
    center_tk_window.center_on_screen(root14)
               ############
    root14.title('Hospital Management - modify doctor details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root14.iconphoto(False,photo)#used for favicon
    label=Label(root14,text="MODIFY",font="arial 25 bold",bg="light blue")
    label.pack()
    frame=Frame(root14,height=300,width=300,bg="light blue")
    frame.pack()
    l1=Label(root14,text = beta,bg="light blue")
    l1.place(x=10,y=120)
    e1=tkinter.Entry(root14)
    e1.place(x=100,y=120)
    b1=Button(root14,text="Submit",command=lambda:[upd_sql_doc(x,e1,p1,root14)])
    b1.place(x=75,y=180)
    root14.configure(bg="light blue")
    root14.resizable(False,False)
    root14.mainloop()

# modifying doctor (sql part)
def upd_sql_doc(num,e1,p1,rt14):
    q1 = e1.get()
    if num == 1:
        col = "name"
    elif num == 2:
        col = "username"
    elif num == 3:
        col = "password"
    elif num == 4:
        col = "age"
    elif num == 5:
        col = "gender"
    elif num==6:
        col = "phone"
    elif num==7:
        col= "specialisation"
    querry = "UPDATE docreg SET "+col+" = '"+q1+"' WHERE username = '"+p1+"'"
    cur.execute(querry)
    con.commit()
    tkinter.messagebox.showinfo("SUCCESS","MODIFIED")
    ins_hosp(rt14)
 
# getting username and password so that they can modify
def mod_sub_pat(rt7,check):
    global e9,e10
    funcs(rt7)
    root15 = Toplevel()
    root15.geometry("300x300")
     #to center tkinter window
    center_tk_window.center(root15,root15)
    center_tk_window.center_on_parent(root15,root15)
    center_tk_window.center_on_screen(root15)
            ########
    root15.title('Hospital Management - modify patient details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root15.iconphoto(False,photo)#used for favicon
    label=Label(root15,text="MODIFICATION",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root15,height=300,width=300,bg="light blue")
    frame.pack()
    l1=Label(root15,text="USER NAME",bg="light blue")
    l1.place(x=10,y=130)
    e9=tkinter.Entry(root15)
    e9.place(x=100,y=130)
    l2=Label(root15,text="PASSWORD",bg="light blue")
    l2.place(x=10,y=150)
    e10=tkinter.Entry(root15)
    e10.place(x=100,y=150)
    b1=Button(root15,text='Submit',command=lambda:[modify_pat(root15,check)])
    b1.place(x=100,y=190)
    root15.configure(bg="light blue")
    root15.resizable(True,True)
    root15.mainloop()

#asking what details to be modified
def modify_pat(rt15,check):
    global e9,e10,e11
    p1=e9.get()
    p2=e10.get()
    funcs(rt15)
    cur.execute('select * from patientreg where pat_username=(%s)',(p1,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH PATIENT FOUND")
    else:
        dat = list(dat[0])
        pass1 = dat[1]
        if pass1 == p2:
            root16 = Toplevel()
            root16.geometry("500x500")
               #to center tkinter window
            center_tk_window.center(root16,root16)
            center_tk_window.center_on_parent(root16,root16)
            center_tk_window.center_on_screen(root16)
                 #############
            root16.title('Hospital Management - modify patient details')#used for change of title
            photo = PhotoImage(file ="hospital favicon.png")#used for favicon
            root16.iconphoto(False,photo)#used for favicon
            label=Label(root16,text="MODIFY",font="arial 25 bold",bg="light blue")
            label.pack()
            frame=Frame(root16,height=500,width=500,bg="light blue")
            frame.pack()
            l1=Label(root16,text="Choose number to modify: 1.Name \n 2.Username \n 3.Password \n 4.Age \n 5.Gender \n 6.Phone \n 7.Blood Group ",bg="light blue")
            l1.place(x=10,y=130)
            e11=tkinter.Entry(root16)
            e11.place(x=220,y=170)
            b1=Button(root16,text="Submit",command=lambda:[mod_all_pat(root16,p1,check)])
            b1.place(x=250,y=210)
            root16.configure(bg="light blue")
            root16.resizable(True,True)
            root16.mainloop()
        else:
            tkinter.messagebox.showwarning("ERROR","NO DATA FOUND")

#asking the new detail that has to be modified
def mod_all_pat(rt16,p1,check):
    global e11
    x = e11.get()
    x = int(x)
    funcs(rt16)
    if x == 1:
        beta = "New name"
    elif x == 2:
        beta = "New username"
    elif x == 3:
        beta = "New password"
    elif x == 4:
        beta = "New age"
    elif x == 5:
        beta = "New gender"
    elif x==6:
        beta = "New phone no"
    elif x==7:
        beta = "New blood group"
    root17 = Toplevel()
    root17.geometry("400x400")
         #to center tkinter window
    center_tk_window.center(root17,root17)
    center_tk_window.center_on_parent(root17,root17)
    center_tk_window.center_on_screen(root17)
         ###############
    root17.title('Hospital Management - modify patient details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root17.iconphoto(False,photo)#used for favicon
    label=Label(root17,text="MODIFY",font="arial 25 bold",bg="light blue")
    label.pack()
    frame=Frame(root17,height=300,width=300,bg="light blue")
    frame.pack()
    l1=Label(root17,text = beta,bg="light blue")
    l1.place(x=10,y=120)
    e1=tkinter.Entry(root17)
    e1.place(x=140,y=120)
    b1=Button(root17,text="Submit",command=lambda:[upd_sql_pat(x,e1,p1,root17,check)])
    b1.place(x=75,y=180)
    root17.configure(bg="light blue")
    root17.resizable(True,True)
    root17.mainloop()

# modifying patient (sql part)
def upd_sql_pat(num,e1,p1,rt17,check):
    q1 = e1.get()
    if num == 1:
        col1 = "name"
        col2= "patient_name"
        querry1 = "UPDATE patientreg SET "+col1+" = '"+q1+"' WHERE pat_username = '"+p1+"'"
        cur.execute(querry1)
        con.commit()
        querry2 = "UPDATE apt SET "+col2+" = '"+q1+"' WHERE patient_username = '"+p1+"'"
        cur.execute(querry2)
        con.commit()
    elif num == 2:
        col1 = "pat_username"
        col2 = "patient_username"
        querry1 = "UPDATE patientreg SET "+col1+" = '"+q1+"' WHERE pat_username = '"+p1+"'"
        cur.execute(querry1)
        con.commit()
        querry2 = "UPDATE apt SET "+col2+" = '"+q1+"' WHERE patient_username = '"+p1+"'"
        cur.execute(querry2)
        con.commit()
    elif num == 3:
        col = "pat_password"
        querry = "UPDATE patientreg SET "+col+" = '"+q1+"' WHERE pat_username = '"+p1+"'"
        cur.execute(querry)
        con.commit()
    elif num == 4:
        col1 = "age"
        col2 = "patient_age"
        querry1 = "UPDATE patientreg SET "+col1+" = '"+q1+"' WHERE pat_username = '"+p1+"'"
        cur.execute(querry1)
        con.commit()
        querry2 = "UPDATE apt SET "+col2+" = '"+q1+"' WHERE patient_username = '"+p1+"'"
        cur.execute(querry2)
        con.commit()
    elif num == 5:
        col1 = "gender"
        col2 = "patient_gender"
        querry1 = "UPDATE patientreg SET "+col1+" = '"+q1+"' WHERE pat_username = '"+p1+"'"
        cur.execute(querry1)
        con.commit()
        querry2 = "UPDATE apt SET "+col2+" = '"+q1+"' WHERE patient_username = '"+p1+"'"
        cur.execute(querry2)
        con.commit()
    elif num == 6:
        col = "phone"
        querry = "UPDATE patientreg SET "+col+" = '"+q1+"' WHERE pat_username = '"+p1+"'"
        cur.execute(querry)
        con.commit()
    elif num == 7:
        col = "bg"
        querry = "UPDATE patientreg SET "+col+" = '"+q1+"' WHERE pat_username = '"+p1+"'"
        cur.execute(querry)
        con.commit()
    tkinter.messagebox.showinfo("SUCCESS","MODIFIED")
    if check == 'patient':
        funcs(rt17)
        pat_ins()
    else:
        ins_hosp(rt17)

#getting doctor username to delete 
def dele_doc_hosp(rt7):
    global x9
    funcs(rt7)
    root13 = Toplevel()
    root13.geometry("600x300")
     #to center tkinter window
    center_tk_window.center(root13,root13)
    center_tk_window.center_on_parent(root13,root13)
    center_tk_window.center_on_screen(root13)
           #############
    root13.title('Hospital Management - delete doctor information')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root13.iconphoto(False,photo)#used for favicon
    label=Label(root13,text="Delete",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root13,height=200,width=500,bg="light blue")
    frame.pack()
    l1=Label(root13,text="DOCTOR USERNAME",bg="light blue")
    l1.place(x=50,y=130)
    x9=tkinter.Entry(root13)
    x9.place(x=250,y=130)
    b1=Button(root13,text='Submit',command=lambda:[delete_doc_hosp(root13)])
    b1.place(x=200,y=160)
    root13.configure(bg="light blue")
    root13.resizable(True,True)
    root13.mainloop()

#deleting doctor part
def delete_doc_hosp(rt13):
    global x9
    p5 = x9.get()
    cur.execute('select * from docreg where username=(%s)',(p5,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH DOCTOR FOUND")
    else:
        cur.execute("Delete from docreg where username = (%s)",(p5,))
        tkinter.messagebox.showwarning("DELETED SUCCESFULLY",'DELETED')
        con.commit()
    ins_hosp(rt13)

# getting username of the patient to delete 
def dele_pat(rt7):
    global x10
    funcs(rt7)
    root14 = Toplevel()
    root14.geometry("600x300")
      #to center tkinter window
    center_tk_window.center(root14,root14)
    center_tk_window.center_on_parent(root14,root14)
    center_tk_window.center_on_screen(root14)
        ###############
    root14.title('Hospital Management - delete patient')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root14.iconphoto(False,photo)#used for favicon
    label=Label(root14,text="Delete",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root14,height=200,width=500,bg="light blue")
    frame.pack()
    l1=Label(root14,text="PATIENT USERNAME",bg="light blue")
    l1.place(x=50,y=130)
    x10=tkinter.Entry(root14)
    x10.place(x=250,y=130)
    b1=Button(root14,text='Submit',command=lambda:[delete_pat(root14)])
    b1.place(x=200,y=160)
    root14.configure(bg="light blue")
    root14.resizable(True,True)
    root14.mainloop()

#deleting patient part
def delete_pat(rt14):
    global x10
    p6 = x10.get() 
    cur.execute('select * from patientreg where pat_username=(%s)',(p6,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH PATIENT FOUND")
    else:
        cur.execute("Delete from patientreg where pat_username = (%s)",(p6,))
        con.commit()
        cur.execute("delete from apt where patient_username = (%s)",(p6,))
        con.commit()
        tkinter.messagebox.showwarning("DELETED SUCCESFULLY",'DELETED')
    ins_hosp(rt14)

#getting patient username
def apoint(rt7,check):
    global x11
    funcs(rt7)
    root15 = Toplevel()
    root15.geometry("600x300")
           #to center tkinter window
    center_tk_window.center(root15,root15)
    center_tk_window.center_on_parent(root15,root15)
    center_tk_window.center_on_screen(root15)
           ###################
    root15.title('Hospital Management - appointment')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root15.iconphoto(False,photo)#used for favicon
    label=Label(root15,text="APPOINTMENT",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root15,height=200,width=500,bg="light blue")
    frame.pack()
    l1=Label(root15,text="PATIENT USERNAME",bg="light blue")
    l1.place(x=50,y=130)
    x11=tkinter.Entry(root15)
    x11.place(x=250,y=130)
    b1=Button(root15,text='Submit',command=lambda:[get_apoint(root15,check)])
    b1.place(x=200,y=160)
    root15.configure(bg="light blue")
    root15.resizable(True,True)
    root15.mainloop()    

#patient should enter their problem
#For appointment
def get_apoint(r15,check):
    global x11,x12, prob
    user=x11.get()
    funcs(r15)
    cur.execute('select * from patientreg where pat_username=(%s)',(user,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH PATIENT FOUND")
    else:
        a=[]
        a = list(dat[0])
        cur.execute('select * from docreg group by specialisation')
        info = cur.fetchall()
        spec_avail = []
        for i in range(len(info)):
            info[i] = list(info[i])
            spec_avail.append(info[i][6])
        if len(a)==0:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND !!")
        else:
            root16 = Toplevel()
            root16.geometry("600x500")
                  #to center tkinter window
            center_tk_window.center(root16,root16)
            center_tk_window.center_on_parent(root16,root16)
            center_tk_window.center_on_screen(root16)
                     ##############
            root16.title('Hospital Management - appointment portal')#used for change of title
            photo = PhotoImage(file ="hospital favicon.png")#used for favicon
            root16.iconphoto(False,photo)#used for favicon
            label=Label(root16,text="APPOINTMENT",font='arial 25 bold')
            label.pack()
            frame=Frame(root16,height=400,width=500,bg="light blue")
            frame.pack()
            if a[4]=='M' or a[4]=='m':
                    x="Mr."
                    k = x + a[2]
            else:
                    x="Mrs\Ms."
                    k = x + a[2]
            name=Label(root16,text='WELCOME',bg="light blue")
            name.place(x=50,y=80)
            name1=Label(root16,text=k,bg="light blue")
            name1.place(x=150,y=80)
            age=Label(root16,text='AGE:-',bg="light blue")
            age.place(x=50,y=100)
            age1=Label(root16,text=a[3],bg="light blue")
            age1.place(x=150,y=100)
            phone=Label(root16,text='PHONE:-',bg="light blue")
            phone.place(x=50,y=120)
            phone1=Label(root16,text=a[5],bg="light blue")
            phone1.place(x=150,y=120)
            bg=Label(root16,text='BLOOD GROUP:-',bg="light blue")
            bg.place(x=50,y=140)
            bg1=Label(root16,text=a[6],bg="light blue")
            bg1.place(x=150,y=140)
            L7=Label(root16,text='Select the specialisation\nrequired',bg="light blue")
            L7.place(x=50,y=160)
            x12 = StringVar(root16)
            x12.set("Specialisations")
            specs = OptionMenu(root16, x12, *spec_avail)
            specs.place(x=250,y=160)
            L8=Label(root16,text='Enter the problems facing',bg="light blue")
            L8.place(x=50,y=200)
            prob=tkinter.Entry(root16)
            prob.place(x=250,y=200)
            B1=Button(root16,text='Submit',command=lambda:[apo_details(user,root16,check)])
            B1.place(x=200,y=300)
            root16.configure(bg="light blue")
            root16.resizable(True,True)
            root16.mainloop()

#getting the doctor name from patient(the doctor who have have the same specialisation)
def apo_details(user,r16,check):
    global x12,x13, prob
    p1=x12.get()
    prob1 = prob.get()
    funcs(r16)
    cur.execute('select * from docreg where specialisation=(%s)',(p1,))
    dat=cur.fetchall()
    doc_names = []
    for i in range(len(dat)):
        dat[i] = list(dat[i])
        doc_names.append(dat[i][0])
    if len(dat)==0:
        tkinter.messagebox.showwarning("APPOINTMENT","NO DOCTOR IS AVAILABLE WITH THAT SPECIALISATION")
    else:
        root17 = Toplevel()
        root17.geometry("300x300")
          #to center tkinter window
        center_tk_window.center(root17,root17)
        center_tk_window.center_on_parent(root17,root17)
        center_tk_window.center_on_screen(root17)
           ##################
        root17.title('Hospital Management - appointment details')#used for change of title
        photo = PhotoImage(file ="hospital favicon.png")#used for favicon
        root17.iconphoto(False,photo)#used for favicon
        label=Label(root17,text="Appointment",font='arial 25 bold',bg="light blue")
        label.pack()
        frame=Frame(root17,height=200,width=200,bg="light blue")
        frame.pack()
        name=Label(root17,text='DOCTOR NAMES',bg="light blue")
        name.place(x=75,y=50)
        x13 = StringVar(root17)
        x13.set("Doctors")
        docnames = OptionMenu(root17, x13, *doc_names)
        docnames.place(x=75, y=100)
        b1=Button(root17,text='OK',command=lambda:[apo_ins(user,prob1,root17,check)])#lambda funcs
        b1.place(x=75,y=150)
        root17.configure(bg="light blue")
        root17.resizable(True,True)
        root17.mainloop()

#getting the date and time values for the appointment
def apo_ins(user,prob,r17,check):
    global x13, date1, time1
    doc = x13.get()
    funcs(r17)
    root18= Toplevel()
    root18.geometry("600x300")
      #to center tkinter window
    center_tk_window.center(root18,root18)
    center_tk_window.center_on_parent(root18,root18)
    center_tk_window.center_on_screen(root18)
            ##########
    root18.title('Hospital Management - appointment date and time')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root18.iconphoto(False,photo)#used for favicon
    label = Label(root18, text = "Timing", font = "arial 25 bold",bg="light blue")
    label.pack()
    frame = Frame(root18, height = 200, width = 500,bg="light blue")
    frame.pack()
    l3 = Label(root18,text= "THE HOSPITAL FUNCTIONS FROM 7 AM TO 11 PM",bg="light blue")
    l3.place( x=50, y= 50)
    l1 = Label(root18, text = "Date YYYY/MM/DD",bg="light blue")
    l1.place(x = 50, y = 70)
    date1=tkinter.Entry(root18)
    date1.place (x=170,y=70)
    l2 = Label(root18, text = "Time \n 24-hr format",bg="light blue")
    l2.place(x = 50, y = 100)
    time1= StringVar(root18)
    time1.set("time slot")
    w= OptionMenu(root18,time1,"7:00","7:30","8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00")
    w.place(x=150,y=105)
    b1 = Button(root18, text = "OK", command = lambda:[apo_sql(user,prob,doc,root18,check)])
    b1.place(x = 250, y = 180)
    root18.configure(bg="light blue")
    root18.resizable(True,True)
    root18.mainloop()
    
    
# APPOINTMENT PART where the values are getting updated in sql
def apo_sql(user,prob,doc,r18,check):
    global date1, time1
    date = date1.get()
    time = time1.get()
    cur.execute('select * from apt')
    row = cur.execute("select * from apt order by pat_app_no")
    row=cur.fetchall()
    if len(row)==0:
        p1=1
    else:
        for i in range (len(row)):
            j=list(row[i])
            k=j[0]
            l=int(k)
            p1=l+1
    cur.execute("SELECT * FROM patientreg WHERE pat_username = (%s)",(user,))
    data = cur.fetchall()
    data = list(data[0])
    pat_name = data[2]
    pat_age = data[3]
    pat_gen = data[4]
    pat_prob = prob
    app_date = date
    app_time = time
    sug = ''
    cur.execute("INSERT INTO apt VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(p1,user,pat_name,doc,pat_age,pat_gen,app_date,app_time,prob,sug,))
    con.commit()
    message = "APPOINTMENT FIXED\nYour apointment number is " + str(p1)
    tkinter.messagebox.showwarning("APPOINTMENT",message)
    if check == 'patient':
        #pat_ins()
        funcs(r18)
        pat_ins()
    else:
        ins_hosp(r18)

#appointment table
def apo_lst(rt7):
    funcs(rt7)
    root10 = Toplevel()
    root10.geometry("1100x600")
     #to center tkinter window
    center_tk_window.center(root10,root10)
    center_tk_window.center_on_parent(root10,root10)
    center_tk_window.center_on_screen(root10)
          ###########
    root10.title('Hospital Management - appointment list')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root10.iconphoto(False,photo)#used for favicon
    label = Label(root10,text="APPOINTMENT TABLE",font="arial 20 bold",bg="light blue")
    cur.execute("SELECT * FROM apt ORDER BY app_date, app_time")
    data = cur.fetchall()
    for i in range(len(data)):
        data[i] = list(data[i])
    frame = Frame(root10,height=500,width=1000,bg="light blue")
    frame.pack()
    apt_no = Label(root10,text = 'Appointment\nNumber',font='arial 14 bold',bg="light blue")
    apt_no.place(x = 50,y = 20)
    apt_user = Label(root10,text = 'Username',font='arial 14 bold',bg="light blue")
    apt_user.place(x = 200,y = 20)
    pat_name = Label(root10,text = 'Patient\nName',font='arial 14 bold',bg="light blue")
    pat_name.place(x = 300,y = 20)
    doc_name = Label(root10,text = 'Doctor\nName',font='arial 14 bold',bg="light blue")
    doc_name.place(x = 400,y = 20)
    pat_age = Label(root10,text = 'Patient\nAge',font='arial 14 bold',bg="light blue")
    pat_age.place(x = 500,y = 20)
    pat_gen = Label(root10,text = 'Patient\nGender',font='arial 14 bold',bg="light blue")
    pat_gen.place(x = 600,y = 20)
    pat_prob = Label(root10,text = 'Date',font='arial 14 bold',bg="light blue")
    pat_prob.place(x = 700,y = 20)
    sug = Label(root10,text = 'Time',font='arial 14 bold',bg="light blue")
    sug.place(x = 800,y = 20)
    y_cor = 100
    for sublst in data:
        l1 = Label(root10,text = sublst[0],bg="light blue")
        l2 = Label(root10,text = sublst[1],bg="light blue")
        l3 = Label(root10,text = sublst[2],bg="light blue")
        l4 = Label(root10,text = sublst[3],bg="light blue")
        l5 = Label(root10,text = sublst[4],bg="light blue")
        l6 = Label(root10,text = sublst[5],bg="light blue")
        l7 = Label(root10,text = sublst[6],bg="light blue")
        l8 = Label(root10,text = sublst[7],bg="light blue")
        l1.place(x = 60,y = y_cor)
        l2.place(x = 210,y = y_cor)
        l3.place(x = 310,y = y_cor)
        l4.place(x = 410,y = y_cor)
        l5.place(x = 510,y = y_cor)
        l6.place(x = 610,y = y_cor)
        l7.place(x = 710,y = y_cor)
        l8.place(x = 810,y = y_cor)
        y_cor += 20
    b = Button(root10, text="Close", command = lambda:[ins_hosp(root10)])
    b.place(x=500,y=470)
    root10.configure(bg="light blue")
    root10.resizable(True,True)
    root10.mainloop()

                                                                    ###################
    
                                                                    ######PATIENT######
    
 # this is the starting of the patient tkinter window 
def patient():
    root18 = Toplevel()
    root18.geometry("500x650")
       #to center tkinter window
    center_tk_window.center(root18,root18)
    center_tk_window.center_on_parent(root18,root18)
    center_tk_window.center_on_screen(root18)
          #################
    root18.title('Hospital Management - patient portal')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root18.iconphoto(False,photo)#used for favicon
        # used for adding image
    canvas = Canvas(root18,width = 300,height = 150)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("hmp1.png"))
    canvas.create_image(70,10,anchor = NW,image=img)
            ##############
    check = 'patient'

    img1 = ImageTk.PhotoImage(Image.open("patregi.png"))
    l1 = Label(root18,text="Registration",font="arial 14 bold",bg = "light blue")
    l1.place(x=75,y=320)

    img2 = ImageTk.PhotoImage(Image.open("patientlogin.png"))
    l2 = Label(root18,text="Login",font="arial 14 bold",bg = "light blue")
    l2.place(x=320,y=320)

    img3 = ImageTk.PhotoImage(Image.open("seravail.jpg"))
    l3 = Label(root18,text="Services Available",font="arial 14 bold",bg = "light blue")
    l3.place(x=50,y=470)

    img4 = ImageTk.PhotoImage(Image.open("exit1.jpg"))
    l4 = Label(root18,text="Modify appointment\ndetail",font="arial 14 bold",bg = "light blue")
    l4.place(x=260,y=470)

    img5 = ImageTk.PhotoImage(Image.open("modifyapt.png"))
    l5 = Label(root18,text="Exit",font="arial 14 bold",bg = "light blue")
    l5.place(x=320,y=621)

    img6 = ImageTk.PhotoImage(Image.open("delapt.png"))
    l6 = Label(root18,text="Delete appointment",font="arial 14 bold",bg = "light blue")
    l6.place(x=50,y=621)
    
    label=Label(root18,text="PATIENT PORTAL",font="arial 30 bold",bg='white')
    b1=Button(root18,text="Registration",font="arial 20 bold",image = img1,relief = RAISED,command = lambda:[pat_reg(root18,check)])
    b2=Button(root18,text="Login",font="arial 20 bold",image=img2,relief = RAISED,command = lambda:[pat_login(root18)])
    b3=Button(root18,text="Services available",font="arial 20 bold",image=img3,relief = RAISED,command = lambda:[ser_avail(root18)])
    b4 = Button(root18,text="Modify appointment\ndetail",font="arial 20 bold",image=img5,relief= RAISED,command=lambda:[mod_sub_apt(root18)])
    b5=Button(root18,text="Exit",font='arial 20 bold',image=img4,relief = RAISED,command=lambda:[funcs(root18)])
    b6=Button(root18,text="Delete\nappointment",relief = RAISED,image=img6,font="arial 14 bold",command=lambda:[delete_apt(root18)])
    label.pack()
    b1.place(x=80,y=230)
    b2.place(x=300,y=230)
    b3.place(x=80,y=380)
    b4.place(x=300,y=380)
    b5.place(x=300,y=530)
    b6.place(x=80,y=530)
    root18.configure(bg="light blue")
    root18.resizable(False,False)
    root18.mainloop()

# this is the services available part
def ser_avail(rt18):
    funcs(rt18)
    root19 = Toplevel()
    root19.geometry("600x600")
      #to center tkinter window
    center_tk_window.center(root19,root19)
    center_tk_window.center_on_parent(root19,root19)
    center_tk_window.center_on_screen(root19)
           ############
    root19.title('Hospital Management - services available')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root19.iconphoto(False,photo)#used for favicon
    frame=Frame(root19,height=500,width=500,bg="light blue")
    frame.pack()
    l1=Label(root19,text='SERVICES AVAILABLE',bg="light blue")
    l1.place(x=20,y=10)
    f=["X-Ray","MRI","CT Scan","Endoscopy","Dialysis","Ultrasound","EEG","ENMG","ECG"]
    count1=20
    for i in f:
       count1=count1+20
       l3=Label(root19,text=i,bg="light blue")
       l3.place(x=20,y=count1)
    l2=Label(root19,text='ROOM NO.',bg="light blue")
    l2.place(x=140,y=10)
    g=[101,102,103,104,105,301,302,303,304]
    count2=20
    for i in g:
       count2=count2+20
       l4=Label(root19,text=i,bg="light blue")
       l4.place(x=140,y=count2)
    count2 += 40
    l5=Label(root19,text='for further information contact 9087665123',bg="light blue")
    l5.place(x=20,y=count2)
    count2 += 40
    b = Button(root19, text="Close", command = lambda:[funcs(root19),patient()])
    b.place(x = 150, y = count2)
    root19.configure(bg="light blue")
    root19.resizable(True,True)
    root19.mainloop()
    
#getting patient username and password to modify
def mod_sub_apt(rt18):
    global w1,w2
    funcs(rt18)
    app1 = Toplevel()
    app1.geometry("400x400")
      #to center tkinter window
    center_tk_window.center(app1,app1)
    center_tk_window.center_on_parent(app1,app1)
    center_tk_window.center_on_screen(app1)
        ##################
    app1.title('Hospital Management - modify apointment details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    app1.iconphoto(False,photo)#used for favicon
    label=Label(app1,text="MODIFY APPOINTMENT\nDETAILS",font='arial 20 bold',bg="light blue")
    label.pack()
    frame=Frame(app1,height=300,width=300,bg="light blue")
    frame.pack()
    l1=Label(app1,text="USER NAME",bg="light blue")
    l1.place(x=10,y=130)
    w1=tkinter.Entry(app1)
    w1.place(x=100,y=130)
    l2=Label(app1,text="PASSWORD",bg="light blue")
    l2.place(x=10,y=150)
    w2=tkinter.Entry(app1)
    w2.place(x=100,y=150)
    b1=Button(app1,text='Submit',command=lambda:[apt_no(app1)])
    b1.place(x=100,y=190)
    app1.configure(bg="light blue")
    app1.resizable(True,True)
    app1.mainloop()

#checking whether the username and password are crct after that getting the appointment number which the patient wants to modify
def apt_no(app1):
    global w1,w2,w3
    p1=w1.get()
    p2=w2.get()
    funcs(app1)
    cur.execute('select * from patientreg where pat_username=(%s)',(p1,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH PATIENT FOUND")
    else:
        dat = list(dat[0])
        pass1 = dat[1]
        if pass1 == p2:
            app2 = Toplevel()
            app2.geometry("400x300")
               #to center tkinter window
            center_tk_window.center(app2,app2)
            center_tk_window.center_on_parent(app2,app2)
            center_tk_window.center_on_screen(app2)
                  ###############
            app2.title('Hospital Management - modify appointment details')#used for change of title
            photo = PhotoImage(file ="hospital favicon.png")#used for favicon
            app2.iconphoto(False,photo)#used for favicon
            label=Label(app2,text="MODIFY",font="arial 25 bold",bg="light blue")
            label.pack()
            frame=Frame(app2,height=200,width=300,bg="light blue")
            frame.pack()
            l1=Label(app2,text="Enter appointment\nnumber",bg="light blue")
            l1.place(x=10,y=130)
            w3=tkinter.Entry(app2)
            w3.place(x=120,y=130)
            b1=Button(app2,text='Submit',command=lambda:[modify_apt(app2)])
            b1.place(x=100,y=190)
            app2.configure(bg="light blue")
            app2.resizable(False,False)
            app2.mainloop()

#details that the patient wants to modify
def modify_apt(app2):
    global w3,w4
    p3=w3.get()
    funcs(app2)
    cur.execute('select * from apt where pat_app_no=(%s)',(p3,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("MODIFY APPOINTMENT","NO SUCH APPOINTMENT NUMBER FOUND")
    else:
        app3 = Toplevel()
        app3.geometry("400x400")
                 #to center tkinter window
        center_tk_window.center(app3,app3)
        center_tk_window.center_on_parent(app3,app3)
        center_tk_window.center_on_screen(app3)
                       ##########
        app3.title('Hospital Management - modify patient details')#used for change of title
        photo = PhotoImage(file ="hospital favicon.png")#used for favicon
        label=Label(app3,text="MODIFY APPOINTMENT\nDETAILS",font="arial 25 bold",bg="light blue")
        label.pack()
        frame=Frame(app3,height=300,width=300,bg="light blue")
        frame.pack()
        l1=Label(app3,text="Choose number to modify: 1.Appointment date \n 2.Appointment time \n 3.Problem",bg="light blue")
        l1.place(x=10,y=130)
        w4=tkinter.Entry(app3)
        w4.place(x=220,y=170)
        b1=Button(app3,text="Submit",command=lambda:[mod_all_apt(app3,p3)])
        b1.place(x=250,y=210)
        app3.configure(bg="light blue")
        app3.resizable(False,False)
        app3.mainloop()

#asking the new modification 
def mod_all_apt(app3,p3):
    global w4,w5
    x = w4.get()
    x = int(x)
    funcs(app3)
    if x == 1:
        app4 = Toplevel()
        app4.geometry("400x400")
           #to center tkinter window
        center_tk_window.center(app4,app4)
        center_tk_window.center_on_parent(app4,app4)
        center_tk_window.center_on_screen(app4)
            ##############
        app4.title('Hospital Management - modify appointment details')#used for change of title
        photo = PhotoImage(file ="hospital favicon.png")#used for favicon
        app4.iconphoto(False,photo)#used for favicon
        label=Label(app4,text="MODIFY",font="arial 25 bold",bg="light blue")
        label.pack()
        frame=Frame(app4,height=300,width=300,bg="light blue")
        frame.pack()
        l1=Label(app4,text = "New appointment date",bg="light blue")
        l1.place(x=10,y=120)
        w5=tkinter.Entry(app4)
        w5.place(x=140,y=120)
        b1=Button(app4,text="Submit",command=lambda:[upd_sql_apt(x,w5,p3,app4,app3)])
        b1.place(x=75,y=180)
        app4.configure(bg="light blue")
        app4.resizable(True,True)
        app4.mainloop()
    elif x == 2:
        app4 = Toplevel()
        app4.geometry("400x400")
          #to center tkinter window
        center_tk_window.center(app4,app4)
        center_tk_window.center_on_parent(app4,app4)
        center_tk_window.center_on_screen(app4)
               ###########
        app4.title('Hospital Management - modify appointment details')#used for change of title
        photo = PhotoImage(file ="hospital favicon.png")#used for favicon
        app4.iconphoto(False,photo)#used for favicon
        label=Label(app4,text="MODIFY",font="arial 25 bold",bg="light blue")
        label.pack()
        frame=Frame(app4,height=300,width=300,bg="light blue")
        frame.pack()
        l1=Label(app4,text = "New appointment time\n 24-hr format",bg="light blue")
        l1.place(x=10,y=120)
        w5= StringVar(app4)
        w5.set("time slot")
        w= OptionMenu(app4,w5,"7:00","7:30","8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00")
        w.place(x=140,y=120)
        b1=Button(app4,text="Submit",command=lambda:[upd_sql_apt(x,w5,p3,app4,app3)])
        b1.place(x=75,y=180)
        app4.configure(bg="light blue")
        app4.resizable(True,True)
        app4.mainloop()
    elif x == 3:
        app4 = Toplevel()
        app4.geometry("400x400")
             #to center tkinter window
        center_tk_window.center(app4,app4)
        center_tk_window.center_on_parent(app4,app4)
        center_tk_window.center_on_screen(app4)
                    #########
        app4.title('Hospital Management - modify appointment details')#used for change of title
        photo = PhotoImage(file ="hospital favicon.png")#used for favicon
        app4.iconphoto(False,photo)#used for favicon
        label=Label(app4,text="MODIFY",font="arial 25 bold",bg="light blue")
        label.pack()
        frame=Frame(app4,height=300,width=300,bg="light blue")
        frame.pack()
        l1=Label(app4,text = "Modify problem",bg="light blue")
        l1.place(x=10,y=120)
        w5=tkinter.Entry(app4)
        w5.place(x=140,y=120)
        b1=Button(app4,text="Submit",command=lambda:[upd_sql_apt(x,w5,p3,app4,app3)])
        b1.place(x=75,y=180)
        app4.configure(bg="light blue")
        app4.resizable(True,True)
        app4.mainloop()

#update that in sql
def upd_sql_apt(num,w5,p3,app4,app3):
    q1 = w5.get()
    if num == 1:
        col = "app_date"
    elif num == 2:
        col = "app_time"
    elif num == 3:
        col = "patient_problem"
    querry = "UPDATE apt SET "+col+" = '"+q1+"' WHERE pat_app_no = '"+p3+"'"
    cur.execute(querry)
    con.commit()
    tkinter.messagebox.showinfo("SUCCESS","MODIFIED")
    funcs(app4)
    funcs(app3)

# asking the username and password to delete the appointment
def delete_apt(rt18):
    global w6,w7
    funcs(rt18)
    app5 = Toplevel()
    app5.geometry("400x400")
        #to center tkinter window
    center_tk_window.center(app5,app5)
    center_tk_window.center_on_parent(app5,app5)
    center_tk_window.center_on_screen(app5)
           #################
    app5.title('Hospital Management - delete apointment details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    app5.iconphoto(False,photo)#used for favicon
    label=Label(app5,text="TO DELETE APPOINTMENT\nDETAILS",font='arial 20 bold',bg="light blue")
    label.pack()
    frame=Frame(app5,height=300,width=300,bg="light blue")
    frame.pack()
    l1=Label(app5,text="USER NAME",bg="light blue")
    l1.place(x=10,y=130)
    w6=tkinter.Entry(app5)
    w6.place(x=100,y=130)
    l2=Label(app5,text="PASSWORD",bg="light blue")
    l2.place(x=10,y=150)
    w7=tkinter.Entry(app5)
    w7.place(x=100,y=150)
    b1=Button(app5,text='Submit',command=lambda:[delete_apt_ins(app5)])
    b1.place(x=100,y=190)
    app5.configure(bg="light blue")
    app5.resizable(True,True)
    app5.mainloop()

#asking appointment number to delete the appointment
def delete_apt_ins(app5):
    global w6,w7,w8
    p1=w6.get()
    p2=w7.get()
    funcs(app5)
    cur.execute('select * from patientreg where pat_username=(%s)',(p1,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH PATIENT FOUND")
    else:
        dat = list(dat[0])
        pass1 = dat[1]
        if pass1 == p2:
            app6 = Toplevel()
            app6.geometry("400x300")
                    #to center tkinter window
            center_tk_window.center(app6,app6)
            center_tk_window.center_on_parent(app6,app6)
            center_tk_window.center_on_screen(app6)
                          #########
            app6.title('Hospital Management - delete appointment details')#used for change of title
            photo = PhotoImage(file ="hospital favicon.png")#used for favicon
            app6.iconphoto(False,photo)#used for favicon
            label=Label(app6,text="DELETE",font="arial 25 bold",bg="light blue")
            label.pack()
            frame=Frame(app6,height=200,width=300,bg="light blue")
            frame.pack()
            l1=Label(app6,text="Enter appointment\nnumber",bg="light blue")
            l1.place(x=10,y=130)
            w8=tkinter.Entry(app6)
            w8.place(x=120,y=130)
            b1=Button(app6,text='Submit',command=lambda:[del_apt(app6,app5)])
            b1.place(x=100,y=190)
            app6.resizable(False,False)
            app6.configure(bg="light blue")
            app6.mainloop()

#delete in sql    
def del_apt(app6,app5):
    global w8
    p3=w8.get()
    cur.execute('select * from apt where pat_app_no=(%s)',(p3,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("DELETE APPOINTMENT","NO SUCH APPOINTMENT NUMBER FOUND")
    else:
        cur.execute('delete from apt where pat_app_no=(%s)',(p3,))
        tkinter.messagebox.showwarning("DELETED SUCCESFULLY",'DELETED THE APPOINTMENT')
        con.commit()
        funcs(app6)

# getting login values (username and password)
def pat_login(rt18):
    global a9,a10
    funcs(rt18)
    root20 = Toplevel()
    root20.geometry("400x300")
            #to center tkinter window
    center_tk_window.center(root20,root20)
    center_tk_window.center_on_parent(root20,root20)
    center_tk_window.center_on_screen(root20)
                 ##########
    root20.title('Hospital Management - patient login')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root20.iconphoto(False,photo)#used for favicon
    label=Label(root20,text="LOGIN",font='arial 25 bold',bg="light blue")
    label.pack()
    frame=Frame(root20,height=200,width=300,bg="light blue")
    frame.pack()
    l1=Label(root20,text="USERNAME",bg="light blue")
    l1.place(x=30,y=70)
    a9=tkinter.Entry(root20)
    a9.place(x=100,y=70)
    l2=Label(root20,text="PASSWORD",bg="light blue")
    l2.place(x=30,y=100)
    a10=tkinter.Entry(root20)
    a10.place(x=100,y=100)
    b1=Button(root20,text="SUBMIT",command=lambda:[pat_login_ins(root20)])
    b1.place(x=150,y=150)
    root20.configure(bg="light blue")
    root20.resizable(True,True)
    root20.mainloop()

#inside patient login , here we are checking whether the username and password is crct
#if its crct, we are showing PATIENT PORTAL , else showing no data found
def pat_login_ins(root20):
    #a9 and a10 is wat we get from patient login
    global a9,a10,x11
    x11 = a9
    p1=a9.get()
    p2=a10.get()
    cur.execute('select * from patientreg where pat_username = (%s)',(p1,))
    dat=cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("USERNAME ERROR","NO SUCH USERNAME AVAILABLE")
    else:
        dat = list(dat[0])
        edhavadhu = dat[0]
        pass1 = dat[1]
        if pass1 == p2:
            pat_ins()
        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")

#PATIENT PORTAL
def pat_ins():
    global a9
    p1 = a9.get()
    root21 = Toplevel()
    root21.geometry("600x600")
              #to center tkinter window
    center_tk_window.center(root21,root21)
    center_tk_window.center_on_parent(root21,root21)
    center_tk_window.center_on_screen(root21)
              #############
    root21.title('Hospital Management - patient portal')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root21.iconphoto(False,photo)#used for favicon
    check = 'patient'

    img1 = ImageTk.PhotoImage(Image.open("appointments2.png"))
    l1 = Label(root21,text="Appointment",font="arial 14 bold",bg = "light blue")
    l1.place(x=95,y=173)

    img2 = ImageTk.PhotoImage(Image.open("listofdoctors.jpg"))
    l2 = Label(root21,text="List of doctors and \ntheir specialisation",font="arial 14 bold",bg = "light blue")
    l2.place(x=320,y=173)
    
    img3 = ImageTk.PhotoImage(Image.open("delete2.jpg"))
    l3 = Label(root21,text="Delete",font="arial 14 bold",bg = "light blue")
    l3.place(x=120,y=343)

    img4 = ImageTk.PhotoImage(Image.open("modifypat.png"))
    l4 = Label(root21,text="Modify",font="arial 14 bold",bg = "light blue")
    l4.place(x=372,y=343)

    img5 = ImageTk.PhotoImage(Image.open("appstatus.png"))
    l5 = Label(root21,text="Appointment\nstatus",font="arial 14 bold",bg = "light blue")
    l5.place(x=90,y=513)

    img6 = ImageTk.PhotoImage(Image.open("exit4.png"))
    l6 = Label(root21,text="Exit",font="arial 14 bold",bg = "light blue")
    l6.place(x=385,y=515)
    
    label=Label(root21,text="PATIENT PORTAL", font='arial 25 bold',bg="white")
    b1 = Button(root21,text="APPOINTMENT",font="arial 18 bold",image=img1,relief=RAISED,command = lambda:[get_apoint(root21,check)])
    b2 = Button(root21,text="LIST OF DOCTORS AND \nTHEIR SPECIALIZATION",relief=RAISED,font="arial 18 bold",image=img2,command = lambda:[lst_doc(root21,check)])
    b3 = Button(root21,text="DELETE",font="arial 18 bold",image=img3,relief=RAISED,command = lambda:[delete_pat_pat(p1,root21)])
    b4 = Button(root21,text="MODIFY",font='arial 18 bold',image=img4,relief=RAISED,command = lambda:[modify_pat_pat(root21,p1,check)])
    b5 = Button(root21,text="APPOINTMENT\nSTATUS",font="arial 18 bold",relief=RAISED,image=img5,command = lambda:[apt_status(p1,root21)])
    b6 = Button(root21,text="EXIT",font='arial 18 bold',image=img6,relief=RAISED,command=lambda:[funcs(root21)])
    label.pack()
    b1.place(x=100,y=70)
    b2.place(x=355,y=70)
    b3.place(x=100,y=240)
    b4.place(x=355,y=238)
    b5.place(x=100,y=410)
    b6.place(x=355,y=410)
    root21.configure(bg="light blue")
    root21.resizable(False,False)
    root21.mainloop()

#appointment status
def apt_status(p1,rt21):
    funcs(rt21)
    root22 = Toplevel()
    root22.geometry("900x600")
             #to center tkinter window
    center_tk_window.center(root22,root22)
    center_tk_window.center_on_parent(root22,root22)
    center_tk_window.center_on_screen(root22)
              ##############
    root22.title('Hospital Management - appointment status')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root22.iconphoto(False,photo)#used for favicon
    label = Label(root22, text="APPOINTMENT\nSTATUS", font="arial 16 bold",bg="light blue")
    label.pack()
    cur.execute("SELECT * FROM apt WHERE patient_username = (%s) ORDER BY app_date,app_time",(p1,))
    data = cur.fetchall()
    for i in range(len(data)):
        data[i] = list(data[i])
    frame = Frame(root22, height=500, width=800,bg="light blue")
    frame.pack()
    pat_apt_no = Label(root22, text="Appointment\nNumber", font="arial 12 bold",bg="light blue")
    pat_apt_no.place(x = 50,y = 60)
    doc_name = Label(root22, text="Doctor Name", font="arial 12 bold",bg="light blue")
    doc_name.place(x = 200,y = 60)
    date = Label(root22, text="Date", font="arial 12 bold",bg="light blue")
    date.place(x = 350,y = 60)
    time = Label(root22, text="Time", font="arial 12 bold",bg="light blue")
    time.place(x = 450,y = 60)
    sug = Label(root22, text="Status", font="arial 12 bold",bg="light blue")
    sug.place(x = 550,y = 60)
    y_cor = 100
    ycord = apt_stat(data, y_cor, root22)
    b = Button(root22, text="Close", command = lambda:[funcs(root22),pat_ins()])
    b.place(x = 250,y = ycord)
    root22.configure(bg="light blue") 
    root22.resizable(True,True)
    root22.mainloop()
    
#displaying appointment status table - recurrsive function
def apt_stat(lst, y_cor, rt22):
    if len(lst) == 0:
        return y_cor
    else:
        sublst = lst[0]
        if sublst[9] == '' or sublst[9] == 'declined':
            l1 = Label(rt22, text = sublst[0],bg="light blue")
            l2 = Label(rt22, text = sublst[3],bg="light blue")
            l3 = Label(rt22, text = sublst[6],bg="light blue")
            l4 = Label(rt22, text = sublst[7],bg="light blue")
            l5 = Label(rt22, text = sublst[9],bg="light blue")
            l1.place(x = 60,y = y_cor)
            l2.place(x = 200,y = y_cor)
            l3.place(x = 360,y = y_cor)
            l4.place(x = 460,y = y_cor)
            l5.place(x = 550,y = y_cor)
            y_cor += 50
        list1 = []
        if sublst[9]=='declined':
            b1=Button(rt22,text="Remove",command=lambda:[remove(sublst[0],rt22)])
            b1.place(x=640,y=(y_cor-50))
            #y_cor += 50
        for i in range(len(lst)):
            if i > 0:
                list1.append(lst[i])
        y_cor = apt_stat(list1, y_cor, rt22)
        return y_cor

#removing the declined suggestion by the patient and deleting it frm sql
def remove(app_no,rt22):
    querry= "delete from apt where pat_app_no = '"+str(app_no)+"'"
    cur.execute(querry)
    con.commit()
    funcs(rt22)
    pat_ins()
    

#we are getting username and password and asking what to modify and we are modifying , the command given in the 'submit' is already given above (inside hospital part)    
def modify_pat_pat(rt21,p1,check):
    global e11
    root16 = Toplevel()
    root16.geometry("500x400")
           #to center tkinter window
    center_tk_window.center(root16,root16)
    center_tk_window.center_on_parent(root16,root16)
    center_tk_window.center_on_screen(root16)
                ############
    root16.title('Hospital Management - modify patient details')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    root16.iconphoto(False,photo)#used for favicon
    label=Label(root16,text="MODIFY",font="arial 25 bold",bg="light blue")
    label.pack()
    frame=Frame(root16,height=500,width=500,bg="light blue")
    frame.pack()
    l1=Label(root16,text="Choose number to modify: 1.Name \n 2.Username \n 3.Password \n 4.Age \n 5.Gender \n 6.Phone \n 7.Blood Group ",bg="light blue")
    l1.place(x=10,y=130)
    e11=tkinter.Entry(root16)
    e11.place(x=200,y=170)
    b1=Button(root16,text="Submit",command=lambda:[mod_all_pat(root16,p1,check)])
    b1.place(x=250,y=210)
    root16.configure(bg="light blue")
    root16.resizable(True,True)
    root16.mainloop()

# DELETE PART INSIDE THE PATIENT PART , delete username ad password is getting from patient login and we are executing the second part of delete using those values
def delete_pat_pat(p1,rt21):
    cur.execute('delete from patientreg where pat_username=(%s)',(p1,))
    con.commit()
    cur.execute('delete from apt where patient_username=(%s)',(p1,))
    con.commit()
    tkinter.messagebox.showwarning("DELETED SUCCESFULLY",'DELETED')
    funcs(rt21)



    
                                                                    ############################


                                                                    ######## EMERGENCY #########

#inside emergency , it asks patient name,email id and problem of the patient
def emergency():
    global address_entry,name_entry,problem_entry,phone_entry
    app = Toplevel()
    app.title('Hospital Management - EMERGENCY!!!!')#used for change of title
    photo = PhotoImage(file ="hospital favicon.png")#used for favicon
    app.iconphoto(False,photo)#used for favicon
    app.geometry("500x500")
     #to center tkinter window
    center_tk_window.center(app,app)
    center_tk_window.center_on_parent(app,app)
    center_tk_window.center_on_screen(app)
             ###########
         # used for adding image
    canvas = Canvas(app,width = 800,height = 300) 
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("emergency1.png"))
    canvas.create_image(40,0,anchor = NW,image=img)
            ############
    name = Label(app,text="name of the patient : ")
    address_field = Label(app,text="Patient email id : ")
    problem = Label(app,text="Patient Problem: ")
    phone_no = Label(app,text="Phone Number:  ")
    name.place(x=15,y=100)
    address_field.place(x=15,y=160)
    problem.place(x=15,y=220)
    phone_no.place(x=15,y=280)
    #name = StringVar()
    address = StringVar()
    name_entry = tkinter.Entry(app,width="30")
    address_entry = Entry(app,textvariable=address,width="30")
    name_entry.place(x=15,y= 130)
    address_entry.place(x=15,y=190)
    problem_entry = tkinter.Entry(app,width="30")
    problem_entry.place(x=15,y=250)
    phone_entry = tkinter.Entry(app,width="30")
    phone_entry.place(x=15,y=310)
    button = Button(app,text="Send Message",command=lambda:[send_message(app)],width="30",height="2",bg="grey")
    button.place(x=150,y=340)
    app.mainloop()

#this sends mail to the patient that their emergency case is informed to the hospital
def send_message(app):
    global address_entry,name_entry
    address_info = address_entry.get()
    address_info1 = str(address_info)
    email_body_info = "Your emergency case is informed to the hospital"
    sender_email = "dhakhospital@gmail.com" 
    sender_password = "dhakhosp"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,address_info,email_body_info)
    mssg_to_hosp(app)
  
# this sends mail to the hospital that a emergency appointment is there
def mssg_to_hosp(app):
    global name_entry,problem_entry,phone_entry
    name1 = name_entry.get()
    prob = problem_entry.get()
    phone = phone_entry.get()
    address_info_hosp = "dhakhospital@gmail.com"
    b = "EMERGENCY CASE!!!!!"
    email_body = "\nPATIENT NAME - "
    a= "\nPROBLEM - "
    c="\nPHONE NUMBER - "
    name_of_pat = str(name1)
    pro = str(prob)
    ph = str(phone)
    email_body_str = b+(email_body)+(name1)+a+(pro)+c+(ph)
    sender_email = "dhakhospital@gmail.com"
    sender_password = "dhakhosp"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,address_info_hosp,email_body_str)
    sql_emer(app, name_of_pat)

# this includes the date,time,patient name and problem in sql inside the table emergency
def sql_emer(app,pat_name):
    global problem_entry
    time = datetime.now()
    current_time = time.strftime("%H:%M:%S")
    today= date.today()
    d1 = today.strftime("%d/%m/%y")
    prob = problem_entry.get()
    cur.execute("select * from emergency order by pat_emer_no")
    row=cur.fetchall()
    if len(row)==0:
        p1=1
    else:
        for i in range (len(row)):
            j=list(row[i])
            k=j[0]
            l=int(k)
            print(l)
            p1=l+1
    cur.execute("INSERT INTO emergency VALUES(%s,%s,%s,%s,%s)",(p1,pat_name,d1,current_time,prob))
    con.commit()
    tkinter.messagebox.showinfo("EMERGENCY","EMERGENCY\nAPPOINTMENT FIXED")
    funcs(app)

                                                                    ###################


# first tkinter window of the program where it shows PATIENT , DOCTOR AND HOSPITAL
root=Tk()
root.geometry("500x600")
    #to center first tkinter window
center_tk_window.center(root,root)
center_tk_window.center_on_parent(root,root)
center_tk_window.center_on_screen(root)
            ###########
root.title('Hospital Management - Welcome to Dhak Hospital')#used for change of title
photo = PhotoImage(file ="hospital favicon.png")#used for favicon
root.iconphoto(False,photo)#used for favicon
bg = PhotoImage(file ="hm21.png") #used for adding image
Label1=Label(root,image=bg)#used for adding image
Label1.pack()
label = Label(root,text= "DHAK HOSPITAL",font="arial 24 bold",bg='white')
b1= Button(root,text="PATIENT",font="arial 20 bold",bg= 'darkcyan' ,relief=RAISED,command=lambda:[patient()])
b2= Button(root,text="DOCTOR",font="arial 20 bold",bg='darkcyan',relief=RAISED,command=lambda:[doc()])
b3=Button(root,text="HOSPITAL",font="arial 20 bold",bg='darkcyan',relief=RAISED,command=lambda:[hosp_login()])
b4=Button(root,text="EMERGENCY",font = "arial 20 bold",bg="red",relief=RAISED,command=lambda:[emergency()])
b5=Button(root,text="EXIT",font="arial 20 bold",bg='darkcyan',relief=RAISED,command=lambda:[funcs(root)])
label.place(x=120,y=10)
b1.place(x=170,y = 160)
b2.place(x=170,y = 220)
b3.place(x=160,y = 280)
b5.place(x=200,y = 340)
b4.place(x=150,y = 400)
root.resizable(False,False)
root.mainloop()
