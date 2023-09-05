import tkinter as tk
from tkinter import messagebox as msg
import pickle


#root elememt
root=tk.Tk()
root.title('My To-do list')


#defining the necessary functios for each command
def add_task():
    gettask=t_entry.get()
    if gettask!="":
        l_box.insert(tk.END,gettask)
        t_entry.delete(0,tk.END)
    else:
        tk.messagebox.showwarning(title='warning!!',message='you should not enter blank tasks')

def delete_task():
    try:
        task_index=l_box.curselection()[0]
        l_box.delete(task_index)
    except:
        tk.messagebox.showwarning(title='Warning!',message='please select a task first')
def load_task():
    try:
        tasks=pickle.load(open('tasks.dat','rb'))
        l_box.delete(0,tk.END)
        for task in tasks:
            l_box.insert(tk.END,task)


    except:
        tk.messagebox.showwarning(title='Warning!',message='cant find tasks.dat')
        
def save_task():
    tasks=l_box.get(0,l_box.size())
    
    pickle.dump(tasks,open('tasks.dat','wb'))



#creating a frame
f_task=tk.Frame(root)
f_task.pack()


#creating a list box 
l_box=tk.Listbox(f_task,height=15,width=110)
l_box.pack(side=tk.LEFT)

sc_task=tk.Scrollbar(f_task)
sc_task.pack(side=tk.RIGHT,fill=tk.Y)

l_box.config(yscrollcommand=sc_task.set)
sc_task.config(command=l_box.yview)


#entry box creation
t_entry=tk.Entry(root,width=88)
t_entry.pack(padx=20,pady=20)



#creating the required buttons 

Button_for_task=tk.Button(root,text="Add  Task",width=48,command=add_task)
Button_for_task.pack(pady=6)

Button_for_deltask=tk.Button(root,text="Delete Task",width=48,command=delete_task)
Button_for_deltask.pack(pady=6)

Button_for_loadtask=tk.Button(root,text="Load Task(s)",width=48,command=load_task)
Button_for_loadtask.pack(pady=6)

Button_for_savetask=tk.Button(root,text=" Save Task(s)",width=48,command=save_task)
Button_for_savetask.pack(pady=6)
root.mainloop()
