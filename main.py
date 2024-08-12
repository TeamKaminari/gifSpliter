from tkinter import messagebox
import split
directory = input("Enter Image Path: ")
folder = input("Enter Folder Name: ")
split.split_terminal(directory, folder)
messagebox.showinfo("Successful", "Image Split Complete")
