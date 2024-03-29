import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("800x750+0+0")
root.title("Tic Tac Toe (x,o)")
root.configure(background = 'Gray')

Tops= Frame(root, bg = 'Gray', pady=2, width= 800, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lbTitle=Label(Tops, font=('times', 50,'bold'), text="Tic Tac Toe Game", bd=21, bg='Gray', fg='Cornsilk', justify=CENTER)
lbTitle.grid(row=0, column=0)

MainFrame= Frame(root, bg='Purple', bd=10, width=1000, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg='Gray', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame= Frame(MainFrame, bd=10, width=560, height=500, padx=10, pady=2, bg='Gray', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1= Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='Gray', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2= Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='Gray', relief=RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons= StringVar()
click= True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scoresign()

#---X,O logica:

def scoresign():
    if(button1['text']== "X" and button2['text']== "X" and button3['text']=="X"):
        button1.configure(background= "babay pink")
        button2.configure(background= "babay pink")
        button3.configure(background= "babay pink")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game! Click on New Game to start a new game")

    if(button4['text']== "X" and button5['text']== "X" and button6['text']=="X"):
        button4.configure(background= "purple")
        button5.configure(background= "purple")
        button6.configure(background= "purple")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game! Click on New Game to start a new game")
        
    if(button7['text']== "X" and button8['text']== "X" and button9['text']=="X"):
        button7.configure(background= "green")
        button8.configure(background= "green")
        button9.configure(background= "green")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game!  Click on New Game to start a new game")

    if(button3['text']== "X" and button5['text']== "X" and button7['text']=="X"):
        button3.configure(background= "pink")
        button5.configure(background= "pink")
        button7.configure(background= "pink")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game! Click on New Game to start a new game")

    if(button1['text']== "X" and button5['text']== "X" and button9['text']=="X"):
        button1.configure(background= "blue")
        button5.configure(background= "blue")
        button9.configure(background= "blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game! Click on New Game to start a new game")
        
    if(button1['text']== "X" and button4['text']== "X" and button7['text']=="X"):
        button1.configure(background= "Orange")
        button4.configure(background= "Orange")
        button7.configure(background= "Orange")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game! Click on New Game to start a new game")
        
        
    if(button2['text']== "X" and button5['text']== "X" and button8['text']=="X"):
        button2.configure(background= "Red")
        button5.configure(background= "Red")
        button8.configure(background= "Red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game! Click on New Game to start a new game")     
        
    if(button3['text']== "X" and button6['text']== "X" and button9['text']=="X"):
        button3.configure(background= "babay pink")
        button6.configure(background= "babay pink")
        button9.configure(background= "babay pink")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You are the winner of this game! Click on New Game to start a new game")
        
          
#---- O 
    if(button1['text']== "O" and button2['text']== "O" and button3['text']=="O"):
        button1.configure(background= "babay pink")
        button2.configure(background= "babay pink")
        button3.configure(background= "babay pink")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")

    if(button4['text']== "O" and button5['text']== "O" and button6['text']=="O"):
        button4.configure(background= "purple")
        button5.configure(background= "purple")
        button6.configure(background= "purple")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")
        
    if(button7['text']== "O" and button8['text']== "O" and button9['text']=="O"):
        button7.configure(background= "green")
        button8.configure(background= "green")
        button9.configure(background= "green")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")

    if(button3['text']== "O" and button5['text']== "O" and button7['text']=="O"):
        button3.configure(background= "pink")
        button5.configure(background= "pink")
        button7.configure(background= "pink")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")

    if(button1['text']== "O" and button5['text']== "O" and button9['text']=="O"):
        button1.configure(background= "blue")
        button5.configure(background= "blue")
        button9.configure(background= "blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")
        
    if(button1['text']== "O" and button4['text']== "O" and button7['text']=="O"):
        button1.configure(background= "Orange")
        button4.configure(background= "Orange")
        button7.configure(background= "Orange")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")
        
        
    if(button2['text']== "O" and button5['text']== "O" and button8['text']=="O"):
        button2.configure(background= "Red")
        button5.configure(background= "Red")
        button8.configure(background= "Red")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")     
        
    if(button3['text']== "O" and button6['text']== "O" and button9['text']=="O"):
        button3.configure(background= "babay pink")
        button6.configure(background= "babay pink")
        button9.configure(background= "babay pink")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You are the winner of this game! Click on New Game to start a new game")
       
        
def reset():
    button1['text']= " "
    button2['text']= " "
    button3['text']= " "
    button4['text']= " "
    button5['text']= " "
    button6['text']= " "
    button7['text']= " "
    button8['text']= " "
    button9['text']= " "
    
    button1.configure(background= "Purple")
    button2.configure(background= "Purple")
    button3.configure(background= "Purple")
    button4.configure(background= "Purple")
    button5.configure(background= "Purple")
    button6.configure(background= "Purple")
    button7.configure(background= "Purple")
    button8.configure(background= "Purple")
    button9.configure(background= "Purple")
    
    
def NewGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)


#---Buttons on the Right
lbPlayerX=Label(RightFrame1, font=('times', 50,'bold'), text="Player X: ", padx=2, pady=2, bg='Purple')
lbPlayerX.grid(row=0, column=0, sticky='w')
txtPlayerX= Entry(RightFrame1, font=('times', 40, 'bold'), bd=2, fg='Blue', textvariable= PlayerX, width=14,
                justify=LEFT).grid(row=0, column=1)

lbPlayerO=Label(RightFrame1, font=('times', 50,'bold'), text="Player O: ", padx=2, pady=2, bg='Purple')
lbPlayerO.grid(row=1, column=0, sticky='w')
txtPlayerO= Entry(RightFrame1, font=('times', 40, 'bold'), bd=2, fg='Blue', textvariable= PlayerO, width=14,
                justify=LEFT).grid(row=1, column=1)

btnReset= Button(RightFrame2, text='Reset Game', font=('Times 26 bold'), height=3, width=25, bg='gainsboro', command=reset)
btnReset.grid(row=2, column=0)

btnNewGame= Button(RightFrame2, text='Play New Game', font=('Times 26 bold'), height=3, width=25, bg='gainsboro', command=NewGame)
btnNewGame.grid(row=3, column=0)



#----buttons on the Left
button1= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky= S+N+E+W)

button2= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky= S+N+E+W)

button3= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky= S+N+E+W)

button4= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky= S+N+E+W)

button5= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky= S+N+E+W)

button6= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky= S+N+E+W)

button7= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky= S+N+E+W)

button8= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky= S+N+E+W)

button9= Button(LeftFrame, text='', font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky= S+N+E+W)



root.mainloop()