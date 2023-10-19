#Author: Naveed Sabir
#Date 15/11/2022
#Objective Simple CRUD application using SQLite

import sqlite3
conn=sqlite3.connect('Students.db')

cur=conn.cursor()


def check_table_exist(table_name:str):
    #SQL statement checks counts number of table_names in the sqlite_master
    cur.execute (""" SELECT count(name) FROM sqlite_master WHERE type='table' 
    AND name= ?;
    """,(table_name,))

    count_of_tables=cur.fetchone()[0]
    conn.commit()

    if count_of_tables==1:
        return True
    else:
        return False


def create_student_table():
    #Creates a  student table
    if check_table_exist("student"):
        print("Table exists.")
    else:
        cur.execute("""CREATE TABLE student
        (
            Forename text,
            surname text,
            email text
        )
        """)
    conn.commit()

def insert_student_data(forename:str, surname:str, email:str):
    #accepts student data as args and inserts into student table"""
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (?, ?, ?)" , (forename,surname,email))
    conn.commit()
    return

def insert_student_record(): #insert record in table
    print("""collects data entered by user and sends to insert_student_data function""")
    forename = input("Please enter forename: ")
    surname = input("Please enter surname: ")
    email = input ("Please enter email: ")
    # send values as args to insert_student_data()
    insert_student_data(forename,surname,email)
    if menu_options == "1":
        insert_student_record()
    return



def menu_options():
    #MENU OPTIONS
    while True:
        print("""
        1. Insert a student record
        2. View all student records
        3. View one student record
        4. Delete one student record
        5. Update one student record
        6. Exit
        """)

        menu_choice = input("Please enter option between 1 and 6: ")

        menu_options = ["1", "2", "3", "4", "5", "6"]
        while menu_choice not in menu_options:
            menu_choice = input("Error! You must choose an option between 1 and 6: ")
            if menu_choice == "1":
                insert_student_record()
            elif menu_choice == "2":
                get_student_records()
            elif menu_choice == "3":
                get_one_student_record()
            elif menu_choice == "4":
                delete_one_student_record()
            elif menu_choice == "5":
                update_one_student_record()
            else:
                print("Good bye")
                conn.close()
                exit()
            continue_choice = input("Would you like to exit (Y/N): ").upper()
            if continue_choice == "Y":
                break
        print("Good bye")
        conn.close()
        exit()

def get_student_records():
    #output all student records"""
    cur = conn.cursor()
    print ("{:<2} {:<12} {:<12} {:<10}"
    .format("ID","Forename","Surname", "Email") 
    )
    for row in cur.execute("SELECT rowid, * FROM student"):
        print("{:<2} {:<12} {:<12} {:<10}"
        .format(row[0],row[1],row[2],row[3])
        )
    return

def get_one_student_record():
#output all student records
    cur = conn.cursor()
    student_id = input("Enter the ID of student: ")
    print ("{:<2} {:<12} {:<12} {:<10}"
    .format("ID","Forename","Surname", "Email")
    )
    for row in cur.execute("SELECT rowid, * FROM student WHERE rowid=?", student_id):
        print("{:<2} {:<12} {:<12} {:<10}"
        .format(row[0],row[1],row[2],row[3])
        )
    return

def delete_one_student_record():
    #delete one student from database"""
    cur = conn.cursor()
    get_student_records() # shows all records before delete process
    student_id = input("Enter student to delete: ")
    cur.execute("DELETE from student WHERE rowid=?", student_id,)
    conn.commit()
    get_student_records() # shows all records after delete process

def update_one_student_record():
    #allows a student record to be altered#
    get_student_records() # shows all records before update
    student_id = input("Enter student id for update: ")
    u_forename = input("Enter updated forename: ")
    u_surname = input("Enter updated forename: ")
    u_email = input("Enter updated forename: ")
    cur.execute("""UPDATE student
    SET forename = ?, surname = ?, email = ?
    WHERE rowid = ?""",(u_forename,u_surname, u_email, student_id))
    get_student_records() # shows all records after update




create_student_table()
menu_options()



