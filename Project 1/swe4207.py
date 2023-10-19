#Author: Naveed Sabir
#Date 13/01/2023
#Objective Assignment 1

import sqlite3
import bcrypt
import getpass
from termcolor import colored
import maskpass
from prettytable import from_db_cursor
from prettytable import prettytable
conn=sqlite3.connect('swe4207.db')

prettytable.PrettyTable()
cur=conn.cursor()



def check_table_exist(table_name:str):
    cur.execute (""" SELECT count(name) FROM sqlite_master WHERE type='table' 
    AND name= ?;""",(table_name,))

    count_of_tables=cur.fetchone()[0]
    conn.commit()

    if count_of_tables==1:
        return True
    else:
        return False

############ TABLE 1 ################
def create_user_table():
    #Create table to store user
    cur.execute("""CREATE TABLE IF NOT EXISTS user
    (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    );
    """)
    # Save (commit) the changes
    conn.commit()
    return

############ TABLE 2 ################
def create_customer_table():
    #Create table to store customers
    cur.execute("""CREATE TABLE IF NOT EXISTS customer
    (
        customerid INTEGER PRIMARY KEY AUTOINCREMENT,
        forename TEXT NOT NULL,
        surname TEXT,
        dob TEXT NOT NULL
    );
    """)
    #save changes
    conn.commit()
    return

############ TABLE 3 ################
def create_address_table():
    #Create table to store all the information related to the customer's address
    cur.execute("""CREATE TABLE IF NOT EXISTS address
    (
        addressid INTEGER PRIMARY KEY AUTOINCREMENT,
        streetnumber TEXT,
        firstline TEXT NOT NULL,
        postcode TEXT,
        region TEXT NOT NULL,
        country TEXT NOT NULL,
        customerid INTEGER NOT NULL,
        FOREIGN KEY(customerid) REFERENCES customer(customerid)
    );
    """)
    #save changes
    conn.commit()
    return

############ TABLE 4 ################
def create_account_table():
    #Create a table to store all the information about the account of the customer
    cur.execute("""CREATE TABLE IF NOT EXISTS account
    (
        accountid INTEGER PRIMARY KEY AUTOINCREMENT,
        balance REAL NOT NULL,
        opendate TEXT NOT NULL,
        closedate TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT "ACTIVE",
        customerid INTEGER NOT NULL,
        FOREIGN KEY(customerid) REFERENCES customer(customerid)
    );
    """)
    #save changes
    conn.commit()
    return

############ TABLE 5 ################
def create_tansaction_table():
    #Create a table to store transactions
    cur.execute("""CREATE TABLE IF NOT EXISTS transact
    (
        transactid INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        type TEXT NOT NULL,
        date TEXT NOT NULL,
        accountid INTEGER NOT NULL,
        FOREIGN KEY(accountid)REFERENCES account(accountid)
    );
    """)
    #save changes
    conn.commit()
    return

def create_authentication_table():
    #create a table that authenticates user information and makes sure its the right information
    cur.execute("""CREATE IF NOT EXISTS authentication
    (
        username TEXT NOT NULL PRIMARY KEY,
        password TEXT NOT NULL PRIMARY KEY,
        FOREIGN KEY(username) REFERENCES user(username)
        FOREIGN KEY(password) REFERENCES user(password)
    );
    """)
    #save changes
    conn.commit()
    return


#------------------USER CRUD-------------------------
# def create_user(username:str, password:str):
#     #accepts user details and stores in sqlite db table"""
#     cur.execute("INSERT INTO user VALUES (?, ?)" ,
#                     (
#                         username,
#                         password
#                     )
#                 )
#     conn.commit()
#     return

def insert_user_data(username:str, password:str):
    #accepts user data as args and inserts into user table
    cur=conn.cursor()
    cur.execute("INSERT OR REPLACE INTO user VALUES (?, ?)" , (username, password))
    conn.commit()
    return

def update_user_details():
    #Update user details in user table
    username = input("Enter username to update password: ").lower().strip()
    hidden_password = maskpass.askpass ("Enter new passwords: ")
    plain_password = hidden_password.strip().encode('utf-8')
    password = hash_password(plain_password)
    cur.execute("UPDATE user SET password = ? WHERE username = ?",(password, username,))
    conn.commit()
    return

def insert_user_record():
    #insert record in table
    #collects data entered by user and sends to insert_user_data function
    username = input("Please enter username: ")
    hash_password.password = input("Enter password: ")
    # send values as args to insert_user_data()
    insert_customer_data(username, hash_password.password)
    return

def view_user_details():
#output one user record
    cur = conn.cursor()
    print("""-----------------------------------------------------------------""")
    username = input("Enter the username of user: ")
    # print ("{:<20}".format("username"))
    # print("""-----------------------------------------------------------------""")
    # for row in cur.execute("SELECT * FROM user WHERE username = ?", (username,)):
    #     print("{:<20}".format(row[0]))
    cur.execute("SELECT * FROM user WHERE username = ?", (username,))
    table14=from_db_cursor(cur)
    print(table14)
    return

def get_user_records():
    #output all customer records
    cur = conn.cursor()
    print("""-----------------------------------------------------------------""")
    # print ("{:<3} {:<20} {:<16}".format("ID","username","password") 
    # )
    # print("""-----------------------------------------------------------------""")
    # for row in cur.execute("SELECT rowid, * FROM user"):
    #     print("{:<3} {:<20}".format(row[0], row[1]))
    cur.execute("SELECT rowid, * FROM user")
    table18=from_db_cursor(cur)
    print(table18)
    return

