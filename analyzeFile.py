__author__ = 'afaherty'
from summaryReport import summaryProcessTokens
from summaryReport import summaryWriteOutputFile

# input to hold file
print('enter file to read:')
file_name = input()

# open file to read
with open(file_name, 'r') as text_file :

    words = text_file.read().split()
    #works for small file. not large

    summaryProcessTokens(words)
    summaryWriteOutputFile(text_file)
    
