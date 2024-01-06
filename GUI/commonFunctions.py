import tkinter as tk
from PIL import Image, ImageTk

def loadImage(pathToImage,sizeX,sizeY):
    try:
        imageBitmap = Image.open(pathToImage)
    except:
        print("ERROR: Bad image string")
        return
    imageBitmapResized = imageBitmap.resize((sizeX,sizeY), Image.ANTIALIAS)
    finalImage = ImageTk.PhotoImage(imageBitmapResized)
    return finalImage

def createFrame(parent, rows, columns):
    returnFrame = tk.Frame(parent)
    for i in range(rows):
        returnFrame.rowconfigure(i, weight=1)
    for i in range(columns):
        returnFrame.columnconfigure(i, weight=1)
    return returnFrame