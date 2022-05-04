# Database
Oracle and MySQL

Lab - Working with Database in Python Programming

1. Create the following tables:
Table name: CLIENT_MASTER
Column Name	Data Type	Size	Attributes
CLIENTNO	Varchar2	6	Primary Key / First letter must start with ‘C’
NAME	Varchar2	20	Not Null
CITY	Varchar2	15	
PINCODE	Number	8	
STATE	Varchar2	15	
BALDUE	Number	10,2	

Table_Name: PRODUCT_MASTER
Column Name	Data Type	Size	Attributes
PRODUCTNO	Varchar2	6	Primary Key / First letter must start with ‘P’
DESCRIPTION	Varchar2	15	Not Null
PROFITPERCENT	Number	4,2	Not Null
UNITMEASURE	Varchar2	10	Not Null
QTYONHAND	Number	8	Not Null
REORDERLVL	Number	8	Not Null
SELLPRICE	Number	8,2	Not Null, cannot be 0
COSTPRICE	Number	8,2	Not Null, cannot be 0

Table_Name: SALESMAN_MASTER
Column Name	Data Type	Size	Attributes
SALESMANNO	Varchar2	6	Primary Key / First letter must start with ‘S’	
SALESMANNAME	Varchar2	20	Not Null
ADDRESS1	Varchar2	30	Not Null
ADDRESS2	Varchar2	30	
CITY	Varchar2	20	
PINCODE	Number	8	
STATE	Varchar2	20	
SALAMT	Number	8,2	Not Null, cannot be 0
TGTTOGET	Number	6,2	Not Null, cannot be 0
YTDSALES	Number	6,2	Not Null
REMARKS	Varchar2	60	

Table_Name: SALES_ORDER
Column Name	Data Type	Size	Attributes
ORDERNO	Varchar2	6	Primary Key / First letter must start with ‘O’
CLIENTNO	Varchar2	6	Foreign Key references ClientNo of Client_Master table
ORDERDATE	Date		Not Null
DELYADDR	Varchar2	25	
SALESMANNO	Varchar2	6	Foreign Key references SalesmanNo of Salesman_Master table
DELYTYPE	Char	1	
BILLYN	Char	1	
DELYDATE	Date		
ORDERSTATUS	Varchar2	10	

Table_Name: SALES_ORDER_DETAILS
Column Name	Data Type	Size	Attributes
ORDERNO	Varchar2	6	Foreign Key references OrderNo of Sales_Order table
PRODUCTNO	Varchar2	6	Foreign Key references ProductNo of Product_Master table
QTYORDERED	Number	8	
QTYDISP	Number	8	
PRODUCTRATE	Number	10,2	


2. Insert the following data into their respective tables:

![image](https://user-images.githubusercontent.com/102298880/166630941-12d65cab-ad4f-4407-ba64-64932b611d11.png)


![image](https://user-images.githubusercontent.com/102298880/166630946-9360f3e3-9c09-49f7-8361-f28462d34897.png)


 ![image](https://user-images.githubusercontent.com/102298880/166630958-523b862a-e723-48f5-836c-1af3205a5c25.png)


![image](https://user-images.githubusercontent.com/102298880/166630973-af80341b-d5cf-4e2f-a93c-da34b91ffd92.png)


![image](https://user-images.githubusercontent.com/102298880/166630985-9d995d31-7f65-46f1-b70a-4bf9f5b48380.png)




3.  Generate the SQL statements to perform the following computations on table data in Python IDLE:
a. List the names of all clients having ‘a’ as the second letter in their names.
b. List the clients who stay in a city whose first letter is ‘M’.
c. List all clients who stay in ‘Bangalore’ or ‘Mangalore’.
d. List all clients whose BalDue is greater than value 10000.
e. List all information from the Sales_order table for order placed in the month of 
   June.
f. List the Order No & day on which clients placed their order.
g. List the names, city and state of clients who are not in the state of ‘Maharashtra’.


4. Exercises on Using Having, Group By and Joins in Python IDLE:
a. Printing the description and total quantity sold for each product.
b. Calculating the average quantity sold for each client that has a maximum order value of 15000.00.

