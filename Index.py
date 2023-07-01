import tkinter
from tkinter import*

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
#root.resizable(False,False)

task_list=[]
def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
    
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file=open("tasklist.txt",'w')
        file.close()

#icon
Image_icon=PhotoImage(file="Image/logo.jpg")
root.iconphoto(False,Image_icon)
#heading
heading = Label(root, text="ALL TASK" ,font="arial 25 bold",width=15,height=1, fg="white",bg="black")
heading.place(x=350,y=50)

#main
frame= Frame(root, width=400,height=50,bg="#32405b")
frame.place(x=300, y=150)

task=StringVar()
task_entry=Entry(frame,width=25, font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold", width=6, bg="#32405b",fg="white", bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
#frame1= Frame(root,bd=3,width=700,height=280,bg="#32405b")
#frame1.pack(pady=(160,0))
frame1=Text(root, font=('arial',24))
frame1.place(x=300, y=200, )


listbox=Listbox(frame1,font=('arial',20),width=50,height=10,bg="#32405b", fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT ,fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete

button=Button(text="DELETE",font="arial 20 bold", width=8, bg="black",fg="white", bd=0,command=deleteTask)
button.place(x=400,y=550)


root.mainloop()