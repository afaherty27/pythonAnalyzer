import os
import datetime

#This module counts how many words are in the file that is analyzed

tokenCount = []
wordCount = 0

# process list of words to get a count of how many are in the list
def summaryProcessTokens(words) :

	global wordCount
	wordCount = len(words)

# write output file containing summary of file analysis
def summaryWriteOutputFile(textFile) :

	statement = 'Application: Python Analyzer\n'
	author = 'Author: Adam Faherty\n'
	analyzedFile = 'Input File: ' + str(textFile.name) + '\n'
	currentTime = 'Analyed on: ' + str(datetime.datetime.now()) + '\n'
	result = 'Word Count: '+ str(wordCount)

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
