#4. Exercises on Using Having, Group By and Joins in Python IDLE:
"""
#a. Printing the description and total quantity sold for each product.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "select p.description,sum(s.qtyordered) from product_master p,sales_order_details s where s.productno=p.productno group by p.description"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("Description : ",i[0])
    print("Quanity : ",i[1])
cursor.close()
con.close()"""



#b. Calculating the average quantity sold for each client that has a maximum order value of 15000.00.
import cx_Oracle
con = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
cursor = con.cursor()
qury = "SELECT CM.CLIENTNO,CM.NAME, AVG(SOD.QTYDISP) FROM SALES_ORDER_DETAILS SOD, CLIENT_MASTER CM,SALES_ORDER SO " \
       "WHERE CM.CLIENTNO = SO.CLIENTNO AND SO.ORDERNO = SOD.ORDERNO GROUP BY CM.CLIENTNO,CM.NAME HAVING MAX(SOD.QTYORDERED * SOD.PRODUCTRATE) > 15000"
cursor.execute(qury)
result = cursor.fetchall()
for i in result:
    print("CLIENT NO : ",i[0],"  ","CLIENT NAME : ",i[1],"   ","ORDER AVERAGE : ",i[2])
cursor.close()
con.close()