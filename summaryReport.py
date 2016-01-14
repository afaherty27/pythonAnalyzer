__author__ = 'afaherty'
import os
import datetime

#This module counts how many words are in the file that is analyzed

token_count = []
word_count = 0

# process list of words to get a count of how many are in the list
def summary_process_tokens(words) :

	global word_count
	word_count = len(words)

# write output file containing summary of file analysis
def summary_write_output_file(text_file) :

	statement = 'Application: Python Analyzer\n'
	author = 'Author: Adam Faherty\n'
	analyzed_file = 'Input File: ' + str(text_file.name) + '\n'
	current_time = 'Analyed on: ' + str(datetime.datetime.now()) + '\n'
	result = 'Word Count: '+ str(word_count)

	file_path = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/output/summaryReport.txt'
	mode = 'a' if os.path.exists(file_path) else 'w+'

	with open(file_path, mode) as file :

		file.seek(0)
		file.truncate() #clears file if it exists already
		file.write(statement)
		file.write(author)
		file.write(analyzed_file)
		file.write(current_time)
		file.write(result)
