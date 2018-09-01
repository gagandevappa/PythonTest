print('Hello Gagan')
message='hello darshan'
print(message)
lenmessage=len(message)
print(lenmessage)
print(message[0:5])
print(message.upper())
print(message.count('hello'))
print(message.find('o'))
newMessage=message.replace('darshan','universe')
print(newMessage)
name='Gagan'
greeting='Enjoy your day'
print('Hello '+name+', '+greeting)
#formated strings
gesture='Hello {}, {}'.format(name,greeting)
print(gesture)
#fstrings
ola=f'Hello {name}, {greeting}'
print(ola)
print(dir(name))
