from tkinter import*
import tkinter.font as font

clicks=0

def button_click():
    global clicks
    clicks += 1
    button_text.set('Clicks: {}'.format(clicks))


root = Tk()
root.title('New Python Program!')
root.geometry('800x600')
root.configure(bg='#424242')

button_text = StringVar()
button_text.set('Make Kiriki: {}'.format(clicks))
button2_text = StringVar()
button2_text.set('Buy Manufacter 1 Level: {}'.format(clicks))
button3_text = StringVar()
button3_text.set('Buy Manufacter 2 Level: {}'.format(clicks))



gametitle = Label(text="NereaJLniy Zavod Kirikov",
           font="Arial 32")

undergametitle = Label(text="PART ONE",
           font=("Arial",
                 24, "bold"))


gametitle.config(bd=5, bg='#F8E6E0')
undergametitle.config(bd=10, bg='#F5BCA9')
gametitle.place(relx=.35, rely=.025)
undergametitle.place(relx=.737, rely=.14)

balance = Label(text='Your Balance Is:',
            font='Arial 32')
balance.place(relx=.01, rely=.9)
balance.config(bg='#FA5858')


def buy_manufacter():
    pass



btn = Button (textvariable=button_text, bg='#088A08', command=button_click)
btn2 = Button (textvariable=button2_text, command=button_click)
btn3 = Button (textvariable=button3_text, command=button_click)
btn.place(relx = .2, rely = .3, anchor = 'c', height = 50, width = 250) 
btn2.place(relx = .2, rely = .4, anchor = 'c', height = 50, width = 250) 
btn3.place(relx = .2, rely = .5, anchor = 'c', height = 50, width = 250) 
myFont = font.Font(weight='bold')
myFont = font.Font(size=10)
btn['font'] = myFont
btn2['font'] = myFont
btn3['font'] = myFont


root.mainloop()