print("***********normal file read*********")
f=open('testdata.txt', 'r')
val2=f.read()
print(val2)


print("\n******context-manager*************")
with open('testdata.txt', 'r') as f:
    val=f.read()
    print(val)