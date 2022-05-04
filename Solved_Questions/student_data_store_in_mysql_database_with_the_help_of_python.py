import mysql.connector
def insert_data_to_student_table(name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number):
    conn = mysql.connector.connect(host='localhost',database='pgdai',user='root',password='Viru9029')
    qury = "insert into student_details(name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number) values(%s,%s,%s,%s,%s,%s,%s)"
    cursor = conn.cursor()
    record_tuple = (name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number)
    cursor.execute(qury,record_tuple)
    conn.commit()
    print("Congratulation! Inserted Record Successfully")
    cursor.close()
    conn.close()

flag = True
while flag:
    loop = int(input("Hello!\nPress 1.To Enter the Record.\nPress 2.To Exit\nEnter choice : "))
    if loop==1:
        #Taking data from user
        name = input("Student Name : ")
        roll_no = int(input("Roll No : "))
        standard = int(input("Standard : "))
        division = input("Division : ")
        address = input("Address : ")
        student_mobile_number = input("Student Mobile No : ")
        parent_mobile_number = input("Parent Mobile No :")
        insert_data_to_student_table(name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number)
    if loop==2:
        flag=False
