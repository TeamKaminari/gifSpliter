from tkinter import messagebox
import split
directory = input("Enter Image Directory: ")
folder = input("Enter Folder Name: ")
split.split(directory, folder)
messagebox.showinfo("Successful", "Image Split Complete")
