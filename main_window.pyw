from tkinter import Tk, Button
from tkinter import filedialog
from split import split
from tkinter import messagebox

path: str = ""
folder: str = "images"
selectedGIF: bool = False
selectedFolder: bool = False


def choose():
    global path, selectedGIF
    path = filedialog.askopenfilename(title="Choose a file", filetypes=[("GIF Image", ".gif"), ("All Files", "*.*")])
    selectedGIF = True


def choosefolder():
    global folder, selectedFolder
    folder = filedialog.askdirectory(title="Choose a folder", initialdir=folder)
    selectedFolder = True


root = Tk()
root.title("GIF Spliter")
root.geometry("200x300")
chooseButton = Button(root, text="Choose GIF", command=choose, height=2, width=25)
chooseButton.place(x=10, y=50)
chooseFolderButton = Button(root, text="Choose Folder", command=choosefolder, height=2, width=25)
chooseFolderButton.place(x=10, y=100)


def split_gif():
    if selectedGIF and selectedFolder:
        chooseButton["state"] = "disabled"
        chooseFolderButton["state"] = "disabled"
        split(path, folder)
        chooseButton["state"] = "normal"
        chooseFolderButton["state"] = "normal"
    elif selectedFolder and not selectedGIF:
        messagebox.showerror("Error", "Please choose a GIF")
    elif selectedGIF and not selectedFolder:
        messagebox.showerror("Error", "Please choose a folder")
    elif not selectedFolder and not selectedGIF:
        messagebox.showerror("Error", "Please choose a folder and a GIF")


startButton = Button(root, text="Start Split", command=split_gif, height=2, width=25)
startButton.place(x=10, y=200)

root.mainloop()
