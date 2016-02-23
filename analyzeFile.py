__author__ = 'afaherty'

from summaryReport import summary_process_tokens
from uniqueTokenAnalyzer import unique_process_tokens
from keywordAnalyzer import keyword_process_tokens
from bigwordAnalyzer import bigword_process_tokens
from tokenSizeAnalyzer import token_size_process_tokens
from tokenCountAnalyzer import token_count_process_tokens

from summaryReport import summary_write_output_file
from uniqueTokenAnalyzer import unique_token_output_file
from keywordAnalyzer import keyword_output_file
from bigwordAnalyzer import bigword_output_file
from tokenSizeAnalyzer import token_size_output_file
from tokenCountAnalyzer import  token_count_output_file


def process_tokens(words) :
    summary_process_tokens(words)
    unique_process_tokens(words)
    keyword_process_tokens(words)
    bigword_process_tokens(words)
    token_size_process_tokens(words)
    token_count_process_tokens(words)


def write_output_files(text_file) :
    summary_write_output_file(text_file)
    unique_token_output_file()
    #keyword_output_file()
    bigword_output_file()
    token_size_output_file()
    token_count_output_file()

# input to hold file
print('enter file to read:')
file_name = input()

# open file to read
with open(file_name, 'r') as text_file :

    words = text_file.read().split()

    #works for small file. not large
    process_tokens(words)
    write_output_files(text_file)

    
