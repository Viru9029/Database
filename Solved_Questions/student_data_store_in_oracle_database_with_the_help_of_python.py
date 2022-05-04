import cx_Oracle
def insert_data_to_student_table(name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number):
    conn = cx_Oracle.connect("system/Viru9029@localhost:1521/orcl")
    #qury = "insert into student_details(name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number) values('KATE VIRENDRA BHAGWAN',1254,12,'A','AT POST : DONGAR AKHEGAON','9029121249','8308540443')"
    qury = ('insert into student_details(name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number)' 
            'values(:name,:roll_no,:standard,:division,:address,:student_mobile_number,:parent_mobile_number)')
    cursor = conn.cursor()
    record_list = [name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number]
    cursor.execute(qury,record_list)
    conn.commit()
    print("Congratulation! Inserted Record Successfully")
    cursor.close()
    conn.close()

if __name__ == '__main__':
    #Taking data from user
    name = input("Student Name : ")
    roll_no = int(input("Roll No : "))
    standard = int(input("Standard : "))
    division = input("Division : ")
    address = input("Address : ")
    student_mobile_number = input("Student Mobile No : ")
    parent_mobile_number = input("Parent Mobile No :")
    insert_data_to_student_table(name,roll_no,standard,division,address,student_mobile_number,parent_mobile_number)
    #insert_data_to_student_table('KATE VIRENDRA',1254,12,'A','AT POST : DON','90291','83085')