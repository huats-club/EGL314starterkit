from tkinter import *
from tkinter.tix import COLUMN

# Functions to print "Button Pressed" Results
def red_pressed():
    print("Button Pressed is RED!")

def green_pressed():
    print("Button Pressed is GREEN!")

def blue_pressed():
    print("Button Pressed is BLUE!")

# Main GUI Windows
main = Tk()
main.title("Tutorial 1 Sample")

# Label Widget
header = Label(main, text="My Fantastic GUI!", font=(300))
header.grid(row=0, columnspan=3)

# Button Widget
red = Button(main, text="R", font=(200), command=red_pressed)
green = Button(main, text="G", font=(200), command=green_pressed)
blue = Button(main, text="B", font=(200), command=blue_pressed)
red.grid(row=1, column=0)
green.grid(row=1, column=1)
blue.grid(row=1, column=2)


main.mainloop()