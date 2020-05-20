import string
from tkinter import *
f= open("score.txt","r")
f.close()

def addPlayer():
    entryPseudo.configure(background='white')
    pseudo = entryPseudo.get()
    if len(pseudo) < 4 or len(pseudo) == 0:
        entryPseudo.configure(background='red')
        return None

    fill = open("score.txt", "a")
    fill.write(pseudo + "   0\n")
    fill.close()
    print("Added")

def printScore():
    fill = open("score.txt", "r")
    line = " "
    c = 0
    while line and c < 7:
        line = fill.readline()
        Label(frameTop, text=line, borderwidth=1 ).pack()
        c+=1
    f.close()

def open_window():
    top = Toplevel()
    top.title("top window")
    top.geometry("300x300+120+120")
    button1 = Button(top, text="close", command=top.destroy)
    button1.pack()

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

labelScore = Label(frameRight, text="Scores", font=("courrier", 30), fg="black")
labelScore.pack()

frameTop = Frame(frameRight, width=100, height=100)
printScore()
frameTop.pack()

entryPseudo = Entry(frameRight, font=("courrier", 20), fg="black")
entryPseudo.pack(side=LEFT, padx=10)

Play = Button(frameRight, text="Play !", font=("courrier", 20), fg="black", command= lambda : addPlayer())
Play.pack(side=RIGHT)
frameRight.grid(row=0, column=3, sticky=W)

window.mainloop()