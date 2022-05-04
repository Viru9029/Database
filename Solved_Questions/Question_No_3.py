#3.  Generate the SQL statements to perform the following computations on table data in Python IDLE:

"""#a.List the names of all clients having ‘a’ as the second letter in their names.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "select name from client_master where name like '_a%'"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("Name of client : ",i[0])
cursor.close()
con.close()"""



"""#b. List the clients who stay in a city whose first letter is ‘M’.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "select name from client_master where city like 'M%'"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("Name of client(Who stay in starting letter 'M') : ",i[0])
cursor.close()
con.close()"""



"""#c. List all clients who stay in ‘Bangalore’ or ‘Mangalore’.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "select name from client_master where city ='Bangalore' or city='Mangalore'"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("Name of those client Who are stay in Bangalore or Mangalore. : ",i[0])
cursor.close()
con.close()"""


"""#d. List all clients whose BalDue is greater than value 10000.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "select name from client_master where baldue > 10000"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("Name of those client whose Balance due is greater then 10000 : ",i[0])
cursor.close()
con.close()
"""



"""#e.List all information from the Sales_order table for order placed in the month of June.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "select * from sales_order where to_char(orderdate,'MON') = 'JUN'"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("ORDERNO : ",i[0],"CLIENTNO : ",i[1],"ORDERDATE : ",i[2].strftime("%A, %b-%d-%Y"),"DELYADDR : ",i[3],"SALESMANNO : ",i[4],
          "DELYTYPE : ",i[5],"BILLTYPE : ",i[6],"DELYDATE : ",i[7].strftime("%A, %b-%d-%Y"),"ORDERSTATUS : ",i[8])
cursor.close()
con.close()"""

"""#f. List the Order No & day on which clients placed their order.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
#qury = "select orderno,orderdate from sales_order"
qury = "SELECT ORDERNO,TO_CHAR("ORDERDATE",'DAY') FROM SALES_ORDER"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    #print("Order No : ",i[0],"Day : ",i[1].strftime("%d"))
    print("Order No : ",i[0],"Day : ",i[1])
cursor.close()
con.close()"""



"""#g. List the names, city and state of clients who are not in the state of ‘Maharashtra’.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "select name,city from client_master where state != 'Maharashtra'"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("Name : ",i[0]," ","City : ",i[1])
cursor.close()
con.close()"""