#from summaryReport import wordCount

# input to hold file
print('enter file to read:')
fileName = input()

# open file to read
with open(fileName, 'r') as textFile :
                
    words = textFile.read().split()
    #works for small file. not large
    
    print(words)
    
    
