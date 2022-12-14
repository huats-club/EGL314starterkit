from tkinter import *

# Function to choose colour
def choose_colour(button_pressed):
    global colour
    colour = button_pressed
    print("Colour choice is {}".format(colour))
# Functions to print "Button Pressed" Results
def red_pressed():
    global colour
    if colour == 0:
        red.config(bg='red')
    elif colour == 1:
        red.config(bg='green')
    elif colour == 2:
        red.config(bg='blue')
    elif colour == 3:
        red.config(bg='gold')
    else:
        red.config(bg='orange') 
    print("Button Pressed is RED!")

def green_pressed():
    global colour
    if colour == 0:
        green.config(bg='red')
    elif colour == 1:
        green.config(bg='green')
    elif colour == 2:
        green.config(bg='blue')
    elif colour == 3:
        green.config(bg='gold')
    else:
        green.config(bg='orange') 
    print("Button Pressed is GREEN!")

def blue_pressed():
    global colour
    if colour == 0:
        blue.config(bg='red')
    elif colour == 1:
        blue.config(bg='green')
    elif colour == 2:
        blue.config(bg='blue')
    elif colour == 3:
        blue.config(bg='gold')
    else:
        blue.config(bg='orange') 
    print("Button Pressed is BLUE!")

# Main GUI Windows
main = Tk()
main.title("Tutorial 2 Sample")

# Label Widget
header = Label(main, text="My Fantastic GUI!", font=(300))
header.grid(row=0, columnspan=5)

# Button Widget
red = Button(main, text="R", font=(200), bg=('red'), command=red_pressed)
green = Button(main, text="G", font=(200), bg=('green'), command=green_pressed)
blue = Button(main, text="B", font=(200), bg=('blue'),command=blue_pressed)
red.grid(row=1, column=0)
green.grid(row=1, column=2)
blue.grid(row=1, column=4)

# Colour Section (Using Button Widget)
colour_value = 0

colourRed = Button(main, text="RED", bg=('red'), font=(200), command=lambda m=0:choose_colour(m))
colourGreen = Button(main, text="Green", bg=('green'), font=(200), command=lambda m=1:choose_colour(m))
colourBlue = Button(main, text="BLUE", bg=('blue'), font=(200), command=lambda m=2:choose_colour(m))
colourGold = Button(main, text="GOLD", bg=('gold'), font=(200), command=lambda m=3:choose_colour(m))
colourOrange = Button(main, text="ORANGE", bg=('orange'), font=(200), command=lambda m=4:choose_colour(m))
colourRed.grid(row=2, column=0)
colourGreen.grid(row=2, column=1)
colourBlue.grid(row=2, column=2)
colourGold.grid(row=2, column=3)
colourOrange    .grid(row=2, column=4)


main.mainloop()