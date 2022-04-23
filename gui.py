from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter import filedialog as fdialogue
import encrypt
import decrypt

root = Tk()

root.geometry("200x150")
frame = Frame(root)
frame.grid()
frame.attributes("-fullscreen", 1)

def encryptButtonClicked():
  filename = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  
def decryptButtonClicked():
  filename = fdialogue.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
  #Connect decryption code here

root.title("Deep_Crypt File Service")
        
encrypt_button = Button (root, text = "Encrypt", command = encryptButtonClicked)
decrypt_button = Button (root, text = "Decrypt", command = decryptButtonClicked)

encrypt_button.place(x=20, y=50)
decrypt_button.place(x=20, y=80)

root.mainloop()
