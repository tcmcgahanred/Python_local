#with open('text.txt') as fp:
#    text = fp.read()     #reads the entire file 

#with open('text.txt') as fp:
#    text = fp.read(5)       #reads first 5 bits

#with open('text.txt') as fp:
#    line = fp.readline()    #reads 1 line
#    line = fp.readlines()   #reads 1 line at a time?

#with open('text.txt') as fp:
#    for line in fp:
#    print(line, end='')     #print each line w/o whitespace

with open('text.txt' as source, open('copy.txt','w') as destination:
    destination.write(source.read())

#copies one file into another
