from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
import mysql.connector as sql
w=Tk()

w.title("BANK MANAGEMENT SYSTEM")
w.config(bg='teal')
w.state("zoomed")
l = Label(w, text = "****WELCOME TO RT BANK SERVICE****")
l.place(x=490,y=40)
l.config(font =("Times New Roman", 24))
img=PhotoImage(file="download.png")
i=Label(w,image=img)
i.place(x=650,y=250)
def exit():
    w.destroy()


def rege():
    name = ra.nm.get()
    acn = ra.an.get()
    brc = ra.bc.get()
    bal = ra.ba.get()
    age = ra.ag.get()
    address = ra.ad.get()
    mobile = ra.mo.get()
    gender = ra.gn.get()
    
    if(name=='' or acn=='' or brc=='' or bal=='' or age=='' or address=='' or mobile =='' or gender == ''):
        mb.showinfo("REGISTER","ENTER ALL DETAILS.ALL FIELD REQUIRED")
    else:
        con = sql.connect(host="localhost",user="root",password="",database="bank_project")
        cursor=con.cursor()
        cursor.execute("insert into regi values('"+ name +"','"+ acn +"','"+ brc +"','"+ bal +"','"+ age +"','"+ address +"','"+ mobile +"','"+ gender +"')")
        cursor.execute("commit")
        
        ra.nm.delete(0,"end")
        ra.an.delete(0,"end")
        ra.bc.delete(0,"end")
        ra.ba.delete(0,"end")
        ra.ag.delete(0,"end")
        ra.ad.delete(0,"end")
        ra.mo.delete(0,"end")
        ra.gn.delete(0,"end")
        
        
        mb.showinfo("REGISTER","ACCOUNT REGISTERED SUCCESSFULLY")
        con.close()


def dele():
    acn=dt.ac.get()

    if(acn==''):
        mb.showinfo("DELETE","ACCOUNT NO IS REQUIRED")
    else:
        con = sql.connect(host="localhost",user="root",password="",database="bank_project")
        cursor=con.cursor()
        cursor.execute("delete from regi where acn='"+ acn +"'")
        cursor.execute("commit")
        dt.ac.delete(0,"end")
        
        
        mb.showinfo("DELETE","ACCOUNT DELETED SUCCESSFULLY")
        con.close()

def get():
    acn=vd.ac.get()

    if(acn == ''):
        mb.showinfo("GET","ACCOUNT NO IS REQUIRED")
    else:
        con = sql.connect(host="localhost",user="root",password="",database="bank_project")
        cursor=con.cursor()
        cursor.execute("select * from regi where acn='"+ acn +"'")
        rows=cursor.fetchall()

        for row in rows:
            vd.nm.insert(0,row[0])
            vd.bc.insert(0,row[2])
            vd.ba.insert(0,row[3])
            vd.ag.insert(0,row[4])
            vd.ad.insert(0,row[5])
            vd.mo.insert(0,row[6])
            vd.gn.insert(0,row[7])
            
        con.close()

def cur():
    acn=de.ac.get()

    if(acn == ''):
        mb.showinfo("DEPOSITE","ACCOUNT NO IS REQUIRED")
    else:
        con = sql.connect(host="localhost",user="root",password="",database="bank_project")
        cursor=con.cursor()
        cursor.execute("select * from regi where acn='"+ acn +"'")
        rows=cursor.fetchall()
 
        for row in rows:
            de.ba.insert(0,row[3])
            cur.m=row[3]
            
        con.close()

def dep():
    acn=de.ac.get()
    money = de.mon.get()
    my = ((cur.m) + int(money))
    m=str(my)
    
    
    if(acn == '' or money==''):
        mb.showinfo("DEPOSITE","ACCOUNT NO & MONEY IS REQUIRED")
    else:
        con = sql.connect(host="localhost",user="root",password="",database="bank_project")
        cursor=con.cursor()
        
        cursor.execute("update regi set bal='"+ m +"' where acn='"+ acn +"'")
        cursor.execute("commit")
        cursor.execute("select * from regi where acn='"+ acn +"'")
        rows=cursor.fetchall()
        
       
        for row in rows:
            de.up.insert(0,row[3])
        con.close

        
def wid():
    acn=de.ac.get()
    money=de.mon.get()
    my = (cur.m) - int(money)
    m=str(my)
    if(acn == '' or money==''):
        mb.showinfo("WITHDRAW","ACCOUNT NO & MONEY IS REQUIRED")
    else:
        con = sql.connect(host="localhost",user="root",password="",database="bank_project")
        cursor=con.cursor()
        cursor.execute("update regi set bal='"+ m +"' where acn='"+ acn +"'")
        cursor.execute("commit")
        cursor.execute("select * from regi where acn='"+ acn +"'")
        rows=cursor.fetchall()
        
       
        for row in rows:
            de.up.insert(0,row[3])

        con.close


