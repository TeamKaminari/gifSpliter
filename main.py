from tkinter import messagebox
import split
directory = input("Enter Image path: ")
folder = input("Enter Folder Name: ")
split.split_terminal(directory, folder)
messagebox.showinfo("Successful", "Image Split Complete")
