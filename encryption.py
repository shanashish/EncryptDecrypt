import os
from cryptography.fernet import Fernet
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, messagebox
from tkinter.ttk import Combobox

def generate_key():
    key = Fernet.generate_key()
    with open("Secret.Key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("Secret.Key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:
            messagebox.showerror("Error", "Invalid Key")
            return
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_file():
    filename = filedialog.askopenfilename()
    if filename:
        generate_key()
        key = load_key()
        encrypt(filename, key)
        messagebox.showinfo("Success", "File encrypted successfully.")

def decrypt_file():
    filename = filedialog.askopenfilename()
    if filename:
        key = load_key()
        decrypt(filename, key)
        messagebox.showinfo("Success", "File decrypted successfully.")

# GUI setup
root = Tk()
root.title("Crypt-R")

Label(root, text="Crypt-R: Choose an action:").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Section for encoding methods
Label(root, text="Encoding Methods:").grid(row=1, column=0, padx=10, pady=10)
encoding_var = StringVar()
encoding_combobox = Combobox(root, textvariable=encoding_var)
encoding_combobox['values'] = ("Text Binary", "Text Hex", "Text Base64", "Text Trinary")
encoding_combobox.grid(row=1, column=1, padx=10, pady=10)
encoding_combobox.current(0)

# Section for cipher methods
Label(root, text="Cipher Methods:").grid(row=2, column=0, padx=10, pady=10)
cipher_var = StringVar()
cipher_combobox = Combobox(root, textvariable=cipher_var)
cipher_combobox['values'] = ("Symmetric (Fernet)", "Asymmetric (RSA)")
cipher_combobox.grid(row=2, column=1, padx=10, pady=10)
cipher_combobox.current(0)

# Buttons for encryption and decryption
Button(root, text="Encrypt File", command=encrypt_file).grid(row=3, column=0, padx=10, pady=10)
Button(root, text="Decrypt File", command=decrypt_file).grid(row=3, column=1, padx=10, pady=10)

root.mainloop()