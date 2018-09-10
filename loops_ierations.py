print("********simple for loop************")
nums=[1,2,3,4,5,6,7,8,9,10]
for num in nums:
    print(num)


print("********break condition************")
myList=[1,2,3,4,5,6,7,8,9,10]
for i in myList:
    if (i == 4):
        print("Error!! your are in the 5rd iterattion of the for loop ")
        break
    print(i)
    i=i+1


print("********continue statement************")
for i in myList:
    if (i == 4):
        print("The time to continue!!")
        continue
    print(i)
    i+=1

print("**********range operation**********")   
for i in range(1,6):
    print(i) 

print("*********** recursive loops********")
testList=[1,4,6]
for num in testList:
    for i in 'abc':
        print(num, i)


print("*********** while loop ***********")
num=4
i=0
while(i <= num):
    if(i==3):
        print("Exit the loop!!")
        break
    print(i)
    i += 1


print("*********** while loop-2 ***********")
num=0
while True:
    if(num == 3):
        print("break from loop-2")
        break
    print(num)
    num += 1




