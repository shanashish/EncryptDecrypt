from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog

global filename
button_height = 2
button_width = 25

def browseFiles():
    browseFiles.filename = filedialog.askopenfilename(initialdir="/", title="Select a File")
    label_file_explorer.configure(text="File Opened: " + browseFiles.filename)

    button_encrypt.pack()
    button_decrypt.pack()

def generate_key():
    return Fernet.generate_key()

def encrypt_file():
    key = generate_key()
    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)

    with open(browseFiles.filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    with open(browseFiles.filename + ".key", 'wb') as key_file:
        key_file.write(key)

    status_label.configure(text="Encrypted")
    status_label.pack()

def decrypt_file():
    with open(browseFiles.filename + ".key", 'rb') as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(browseFiles.filename, 'wb') as dec_file:
        dec_file.write(decrypted)

    status_label.configure(text="Decrypted")
    status_label.pack()

window = Tk()

window.title('File Explorer')
window.geometry("940x740")
window.config(background="black")

main_title = Label(window, text="File Encryptor and Decryptor", width=100, height=2, fg="white", bg="black", font=("", 30))

credit = Label(window, bg="black", height=2, fg="white", font=("", 15))
label_file_explorer = Label(window, text="File Name : ", width=100, height=2, fg="white", bg="black", font=("", 20))

button_explore = Button(window, text="Browse File", command=browseFiles, width=button_width, height=button_height, font=("", 15))
button_encrypt = Button(window, text="Encrypt", command=encrypt_file, width=button_width, height=button_height, font=("", 15))
button_decrypt = Button(window, text="Decrypt", command=decrypt_file, width=button_width, height=button_height, font=("", 15))

status_label = Label(window, text="", width=100, height=4, fg="white", bg="black", font=("", 17))

credit.pack()
main_title.pack()
label_file_explorer.pack()
button_explore.pack()
window.mainloop()
