import tkinter as tkn
app = tkn.Tk()
app.geometry('300x400')
app.title('Free Calculator')

var1 = tkn.Variable(app)
var2 = tkn.Variable(app)
res = tkn.Variable(app)
res.set('0')

tkn.Entry(app, textvariable = var1, font=('Arial',20),
          width=10).place(x=60, y=50)
tkn.Entry(app, textvariable = var2, font=('Arial',20),
          width=10).place(x=60, y=100)
tkn.Label(app, textvariable = res, font=('Arial',20),
          fg='green').place(x=60, y= 160)

def calculate(op):
    res.set(eval(var1.get() + op + var2.get()))
##    '4' + '+' + '5'
##    eval('4*5')

tkn.Button(app,text='+',font = ('Arial',20),width = 3,
           command=lambda :calculate('+')).place(x=20,y=300)
tkn.Button(app,text='-',font = ('Arial',20),width = 3,
           command=lambda :calculate('-')).place(x=80,y=300)
tkn.Button(app,text='*',font = ('Arial',20),width = 3,
           command=lambda :calculate('*')).place(x=140,y=300)
tkn.Button(app,text='/',font = ('Arial',20),width = 3,
           command=lambda :calculate('/')).place(x=200,y=300)

app.mainloop()







##import tkinter as tkn
##
##app = tkn.Tk()
##app.geometry('400x400')
##app.title('My App')
##
##txt = tkn.Variable(app)
##txt.set('Hello')
##t = 'Nice'
##
##tkn.Label(app, textvariable = txt, fg='green', font = ('Arial',20)).place(x=30,y=30)
##tkn.Label(app, text=t, font = ('Arial',20)).place(x=130,y=10)
##tkn.Label(app, text='Wow', font = ('Arial',30)).place(x=30,y=230)
##
##e = tkn.Variable(app)
##tkn.Entry(app, textvariable=e).place(x=40,y=70)
##
##def abc():
##    txt.set('Hello')
##tkn.Button(app, text='Show Hello', command=abc).place(x=60, y=100)
##
##def abc2():
##    txt.set(e.get())
##tkn.Button(app, text='Show Bye', command=abc2).place(x=60, y=150)
##
##app.mainloop()
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####tkn.Label(app, text='Hello',fg='green', font = ('Arial',20)).pack()
####tkn.Label(app, text='Nice', font = ('Arial',20)).pack()
####tkn.Label(app, text='Wow', font = ('Arial',30)).pack()
##
####tkn.Label(app, text='Hello',fg='green', font = ('Arial',20)).grid(row=0,column=0)
####tkn.Label(app, text='Nice', font = ('Arial',20)).grid(row=2,column=1)
####tkn.Label(app, text='Wow', font = ('Arial',30)).grid(row=1,column=2)
##

