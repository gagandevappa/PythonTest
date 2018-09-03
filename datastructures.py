##List
mylist=['Adesh','Sindhu','Abhiman','Ashik','Krushik']
print(mylist)
print(len(mylist))
print(mylist[3])
print(mylist[-1])
#slicing
print(mylist[0:4])
print(mylist[:4])
print(mylist[2:4])
mylist.append('Anugna')
print(mylist)
mylist.insert(1,'Gagan')
print(mylist)
grandparents=['bharmaiah','chinamma']
mylist.append(grandparents)
print(mylist)
location=['nedale','heddur']
mylist.extend(location)
print(mylist)
mylist.remove('heddur')
print(mylist)
popped=mylist.pop()
print(mylist)
print(popped)
mylist.pop()
mylist.sort()
print(mylist)
numlist=[12,4,67,23,15,27]
numlist.sort()
print(numlist)
numlist.sort(reverse=True)
print(numlist)
sortList=sorted(mylist, reverse=True)
print(sortList)

##Tuples
mytuple = ('test',5,'hello',2,'main',4)
print(mytuple)
#revtuple=sorted(mytuple, reverse=True)
#print(revtuple)

#dictionary
mydict = {'karnataka' : 'Bengaluru','Telengana':'Hydrabad','Andra-pradesh':'amaravathi','tamilnadu':'chennai','kerala':'thiruvanathapuram'}
print(mydict)
dictkey = mydict.keys()
print(dictkey)
print(mydict.values())
revdict=sorted(mydict)
print(revdict)