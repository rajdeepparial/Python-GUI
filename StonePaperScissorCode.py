from tkinter import *
import webbrowser
import random
root = Tk()
root.title("Stone-Paper-Scissor")
root.geometry("450x400")
root.minsize(450, 400)
root.maxsize(450, 400)
root.configure(bg="red")
userScore = 0
compScore = 0
string1 = 'REACH 10'

def fb():
    webbrowser.open_new("https://www.facebook.com/rajdeep.parial.35/")
def ins():
    webbrowser.open_new("https://www.instagram.com/rajdeepparial21/")

def stone():
    global userScore
    global compScore
    userresultlbl.config(text="You Selected Stone")
    x = random.randint(1,3)
    if userScore == 10:
        compScore = 0
        userScore = 0
        complbl.config(text=compScore)
        userlbl.config(text=userScore)
        declarelbl.config(text="YOU WIN", bg="darkblue", fg="white", relief=SUNKEN)
    elif compScore == 10:
        compScore = 0
        userScore = 0
        complbl.config(text=compScore)
        userlbl.config(text=userScore)
        declarelbl.config(text="YOU LOSS", bg="darkred", fg="white", relief=SUNKEN)
    else:
        declarelbl.config(text="REACH 10", bg="white", fg="black")
        if x == 1:
            compresultlbl.config(text="Computer Selected Stone")
            FinalResultLabel.config(text="DRAWN")
        elif x == 2:
            compresultlbl.config(text="Computer Selected Paper")
            FinalResultLabel.config(text="COMPUTER WINS")
            compScore += 1
            complbl.config(text=compScore)
        else:
            compresultlbl.config(text="Computer Selected Scissor")
            FinalResultLabel.config(text="YOU WIN")
            userScore = userScore + 1
            userlbl.config(text=userScore)

def paper():
    global userScore
    global compScore
    userresultlbl.config(text="You Selected Paper")
    x = random.randint(1,3)
    if userScore == 10:
        compScore = 0
        userScore = 0
        complbl.config(text=compScore)
        userlbl.config(text=userScore)
        declarelbl.config(text="YOU WIN", bg="darkblue", fg="white", relief=SUNKEN)
    elif compScore == 10:
        compScore = 0
        userScore = 0
        complbl.config(text=compScore)
        userlbl.config(text=userScore)
        declarelbl.config(text="YOU LOSS", bg="darkred", fg="white", relief=SUNKEN)
    else:
        declarelbl.config(text="REACH 10", bg="white", fg="black")
        if x == 1:
            compresultlbl.config(text="Computer Selected Stone")
            FinalResultLabel.config(text="YOU WIN")
            userScore = userScore + 1
            userlbl.config(text=userScore)
        elif x == 2:
            compresultlbl.config(text="Computer Selected Paper")
            FinalResultLabel.config(text="DRAWN")
        else:
            compresultlbl.config(text="Computer Selected Scissor")
            FinalResultLabel.config(text="COMPUTER WINS")
            compScore += 1
            complbl.config(text=compScore)

def scissor():
    global userScore
    global compScore
    userresultlbl.config(text="You Selected Scissor")
    x = random.randint(1,3)
    if userScore == 10:
        compScore = 0
        userScore = 0
        complbl.config(text=compScore)
        userlbl.config(text=userScore)
        declarelbl.config(text="YOU WIN", bg="darkblue", fg="white", relief=SUNKEN)
    elif compScore == 10:
        compScore = 0
        userScore = 0
        complbl.config(text=compScore)
        userlbl.config(text=userScore)
        declarelbl.config(text="YOU LOSS", bg="darkred", fg="white", relief=SUNKEN)
    else:
        declarelbl.config(text="REACH 10", bg="white", fg="black")
        if x == 1:
            compresultlbl.config(text="Computer Selected Stone")
            FinalResultLabel.config(text="COMPUTER WINS")
            compScore += 1
            complbl.config(text=compScore)
        elif x == 2:
            compresultlbl.config(text="Computer Selected Paper")
            FinalResultLabel.config(text="YOU WIN")
            userScore = userScore + 1
            userlbl.config(text=userScore)
        else:
            compresultlbl.config(text="Computer Selected Scissor")
            FinalResultLabel.config(text="DRAWN")

def rstbtn():
    global userScore
    global compScore
    userScore = 0
    compScore = 0
    userlbl.config(text=userScore)
    complbl.config(text=compScore)


declarelbl = Label(root, text=string1, font="comicsansms 18 bold")
declarelbl.grid(padx=5, row=1, column=7)

lbl1 = Label(root, text="Player", bg="yellow", font="comicsansms 20 bold", relief=SUNKEN)
lbl1.grid(padx=10, pady=10, row=2, column=6)
lbl1 = Label(root, text="Computer", bg="yellow", font="comicsansms 20 bold", relief=SUNKEN)
lbl1.grid(padx=10, pady=10, row=2, column=8)

userlbl = Label(root, text=userScore, padx=15, font="comicsansms 25 bold", relief=SUNKEN)
userlbl.grid(padx=10, pady=10, row=3, column=6)
complbl = Label(root, text=compScore, padx=15, font="comicsansms 25 bold", relief=SUNKEN)
complbl.grid(padx=10, pady=10, row=3, column=8)


userresultlbl = Label(root, text="     ", font="comicsansms 10 italic")
userresultlbl.grid( row=4, column=6)
compresultlbl = Label(root, text="     ", font="comicsansms 10 italic")
compresultlbl.grid( row=4, column=8)


FinalResultLabel = Label(root, text="", font="comicsansms 10 italic",  bg="purple", fg="white")
FinalResultLabel.grid(row=5, column=7)


stnButton = Button(root, text="STONE", bg="black", fg="white", font="comicsansms 22 bold", command=stone)
stnButton.grid(row=7, column=6, padx=6, pady=5)
paperButton = Button(root, text="PAPER", bg="black", fg="white", font="comicsansms 22 bold", command=paper)
paperButton.grid(row=7, column=7, padx=6, pady=5)
sciButton = Button(root, text="SCISSOR", bg="black", fg="white", font="comicsansms 22 bold", command=scissor)
sciButton.grid(row=7, column=8, padx=6, pady=5)

fbBtn = Button(root, text="Follow me on Facebook", font="comicsansms 7", command=fb)
fbBtn.grid(padx=5, pady=20, row=9, column=6)
resetBtn = Button(root, text="RESET", font="comicsansms 15 bold", bg="green", fg="black", command=rstbtn )
resetBtn.grid(padx=5, pady=20, row=8, column=7)
insBtn = Button(root, text="Follow me on Instagram", font="comicsansms 7", command=ins)
insBtn.grid(padx=5, pady=20, row=9, column=8)
root.mainloop()