def delete_one_user():
    #delete one user from database
    cur = conn.cursor()
    get_user_records() # shows all records before delete process
    username = input("Enter user to delete: ")
    cur.execute("DELETE from user WHERE username = ?", (username,))
    conn.commit()
    get_user_records() # shows all records after delete process

#--------------CUSTOMER CRUD----------------
def create_customer(customerid:int, forename:str, surname:str, dob:str):
    #accepts customer details and stores in sqlite db table
    cur.execute("INSERT INTO customer VALUES (?, ?, ?, ?)" ,
                    (
                        customerid,
                        forename,
                        surname,
                        dob
                    )
                )
    conn.commit()
    return

def insert_customer_data(customerid:int,forename:str, surname:str, dob:str):
    #accepts customer data as args and inserts into customer table
    cur = conn.cursor()
    cur.execute("INSERT or IGNORE INTO customer VALUES (?, ?, ?, ?)" , (customerid,forename,surname,dob))
    conn.commit()
    return


def get_customer_records():
    #output all customer records
    #cur = conn.cursor()
    print(colored("""-----------------------------------------------------------------""","grey"))
    cur.connection.cursor()
    cur.execute("SELECT * FROM customer")
    table1=from_db_cursor(cur)
    print(table1)
    return

def view_customer_details():
#output one customer record
    cur = conn.cursor()
    customerid = input("Enter the ID of customer: ")
    print("""-----------------------------------------------------------------""")
    # print ("{:<10} {:<12} {:<12} {:<10}".format("customerid","forename","surname", "dob"))
    # for row in cur.execute("SELECT * FROM customer WHERE customerid = ?", customerid):
    #     print("{:<10} {:<12} {:<12} {:<10}"
    #     .format(row[0],row[1],row[2],row[3])
    #     )
    cur.execute("SELECT * FROM customer WHERE customerid = ?", (customerid,))
    table2=from_db_cursor(cur)
    print(table2)

    print("""-----------------------------------------------------------------""")
    return

def update_one_customer_record():
    #Change customer record
    get_customer_records() # shows all customers before update
    print("""-----------------------------------------------------------------""")
    customerid = input("Enter customer's id to update details of: ")
    forename = input("Enter updated forename: ")
    surname = input("Enter updated surname: ")
    dob = input("Enter updated dob: ")
    print("""-----------------------------------------------------------------""")
    cur.execute("UPDATE customer SET forename = ?, surname = ?, dob = ? WHERE customerid = ?", (forename,surname, dob, customerid))
    get_customer_records() # shows all records after update 

def insert_customer_record():
    #insert record in table
    print("""-----------------------------------------------------------------""")
    customerid = input("Please enter customer id: ")
    forename = input("Please enter forename: ")
    surname = input("Please enter surname: ")
    dob = input ("Please enter date of birth: ")
    print("""-----------------------------------------------------------------""")
    # send values as args to insert_student_data()
    insert_customer_data(customerid,forename,surname,dob)
    conn.commit()
    return

def delete_one_customer_record():
    #delete one customer from database
    cur = conn.cursor()
    print("""-----------------------------------------------------------------""")
    get_customer_records() # shows all records before delete process
    customerid = input("Enter customer to delete: ")
    cur.execute("DELETE from customer WHERE customerid = ?", (customerid,))
    conn.commit()
    get_customer_records() # shows all records after delete process

#--------------ACCOUNT CRUD----------------
def create_account(accountid:int, balance:int, opendate:str, closedate:str, status:str, customerid:int):
    #accepts account details and stores in sqlite db table
    cur.execute("INSERT INTO account VALUES (?, ?, ?, ?, ?, ?)" ,
                    (
                        accountid,
                        balance,
                        opendate,
                        closedate,
                        status,
                        customerid
                    )
                )
    conn.commit()
    return


def insert_account_data(accountid:int, balance:int, opendate:str, closedate:str, status:str, customerid:int):
    #accepts account data as args and inserts into account table
    cur = conn.cursor()
    cur.execute("INSERT INTO account VALUES (?, ?, ?, ?, ?, ?)" , (accountid, balance, opendate, closedate, status, customerid))
    conn.commit()
    return

def get_account_records():
    #output all account records
    cur = conn.cursor()
    # print("""-----------------------------------------------------------------""")
    # print ("{:<10} {:<12} {:<20} {:<20} {:<10} {:<10}"
    # .format("accountid","balance","opendate", "closedate", "status", "customerid") 
    # )
    # for row in cur.execute("SELECT * FROM account"):
    #     print("{:<10} {:<12} {:<12} {:<10} {:<10} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4],row[5])
    #     )
    
    # print("""-----------------------------------------------------------------""")
    cur.execute("SELECT * FROM account")
    table20=from_db_cursor(cur)
    print(table20)
    return

