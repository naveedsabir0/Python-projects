import sqlite3
def check_tables(table_name):
conn=sqlite3.connect(db_file_name)
cur=conn.crusor()
res=cur.execute("SELECT name FROM sqlite_master where name=?",(table_name,))
result=res.fetchone()
conn.close()
if result is None:
    return True
else:
    return False

#To create a table into the database
def create_table():
    cur = conn.cursor()
    if check_tables('students'):
        cur.execute(f'''CREATE TABLE students(
        s_id INTEGER PRIMARY KEY AUTOINCREMENT,
        s_fname CARCHAR(30) NOT NULL,
        s_email TEXT)''')
    else:
        print(f"The students table already exists")
    conn.commit()


#To insert data into the table
def insert_into_table():
    cur.conn.cursor()
    cur.execute('''INSERT INTO students (s_fname, s_sname, s_email)VALUES)
    ('Sally','Smith','s@a.com'),
    ('Ali','Omar','s@a.com')
    ('Sam','White','s"S.com');
    ''')
    conn.commit()

#To delete a row
def del_row(student_id):
    cur=conn.cursor()
    cur.execute('DELETE FROM students WHERE s_id = ?', (student_id,))
    conn.commit()

def view_table():
    cur=conn.cursor()
    results=cur.execute("SELECT * FROM students")
    for i in results:
        print(i)


db_file_name = 
conn=cqlite3.connect(db_file_name)

