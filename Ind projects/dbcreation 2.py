#Author: Naveed Sabir
#Date 15/11/2022
#Objective Simple CRUD application using SQLite

import sqlite3
import bcrypt
import getpass

con = sqlite3.connect('Timetables.db')
cur = con.cursor()

def create_user_table():
    #Create table to store accounts#
    cur.execute("""CREATE TABLE IF NOT EXISTS user
    (
        user_email TEXT PRIMARY KEY,
        user_password TEXT NOT NULL,
        user_role TEXT NOT NULL
    )
    """)
    # Save (commit) the changes
    con.commit()
    return


def create_user_account():
    #Get details and insert record in database#
    while True:
        user_email = input ("Enter user's email: "
        ).strip().lower()
        hidden_password = getpass.getpass("Enter user's password: ")
        plain_password = hidden_password.strip().encode('utf-8')
        # send plain_password as an argument to function
        # password returned will be hashed
        # .encode('utf-8') is requred for bcrypt
        user_password = hash_password(plain_password)
        role_choice = input("Is user admin? [Y], press ENTER for default: "
        ).strip().upper() 
        if role_choice == "Y":
            user_role = "admin"
        else:
            user_role = "default"
        insert_user_account(user_email, user_password, user_role)
        print(f"The following details have been entered",
            f"\nuser_email = {user_email}",
            f"\nuser_password = {user_password}",
            f"\nuser_role = {user_role}")
        add_another = input("Would you like to add another [Y/N] " ).strip().upper()
        while add_another not in ["Y", "N"]:
            add_another = input("Invalid option, choose [Y/N] ").strip().upper()
        if add_another == "N":
            break
    return

def hash_password(plain_password:str):
    #Hash and return user_password
    salt = bcrypt.gensalt()
    hashed_passsword = bcrypt.hashpw(plain_password, salt)
    return hashed_passsword


def insert_user_account(user_email:str, user_password:str, user_role:str):
    #accepts user details and stores in sqlite db table"""
    cur.execute("INSERT INTO user VALUES (?, ?, ?)" ,
                    (
                        user_email,
                        user_password,
                        user_role
                    )
                )
    con.commit()
    return


def check_password():
    #function uses bcyrpt to check if user is in database with matching password"""
    user_email = input("Enter email address for user: " ).lower().strip()
    password_to_check = input(f"Enter password for user <{user_email}>: " ).strip().encode('utf-8')
    cur.execute(""" SELECT user_password, user_role FROM user WHERE user_email = ?""", (user_email,))
    result = cur.fetchall()
    print(result) # test print for list of tuples returned
    fetched_password = result[0][0] # assign 1st value from the 1st record returned
    fetched_role = result[0][1] # assign 2nd value from the 1st record returned
    if bcrypt.checkpw(password_to_check, fetched_password):
        print(f"Record match found with <{fetched_role.upper()}> role.")
    else:
        print("Record not found. Possibly incorrect email or password.")
    return

def menu():
    #provides menu options and directs user to relevant function"""
    print("Choose of the the following: \n 1. Add record \n 2. Check record")
    choice = input("Enter corresponding number for option: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Error! Enter corresponding number for option: " ).strip()
    if choice == "1":
        create_user_account()
    else:
        check_password()
    return

create_user_table()
menu()