def view_account_details():
#output all account records
    cur = conn.cursor()
    accountid = input("Enter the ID of account: ")
    print("""-----------------------------------------------------------------""")
    # print("{:<10} {:<12} {:<12} {:<10} {:<10} {:<10}"
    # .format("accountid","balance","opendate", "closedate", "status", "customerid"))
    # for row in cur.execute("SELECT * FROM account WHERE accountid = ?", accountid):
    #     print("{:<10} {:<12} {:<12} {:<10} {:<10} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4],row[5]))
    cur.execute("SELECT * FROM account WHERE accountid = ?", (accountid,))
    table3=from_db_cursor(cur)
    print(table3)
    print("""-----------------------------------------------------------------""")
    return

def view_all_active_accounts():
    #output all active accounts
    cur = conn.cursor()
    status = "ACTIVE".upper()
    # print ("{:<10} {:<12} {:<12} {:<10} {:<10} {:<10}".format("accountid","balance","opendate", "closedate", "status", "customerid"))
    # for row in cur.execute("SELECT * FROM account WHERE status = 'ACTIVE'", status,):
    #     print("{:<10} {:<12} {:<12} {:<10} {:<10} {:<10} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    cur.execute("SELECT * FROM account WHERE status = ?", (status,))
    table4=from_db_cursor(cur)
    print(table4)
    return


def insert_account_record():
    accountid = input("Please enter account id: ")
    balance = input("Please enter balance: ")
    opendate = input("Please enter open date: ")
    closedate = input ("Please enter close date: ")
    status= input ("Please enter status: ")
    customerid = input("Please enter customer id: ")
    # send values as args to insert_account_data()
    insert_account_data(accountid, balance, opendate, closedate, status, customerid)

def update_one_account_record():
    #Change account record
    get_account_records() # shows all accounts before update
    accountid = input("Enter account id for update: ")
    balance = input("Enter balance for update: ")
    opendate = input("Enter opendate for update: ")
    closedate = input("Enter closedate for update: ")
    status = input("Enter status for update: ")
    customerid= input("Enter custome id for udpate: ")
    cur.execute("""UPDATE OR REPLACE account
    SET accountid = ?, balance = ?, opendate = ?, closedate = ?, status = ?, customerid = ?""",(accountid, balance, opendate, closedate, status, customerid))
    get_customer_records() # shows all records after update 


def close_one_account_record():
    # Close one account from database
    cur = conn.cursor()
    get_account_records() # shows all records before starting process
    accountid = input("Enter account id to set inactive: ")
    closedate = input("Enter account close date: ")
    cur.execute("""UPDATE account SET status = 'INACTIVE', closedate = ? WHERE accountid = ?""",(closedate, accountid,))
    conn.commit()
    return

#--------------Transaction CRUD----------------
def create_transaction(transactionid:int, amount:float, type:str, date:str, accountid:int):
    #Accepts transactions and stores in table
    cur.execute ("INSERT INTO  transact VALUES (?, ?, ?, ?, ?)" ,
                    (
                        transactionid,
                        amount,
                        type,
                        date,
                        accountid
                    )
                )
    conn.commit()
    return

def insert_transaction_data(transactionid:int, amount:int, type:str, date:str, accountid:int):
    #accepts transaction data as args and inserts into transaction table
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO transact VALUES (?, ?, ?, ?, ?)", (transactionid, amount, type, date, accountid,))
    conn.commit()
    return
 
def read_one_transact_based_on_account():
    #shows specific transaction based on account
    cur = conn.cursor()
    accountid = input("Enter the ID of account: ")
    # print("{:<10} {:<12} {:<12} {:<10} {:<10} {:<10}"
    # .format("accountid","balance","opendate", "closedate", "status", "customerid"))
    # for row in cur.execute("SELECT * FROM account WHERE accountid = ?", accountid):
    #     print("{:<10} {:<12} {:<12} {:<10} {:<10} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4],row[5]))
    cur.execute("SELECT * FROM transact WHERE accountid = ?", (accountid,))
    table6=from_db_cursor(cur)
    print(table6)
    #"SELECT t.transactid, t.amount, t.type, t.date, t.accountid FROM transact AS t INNER JOIN account AS a ON t.accountid = a.accountid WHERE t.accountid=?"
    date = input("Please enter date of transaction ")
    customerid = input("Please enter customer id to check transactions of ")
    # for row in cur.execute("SELECT t.transactid, t.amount, t.type, t.date, t.accountid FROM transact AS t INNER JOIN account AS a ON a.accountid = t.accountid INNER JOIN customer AS c ON c.customerid = a.customerid WHERE date=? AND c.customerid=?" ,(date, customerid,)):
    #     print('{:<10} {:<12} {:<12} {:<10} {:<10}'.format(row[0],row[1],row[2],row[3],row[4]))
    cur.execute("SELECT t.transactid, t.amount, t.type, t.date, t.accountid FROM transact AS t INNER JOIN account AS a ON a.accountid = t.accountid INNER JOIN customer AS c ON c.customerid = a.customerid WHERE date=? AND c.customerid=?" ,(date, customerid,))
    table5=from_db_cursor(cur)
    print(table5)
    return


def get_transaction_records():
    #output all transaction records
    cur = conn.cursor()
    # print("""-----------------------------------------------------------------""")
    # print ("{:<2} {:<10} {:<5} {:<10} {:<10} {:<10}".format("ID","transactionid, amount, type, date, accountid"))
    # for row in cur.execute("SELECT * FROM transact"):
    #     print('{:<10} {:<5} {:<10} {:<10} {:<10}'
    #     .format(row[0],row[1],row[2],row[3],row[4])
    #     )
    cur.execute("SELECT * FROM transact")
    table7=from_db_cursor(cur)
    print(table7)
    return

