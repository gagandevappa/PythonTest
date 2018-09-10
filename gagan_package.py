def welcomeMessage():
    print("Your are inside gagan_package")

def findIndex(list,target):
    for index,value in enumerate(list):
        if value == target:
            return index
    return -1


testVal=10