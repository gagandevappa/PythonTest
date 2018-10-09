with open('filename_split.py','r+ ') as f:
    test=f.read()
    for t in test.split(':'):
        print(t)

