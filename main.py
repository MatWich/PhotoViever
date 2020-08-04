from tkinter import *
from PIL import ImageTk, Image
import os

# variables
imgIndex = 0

# Path to files 
path = os.path.dirname(os.path.realpath(__file__))
path = path + '\photos\\'

# files in folder photos
files = os.listdir(path)
print(files)

# Window
root = Tk()
root.title("Photos")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path+'imageIcon.png'))

# all file names
images = [ImageTk.PhotoImage(Image.open(path+file)) for file in files]
print(len(images))

def next(imgIndex):
    global photoLabel
    global previousButton
    global nextButton

    photoLabel.grid_remove()
    photoLabel = Label(photoFrame, image=images[imgIndex - 1])
    photoLabel.grid_size()
   
    nextButton = Button(buttonFrame, text=">>", command=lambda: next(imgIndex + 1))
    previousButton = Button(buttonFrame, text="<<", command=lambda: back(imgIndex - 1))
    
    if imgIndex == int(len(images)):
        nextButton = Button(buttonFrame, text=">>", state=DISABLED)


    photoLabel.grid(row=0, column=0, sticky=W+E+N+S)
    nextButton.grid(row=1, column=2)    
    previousButton.grid(row=1, column=0)

def back(imgIndex):
    global photoLabel
    global previousButton
    global nextButton

    photoLabel.grid_remove()
    photoLabel = Label(photoFrame, image=images[imgIndex - 1])
    photoLabel.grid_size()
   
    nextButton = Button(buttonFrame, text=">>", command=lambda: next(imgIndex + 1))
    previousButton = Button(buttonFrame, text="<<", command=lambda: back(imgIndex - 1))
    
    if imgIndex == 1:
        previousButton = Button(buttonFrame, text="<<", state=DISABLED)

    photoLabel.grid(row=0, column=0, sticky=W+E+N+S)
    nextButton.grid(row=1, column=2)    
    previousButton.grid(row=1, column=0)


# Frames
photoFrame = Frame(root, width=500, height=500, bg="black")
photoFrame.grid(row=0, column=0)

buttonFrame = Frame(root, width=200, heigh= 25)
buttonFrame.grid(row=1,column=0, columnspan=3 )

# Labels
photoLabel = Label(photoFrame, image=images[0])
photoLabel.grid(row=0, column=0, columnspan=3)
# Buttons
previousButton = Button(buttonFrame, text="<<", state=DISABLED, command=lambda: back(0))
quitButton = Button(buttonFrame, text="EXIT", command=root.quit)
nextButton = Button(buttonFrame, text=">>", command=lambda: next(2))

previousButton.grid(row=1, column=0)
quitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2)

root.mainloop()