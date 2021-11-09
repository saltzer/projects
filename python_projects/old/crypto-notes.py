import pyAesCrypt
import os, sys
from os import stat, remove
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file():
    global file_name
    file_name = "123"
    text.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode='w', defaultextension = '.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Error!", "An error has occurred!")

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

def encrypt_file():
    bufferSize=64*1024
    password=input("[1/3] Write the key: ")
    with open("crypt.txt", "rb") as fIn:
        with open("crypt.txt.crypt", "wb") as fOut:
            try:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
                print("[2/3] Encrypting...")
            except ValueError:
                print("[Failed/3] Error! Restart programm and try again...")
                encrypt_file()
    os.remove("crypt.txt")
    print("[3/3] Done!")


def decrypt_file():
    bufferSize=64*1024
    encFileSize = stat("crypt.txt.crypt").st_size
    password=input("[1/3] Write the key for decrypt file: ")
    with open("crypt.txt.crypt", "rb") as fIn:
        with open("crypt.txt", "wb") as fOut:
            try:
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                print("[2/3] Decrypting...")
            except ValueError:
                print("[Failed/3] Wrong key! Restart programm and try again...")
                decrypt_file()
    os.remove("crypt.txt.crypt")
    print("[3/3] Done!")


root = Tk()
root.title("NoteBook")
root.geometry("400x400")
text = Text(root, width=400, height=400)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
crypt_menu = Menu(menu_bar)
file_menu.add_command(label="New...", command=new_file)
file_menu.add_command(label="Save...", command=save_as)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Exit...", command=lambda:root.destroy())
menu_bar.add_cascade(label = "File", menu = file_menu)
menu_bar.add_cascade(label = "Crypting file", menu = crypt_menu)
crypt_menu.add_command(label="Encrypt file crypt.txt...", command=encrypt_file)
crypt_menu.add_command(label="Decrypt file crypt.crypt...", command=decrypt_file)


root.config(menu = menu_bar)
root.mainloop()
