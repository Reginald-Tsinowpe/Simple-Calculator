"""   CALCULATOR APP  """

from tkinter import *



def entered(num):   #Its parameter 'num' is the text of the button selected. it inputs that into the entry field 'Data_Entry'.
    Data_Entry.insert(END, num)

def Eql_But_Func():
    calc = Data_Entry.get() #Gets all text in the 'Data_Entry' entry field
    #print(calc)
    Calculate(calc) #Makes the string in 'calc' the parameter of the function 'Calculate'

def Calculate(entry):
    a = eval(entry)     #runs the 'eval' function with 'Data_Entry's input as its parameter. It basically does the calculation
    Data_Entry.delete(0, END)   #deletes everything from the 'Data_Entry' entry field
    Data_Entry.insert(0, a)     #inserts the result of the calculation in the 'Data_Entry' entry field


def Clear():    #delete all content in the entry box. It is called when the button on line 37 is clicked.
    Data_Entry.delete(0, END)



"""     GUI     """
win = Tk()
win.title("SIMPLE CALCULATOR")
#The two lines below ensure that the window opens with a specific size, and the size is unchangeable
win.maxsize(width=359, height=350)
win.minsize(width=359, height=350)

entry_frame = Frame(win) # frame for the entry field and the clear button
Data_Entry = Entry(entry_frame, font=('Callibri', 20))  #Entry field creation
Data_Entry.focus()              #places the cursor in the entry field.
Data_Entry.pack(fill=Y, side=LEFT)      #entry field placement... basically shows it.
but_cls = Button(entry_frame, text='CLEAR', font=('Callibri', 10, 'bold'), command=Clear)   #'Clear' button creation
but_cls.pack(fill=Y, expand=1)
entry_frame.pack(ipady=15, fill=BOTH)   #entry_frame frame placement



buttons_frame = Frame(win)      #Frame for all buttons.
big_frame = Frame(buttons_frame)    #Frame for first 3 columns. ("987" and below)
small_frame = Frame(buttons_frame)  #Frame for fourth column -- leftmost column. ("/" and below)

_987 = Frame(big_frame)
but_7 = Button(_987, text='7', font=('Callibri', 20), command=lambda:entered(7)).pack(side=LEFT, fill=BOTH, expand=1)
but_8 = Button(_987, text='8', font=('Callibri', 20), command=lambda:entered(8)).pack(side=LEFT, fill=BOTH, expand=1)
but_9 = Button(_987, text='9', font=('Callibri', 20), command=lambda:entered(9)).pack(side=LEFT, fill=BOTH, expand=1)
_987.pack(fill=BOTH, expand=1)

_654 = Frame(big_frame)
but_4 = Button(_654, text='4', font=('Callibri', 20), command=lambda:entered(4)).pack(side=LEFT, fill=BOTH, expand=1)
but_5 = Button(_654, text='5', font=('Callibri', 20), command=lambda:entered(5)).pack(side=LEFT, fill=BOTH, expand=1)
but_6 = Button(_654, text='6', font=('Callibri', 20), command=lambda:entered(6)).pack(side=LEFT, fill=BOTH, expand=1)
_654.pack(fill=BOTH, expand=1)

_321 = Frame(big_frame)
but_1 = Button(_321, text='1', font=('Callibri', 20), command=lambda:entered(1)).pack(side=LEFT, fill=BOTH, expand=1)
but_2 = Button(_321, text='2', font=('Callibri', 20), command=lambda:entered(2)).pack(side=LEFT, fill=BOTH, expand=1)
but_3 = Button(_321, text='3', font=('Callibri', 20), command=lambda:entered(3)).pack(side=LEFT, fill=BOTH, expand=1)
_321.pack(fill=BOTH, expand=1)

_0 = Frame(big_frame)
but_open_bracket = Button(_0, text='(', font=('Callibri', 20), command=lambda:entered('(')).pack(side=LEFT, fill=BOTH, expand=1)
but_0 = Button(_0, text='0', font=('Callibri', 20), command=lambda:entered(0)).pack(side=LEFT, fill=BOTH, expand=1)
but_close_bracket = Button(_0, text=')', font=('Callibri', 20), command=lambda:entered(')')).pack(side=LEFT, fill=BOTH, expand=1)
_0.pack(fill=BOTH, expand=1)
big_frame.pack(side=LEFT, fill=BOTH, ipadx=70)

div_but = Button(small_frame, text='/', font=('Callibri', 20), command=lambda:entered('/')).pack(fill=X)
mult_but = Button(small_frame, text='*', font=('Callibri', 20), command=lambda:entered('*')).pack(fill=X)
subt_but = Button(small_frame, text='-', font=('Callibri', 20), command=lambda:entered('-')).pack(fill=X)
add_but = Button(small_frame, text='+', font=('Callibri', 18), command=lambda:entered('+')).pack(fill=X)
eql_but = Button(small_frame, text='=', font=('Callibri', 30), command=Eql_But_Func).pack(ipady=15, fill=X)

small_frame.pack(fill=BOTH, expand=True, ipadx=10)
buttons_frame.pack(side='bottom', fill=BOTH, expand=1)

#Keybinding
win.bind('<Return>', lambda x: Eql_But_Func())


win.mainloop()