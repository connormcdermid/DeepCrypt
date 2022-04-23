from tkinter import * 
from tkinter.ttk import *

root = Tk()

root.geometry("200x150")
frame = Frame(root)
frame.grid()

def encryptButtonClicked():
  filename = fdialogue.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  #Connect encryption code here
  
def decryptButtonClicked():
  filename = fdialogue.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  #Connect decryption code here

root.title("Deep_Crypt File Service")
        
encrypt_button = Button (root, text = "Encrypt", command = encryptButtonClicked)

encrypt_button.place(x=20, y=50)
        
root.mainloop()
