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

def closeMainFrame():
  root.destroy()


def encryptButtonClicked():
  filename = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  
def decryptButtonClicked():
  filename = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  #Connect decryption code here

def keygenButtonClicked():
  top = Toplevel(root)
  top.geometry("400x400")
  top.title("Key Generation")

  def closeKeyGenWindow():
    top.destroy()

  textEntry = StringVar()

  e = ttk.Entry(top, textvariable=textEntry, width=10)

  Label(top, text= "Enter your key's name").place(x=20,y=50)
  e.place(x=20, y=100)
  confirm_button = Button (top, text="Confirm", command=closeKeyGenWindow)

        
encrypt_button = Button (root, text = "Encrypt", command = encryptButtonClicked)
decrypt_button = Button (root, text = "Decrypt", command = decryptButtonClicked)
keygen_button = Button(root, text="Generate Key", command=keygenButtonClicked)
close_button = Button (root, text = "Close", command = closeMainFrame)

encrypt_button.place(x=20, y=50)
decrypt_button.place(x=20, y=80)
keygen_button.place(x=20, y=110)
close_button.grid(sticky="nw")

root.mainloop()
