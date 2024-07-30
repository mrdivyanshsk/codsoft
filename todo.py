import tkinter as tk
from ttkbootstrap import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk


def add():
     x=entry_var.get()
     listbox.insert(listbox.size(),f"Task {listbox.size()+1} : "+x)
     entry.delete(0,len(x))

def delete():
     selected_indices = listbox.curselection()  # Get indices of selected items
     if(selected_indices):  
        for index in reversed(selected_indices): 
            listbox.delete(index)

def delall():
    listbox.delete(0,tk.END)

# WINDOW
window = tk.Tk()
window.title("To-Do List")
window.geometry('400x650')
window.config(bg='#000000')

# icon
icon = PhotoImage(file='Green-check-.png')  
window.iconphoto(True, icon)

# label
label=tk.Label(window,
               text="TO-DO List",
               foreground='white',
               background='#000000',
               font='Oswald 20 bold')
label.pack(pady=20)

# inputframe
inputframe1=tk.Frame(window,background='#000000')
inputframe1.pack(pady=10)
# label2
label2=tk.Label(inputframe1,text="TASK LIST : ",
                font='Calibri 15 bold',
                foreground='white',
                background='#000000')
label2.pack(side='left')

# LISTBOX
listbox=tk.Listbox(window,
                   bg='#000000',
                   fg='#f7f7f7',
                   font='15'
                   )
listbox.pack(pady=10)

# inputframe2
inputframe2=tk.Frame(window,
                background='#000000')
inputframe2.pack(pady=10)
# label3
label3=tk.Label(inputframe2,text="Enter task here : ",
                foreground='white',
                background='#000000',
                font='8')
label3.pack(side='left',padx=5,pady=10)
# entry
entry_var=tk.StringVar()
entry=tk.Entry(inputframe2, textvariable=entry_var,font='10')
entry.pack(side='left',pady=10,padx=5)

# add button
pil_image = Image.open('plus.png')  # Replace with the path to your image file

    # Resize the image to be smaller
smaller_image = pil_image.resize((20, 20), Image.LANCZOS)  # Resize to 20x20 pixels

photo=ImageTk.PhotoImage(smaller_image)
addbutton=tk.Button(window, text='ADD TASK TO LIST',
                    command=add,
                    image=photo,
                    bg='#ffffff',
                    activebackground='#005b80',
                    compound='left',
                    )
addbutton.pack(pady=10)

# inputframe3
frameeee=tk.Frame(window,bg='#000000')
frameeee.pack(pady=10)
# label4
label4=tk.Label(frameeee,text="Select the TASK and press DONE button",bg='#000000',fg='#ffffff')
label4.pack(padx=5,pady=5)
# delete button
delbutton=tk.Button(frameeee,text="Done",command=delete,activebackground='#e62727',bg='#ffffff')
delbutton.pack(padx=5,pady=5)

# DELETE ALL TASK
allbutton=tk.Button(window, text="DELETE ALL TASK", command=delall,activebackground='#f20202',bg='#ffffff')
allbutton.pack(pady=10)

# run
window.mainloop()
