import streamlit as st
import mysql.connector
import datetime
st.set_page_config(page_title="EMPLOYEE MANAGEMENT SYSTEM", page_icon="https://cdn-icons-png.flaticon.com/512/3616/3616930.png")
st.title("EMPLOYEE MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("My Menu",("HOME","EMPLOYEE","ADMIN"))
if(choice == "HOME"):
    st.image("https://img.freepik.com/free-vector/hiring-agency-candidates-job-interview_1262-18940.jpg")
    st.write("This application is developed by Vaishvi Gupta.")
elif(choice=="EMPLOYEE"):
    if "islogin" not in st.session_state:
        st.session_state["islogin"]=False
    eid=st.text_input("Enter Employee ID")
    pwd=st.text_input("Enter Employee Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
        c=mydb.cursor()
        c.execute("select emp_id, emp_pwd from employee_details")
        for r in c:
            if(r[0]==eid and r[1]==pwd):
               islogin=True
               break
        if(not islogin):
            st.write("Invalid ID or Password")
    if(st.session_state["islogin"]):
        st.write("Login Successful")
        choice2=st.selectbox("Features",("None", "Profile Info", "Apply for Leave"))
        if(choice2=="Profile Info"):
            mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
            c=mydb.cursor()
            c.execute("select * from employee_details")
            for row in c:
                if(row[0]==eid):
                    st.write("Employee ID: ", row[0])
                    st.write("Password: ", row[1])
                    st.write("Name: ", row[2])
                    st.write("Salary: ", row[3])
        elif(choice2=="Apply for Leave"):
            reason=st.text_input("Enter the reason for leave")
            btn3=st.button("Apply")
            if btn3:
                aid=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
                c=mydb.cursor()
                c.execute("insert into leave_application values(%s,%s,%s)"(aid,eid,reason))
                mydb.commit()
                st.header("Leave Applied Successfully")
                
elif(choice=="ADMIN"):
        if "islogin" not in st.session_state:
            st.session_state["islogin"]=False
        eid=st.text_input("Enter Admin ID")
        pwd=st.text_input("Enter Admin Password")
        btn=st.button("Login")
        if btn:
            mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
            c=mydb.cursor()
            c.execute("select * from admins")
            for r in c:
                if(r[0]==eid and r[1]==pwd):
                   islogin=True
                   break
            if(not islogin):
                st.write("Invalid ID or Password")
        if(st.session_state["islogin"]):
            st.write("Login Successful")
            choice3=st.selectbox("Features",("None","Mark Attendance","Add Employee","Delete Employee"))
            if(choice3=="Mark Attendance"):
                eid=st.text_input("Enter Employee ID")
                status=st.selectbox("Enter Status", ("Present", "Absent", "Half Day"))
                bnt4=st.button("Submit")
                if btn4:
                    dt=str(datetime.datetime.now())
                    mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
                    c=mydb.cursor()
                    c.execute("insert into emp_attendance values(%s,%s,%s)", (dt,eid,status))
                    mydb.commit()
                    st.header("Attendance Marked Successfully")
            elif(choice=="Add Employee"):
                eid=st.text_input("Choose Employee ID")
                pwd=st.text_input("Choose Employee Password")
                name=st.text_input("Enter Employee Name")
                salary=st.text_input("Enter Salary")
                btn5=st.button("Add Employee")
                if btn5:
                    mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
                    c=mydb.cursor()
                    c.execute("insert into employee_details values(%s,%s,%s)", (eid,pwd,name, salary))
                    mydb.commit()
                    st.header("Employee Added Successfully")
            elif(choice=="Delete Employee"):
                eid=st.text_input("Choose Employee ID")
                btn5=st.button("Delete Employee")
                if btn5:
                    mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
                    c=mydb.cursor()
                    c.execute("delete from employee_details where emp_id=%s", (eid))
                    mydb.commit()
                    st.header("Employee Deleted Successfully")
            elif(choice=="Update Salary"):
                eid=st.text_input("Choose Employee ID")
                us=st.text_input("Enter Updated Salary")
                btn5=st.button("Update Salary")
                if btn5:
                    mydb=mysql.connector.connect(host="localhost", user="root", password="12345678", database="ems")
                    c=mydb.cursor()
                    c.execute("update employee_details set emp_salary=%s where emp_id=%s", (us,eid))
                    mydb.commit()
                    st.header("Update Salary Successfully")
                    
    
