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
    open_window()

def printScore():
    fill = open("score.txt", "r")
    line = " "
    c = 0
    while line and c < 7:
        line = fill.readline()
        Label(frameTopScore, text=line, borderwidth=1, font=("courrier", 14), bg='#5dbcd2').pack()
        c+=1
    f.close()

def open_window():
    top.deiconify()


window = Tk(className='Sidoux')
# for r in range(26):
#    for c in range(22):
#       Label(window, text='R%s/C%s'%(r,c),
#          borderwidth=1 ).grid(row=r,column=c)

window.geometry("900x450")
window.iconbitmap("spongebob.ico")
window.configure(bg='#5dbcd2')
window.resizable(False, False)

frameLeft = Frame(window, width=100, height=100)
photo = PhotoImage(file="spongebob.png")
label = Label(frameLeft, image=photo, bg='#5dbcd2')
label.pack(side=RIGHT)
frameLeft.grid(row=0, column=0, sticky=W)

frameRight = Frame(window, width=100, height=100, bg='#5dbcd2')

labelScore = Label(frameRight, text="Scores", font=("courrier", 30), fg="black", bg='#5dbcd2')
labelScore.pack()

frameTopScore = Frame(frameRight, width=100, height=100, bg='#5dbcd2')
printScore()
frameTopScore.pack()

entryPseudo = Entry(frameRight, font=("courrier", 20), fg="black", bg='#edb879')
entryPseudo.pack(side=LEFT, padx=10)

Play = Button(frameRight, text="Play !", font=("courrier", 20), fg="black", bg='#edb879', command= lambda : addPlayer())
Play.pack(side=RIGHT)
frameRight.grid(row=0, column=3, sticky=W)

top = Toplevel()
top.title("top window")
top.geometry("971x545")
top.configure(bg = '#5dbcd2')
window.configure(bg='#5dbcd2')
top.withdraw()
width = 971
height = 545
frameBgTop = Frame(top, width=width, height=height, bg='#5dbcd2')
topBg = PhotoImage(file="background.png")
labeltop = Label(frameBgTop, image=topBg, bg='#5dbcd2')
labeltop.pack(side=RIGHT)
frameBgTop.pack()
window.mainloop()