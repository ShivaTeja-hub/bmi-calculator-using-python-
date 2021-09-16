from tkinter import*
from pymongo import MongoClient
def bmi_calculation():
    h=e1.get()
    w=e2.get()
    h=float(h)
    z=h
    w=float(w)
    name=e3.get()
    age=e4.get()
    age=int(age)
    units_height=dropdown1_dt.get()
    weight_units=dropdown2_dt.get()
    if units_height=='inch':
        h=h*0.0254
       # h=h*h
    elif units_height=='feet':
        h=h/3.281
    elif units_height=='meters':
        h=h
    elif units_height=='cm':
        h=h/100
    if weight_units=='kg':
        w=w
    elif weight_units=='pounds':
        w=w/2.2046
    elif weight_units=='tons':
        w=w*1000
    h=h*h
    bmi=w/h
    Label(root, text="your bmi is",bg='red').grid(row=10,column=1)
    Label(root,text=bmi,bg='red').grid(row=10,column=2)
    Label(root,text=name,bg='red').grid(row=10,column=0)
    Label(root,text="and",bg='red').grid(row=10,column=3)
    if bmi<18.5:
        Label(root,text="you are under weight please increase your weight",bg='floral white').grid(row=10,column=4)
    elif (bmi >18.5 and bmi<24.9):
        Label(root,text="you are healthy",bg='green').grid(row=10,column=4)
    elif (bmi>25 and bmi<29.9):
        Label(root,text="you are over weight please decrease your weight",bg='red').grid(row=10,column=4)
    elif bmi>30:
        Label(root,text="you are obese",bg='red').grid(row=10,column=4)
    
    try:
        client = MongoClient('localhost', 27017)
        mydb=client.bmi
        information=mydb.table
        rec={
        "name":name,
        "age":age,
        "height":z,
        "weight":w,
        "height units":units_height,
        "weight units":weight_units,
        "bmi":bmi
        }
        result=information.insert_one(rec)
        print('Created {0} of 500 as {1}'.format(rec,result.inserted_id))
    except Exception as e:
        print(e)
        print("encountered error while adding to data base")

def collect_stats_info():
    client = MongoClient('localhost', 27017)
    mydb=client.bmi
    information=mydb.table
    stats = information.find({})
    data=[]
    for i in stats:
        data.append(i)
    return data

def stat():
    c=collect_stats_info()
    Label(root,text="Name").grid(row=13,sticky=W)
    Label(root,text="age").grid(row=13,column=1,sticky=W)
    Label(root,text="bmi").grid(row=13,column=2,sticky=W)
    roww=14
    columnn=0
    for l in c:
        
        Label(root,text=l['name']).grid(row=roww,column=0,sticky=W)
        
        Label(root,text=l['age']).grid(row=roww,column=1,sticky=W)
        
        Label(root,text=l['bmi']).grid(row=roww,column=2,sticky=W)
        roww+=1
        column=0

root=Tk()
root.geometry('1000x1000')

opt1=["inch","feet","meters","cm"]
opt2=["kg","pounds","tons"]
dropdown1_dt=StringVar()
dropdown2_dt=StringVar()
dropdown1_dt.set("meters")
dropdown2_dt.set("kg")


dropdown1=OptionMenu(root,dropdown1_dt,*opt1)
dropdown1.grid(row=3,column=3,sticky=W)
dropdown2=OptionMenu(root,dropdown2_dt,*opt2)
dropdown2.grid(row=4,column=3)


Label(root,text="enter name").grid(row=1,sticky=W)
Label(root,text="enter age").grid(row=2,sticky=W)
Label(root, text="Enter height ").grid(row=3, sticky=W)
Label(root, text="Enter weight ").grid(row=4, sticky=W)

e1 = Entry(root)
e2 = Entry(root)
e3=Entry(root)
e4=Entry(root)

e3.grid(row=1,column=1)
e4.grid(row=2,column=1)
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)

'''
Label(root, text="sum:").grid(row=3, sticky=W)

calcu=Label(root, text="").grid(row=3,column=1, sticky=W)

 '''
b = Button(root, text="Calculate", command=bmi_calculation)
b.grid(row=8, column=5,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
c=Button(root,text="display statistics",command=stat)
c.grid(row=11, column=8,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)




mainloop()

