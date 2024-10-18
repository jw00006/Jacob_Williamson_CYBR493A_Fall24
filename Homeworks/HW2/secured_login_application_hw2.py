# Jacob Williamson
# CYBR493A
# October 17, 2024
# HW#2 Secured Login Application

# The objective of this project is to build upon the logic of the
# secured_login.py file by keeping the same method names but
# utilizing a different encryption and decryption mechanism of
# your choice.

import string
import tkinter as tk
from tkinter import messagebox
import DBConnector


def encrypt_password(message, key):
    # creates alphabet
    chars = string.ascii_uppercase
    # save param message into encrypt uppercase
    encrypt = message.upper()
    # variable to hold result
    result = ""
    # loop for iterating through message
    for char in encrypt:
        # check if char in param message is actually a letter
        if char in chars:
            # find and save proper letter from key for shifting
            index = (chars.find(char) + key) % 26
            # save resulting letter after shift
            result += chars[index]
        else:
            # if char in param is not a letter, just let it through or else it's removed
            result += char

    return result

def decrypt_password(message, key):
    # creates alphabet
    chars = string.ascii_uppercase
    # save param message into decrypt uppercase
    decrypt = message.upper()
    # variable to hold result
    result = ""
    # loop for iterating through message
    for char in decrypt:
        # check if char in param message is actually a letter
        if char in chars:
            # find and save proper letter from key for shifting
            index = (chars.find(char) - key) % 26
            # save resulting letter after shift
            result += chars[index]
        else:
            # if char in param is not a letter, just let it through or else it's removed
            result += char

    return result

def create_users_table(db):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Williamson_Jacob_HW2 (
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        shift TEXT NOT NULL
    );
    """
    db.query(create_table_query, '')

def insert_user(db, username, password, shift):
    encrypted_username = encrypt_password(username, shift)
    # Ensure the encrypted username is stored as a string
    # encrypted_username_str = encrypted_username.decode('utf-8')

    encrypted_password = encrypt_password(password, shift)
    # Ensure the encrypted password is stored as a string
    # encrypted_password_str = encrypted_password.decode('utf-8')

    insert_user_query = "INSERT INTO Williamson_Jacob_HW2 (username, password, shift) VALUES (%s, %s, %s);"
    db.query(insert_user_query, (encrypted_username, encrypted_password, shift))


# Method to authenticate user by checking decrypted username and password
def authenticate_user(db, username, password, shift):
    # Query to fetch the encrypted username and password from the database
    fetch_user_query = "SELECT username, password, shift FROM Williamson_Jacob_HW2;"
    result = db.query(fetch_user_query, ())

    for row in result:
        stored_encrypted_username = row[0]
        stored_encrypted_password = row[1]
        stored_shift = int(row[2])

        # Decrypt the stored username
        decrypted_username = decrypt_password(stored_encrypted_username, stored_shift)
        print(f"decrypted Username: {decrypted_username}")
        print(f"input Username: {username}")
        if decrypted_username == username:
            print("username matches.")
            if stored_shift == shift:
                print("shift matches.")
                # Decrypt the stored password if the username matches
                decrypted_password = decrypt_password(stored_encrypted_password, stored_shift)
                print(f"decrypted Password: {decrypted_password}")
                print(f"input Password: {password}")
                if decrypted_password == password:
                    print("password matches")
                    return True

    return False


# GUI for Login Screen
def create_login_screen(db):
    def attempt_login():
        username = entry_username.get().upper()
        password = entry_password.get().upper()
        # Need to convert shift from string to int
        shift = int(entry_shift.get())
        if authenticate_user(db, username, password, shift):
            messagebox.showinfo("Login Success", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    root = tk.Tk()
    root.title("Secure Login Screen")

    label_username = tk.Label(root, text="Username")
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    label_password = tk.Label(root, text="Password")
    label_password.grid(row=1, column=0)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    label_shift = tk.Label(root, text="Shift")
    label_shift.grid(row=2, column=0)
    entry_shift = tk.Entry(root)
    entry_shift.grid(row=2, column=1)

    login_button = tk.Button(root, text="Login", command=attempt_login)
    login_button.grid(row=3, columnspan=2)

    root.mainloop()


# Main Function
def main():
    # Connect to the database
    db = DBConnector.MyDB()

    # Create the users table
    create_users_table(db)

    # Insert sample users (comment this out after running once to avoid duplicate users)
    user_name = input("Give me a username to store in the database:").upper()
    password = input("Give me a password to store in the database:").upper()
    shift = int(input("Give me a key to shift both the username and password by:"))
    insert_user(db, user_name, password, shift)

    # Launch the login screen
    create_login_screen(db)


if __name__ == "__main__":
    main()