from Tkinter import *
import backend as b
import app1 as a
import json
import pandas
import ttk

window=Tk()
scrollbar=Scrollbar(window)
window.geometry('500x300')
window.title("Value Sets")
l1=Label(window,text="Enter Value Set")
l1.grid(row=0,column=0)

value_set_name=StringVar()
e1=Entry(window,textvariable=value_set_name)
e1.grid(row=0,column=5)

# tree = ttk.Treeview(window)
def closeWindow():
    window.destroy()

def helloCallBack():
    global data
    
    data = a.func1(value_set_name.get())
#     tree["columns"]=("Code Type","Codes")
#     tree.column("Code Type", width=100 )
#     tree.column("Codes", width=100)
#     tree.heading("Code Type", text="Code Type")
#     tree.heading("Codes", text="Codes")
    list1=Listbox(window,height=6,width=35)
    list1.grid(row=6,column=2,rowspan=6,columnspan=8)
    scrollbar.config(command=list1.yview)
    scrollbar.config(command=list1.xview)
    list1.config(yscrollcommand=scrollbar.set)
    list1.config(xscrollcommand=scrollbar.set)
    if data is None:
        list1.insert(END,"No such Value Set exists")

    for i in data:

        for j in data[i]:
#             treeview.insert(" " ,0,values=(json.dumps(j)))
                list1.insert(END,json.dumps(j))


#             # json.dumps(data[i][j])
#             treeview.insert(" " ,0,values=(json.dumps(j)))
                list1.insert(END,json.dumps(data[i][j]))




#



b1=Button(window,text="View",width=12,command = helloCallBack)
b1.grid(row=5,column=3)

b1=Button(window,text="Close",width=12,command = closeWindow)
b1.grid(row=5,column=8)

window.mainloop()
