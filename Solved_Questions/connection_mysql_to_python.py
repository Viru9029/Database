import mysql.connector
#conncetion by using dictonary
#con_data = {'user':'root','password':'Viru9029','host':'localhost','database':'pgdai'}
#connection = mysql.connector.connect(**con_data)
connection = mysql.connector.connect(host='localhost',database='pgdai',user='root',password='Viru9029')
if connection.is_connected():
    print(connection.get_server_info())
    cursor = connection.cursor()
    cursor.execute("select database();")
    record=cursor.fetchone()
    print("You are connected to database : ",record)
    cursor.close()
    connection.close()