from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter import filedialog as fdialogue
import encrypt
import decrypt

root = Tk()
root.title("Deep_Crypt File Service")
root.geometry("200x150")

mainFrame = Frame(root)
mainFrame.grid()

def closeWindow():
  root.destroy()

def encryptButtonClicked():
  filename = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  
def decryptButtonClicked():
  filename = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  #Connect decryption code here

def keygenButtonClicked():
  top = Toplevel(root)
  top.geometry("200x150")
  top.title("Key Generation")
  Label(top, text= "Enter your key's name").place(x=20,y=50)
        
encrypt_button = Button (root, text = "Encrypt", command = encryptButtonClicked)
decrypt_button = Button (root, text = "Decrypt", command = decryptButtonClicked)
keygen_button = Button(root, text="Generate Key", command=keygenButtonClicked)
close_button = Button (root, text = "Close", command = closeWindow)

encrypt_button.place(x=20, y=50)
decrypt_button.place(x=20, y=80)
keygen_button.place(x=20, y=110)
close_button.place(side=TOP, anchor="ne")

root.mainloop()
