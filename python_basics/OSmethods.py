import os,glob
from datetime import datetime
#print(dir(os))
print(os.getcwd())
desktop='C:/Users/devapga/Desktop'
os.chdir(desktop)
print(os.getcwd())
#print(os.listdir('C:/Users/devapga/Desktop'))
#os.chdir('')

#make dirs
os.mkdir('Python-test1')
os.makedirs('Python-test2/gagan1')
#rename
#os.rename('connection2.yaml','connection1.yaml')
#remove dir
os.rmdir('Python-test1')
os.removedirs('Python-test2/gagan1')
#details of dir()
st_time=(os.stat('156A_defect_fixes.txt').st_mtime)
print(datetime.fromtimestamp(st_time))
#dispay the directory of 3 level depth
for dirpath,dirname,filenames in os.walk('C:/Users/devapga/Desktop/final_objects/'):
    print('The directory path: ',dirpath)
    print('The directory name is: ',dirname)
    print('The file names are : ',filenames)
    print()
#joining 2 path
#for i in  os.path(desktop,'final_objects/final_objects'):
print(os.path.join('Python-test2','gagan'))
print(os.environ.get('java_home'))
mytest=os.path.join(os.getcwd(),'gagan.txt')
f=open(mytest,'w+')
f.write('gagan Hello\n')
f.close()

with open(mytest,'a') as f:
    f.write('Hello Gagan')

print(os.path.basename(mytest))
print(os.path.dirname(mytest))
print(os.path.isdir(mytest))
print(os.path.exists(mytest))
print(os.path.split(mytest))
print(os.path.isfile(mytest))
print(os.path.splitext(mytest)[0])