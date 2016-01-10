# Python File Analyzer

##Background
The idea for this program is not an original one.  This project originated from the Advanced Java class I took last year.
I have noticed several companies within my job search had Python listed as a requisite for the position. I started going
through tutorials within the Python documentation, but soon started feeling no challenge.

After some thought on how I could challenge myself while learning a new programming language, I kept going back to the 
file analyzer project I had in the Advanced Java.  Looking back, the project was a great example for learning the skills 
I learned that semester. The project involved reading a file, processing the contained information in the file in several
different ways, and then writing a file for each processed result.

##Program Files
###analyzeFile.py
`anaylyzeFile.py` is the workhorse of the program.  This portion of the program is responsible for prompting the user
 for a file that the Analyzer will process.  Once the file is selected, it is opened, and the words within the file are
 added to a list for later use.

###summaryReport.py
`summaryReport.py` simply processes the list of words from `analyzeFile.py` and presents a count of words within the 
file.  This data is written to a new file called `summary.txt` for the user to view after the analyzer has completed its
processing.