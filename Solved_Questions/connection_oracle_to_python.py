import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
cursor.execute("create table kate1(a integer,b varchar(50))")
print("Table create successfully")
cursor.close()
con.close()
