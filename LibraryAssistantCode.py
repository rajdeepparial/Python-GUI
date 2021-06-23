from tkinter import *
from time import strftime
from datetime import datetime
root = Tk()
root.title("Library Record Book")
root.configure(bg = "black")
root.geometry("450x200")
root.minsize(450,200)
root.maxsize(450,200)

def writeFile():
        name_info = userName.get()
        user_info = userID.get()
        dept_info = userDept.get()
        print(name_info, user_info, dept_info)
        file = open("Library_records.txt", "a")
        file.write("First Name: " + name_info)
        file.write("\n")
        file.write(" User ID: " + user_info)
        file.write("\n")
        file.write("Department " + dept_info)
        file.write("\n")
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        file.write("Entry Date :" + year + "-" + month + "-" + day)
        file.write("\n")
        string = strftime('Entry time is: %H:%M:%S %p')
        file.write(string)
        file.write("\n\n")
        file.close()

title = Label(root, text= "Enter your details Student", font= "comicsansms 15 bold", background="red", foreground="white",borderwidth=2, relief=SUNKEN)
user = Label(root,text="Enter your name", font= "comicsansms 10 bold", background="purple", foreground="white", borderwidth=5, relief=SUNKEN)
ID = Label(root, text="Enter your Library ID", font= "comicsansms 10 bold", background="purple", foreground="white", borderwidth=5, relief=SUNKEN)
Department = Label(root, text="Enter your Department", font= "comicsansms 10 bold", background="purple", foreground="white", borderwidth=5, relief=SUNKEN)
title.grid(column =1,padx=5, pady=5)
user.grid(row=7, padx=5, pady=5)
ID.grid(row=8,  padx=5, pady=5)
Department.grid(row=9,  padx=5, pady=5)

userName = StringVar()    #Declaration of variable
userID = StringVar()
userDept = StringVar()

userNameEntry = Entry(root, textvariable=userName, borderwidth=3, relief= SUNKEN,width="40")
userIDEntry = Entry(root, textvariable=userID, borderwidth=3, relief= SUNKEN,width="40")
userDeptEntry = Entry(root, textvariable=userDept, borderwidth=3, relief= SUNKEN, width="40")

userNameEntry.grid( row=7, column=1, pady=5)
userIDEntry.grid(row=8, column=1, pady=5)
userDeptEntry.grid(row=9, column=1, pady=5)

Button(root, text="Submit",  bg="darkblue", font="15", fg="white", command=writeFile,).grid(column=1, padx=5)
root.mainloop()