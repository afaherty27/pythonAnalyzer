import os
import datetime

#function to count words

tokenCount = []
count = 0

# process list of words to get a count of how many are in the list
def summaryProcessTokens(words) :
	global count
	for token in words:
		tokenCount.append(token)
		count += tokenCount.count(token) #TODO figure out why the count is skipping list index numbers
		print(str(count) + token) #DEBUG
	print(tokenCount) # DEBUG

# write output file containing summary of file analysis        
def summaryWriteOutputFile(textFile) :

	statement = 'Application: Python Analyzer\n'
	author = 'Author: Adam Faherty\n'
	analyzedFile = 'Input File: ' + str(textFile.name) + '\n'
	currentTime = 'Analyed on: ' + str(datetime.datetime.now()) + '\n'
	result = 'Word Count: '+ str(count)

	filePath = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/summaryReport.txt'
	mode = 'a' if os.path.exists(filePath) else 'w+'

	with open(filePath, mode) as file :

		file.seek(0)
		file.truncate() #clears file if it exists already
		file.write(statement)
		file.write(author)
		file.write(analyzedFile)
		file.write(currentTime)
		file.write(result)
