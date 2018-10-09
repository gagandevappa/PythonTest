import sqlite3
from employee import Employee
conn = sqlite3.connect(':memory:')
c=conn.cursor()
c.execute("""CREATE TABLE employee(
                  first text,
                  last text,
                  pay integer)""")

def insert_emp(emp):
      with conn:
        c.execute("INSERT INTO employee VALUES(:first, :last, :pay)", {'first':emp.first,'last':emp.last,'pay':emp.pay})

def get_emps_by_name(lastname):
      c.execute("SELECT * FROM employee WHERE last=:last", {'last':lastname})
      return c.fetchall()

def update_pay(emp, pay):
      c.execute("""UPDATE employee SET pay=:pay where first=:first 
                AND last=:last""", {'pay':pay, 'first':emp.first, 'last':emp.last})

def remove_emp(emp):
      c.execute("""DELETE FROM employee where 
                  first=:first AND last=:last""", {'first':emp.first, 'last':emp.last})

emp1=Employee('Gagan','Devappa',20000)
emp2=Employee('Adesh','Devappa',30000)
emp3=Employee('Abhiman','Ramesh',40000)

insert_emp(emp1)
insert_emp(emp2)
insert_emp(emp3)

print("emp1 email: "+bemp1.email)
print("emp2 full name: "+emp2.fullname)
nameList=get_emps_by_name('Devappa')
print("1.\n",nameList)

update_pay(emp2,50000)

nameList2=get_emps_by_name('Devappa')
print("2.\n",nameList2)

remove_emp(emp3)

nameList3=get_emps_by_name('Ramesh')
print("3.\n",nameList3)


conn.close()
