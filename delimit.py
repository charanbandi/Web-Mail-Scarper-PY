#import re
 
fileToRead = 'final_list.txt'
fileToWrite = 'Extracted.txt'
 
 
#delimiterInFile = [',', ';']
file = open(fileToRead, 'r') 
fo = open(fileToWrite, 'w+') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    #print(item)
    a = item.replace(";","")
    fo.write(a)
    #print a
fo.close() 