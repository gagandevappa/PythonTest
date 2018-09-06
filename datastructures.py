##########################################################################################
#                                                                                        #
#           Lists                                                                        #
#                                                                                        #
##########################################################################################
print('\n LISTS \n')
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
print('The index of 67 is : ',numlist.index(67))
numlist.sort()
print(numlist)
numlist.sort(reverse=True)
print(numlist)
sortList=sorted(mylist, reverse=True)
print(sortList)
for index,name in enumerate(sortList, start=1):
    print(index, name)
join_string=' - '.join(sortList)
print(join_string)
name_list=join_string.split(' - ')
print(name_list)
empty_list=[]
empty_list2=list()
print(empty_list)
print(empty_list2)
##########################################################################################
#                                                                                        #
#           Tuples                                                                       #
#                                                                                        #
##########################################################################################
print('\n TUPLES \n')
mytuple = ('test',5,'hello',2,'main',4)
tuple2=mytuple;
print(mytuple)
print(tuple2)
#mytuple[0]='Gagan'
#print(mytuple)
empty_tuple=()
empty_tuple2=tuple()
print(empty_tuple)
print(empty_tuple2)
##########################################################################################
#                                                                                        #
#           Sets                                                                         #
#                                                                                        #
##########################################################################################
print('\n SETS \n')
cs_courses={'ds','dbms','python','unix','dbms'}
mech_courses={'fme','atd','btd','som'}
comman_courses={'unix','dbms','maths','physics'}
print(cs_courses)
print(mech_courses)
print(cs_courses.intersection(comman_courses))
print(cs_courses.union(comman_courses))
empty_set=set()
print(empty_set)
##########################################################################################
#                                                                                        #
#           Dictionaries                                                                 #
#                                                                                        #
##########################################################################################
print('\n DICTIONARY \n')
mydict = {'karnataka' : 'Bengaluru','Telengana':'Hydrabad','Andra-pradesh':['hydrabad','amaravathi'],'tamilnadu':'chennai','kerala':'thiruvanathapuram'}
print(mydict)
print(mydict['Andra-pradesh'])
dictkey = mydict.keys()
print('\ndictionary keys are: ',dictkey)
print('\ndictionary values are: ',mydict.values())
print('\ndictionary itmes are: ',mydict.items())
revdict=sorted(mydict)
print('sorted dict: ',revdict)
for keys,values in mydict.items():
    print(keys,values)
mydict['maharastra']='Mumbai'
print('The updated list-1 is: ',mydict)
mydict.update({'Telengana':'Manam Hydrabad'})
print(mydict.items())
pop_dict=mydict.pop('Telengana')
print('The popped dict item is:',pop_dict)
del mydict['tamilnadu']
print('The remaining dictinory is: ',mydict.items())
empty_dict={}
print('empty dict is: ',empty_dict)
