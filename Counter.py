from tkinter import *
import datetime

now = datetime.datetime.now()

#window
root = Tk()
root.geometry("680x160")
root.title("Luke's Task Counter")
heading = Label(root,
text = "Count your daily tasks", bg = "white", fg = "black", width = "680", height = "3")
heading.pack()

T = Label(root, text=(now.strftime("%d-%m-%Y ")), bg = "white")
T.place(x = 15, y = 15)

#variables for each function
root.counter = 0
root.counter2 = 0
root.counter3 = 0
root.counter4 = 0
root.counter5 = 0

# count pr click functions
def clicked():
    root.counter += 1
    L['text'] = 'Tickets closed: ' + str(root.counter)

def clicked2():
    root.counter2 += 1
    L2['text'] = 'Tickets created: ' + str(root.counter2)

def clicked3():
    root.counter3 += 1
    L3['text'] = 'Interruption count: ' + str(root.counter3)

def clicked4():
    root.counter4 += 1
    L4['text'] = 'Emails sent: ' + str(root.counter4)

def clicked5():
    root.counter5 += 1
    L5['text'] = 'Long phone calls: ' + str(root.counter5)

#Buttons and labels
b = Button(root, text="Tickets closed", command=clicked)
b.place(x = 15, y = 100)

L = Label(root, text="No clicks yet.")
L.place(x = 15, y = 65)

b2 = Button(root, text="Tickets created", command=clicked2)
b2.place(x = 130, y = 100)

L2 = Label(root, text="No clicks yet.")
L2.place(x = 130, y = 65)

b3 = Button(root, text="Interruptions", command=clicked3)
b3.place(x = 260, y = 100)

L3 = Label(root, text="No clicks yet.")
L3.place(x = 260, y = 65)

b4 = Button(root, text="Emails sent", command=clicked4)
b4.place(x = 390, y = 100)

L4 = Label(root, text="No clicks yet.")
L4.place(x = 390, y = 65)

b5 = Button(root, text="Long phone calls", command=clicked5)
b5.place(x = 520, y = 100)

L5 = Label(root, text="No clicks yet.")
L5.place(x = 520, y = 65)

root.mainloop()
