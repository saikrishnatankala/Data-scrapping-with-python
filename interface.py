from tkinter import *
from processing import find, GTopBat, GTopBowl
from processing import FantasyTeam

root = Tk()
root.title("Players")
#root.geometry("800x400")

def GetData():
    global text,e, temp, l, lablelist,b2,b3

    l.destroy()
    b2.destroy()
    b3.destroy()
    for i in lablelist:
        i.destroy()
    lablelist=[]
    text=e.get()
    temp=find(text)
    x=['Name','Matches','Innings','NO','Runs','Highest Score','Average','Balls Faced','Strike Rate','100','200','50','4s','6s',
          'Matches','Innings','Balls','Runs','Wickets','Best','Best','Economy','Average','Strike Rate','5W','10W']

    if (temp[0] == "Not Enough Data"):
        l = Label(root, text="Not Enough Data on "+temp[1])
        l.grid(row=3, column=0, columnspan=2)
        return None

    if (len(temp) == 27):
        for i in range(len(x)):
            l4 = Label(root, text=x[i])
            l4.grid(row=i + 3, column=0)
            lablelist.append(l4)

        l2 = Label(root, text="Grade")
        l2.grid(row=15, column=2)
        l3 = Label(root, text=temp[26])
        l3.grid(row=15, column=3)
        lablelist.append(l2)
        lablelist.append(l3)

        for i in range(len(temp) - 1):
            l4 = Label(root, text=temp[i])
            l4.grid(row=i + 3, column=1)
            lablelist.append(l4)
        return None
    else:
        l = Label(root, text=temp[0] + " Player Not Found")
        l.grid(row=3, column=0, columnspan=2)






def Update():
    global text,e
    bm.grid_forget()
    bm2.grid_forget()
    bm3.grid_forget()
    ln=Label(text="Enter Player's Name:")
    e = Entry(root, width=40)
    text=e.get()
    b=Button(text="Get Data", command= GetData)

    ln.grid(column=0)
    e.grid(column=1,row=0, padx=10)
    b.grid(column=2,row=0, padx=10)
    exec(open('main.py').read())

def Search():
    global text,e,b2,b3
    bm.grid_forget()
    bm2.grid_forget()
    bm3.grid_forget()
    ln=Label(text="Enter Player's Name:")
    e = Entry(root, width=40)
    text=e.get()
    b=Button(text="Get Data", command= GetData)
    b2=Button(text='TOP BAT', command= TopBat)
    b3 = Button(text='TOP BOWL', command=TopBowl)
    ln.grid(column=0, pady=100)
    e.grid(column=1,row=0, padx=10, pady=100)
    b.grid(column=2,row=0, padx=10, pady=100)
    b2.grid(column=1, row=1, padx=40,pady=10)
    b3.grid(column=1, row=2, padx=40)

def Fantasy():
    global text,e,e2
    bm.grid_forget()
    bm2.grid_forget()
    bm3.grid_forget()
    ln=Label(text="Enter Two Teams:")
    e = Entry(root, width=20)
    e2 = Entry(root, width=20)
    text= e.get()
    b= Button(text="Get Fantasy 11", command=GetFantasy11)

    ln.grid(column=0, pady=100)
    e.grid(column=1, row=0, padx=40, pady=100)
    e2.grid(column=2, row=0, padx=40, pady=100)
    b.grid(column=3, row=0, padx=40)

def GetFantasy11():
    global text,text2,e,e2, l,lablelist

    l.destroy()
    for i in lablelist:
        i.destroy()
    lablelist = []

    text=e.get()
    text2=e2.get()
    x=FantasyTeam(text,text2)
    print(x)

    l2=Label(root, text='The Fantasy Team IS:')
    l2.grid(row=1,column=1)
    lablelist.append(l2)


    for i in range(len(x)):
        l3 = Label(root, text=x[i])
        l3.grid(row=i + 2, column=1)
        lablelist.append(l3)

    return None

def TopBat():
    global text, text2, e, e2, l, lablelist

    l.destroy()
    for i in lablelist:
        i.destroy()
    lablelist = []

    x=GTopBat()
    print(x)
    l2 = Label(root, text='Top 10 Batsmen are:')
    l2.grid(row=4, column=1)
    lablelist.append(l2)

    for i in range(len(x)):
        l3 = Label(root, text=x[i])
        l3.grid(row=i + 6, column=1)
        lablelist.append(l3)


def TopBowl():
    global text, text2, e, e2, l, lablelist

    l.destroy()
    for i in lablelist:
        i.destroy()
    lablelist = []

    x = GTopBowl()
    print(x)
    l2 = Label(root, text='Top 10 Bowlers are:')
    l2.grid(row=4, column=1)
    lablelist.append(l2)

    for i in range(len(x)):
        l3 = Label(root, text=x[i])
        l3.grid(row=i + 6, column=1)
        lablelist.append(l3)


bm=Button(root, text="Update", command= Update)
bm.grid(row=0,column=0, padx=90, pady=100)
bm2=Button(root, text="Search", command= Search)
bm2.grid(row=0,column=1, padx=90, pady=100)
bm3=Button(root, text="Fantasy",command= Fantasy)
bm3.grid(row=0,column=2, padx=90, pady=100)
l=Label(root, text="")
lablelist=[]


root.mainloop()
