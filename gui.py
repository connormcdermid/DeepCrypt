from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter import filedialog as fdialogue
from encrypt import encrypt
from decrypt import decrypt
from keygen import keygen

root = Tk()
root.title("Deep_Crypt File Service")
root.geometry("200x150")

mainFrame = Frame(root)
mainFrame.grid()

def closeMainFrame():
  root.destroy()


def encryptButtonClicked():
  filename = askopenfilename(initialdir = "./", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  key_file = askopenfilename(initialdir="keys/", title="Select a Key",
                             filetypes=(("Key Files", "*.key*"), ("All Files", "*.*")))
  encrypt(filename, key_file)
  
def decryptButtonClicked():
  filename = askopenfilename(initialdir = "./", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  key_file = askopenfilename(initialdir="keys/", title="Select a Key",
                             filetypes=(("Key Files", "*.key*"), ("All Files", "*.*")))
  decrypt(filename, key_file)

def keygenButtonClicked():
  top = Toplevel(root)
  top.geometry("100x75")
  top.title("Key Generation")

  def closeKeyGenWindow():
    top.destroy()
    keygen(textEntry.get())

  textEntry = StringVar()

  e = Entry(top, textvariable=textEntry, width=10)

  Label(top, text= "Enter your key's name").grid(column=1, row=1)
  e.grid(column=1, row=2)
  confirm_button = Button (top, text="Confirm", command=closeKeyGenWindow, )
  confirm_button.grid(column=1, row=3)

        
encrypt_button = Button (root, text = "Encrypt", command = encryptButtonClicked)
decrypt_button = Button (root, text = "Decrypt", command = decryptButtonClicked)
keygen_button = Button(root, text="Generate Key", command=keygenButtonClicked)
close_button = Button (root, text = "Close", command = closeMainFrame)

encrypt_button.place(x=20, y=50)
decrypt_button.place(x=20, y=80)
keygen_button.place(x=20, y=110)
close_button.grid(sticky="nw")

root.mainloop()