def view_transact_of_account(): #new
    #output transactions of an account
    cur = conn.cursor()
    accountid = input("Enter account ID to print transactions: ")
    #print ("{:<2} {:<5} {:<10} {:<6} {:<2}".format("accountid, amount, type, date, transactionid"))
    # print("""-----------------------------------------------------------------""")
    # print ("{:<10}".format("accountid"),end=" ")
    # print ("{:<5}".format("amount"),end=" ")
    # print ("{:<10}".format("type"),end=" ")
    # print ("{:<6}".format("date"),end=" ")
    # print ("{:<10}".format("transactionid"))
    # for row in cur.execute("""SELECT t.transactid, t.amount, t.date, t.accountid 
    #                     FROM transact AS t INNER JOIN account AS a ON t.accountid = a.accountid
    #                     WHERE a.status = 'ACTIVE' AND t.accountid = ?""",(accountid,)):
    #     print("{:<10} {:<5} {:<10} {:<10} {:<10}".format(row[0],row[1],row[2],row[3],row[4]))
    cur.execute("""SELECT t.transactid, t.amount, t.date, t.accountid 
                        FROM transact AS t INNER JOIN account AS a ON t.accountid = a.accountid
                        WHERE a.status = 'ACTIVE' AND t.accountid = ?""",(accountid,))
    table8=from_db_cursor(cur)
    print(table8)
    return

def view_transact_date(): #new
    #output transactions based on date
    cur = conn.cursor()
    accountid = input("Enter account ID to print transactions based on a date: ")
    date1 = input("Enter date: ")
    date2 = input("Enter second date: ")
    #print ("{:<2} {:<5} {:<10} {:<6} {:<2}".format("accountid, amount, type, date, transactionid"))
    # print("""-----------------------------------------------------------------""")
    # print ("{:<10}".format("accountid"),end=" ")
    # print ("{:<5}".format("amount"),end=" ")
    # print ("{:<10}".format("type"),end=" ")
    # print ("{:<6}".format("date"),end=" ")
    # print ("{:<10}".format("transactionid"))
    # for row in cur.execute("SELECT * FROM transact WHERE accountid = ? AND date BETWEEN ? AND ?", (accountid, date1, date2)):
    #     print("{:<10} {:<5} {:<10} {:<10} {:<10}".format(row[0],row[1],row[2],row[3],row[4]))
    cur.execute("SELECT * FROM transact WHERE accountid = ? AND date BETWEEN ? AND ?", (accountid, date1, date2))
    table9=from_db_cursor(cur)
    print(table9)
    return


def view_transaction_customer():
#output all transact records
    cur = conn.cursor()
    customerid = input("Enter the customer ID to view transactions: ")
    date1 = input("Enter date: ")
    date2 = input("Enter second date: ")
    #print ("{:<2} {:<5} {:<10} {:<6} {:<2}".format("transactionid, amount, type, date, accountid"))
    # print("""-----------------------------------------------------------------""")
    # print ("{:<10}".format("accountid"),end=" ")
    # print ("{:<5}".format("amount"),end=" ")
    # print ("{:<10}".format("type"),end=" ")
    # print ("{:<10}".format("date"),end=" ")
    # print ("{:<10}".format("accountid"),end=" ")
    # print ("{:<10}".format("customerid"))
    # for row in cur.execute("SELECT * FROM account as a  WHERE transactid = ? date BETWEEN ? AND ?", transactionid, date1, date2):
    #     print("{:<10} {:<5} {:<10} {:<6} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4])
    #     )
    # return
    # for row in cur.execute("SELECT t.transactid, t.amount, t.type, t.date, t.accountid, a.customerid FROM transact AS t INNER JOIN account AS a ON t.accountid = a.accountid WHERE a.customerid = ?", (customerid,)):
    #     print("{:<10} {:<5} {:<10} {:<10} {:<10} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4], row[5])
    #     )
    cur.execute("SELECT t.transactid, t.amount, t.type, t.date, t.accountid, a.customerid FROM transact AS t INNER JOIN account AS a ON t.accountid = a.accountid WHERE a.customerid = ?", (customerid,))
    table10=from_db_cursor(cur)
    print(table10)
    return

def view_all_transactions_of_account():
#output all transact records
    cur = conn.cursor()
    accountid = input("Enter account ID to print transactions: ")
    print("""-----------------------------------------------------------------""")
    #print ("{:<2} {:<5} {:<10} {:<6} {:<2}".format("transactionid, amount, type, date, accountid"))
    # print ("{:<10}".format("transactionid"),end=" ")
    # print ("{:<5}".format("amount"),end=" ")
    # print ("{:<10}".format("type"),end=" ")
    # print ("{:<10}".format("date"),end=" ")
    # print ("{:<10}".format("accountid"),end=" ")
    #print ("{:<10}".format("customerid"))
    # for row in cur.execute("SELECT * FROM account as a  WHERE transactid = ? date BETWEEN ? AND ?", transactionid, date1, date2):
    #     print("{:<10} {:<5} {:<10} {:<6} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4])
    #     )
    # return
    # for row in cur.execute("SELECT t.transactid, t.amount, t.type, t.date, t.accountid FROM transact AS t INNER JOIN account AS a ON t.accountid = a.accountid WHERE t.accountid=?", (accountid,)):
    #     print("{:<10} {:<5} {:<10} {:<10} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4])
    #     )
    print("""-----------------------------------------------------------------""")
    cur.execute("SELECT t.transactid, t.amount, t.type, t.date, t.accountid FROM transact AS t INNER JOIN account AS a ON t.accountid = a.accountid WHERE t.accountid=?", (accountid,))
    table11=from_db_cursor(cur)
    print(table11)
    return



