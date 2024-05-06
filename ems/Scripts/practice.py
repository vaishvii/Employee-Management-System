import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Vaishvi@55", database="ems")
c=mydb.cursor()
#view employee details
eid=input("Enter Employee ID")
c.execute("select * from employee_details where emp_id=%s",(eid,))
mydata=c.fetchall()
print(mydata)
