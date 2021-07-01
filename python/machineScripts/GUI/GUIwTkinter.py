from tkinter import *
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image



window = tk.Tk()

window.title("EL TEST")
window.geometry("500x500")
# add label
lbl = Label(window, text="output image", font=("Arial Bold", 15))
lbl.place(relx=0.5, rely=0.2, anchor=CENTER)# label position
# Add button
# define font
myFont = font.Font(family='Courier', size=20, weight='bold')
# Add button
btn = Button(window, text="Run Test", bg="orange", fg="red",
             width=10,height=2, compound="c")
# apply font to the button label
btn['font'] = myFont
# add button to gui window
btn.pack()

#btn.grid(column=250, row=1) # botton position
btn.place(relx=0.5, rely=0.05, anchor=CENTER)

### open Image
##path = "robot.jpg"
##
###Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
##image = Image.open(path)
##image = image.resize((300,300))
##img = tk.PhotoImage(image)
####img = ImageTk.PhotoImage(Image.open(path))
####img = img.resize((200,100))
##
##panel = Label(window, image = img)
path = "robot.jpg"
img = tk.PhotoImage(path)

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
##
canvas.create_image((100, 100), image=img)  # center

##canvas = tk.Canvas(window, height=400, width=1100)
###panel.create_image(0, 0, anchor="center", image=img)
##panel.place(relx=0.5, rely=0.5, anchor="center")
##panel.pack()
#canvas.pack()
             
window.mainloop()

#