def insert_transaction_record():
    #print("""collects data entered by user and sends to insert_transaction_data function""")
    transactionid = input("Please enter trasnaction id: ")
    amount = input("Please enter amount: ")
    type = input("Please enter type: ")
    date = input ("Please enter date: ")
    accountid = input("Please enter account id: ")
    # send values as args to insert_transaction_data()
    insert_transaction_data(transactionid, amount, type, date, accountid)
    # cur.execute("SELECT balance FROM account WHERE accountid = ?",(accountid,))
    # if type == 'CREDIT':
    #     cur.execute("UPDATE account SET balance = ?",(,))
    # else:
    #     cur.execute("UPDATE account SET balance = ?",(balance3+amount,))
    conn.commit()
    return


def update_one_transaction_record():
    #Change account record
    get_transaction_records() # shows all transactions before update
    transactionid = input("Enter transaction id for update: ")
    amount = input("Enter amount for update: ")
    type = input("Edit type of transaction ")
    date = input("Enter transaction date for update: ")
    accountid = input("Enter account id for update: ")
    cur.execute("""UPDATE transact
    SET transactid = ?, amount = ?, type = ?, date = ?, accountid = ?
    WHERE rowid = ?""",(transactionid, amount, type, date, accountid))
    get_transaction_records() # shows all records after update

def delete_one_transaction_record():
    #delete one transaction from database
    cur = conn.cursor()
    get_transaction_records() # shows all records before delete process
    transactionid = input("Enter transaction to delete: ")
    cur.execute("DELETE from transact WHERE rowid=?", transactionid)
    conn.commit()
    get_transaction_records() # shows all records after delete process

#--------------Address CRUD----------------
# def create_address(addressid:int, streetnumber:str, firstline:str, postcode:str, region:str, country:str, customerid:int):
#     #Accepts addresses and stores in table
#     cur.execute ("INSERT INTO  address VALUES (?, ?, ?, ?, ?, ?, ?)" ,
#                     (
#                         addressid,
#                         streetnumber,
#                         firstline,
#                         postcode,
#                         region,
#                         country,
#                         customerid
#                     )
#                 )
#     conn.commit()
#     return

def insert_address_data(addressid:int, streetnumber:str, firstline:str, postcode:str, region:str, country:str, customerid:int):
    #accepts address data as args and inserts into transaction table
    cur = conn.cursor()
    cur.execute("INSERT INTO address VALUES (?, ?, ?, ?, ?, ?, ?)" , (addressid, streetnumber, firstline, postcode, region, country, customerid))
    conn.commit()
    return

def get_address_records():
    #output all address records
    cur = conn.cursor()
    #print ("{:<2} {:<3} {:<20} {:<6} {:<15} {:<12} {:<2}".format("addressid, streetnumber, firstline, postcode, region, country, customerid"))
    # print("""-----------------------------------------------------------------""")
    # print ("{:<10}".format("addressid"),end = " ")
    # print ("{:<3}".format("streetnumber"),end = " ")
    # print ("{:<20}".format("firstline"),end = " ")
    # print ("{:<6}".format("postcode"),end = " ")
    # print ("{:<15}".format("region"),end = " ")
    # print ("{:<12}".format("country"),end = " ")
    # print ("{:<10}".format("customerid"))
    # for row in cur.execute("SELECT * FROM address"):
    #     print("{:<10} {:<3} {:<20} {:<6} {:<15} {:<12} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    #     )
    # print("""-----------------------------------------------------------------""")
    cur.execute("SELECT * FROM address")
    table12=from_db_cursor(cur)
    print(table12)
    return

def view_address_details():
#output one address record
    cur = conn.cursor()
    print("""-----------------------------------------------------------------""")
    customerid = input("Enter the customer ID to print address: ")
    #print ("{:<2} {:<3} {:<20} {:<6} {:<15} {:<12} {:<2}".format("addressid, streetnumber, firstline, postcode, region, country, customerid"))
    # print ("{:<10}".format("addressid"),end = " ")
    # print ("{:<3}".format("streetnumber"),end = " ")
    # print ("{:<20}".format("firstline"),end = " ")
    # print ("{:<6}".format("postcode"),end = " ")
    # print ("{:<15}".format("region"),end = " ")
    # print ("{:<12}".format("country"),end = " ")
    # print ("{:<10}".format("customerid"))
    # for row in cur.execute("SELECT *  FROM address WHERE customerid = ?", (customerid,)):
    #     print("{:<10} {:<3} {:<20} {:<6} {:<15} {:<12} {:<10}"
    #     .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    #     )
    print("""-----------------------------------------------------------------""")
    cur.execute("SELECT *  FROM address WHERE customerid = ?", (customerid,))
    table13=from_db_cursor(cur)
    print(table13)
    return

