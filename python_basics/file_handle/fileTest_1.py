print("***********normal file read*********")
f=open('testdata.txt', 'r')
val2=f.read()
print(val2)
f.close()


print("\n******context-manager*************")
with open('testdata.txt', 'r') as f:
    val3=f.read()
    print(val3)


print("\n******context-manager- write*************")
with open('testwrite.txt', 'w') as w:
    w.write('Gagan How are you!!')


print("*******file copy*********")
with open('testdata.txt', 'r') as rd:
    with open('testwrite-copy.txt', 'w') as wr:
        val1=rd.read()
        wr.write(val1)


print("*******copy an image with chunk-size*********")
with open('Digital-Commerce.png', 'rb') as rb:
    with open('DC.png', 'wb') as wb:
        chunk_size=100
        jpegread=rb.read(chunk_size)
        while len(jpegread) > 0:
            wb.write(jpegread)
            jpegread=rb.read(chunk_size)
    