def show():
    con = sql.connect(host="localhost",user="root",password="",database="bank_project")
    cursor=con.cursor()
    cursor.execute("select * from regi")
    p=Toplevel(w)
    p.state("zoomed")
    p.title("ALL ACCOUNTS")
    p.config(bg='teal')
    tree=ttk.Treeview(p)
    tree['show']='headings'

    tree['columns'] = ("name","acn","brc","bal","age","address","mobile","gender")

    tree.column("name",width=50,minwidth=50,anchor=CENTER)
    tree.column("acn",width=100,minwidth=100,anchor=CENTER)
    tree.column("brc",width=100,minwidth=100,anchor=CENTER)
    tree.column("bal",width=100,minwidth=100,anchor=CENTER)
    tree.column("age",width=50,minwidth=50,anchor=CENTER)
    tree.column("address",width=100,minwidth=100,anchor=CENTER)
    tree.column("mobile",width=140,minwidth=140,anchor=CENTER)
    tree.column("gender",width=100,minwidth=100,anchor=CENTER)

    tree.heading("name",text="NAME",anchor=CENTER)
    tree.heading("acn",text="ACCOUNT NO",anchor=CENTER)
    tree.heading("brc",text="BRANCH CODE",anchor=CENTER)
    tree.heading("bal",text="BALANCE",anchor=CENTER)
    tree.heading("age",text="AGE",anchor=CENTER)
    tree.heading("address",text="ADDDRESS",anchor=CENTER)
    tree.heading("mobile",text="PHONE NO",anchor=CENTER)
    tree.heading("gender",text="GENDER",anchor=CENTER)

    s=ttk.Style()
    s.theme_use('clam')
    s.configure('.',font=('Times New Roman',10))

    
    '''
    sb=ttk.Scrollbar(p,orient='horizontal')
    sb.configure(command=tree.xview)
    tree.configure(xscrollcommand=sb.set)
    sb.pack(fill=X,side=BOTTOM)
    '''

    i=0
    for row in cursor:
        tree.insert('',i, text='', values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        i=i+1
    
    con.close()

    
    tree.pack(pady=40)
    
    def back():
        p.destroy()
    reg=Button(p,text="BACK",font=('Lora',15),command=back)
    reg.place(x=700,y=300)
       
def ra():
    cr_screen=Toplevel(w)
    cr_screen.state("zoomed")
    cr_screen.title("REGISTER ACCOUNT")
    cr_screen.config(bg="teal")
    l = Label(cr_screen, text = "****PLEASE ENTER YOUR DETAILS****")
    l.place(x=490,y=40)
    l.config(bg='teal',font =("Times New Roman", 20))
    l1=Label(cr_screen,text="NAME ")
    l1.place(x=200,y=100)
    l1.config(bg="teal",font=("",12))
    l2=Label(cr_screen,text="ACCOUNT NO")
    l2.place(x=200,y=150)
    l2.config(bg="teal",font=("",12))
    l3=Label(cr_screen,text="BRANCH CODE")
    l3.place(x=200,y=200)
    l3.config(bg="teal",font=("",12))
    l4=Label(cr_screen,text="BALANCE")
    l4.place(x=200,y=250)
    l4.config(bg="teal",font=("",12))
    l5=Label(cr_screen,text="AGE")
    l5.place(x=200,y=300)
    l5.config(bg="teal",font=("",12))
    l6=Label(cr_screen,text="ADDRESS")
    l6.place(x=200,y=350)
    l6.config(bg="teal",font=("",12))
    l7=Label(cr_screen,text="MOBILE")
    l7.place(x=200,y=400)
    l7.config(bg="teal",font=("",12))
    l8=Label(cr_screen,text="GENDER")
    l8.place(x=200,y=450)
    l8.config(bg="teal",font=("",12))
    ra.nm=Entry(cr_screen)
    ra.nm.place(x=380,y=100)
    ra.an=Entry(cr_screen)
    ra.an.place(x=380,y=150)
    ra.bc=Entry(cr_screen)
    ra.bc.place(x=380,y=200)
    ra.ba=Entry(cr_screen)
    ra.ba.place(x=380,y=250)
    ra.ag=Entry(cr_screen)
    ra.ag.place(x=380,y=300)
    ra.ad=Entry(cr_screen)
    ra.ad.place(x=380,y=350)
    ra.mo=Entry(cr_screen)
    ra.mo.place(x=380,y=400)
    ra.gn=Entry(cr_screen)
    ra.gn.place(x=380,y=450)
    def back():
        cr_screen.destroy()
    reg=Button(cr_screen,text="REGISTER",font=('Lora',15),command=rege)
    reg.place(x=200,y=510)
    reg=Button(cr_screen,text="BACK",font=('Lora',15),command=back)
    reg.place(x=400,y=510)
    

def dt():
    dt_screen=Toplevel(w)
    dt_screen.state("zoomed")
    dt_screen.title("DELETE ACCOUNT")
    dt_screen.config(bg='teal')
    l = Label(dt_screen, text = "****PLEASE ENTER ACCOUNT NUMBER****")
    l.place(x=490,y=40)
    l.config(bg='teal',font =("Times New Roman", 15))
    l1=Label(dt_screen,text="ACCOUNT NO")
    l1.place(x=200,y=125)
    l1.config(bg='teal',font=('',12))
    dt.ac=Entry(dt_screen)
    dt.ac.place(x=380,y=125)
    def back():
        dt_screen.destroy()
    reg=Button(dt_screen,text="DELETE",font=('Lora',15),command=dele)
    reg.place(x=200,y=200)
    reg=Button(dt_screen,text="BACK",font=('Lora',15),command=back)
    reg.place(x=400,y=200)

def vd():
    vd_screen=Toplevel(w)
    vd_screen.state("zoomed")
    vd_screen.title("VIEW DETAILS")
    vd_screen.config(bg="teal")
    l = Label(vd_screen, text = "****PLEASE ENTER YOUR ACCCOUNT NO****")
    l.place(x=490,y=40)
    l.config(bg='teal',font =("Times New Roman", 20))
    l1=Label(vd_screen,text="ACCOUNT NO")
    l1.place(x=200,y=100)
    l1.config(bg="teal",font=("",12))
    l2=Label(vd_screen,text="NAME ")
    l2.place(x=200,y=150)
    l2.config(bg="teal",font=("",12))
    l3=Label(vd_screen,text="BRANCH CODE")
    l3.place(x=200,y=200)
    l3.config(bg="teal",font=("",12))
    l4=Label(vd_screen,text="BALANCE")
    l4.place(x=200,y=250)
    l4.config(bg="teal",font=("",12))
    l5=Label(vd_screen,text="AGE")
    l5.place(x=200,y=300)
    l5.config(bg="teal",font=("",12))
    l6=Label(vd_screen,text="ADDRESS")
    l6.place(x=200,y=350)
    l6.config(bg="teal",font=("",12))
    l7=Label(vd_screen,text="MOBILE")
    l7.place(x=200,y=400)
    l7.config(bg="teal",font=("",12))
    l8=Label(vd_screen,text="GENDER")
    l8.place(x=200,y=450)
    l8.config(bg="teal",font=("",12))
    vd.ac=Entry(vd_screen)
    vd.ac.place(x=380,y=100)
    vd.nm=Entry(vd_screen)
    vd.nm.place(x=380,y=150)
    vd.bc=Entry(vd_screen)
    vd.bc.place(x=380,y=200)
    vd.ba=Entry(vd_screen)
    vd.ba.place(x=380,y=250)
    vd.ag=Entry(vd_screen)
    vd.ag.place(x=380,y=300)
    vd.ad=Entry(vd_screen)
    vd.ad.place(x=380,y=350)
    vd.mo=Entry(vd_screen)
    vd.mo.place(x=380,y=400)
    vd.gn=Entry(vd_screen)
    vd.gn.place(x=380,y=450)
    def back():
        vd_screen.destroy()
    reg=Button(vd_screen,text="VIEW",font=('Lora',15),command=get)
    reg.place(x=200,y=510)
    reg=Button(vd_screen,text="BACK",font=('Lora',15),command=back)
    reg.place(x=400,y=510)
    

def de():
    de_screen=Toplevel(w)
    de_screen.state("zoomed")
    de_screen.title("DEPOSIT")
    de_screen.config(bg='teal')
    l = Label(de_screen, text = "****PLEASE ENTER ACCOUNT NUMBER****")
    l.place(x=100,y=40)
    l.config(bg='teal',font =("Times New Roman", 15))
    l = Label(de_screen, text = "****PLEASE ENTER THE AMOUNT TO DEPOSITE****")
    l.place(x=850,y=40)
    l.config(bg='teal',font =("Times New Roman", 15))
    l1=Label(de_screen,text="ACCOUNT NO")
    l1.place(x=180,y=120)
    l1.config(bg="teal",font=("",12))
    l2=Label(de_screen,text="Current Balance")
    l2.place(x=180,y=260)
    l2.config(bg="teal",font=("",12))
    l3=Label(de_screen,text="AMOUNT")
    l3.place(x=900,y=120)
    l3.config(bg="teal",font=("",12))
    l4=Label(de_screen,text="UPDATED BALANCE")
    l4.place(x=900,y=260)
    l4.config(bg="teal",font=("",12))
    de.ac=Entry(de_screen)
    de.ac.place(x=330,y=120)
    de.ba=Entry(de_screen)
    de.ba.place(x=330,y=260)
    de.mon=Entry(de_screen)
    de.mon.place(x=1000,y=120)
    de.up=Entry(de_screen)
    de.up.place(x=1070,y=260)
    def back():
        de_screen.destroy()
    reg=Button(de_screen,text="CURRENT",font=('Lora',10),command=cur)
    reg.place(x=210,y=190)
    reg=Button(de_screen,text="DEPOSITE",font=('Lora',10),command=dep)
    reg.place(x=930,y=190)
    reg=Button(de_screen,text="BACK",font=('Lora',15),command=back)
    reg.place(x=650,y=350)


def wd():
    de_screen=Toplevel(w)
    de_screen.state("zoomed")
    de_screen.title("WITHDRAw")
    de_screen.config(bg='teal')
    l = Label(de_screen, text = "****PLEASE ENTER ACCOUNT NUMBER****")
    l.place(x=100,y=40)
    l.config(bg='teal',font =("Times New Roman", 15))
    l = Label(de_screen, text = "****PLEASE ENTER THE AMOUNT TO WITHDRAW****")
    l.place(x=850,y=40)
    l.config(bg='teal',font =("Times New Roman", 15))
    l1=Label(de_screen,text="ACCOUNT NO")
    l1.place(x=180,y=120)
    l1.config(bg="teal",font=("",12))
    l2=Label(de_screen,text="Current Balance")
    l2.place(x=180,y=260)
    l2.config(bg="teal",font=("",12))
    l3=Label(de_screen,text="AMOUNT")
    l3.place(x=900,y=120)
    l3.config(bg="teal",font=("",12))
    l4=Label(de_screen,text="UPDATED BALANCE")
    l4.place(x=900,y=260)
    l4.config(bg="teal",font=("",12))
    de.ac=Entry(de_screen)
    de.ac.place(x=330,y=120)
    de.ba=Entry(de_screen)
    de.ba.place(x=330,y=260)
    de.mon=Entry(de_screen)
    de.mon.place(x=1000,y=120)
    de.up=Entry(de_screen)
    de.up.place(x=1070,y=260)
    def back():
        de_screen.destroy()
    reg=Button(de_screen,text="CURRENT",font=('Lora',10),command=cur)
    reg.place(x=210,y=190)
    reg=Button(de_screen,text="WITHDRAW",font=('Lora',10),command=wid)
    reg.place(x=930,y=190)
    reg=Button(de_screen,text="BACK",font=('Lora',15),command=back)
    reg.place(x=650,y=350)


def be():
    de_screen=Toplevel(w)
    de_screen.state("zoomed")
    de_screen.title("BALANCE CHECKUP")
    de_screen.config(bg='teal')
    l = Label(de_screen, text = "****PLEASE ENTER ACCOUNT NUMBER****")
    l.place(x=490,y=40)
    l.config(bg='teal',font =("Times New Roman", 15))
    l1=Label(de_screen,text="ACCOUNT NO")
    l1.place(x=450,y=150)
    l1.config(bg="teal",font=("",12))
    l1=Label(de_screen,text="CURRENT BALANCE")
    l1.place(x=450,y=200)
    l1.config(bg="teal",font=("",12))
    de.ac=Entry(de_screen)
    de.ac.place(x=650,y=150)
    de.ba=Entry(de_screen)
    de.ba.place(x=650,y=200)
    def back():
        de_screen.destroy()
    reg=Button(de_screen,text="BALANCE",font=('Lora',15),command=cur)
    reg.place(x=460,y=250)
    reg=Button(de_screen,text="BACK",font=('Lora',15),command=back)
    reg.place(x=650,y=250)




t1=Button(w, text="REGISTER ACCOUNT",font=('Robota',15),command=ra)
t1.place(x=200,y=200)

t2=Button(w, text="VIEW DETAILS",font=('Robota',15),command=vd)
t2.place(x=200,y=400)

t3=Button(w, text="DEPOSIT",font=('Robota',15),command=de)
t3.place(x=200,y=600)

t4=Button(w, text="WITHDRAW",font=('Robota',15),command=wd)
t4.place(x=1150,y=200)

t5=Button(w, text="BALANCE ENQIRY",font=('Robota',15),command=be)
t5.place(x=1150,y=400)

t6=Button(w, text="DELETE ACCOUNT",font=('Robota',15),command=dt)
t6.place(x=1150,y=600)

t7=Button(w, text="VIEW ALL ACCOUNT",font=('Robota',15),command=show)
t7.place(x=650,y=600)

t8=Button(w, text="EXIT",font=('Robota',15),command=exit)
t8.place(x=730,y=700)

w.mainloop()