def insert_address_record():
    print("""-----------------------------------------------------------------""")
    addressid = input("Please enter address id: ")
    streetnumber = input("Please enter streetnumber: ")
    firstline = input("Please enter firstline: ")
    postcode = input ("Please enter postcode: ")
    region = input ("Please enter region: ")
    country = input ("Please enter country: ")
    customerid = input ("Please enter customer id: ")
    print("""-----------------------------------------------------------------""")
    # send values as args to insert_address_data()
    insert_address_data(addressid, streetnumber, firstline, postcode, region, country, customerid)

def update_one_address_record():
    #Change address record
    get_address_records() # shows all addresses before update
    print("""-----------------------------------------------------------------""")
    addressid = input("Enter address id for update: ")
    streetnumber = input("Enter streetnumber for update: ")
    firstline = input("Enter firstline for update: ")
    postcode = input("Enter postcode for update: ")
    region = input("Enter region for update: ")
    country = input("Enter country for update: ")
    customerid = input("Enter customer id for update: ")
    print("""-----------------------------------------------------------------""")
    cur.execute("""UPDATE OR REPLACE address
    SET addressid = ?, streetnumber = ?, firstline = ?, postcode = ?, region = ?, country = ?, customerid = ?""",(addressid, streetnumber, firstline, postcode, region, country, customerid,))
    get_address_records() # shows all records after update

def delete_one_address_record():
    #delete one address from database
    cur = conn.cursor()
    get_address_records() # shows all records before delete process
    addressid = input("Enter address to delete: ")
    print("""-----------------------------------------------------------------""")
    cur.execute("DELETE from address WHERE addressid = ?", (addressid,))
    conn.commit()
    get_address_records() # shows all records after delete process

########################################################################
#Account creation

def create_user_account():
    #Get details and insert record in database#
    while True:
        username = input ("Enter username: "
        ).strip().lower()
        hidden_password = maskpass.askpass("Enter user's password: ")
        plain_password = hidden_password.strip().encode('utf-8')
        # send plain_password as an argument to function
        # password returned will be hashed
        # .encode('utf-8') is requred for bcrypt
        password = hash_password(plain_password)
        insert_user_data(username, password)
        print(f"The following details have been entered",
            f"\nuser_username = {username}",
            f"\nuser_password = {password}")
        add_another = input("Would you like to add another [Y/N] " ).strip().upper()
        while add_another not in ["Y", "N"]:
            add_another = input("Invalid option, choose [Y/N] ").strip().upper()
        if add_another == "Y".strip().upper:
            print(" ")
        if add_another == "N".strip().upper():
            break
                
            


def check_password():
    #function uses bcyrpt to check if user is in database with matching password"""
    print("""-----------------------------------------------------------------""")
    username = input("Enter username for login: " ).lower().strip()
    password_to_check = maskpass.askpass(f"Enter password for user <{username}>: " )
    password_to_check2= password_to_check.strip().encode('utf-8')
    cur.execute(""" SELECT password FROM user WHERE username = ?""", (username,))
    result = cur.fetchall()
    print(result) # test print for list of tuples returned
    fetched_password = result[0][0] # assign 1st value from the 1st record returned
    if bcrypt.checkpw(password_to_check2, fetched_password):
        print(f"Record match found with <{username.upper()}> username.")
        menu_options()
    else:
        print("Record not found. Possibly incorrect username or password.")
    print("""-----------------------------------------------------------------""")
    return

def hash_password(plain_password:str):
    #Hash and return user_password
    salt = bcrypt.gensalt()
    hashed_passsword = bcrypt.hashpw(plain_password, salt)
    return hashed_passsword



def newclient():
    #Create customer, address, account and transaction for new users.
    #Default inputs once the user register's his user account.
    print(colored("""* * * * * * * * * * * * * *
            WELCOME
* * * * * * * * * * * * * *

Please create customer: ""","green"))
    print("""-----------------------------------------------------------------""")
    insert_customer_record()
    print("Please create address: ")
    print("""-----------------------------------------------------------------""")
    insert_address_record()
    print("Please create account: ")
    print("""-----------------------------------------------------------------""")
    insert_account_record()
    print("Please create transaction: ")
    print("""-----------------------------------------------------------------""")
    insert_transaction_record()
    return

#################### PrettyTable Tables #######################
mytable=prettytable.PrettyTable(['NO.','MENU OPTION'])
mytable.add_row(['0','Create customer details'])
mytable.add_row(['1','View customers details.'])
mytable.add_row(['2','Update customers details.'])
mytable.add_row(['3','Record new transactions relating to individual customers.'])
mytable.add_row(['4','Mark accounts as closed using status and date fields.'])
mytable.add_row(['5','View a customers transactions for a specific date range.'])
mytable.add_row(['6','View all transactions for a specific date range.'])
mytable.add_row(['7','View sub menu.'])
mytable.add_row(['8','EXIT'])

