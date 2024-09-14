from tkinter import *


root = Tk()

# geo

root.geometry("400x400")

# confi


root.title("First Tkinter")
root.config(bg= "purple")



# exit





def  getData():

    n = e_1.get()

    my_label = Label(root, text=n)
    my_label.pack()

e_1 = Entry(root,  width=30)
e_1.pack(padx=10, pady=30)


# button

btn = Button(root, text="submit", width=10 , bg="green", fg="white", command=getData)
btn.pack()