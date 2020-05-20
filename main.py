import string
from tkinter import *

def addPlayer():
    pseudo = entryPseudo.get()
    print("username entered :", entryPseudo.get())
    if len(pseudo) < 4 or len(pseudo) == 0:
        entryPseudo.configure(background='red')
    else:
        print("good!")

width = 1000
height = 500

window = Tk(className='Sidoux')
# for r in range(26):
#    for c in range(22):
#       Label(window, text='R%s/C%s'%(r,c),
#          borderwidth=1 ).grid(row=r,column=c)

window.geometry("1000x500")
window.iconbitmap("spongebob.ico")

frameLeft = Frame(window, width=100, height=100)
photo = PhotoImage(file="spongebob.png")
label = Label(frameLeft, image=photo)
label.pack(side=RIGHT)
frameLeft.grid(row=0, column=0, sticky=W)


frameRight = Frame(window, width=100, height=100)

labelScore = Label(frameRight, text="Score", font=("courrier", 30), fg="black")
labelScore.pack()

entryPseudo = Entry(frameRight, text="Score", font=("courrier", 20), fg="black")
entryPseudo.pack(side=LEFT, padx=10)

Play = Button(frameRight, text="Score", font=("courrier", 20), fg="black", command= lambda : addPlayer())
Play.pack(side=RIGHT)
frameRight.grid(row=0, column=2, sticky=W)

window.mainloop()