from tkinter import *

width = 1000
height = 500

window = Tk(className='Sidoux')
# for r in range(26):
#    for c in range(22):
#       Label(window, text='R%s/C%s'%(r,c),
#          borderwidth=1 ).grid(row=r,column=c)

window.geometry("1000x500")
window.iconbitmap("spongebob.ico")

photo = PhotoImage(file="spongebob.png")
label = Label(window, image=photo)
label.grid(row=0, column=0, sticky=W)

frame = Frame(window)
labelScore = Label(frame, text="Score", font=("courrier", 30), fg="black")
labelScore.pack()

entryPseudo = Entry(frame, text="Score", font=("courrier", 20), fg="black")
entryPseudo.pack(side=LEFT, padx=(100, 10))

Play = Button(frame, text="Score", font=("courrier", 20), fg="black")
Play.pack(side=RIGHT)
frame.grid(row=0, column=2, sticky=W)

window.mainloop()