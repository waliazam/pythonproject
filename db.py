import sqlite3

#students
#teacher
#activities
#volitions
#results
#homework
#studentBody

# databse connection , it will create if not exist
con = sqlite3.connect("akhss.db")


curser = con.cursor()

curser.execute("""
               CREATE TABLE IF NOT EXISTS student(
                   
                   id INTEGER primary key autoincrement,
                   std_name TEXT,
                   std_roll INTEGER,
                   std_dept TEXT,
                   std_batch TEXT,
                   std_phone NUMBER,
                   std_email TEXT,
                   std_address TEXT,
                   std_class TEXT,
                   std_father TEXT,
                   std_gender TEXT
               )
                                            
               """)

curser.execute("""
               CREATE TABLE IF NOT EXISTS teacher (
                   id INTEGER primary key autoincrement,
                   t_name TEXT,
                   t_email TEXT,
                   t_phone TEXT,
                   t_address TEXT,
                   t_subject TEXT,
                   t_gender TEXT
               ) 
               """)

# curser.execute("""
#                insert into teacher(
#                    id,
#                    t_name,
#                    t_email,
#                    t_phone,
#                    t_address,
#                    t_subject,
#                    t_gender
#                ) values 
               
#                ("1" , "Ahmad", "ahmed.edu", "23233232", "Jutial", "Computer", "Male")
#                """)

curser.execute("""
               
               delete from teacher where t_name = 'Ahmad'
               """)

con.commit()
con.close()






