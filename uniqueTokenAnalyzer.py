__author__ = 'afaherty'

def unique_process_tokens() :
    # TODO process tokens from list into a sorted list and remove duplicates


def unique_token_output_file():
    # TODO complete variables to complete report

    file_path = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/summaryReport.txt'
    mode = 'a' if os.path.exists(file_path) else 'w+'

    with open(file_path, mode) as file :

        file.seek(0)
        file.truncate() #clears file if it exists already
        # TODO complete file.write() for report