import cx_Oracle
import config_oracle_to_python_connection as config
connection = cx_Oracle.connect(config.username,config.password,config.dsn,encoding=config.encoding)
cursor = connection.cursor()
qury = "create table world2(a integer,b varchar(50))"
cursor.execute(qury)
connection.commit()
print("Table created successfully")
cursor.close()
connection.close()