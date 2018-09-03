from operator import attrgetter
class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return 'The Employee {}, with age {} and salary {}'.format(self.name,self.age,self.salary)


e1=Employee('gagan',28,3000)
e2=Employee('adesh',32,8000)
emp_list=[e1,e2]
def emp_sort(emp):
    return emp.age
s_emp=sorted(emp_list, key=emp_sort, reverse=True)
print(s_emp)

t_emp=sorted(emp_list, key=lambda e: e.age, reverse=True)
print(t_emp)

u_emp=sorted(emp_list, key=attrgetter('name'), reverse=True)
print(u_emp)