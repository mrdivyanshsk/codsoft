import tkinter as tk
from tkinter import messagebox,Listbox,PhotoImage


def delete():
         selected_indices = list.curselection()  # Get indices of selected items
         if(selected_indices):  
            for index in reversed(selected_indices): 
                list.delete(index)
         else:
             messagebox.showwarning("No Selection", "Please select an item from the listbox to delete.") 
def addtolist():
    if not name.get() or not phone.get():
        messagebox.showwarning("Input Error", "Name and Phone are required fields.")
        return
    
    list.insert(list.size(), f"CONTACT {list.size() + 1} : {name.get()} + {phone.get()}")
    entry1.delete(0, len(name.get()))
    entry2.delete(0, len(entry2.get()))
    entry3.delete(0, len(entry3.get()))
    entry4.delete(0, len(entry4.get()))

def update():
    # Get the selected item index
    selected_index = list.curselection()
    if selected_index:
        # Get the new value for the selected item
        new_name = name.get()
        new_phone = phone.get()
        if new_name and new_phone:
            # Delete the old item and insert the new one at the same position
            list.delete(selected_index)
            list.insert(selected_index, f"CONTACT {selected_index[0] + 1} : {new_name} + {new_phone}")
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")
    else:
        messagebox.showwarning("No Selection", "Please select an item from the listbox to update.")
    entry1.delete(0, len(name.get()))
    entry2.delete(0, len(entry2.get()))
    entry3.delete(0, len(entry3.get()))
    entry4.delete(0, len(entry4.get()))

#  window
window=tk.Tk()
window.title('Contact Book')
window.geometry('500x700')

# icon
icon = PhotoImage(file='cb.png')  
window.iconphoto(True, icon)

# details
detail=tk.Label(window,text='DETAILS',font='Calibri 20 bold')
detail.pack(pady=15)
# ------------------------------------------------
# inputframe
inframe1=tk.Frame(window)
inframe1.pack(pady=5)
label1=tk.Label(inframe1,text='NAME')
label1.pack(side='left',padx=5,pady=10)
name=tk.StringVar()
entry1=tk.Entry(inframe1,textvariable=name)
entry1.pack(side='left',padx=5,pady=10)

inframe2=tk.Frame(window)
inframe2.pack(pady=10)
phone=tk.IntVar(value="+91")
label2=tk.Label(inframe2,text='Phone No.')
label2.pack(side='left',pady=10)
entry2=tk.Entry(inframe2,textvariable=phone)
entry2.pack(side='left',padx=5,pady=10)

inframe3=tk.Frame(window)
inframe3.pack(pady=10)
label3=tk.Label(inframe3,text='Email')
label3.pack(side='left',padx=5,pady=10)
entry3=tk.Entry(inframe3)
entry3.pack(side='left',padx=5,pady=10)

inframe4=tk.Frame(window)
inframe4.pack(pady=10)
label4=tk.Label(inframe4,text='Address')
label4.pack(side='left',padx=5,pady=10)
entry4=tk.Entry(inframe4)
entry4.pack(side='left',padx=5,pady=10)
# -------------------------------------------------

# listbox
list=tk.Listbox(window, width=60, height=15)
list.pack(pady=10)

# add button
add=tk.Button(window,text='Add',command=addtolist)
add.pack(pady=10)

# update button
updatebutton=tk.Button(window,text="UPDATE",command=update)
updatebutton.pack(pady=10)

# del button
delbutton=tk.Button(window,text="DELETE",command=delete)
delbutton.pack(pady=10) 

# run
window.mainloop()