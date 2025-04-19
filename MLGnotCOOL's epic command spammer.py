#to start the program
#u need to have pyautogui installed with the terminal
#pip install pyautogui

from tkinter import *
import re
import time
import pyautogui

#
#actual code
#

def start():
    inp1 = str(e1.get()) #from
    inp2 = str(e2.get()) #to
    inp3 = str(e3.get()) #wait time
    inp4 = str(e4.get()) #spam speed
    inp6 = str(e6.get()) #starting key
    inp5 = str(textbox1.get())

    if "*" not in inp5:
        l5.config(text="plz add * to the command") 
    elif (re.sub(r'[^0-9]', '', inp1) != inp1) or inp1 == "" or (re.sub(r'[^0-9]', '', inp2) != inp2) or inp2 == "" or (re.sub(r'[^0-9]', '', inp3) != inp3) or inp3 == "" or (re.sub(r'[^0-9]', '', inp4) != inp4) or inp4 == "":
        l5.config(text="plz input number :(")
    else:
        typing = True

        time.sleep(int(inp3)/1000)

        for i in range(int(inp1), int(inp2)+1):
            command = ""
            for char in inp5:
                if char == "*":
                    command += str(i)
                else:
                    command += char

            pyautogui.write(inp6) 
            time.sleep(0.05)     
            pyautogui.write(command, interval=0.001)
            pyautogui.hotkey("enter")
            time.sleep(int(inp4)/1000)
        typing = False

#
#the window thing
#

window = Tk()
window.title("MLGnotCOOL's epic command spammer")
window.geometry('520x600')

window.wm_attributes("-topmost", True)
window.configure(bg='cornsilk1')

label1=Label(window,text='enter the command (replace the number with "*")', fg='deepskyblue1', font=('Arial Bold', 15), bg='cornsilk1')
label1.grid(row=0,column=0, padx=(25, 0), pady=(10, 0))
textbox1=Entry(window, fg='cadetblue3', font=('Arial Bold', 15), width= 40, bg='lemonchiffon2')
textbox1.grid(row=1,column=0, padx=(25, 0), pady=(10, 0))

label2=Label(window,text='enter the numbers you want', fg='deepskyblue1', font=('Arial Bold', 15), bg='cornsilk1')
label2.grid(row=2,column=0, padx=(0, 0), pady=(20, 0))

l1 = Label(window, text = "from:", fg='indianred1', font=('Arial Bold', 15), bg='cornsilk1')
l2 = Label(window, text = "to:", fg='indianred1',font=('Arial Bold', 15), bg='cornsilk1')
l1.grid(row = 3, column = 0, sticky = W, padx = 50, pady = 2)
l2.grid(row = 4, column = 0, sticky = W, padx = 50, pady = 2)

e1 = Entry(window, fg='bisque4', width=5, font=('Arial Bold', 15), bg='lemonchiffon2')
e2 = Entry(window, fg='bisque4', width=5, font=('Arial Bold', 15), bg='lemonchiffon2')
e1.grid(row = 3, column = 0, pady = 2, padx=(0, 170))
e2.grid(row = 4, column = 0, pady = 2, padx=(0, 170))

l3 = Label(window, text = "initial wait time(ms): ", fg='indianred1', font=('Arial Bold', 15), bg='cornsilk1')
l4 = Label(window, text = "interval time(ms):", fg='indianred1', font=('Arial Bold', 15), bg='cornsilk1')
l3.grid(row = 5, column = 0, sticky = W, padx=(40, 0), pady=(50, 0))
l4.grid(row = 6, column = 0, sticky = W, padx=(40, 0), pady=(20, 0))

e3 = Entry(window, fg='bisque4', font=('Arial Bold', 15), width=5, bg='lemonchiffon2')
e4 = Entry(window, fg='bisque4', font=('Arial Bold', 15), width=5, bg='lemonchiffon2')
e3.insert(0, "1000")
e4.insert(0, "10")
e3.grid(row = 5, column = 0, padx=(35, 0), pady=(50, 0))
e4.grid(row = 6, column = 0, padx=(35, 0), pady=(20, 0))

l6 = Label(window, text = "prefix key:", fg='indianred1', font=('Arial Bold', 15), bg='cornsilk1')
l6.grid(row = 7, column = 0, sticky = W, padx=(40, 0), pady=(50, 0))

e6 = Entry(window, fg='brown1', font=('Arial Bold', 15), width=5, bg='lemonchiffon2')
e6.insert(0, "u")
e6.grid(row = 7, column = 0, padx=(0, 100), pady=(50, 0))

button = Button(window, text="start!", height=2, width=15, command=start, fg='red', font=('Arial Bold', 15), bg='lemonchiffon2')
button.grid(row = 8, column = 0, padx=(0, 0), pady=(40, 0))

l5 = Label(window, fg='indianred1', font=('Arial Bold', 15), bg='cornsilk1')
l5.grid(row = 9, column = 0, sticky = W, padx=(40, 0), pady=(30, 0))

window.mainloop()