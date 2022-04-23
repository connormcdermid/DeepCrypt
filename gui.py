from tkinter import * 
from tkinter.ttk import *

root = Tk()

def encryptButtonClicked():
  #Connect code for encryption button here 
  print("hello")
  
def decryptButtonClicked():
  #Connect code for decryption button here
  print("hello)

root.title("Deep_Crypt File Service")
        
encrypt_button = Button (root, text = "Encrypt", command = encryptButtonClicked)

encrypt_button.place(x=20, y=40)
        
root.mainloop()
