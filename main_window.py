import tkinter
from tkinter import filedialog
from split import split

path: str = ""
folder: str = ""
selected: bool = False



def choose():
    global path, selected
    path = filedialog.askopenfilename(title="Choose a file", filetypes=[("GIF Image", ".gif"), ("All Files", "*.*")])
    selected = True


def choosefolder():
    global folder
    folder = filedialog.askdirectory(title="Choose a folder", initialdir=folder)


root = tkinter.Tk()
root.title("GIF Spliter")
root.geometry("200x300")
chooseButton = tkinter.Button(root, text="Choose GIF", command=choose, height=2, width=25)
chooseButton.place(x=10, y=100)
chooseFolderButton = tkinter.Button(root, text="Choose Folder", command=choosefolder, height=2, width=25)
chooseFolderButton.place(x=10, y=150)

split(path, folder)

while 1:
    root.update()