mysubtable1=prettytable.PrettyTable(['NO.','USER SETTINGS'])
mysubtable1.add_row(['1','Read ALL users'])
mysubtable1.add_row(['2','Read ONE user'])
mysubtable1.add_row(['3','Update user details'])
mysubtable1.add_row(['4','Delte user'])
mysubtable2=prettytable.PrettyTable(['NO.','CUSTOMER SETTINGS'])
mysubtable2.add_row(['5','Read customers'])
mysubtable2.add_row(['6','Read ONE customer'])
mysubtable2.add_row(['7','Update ONE customer'])
mysubtable2.add_row(['8','Delete one Customer'])
mysubtable3=prettytable.PrettyTable(['NO.','ADDRESS SETTINGS'])
#mysubtable.add_row(['MENU NO.','ADDRESS SETTINGS'])
mysubtable3.add_row(['8b','Insert address for a customer'])
mysubtable3.add_row(['9','Read customer address'])
mysubtable3.add_row(['10','Read ONE customer address'])
mysubtable3.add_row(['11','Update address'])
mysubtable3.add_row(['12','Delete address'])
mysubtable4=prettytable.PrettyTable(['NO.','ACCOUNT SETTINGS'])
#mysubtable.add_row(['MENU NO.','ACCOUNT SETTINGS'])
mysubtable4.add_row(['12b','Create account'])
mysubtable4.add_row(['13','Read ONE account'])
mysubtable4.add_row(['14','Read all open active accounts'])
mysubtable4.add_row(['15','Update account details'])
mysubtable4.add_row(['15b','Close account'])
mysubtable5=prettytable.PrettyTable(['NO.','TRANSACTION SETTINGS'])
#mysubtable.add_row(['MENU NO.','TRANSACTION SETTINGS'])
mysubtable5.add_row(['15c','Create transaction'])
mysubtable5.add_row(['16','Read ONE transaction'])
mysubtable5.add_row(['17','Read ALL transactions from an account'])
mysubtable5.add_row(['18','Update Transaction'])
mysubtable5.add_row(['19','Delete transaction'])
mysubtable6=prettytable.PrettyTable(['NO.','GENERAL SETTINGS'])
#mysubtable5.add_row(['MENU NO.','GENERAL OPTIONS'])
mysubtable6.add_row(['20','View main menu'])
mysubtable6.add_row(['21','Exit process'])

mymainmenu=prettytable.PrettyTable(['WELCOME'])
mymainmenu.add_row(['Enter Main Menu'])
mymainmenu.add_row(['Enter Sub Menu'])
mymainmenu.add_row(['EXIT'])
mymainmenu.add_autoindex('NO.')

#################### PrettyTable Tables #######################


def menu_options():
    #MENU OPTIONS

    continue_choice = "Y".upper() 
    while True:
        print(mymainmenu)

        menu_choice = input(colored("Please enter option between 1 and 3: ","yellow"))
        menu_options1 = ["1","2","3"]
        while menu_choice in menu_options1:
            if menu_choice not in menu_options1:
                menu_choice = input(colored("Error! You must chooce an option between 1 and 3: ","red"))
            elif menu_choice == "1":
                print(mytable)
#                 print("""


# 0.Create customer details.
# 1. View customers details.
# 2. Update customers details.
# 3. Record new transactions relating to individual customers.
# 4. Mark accounts as closed using status and date fields.
# 5. View a customers transactions for a specific date range.
# 6. View all transactions for a specific date range.
# 7. View sub menu.
# 8. Exit


#""")
                mainmenu_choice = input(colored("Please enter option between 0 and 8: ","yellow"))
                mainmenu_options = ["0","1","2","3","4","5","6","7","8"]
                while mainmenu_choice in mainmenu_options:
                    if mainmenu_choice not in mainmenu_options:
                        mainmenu_choice = input(colored("Error! You must choose an option between 0 and 8: ","red"))
                    elif mainmenu_choice == "0":
                        insert_customer_record()
                    elif mainmenu_choice == "1":
                        view_customer_details() #done
                    elif mainmenu_choice == "2":
                        update_one_customer_record() #done
                    elif mainmenu_choice== "3":
                        insert_transaction_record() #done
                    elif mainmenu_choice=="4":
                        close_one_account_record()
                    elif mainmenu_choice=="5":
                        view_transaction_customer()
                    elif mainmenu_choice == "6":
                        view_transact_date()
                    elif mainmenu_choice == "7":
                        menu_choice = "2"
                    elif mainmenu_choice == "8":
                        print(colored("Good bye","yellow"))
                        conn.close()
                        exit()
                    else:
                        print(colored("Error","red","red"))
                    if mainmenu_choice != "7":
                        continue_choice = input(colored("Would you like to exit (Y/N): ","yellow")).upper()
                    if continue_choice == "Y".upper():
                        break
                    else:
                        menu_choice = "2"
                        #mainmenu_choice = input("Please enter option between 0 and 7: ")
            elif menu_choice == "2":
                print("""-----------------------------------------------------------------""")
                print(mysubtable1)
                print(""" """)
                print(mysubtable2)
                print(""" """)
                print(mysubtable3)
                print(""" """)
                print(mysubtable4)
                print(""" """)
                print(mysubtable5)
                print(""" """)
                print(""" """)
                print(mysubtable6)
                print("""-----------------------------------------------------------------""")

#                 print("""


