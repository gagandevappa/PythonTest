#conditional equal to
print("***** conditional equal to**********")
language='python'
if language =='Java':
    print('The lanuage entered: '+language+' but expected: java')
elif language=='python':
    print('The lanuage entered: '+language+' but expected: python')
else:
    print('The lanugae is unknown')

#conditional not
print("***** conditional not**********")
if language != 'python':
    print("The language is not python")
else:
    print("The langauge is pythoon")

#logical and
print("***** logical and**********")
admin = False
if language == 'python' and admin:
    print("you are an python admin")
elif admin:
    print("you are the system admin")
elif language =='python':
    print("you are the python developer")
else:
    print("You are beginer")

#logical not
print("***** logical not**********")
if not admin:
    print("you are not an admin")
else:
    print("you are an admin")

#Object Identity
print("***** is operator(object Identity)**********")
a=[1,2,3]
b=[1,2,3]
c=a
print(id(a))
print(id(b))
print(id(c))
if a is b:
    print("both a and b location is same")
elif a is c:
    print("both a and c location is same")
else:
    print("all the location-pointer are different")

#boolean operation for empty list
print("*************boolean operation for empty list***************")

d=[]
if d:
    print("Evaluated to True")
else:
    print("Evaluated to false")

#boolean operation for empty dictionary
print("*************boolean operation for dictionary***************")

d={}
if d:
    print("Evaluated to True")
else:
    print("Evaluated to false")
#boolean operation for variable with zero value
print("*************boolean operation for variable with zero value***************")
e=0
if e:
    print("Evaluated to True")
else:
    print("Evaluated to false")

#boolean operation for variable with non-zero value
print("*************boolean operation for variable with non-zero value***************")
e=10
if e:
    print("Evaluated to True")
else:
    print("Evaluated to false")

