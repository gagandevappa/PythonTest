print("***********simple function*********")
def hello_function():
    print("Hello Gagan")
hello_function()

print("***********function with return values*********")
def hi_function():
    return 'Hello Gagan'
print(hi_function())
print(hi_function().upper())
print(len(hi_function()))

print("********functions with arguments and default values **********")
def testFunc(greetings, name='Gagan'):
    return '{},{} How are you'.format(greetings,name)
print(testFunc('Hello'))

print("********function with multiple arguments *********")

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)


student_info('Gagan','Adesh',village='Nedale',District='Shivamogga')

print("**********custom functions************")
name=['Adesh','Gagan','Ashik','Krushik']
details={'qualification':'B.Tech','university':'VTU','state':'Karnataka'}
def admision(*args, **kwargs):
    print(args)
    print(kwargs)

admision(*name,**details)


print("\n**********days count in a month of respective year***********")
num_days=[0,31,28,31,30,31,30,31,31,30.31,30,31]

def leap_year(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)


def days_check(year,month):
    if not 1 <= month <= 12:
        return 'invalid month'

    if month == 2 and leap_year(year):
        return 29
    return num_days[month]


print('The number of days: ',days_check(2019,0))
print('The number of days: ',days_check(2020,2))
print('The number of days: ',days_check(2018,2))