# ******USER SETTINGS******
# 1. Read all users
# 2. Read one user
# 3. Update user details
# 4. Delete user
# ******CUSTOMER SETTINGS******
# 5. Read Customers
# 6. Read one Customer
# 7. Update one Customer
# 8. Delete one Cucstomer
# ******ADDRESS SETTINGS******
# 8b. Insert address for a customer
# 9. Read Customer Address
# 10. Read one Customer Address
# 11. Update Address
# 12. Delete Address
# ******ACCOUNT SETTINGS******
# 12b. Create account
# 13. Read one Account
# 14. Read all open Active Accounts
# 15. Update Account details
# 15b. Close Account
# ******TRANSACTION SETTINGS******
# 15c. Create transaction
# 16. Read one transaction
# 17. Read all transactions from an account
# 18. Update transaction
# 19. Delete transaction
# 20. View main menu
# 21. Exit


# """)
                submenu_choice = input(colored("Please enter option between 1 and 21: ","yellow"))
                submenu_options2 = ["1","2","3","4","5","6","7","8","8b","9","10","11","12","12b","13","14","15","15b","15c","16","17","19","20","21"]
                while submenu_choice in submenu_options2:
                    if submenu_choice not in submenu_options2:
                        submenu_choice = input(colored("Error! You must choose an option between 1 and 21: ","red"))
                    if submenu_choice == "1":
                        get_user_records()
                    elif submenu_choice == "2":
                        view_user_details()
                    elif submenu_choice == "3":
                        update_user_details()
                    elif submenu_choice == "4":
                        delete_one_user()
                    elif submenu_choice == "5":
                        get_customer_records()
                    elif submenu_choice == "6":
                        view_customer_details()
                    elif submenu_choice == "7":
                        update_one_customer_record()
                    elif submenu_choice =="8":
                        delete_one_customer_record()
                    elif submenu_choice == "8b":
                        insert_address_record()
                    elif submenu_choice == "9":
                        get_address_records()
                    elif submenu_choice == "10":
                        view_address_details()
                    elif submenu_choice == "11":
                        update_one_address_record()
                    elif submenu_choice == "12":
                        delete_one_address_record()
                    elif submenu_choice == "12b":
                        insert_account_record()
                    elif submenu_choice == "13":
                        view_account_details()
                    elif submenu_choice == "14":
                        view_all_active_accounts()
                    elif submenu_choice == "15":
                        update_one_account_record()
                    elif submenu_choice == "15b":
                        close_one_account_record()
                    elif submenu_choice == "15c":
                        insert_transaction_record()
                    elif submenu_choice == "16":
                        read_one_transact_based_on_account()
                    elif submenu_choice == "17":
                        view_all_transactions_of_account()
                    #elif submenu_choice == "18":
                        #update_one_transaction_record()
                    elif submenu_choice == "19":
                        delete_one_transaction_record()
                    elif submenu_choice == "20":
                        print(mymainmenu)
                        print("""-----------------------------------------------------------------""")
#                         print("""

# 1. Enter Main Menu
# 2. Enter Sub Menu
# 3. Exit""")
                        menu_choice = input(colored("Please enter option between 1 and 3: ","yellow")) 
                    elif submenu_choice == "21":
                        print("""-----------------------------------------------------------------""")
                        print(colored("Good Bye","yellow"))
                        exit()
                    else:
                        print("""-----------------------------------------------------------------""")
                        continue_choice == 'Y'
                        continue_choice = input(colored("Would you like to exit (Y/N): ","yellow")).upper()
                    if continue_choice == "Y":
                        break
            elif menu_choice == "3":
                print("""-----------------------------------------------------------------""")
                continue_choice = input(colored("Would you like to exit (Y/N): ","yellow")).upper()
                if continue_choice == "Y":
                    print(colored("Thank you, Good bye","yellow"))
                    exit()
                elif continue_choice == "N":
                    menu_options()
                else:
                    continue_choice = input(colored("Would you like to exit (Y/N): ","yellow")).upper()
            else:
                print("""-----------------------------------------------------------------""")
                print(mymainmenu)
                print("""-----------------------------------------------------------------""")

                menu_choice = input(colored("Please enter option between 1 and 3: ","yellow"))  
        menu_options()
        conn.close()
        return

print("""
#Author: Naveed Sabir
#Date 20/01/2023
#Objective Assignment 1
------------------------------------------------------------------
BSc Degree in Computing|BEng Degree in Software EngineeringSWE4207:
Computer Science Fundamentals
Francis Morrissey | Dr Mohammed Benmubarak | Aamir Abbas
1.Design, development, and testing 80% of overall module grade
Approximately 10 minutes for screencast
Report, Code and Screencast must be submitted before 20/01/2023@2355 via Moodle For late submission""")



create_user_table()
create_customer_table()
create_address_table()
create_account_table()
create_tansaction_table()
while True:
    option = input(colored("""
1.LOGIN.
2.REGISTER.

Selected option ""","yellow"))
    print("""-----------------------------------------------------------------""")
    options = ["1", "2"]
    while option in options:
        if option not in options:
            print(colored("Please try again by choosing 1 to LOGIN or 2 to REGISTER","red"))
            print("""-----------------------------------------------------------------""")
            option = input(colored("""
1.LOGIN.
2.REGISTER.

Please select option 1 or 2: ""","yellow"))
            print("""-----------------------------------------------------------------""")
        elif option == "1":
            check_password()
            #menu_options()
        elif option == "2":
            create_user_account()
            newclient()
            menu_options()
        else:
            exit()
#     option = input("""
# PLEASE TRY AGAIN

# 1.LOGIN.
# 2.REGISTER.

# Selected option """)