'''
Implement a function that will create a new file based on three other files using Python.
Requirements

The file_parser function accepts four parameters that are paths to files.

The arguments are, in order:
1. base_path (path to the file that is later referred to as base file):
    o base file will contain at least two non-empty lines and zero or more than one empty lines.
2. fill_path (path to the file that is later referred to as fill file):
    • fill file will always contain exactly one line;
    • This line should fill all empty lines in base file.
3. remove_path (path to the file that is later referred to as remove file):
    • remove file might be an empty file or it will contain exactly one line;
    • In case of one line: all occurrences of the specified word (string) in base file should be removed;
    • In case of an empty remove file: no substring has to be removed from output file.
4. output_path (path to the file that is later referred to as output file):
    • the function should create a new file under the path specified in output file;
    • output file should have metadata about base file;
    • output file should contain the parsed content based on base file, fill file and remove file.

To satisfy the above requirements the following conditions have to be met:
    • The first line of output file should display the overall number of lines in base file in the format:
There are <number> lines in base file
    • The second line of output file should display the number of empty lines in base file in the format:
There are <number> empty lines in base
    • The next lines should contain the parsed lines from base file.
    • Lines from base file should be in the same order in output file as in base file.
    • The empty lines from base file should be replaced in output file with the line from fill file.
    • All occurrences of the word in remove file should be removed from output file. There might be multiple occurrences of the word defined in remove file in each line of base file: each of them should be removed.
'''

def getFileContents(filename):
    with open(filename) as f:
        contents = f.readlines()
        return contents

def saveFile(output_path, contents):
    with open(output_path, mode='wt', encoding='utf-8') as f:
        f.write(''.join(contents))

def file_parser(base_path, fill_path, remove_path, output_path):
    base_file_contents = getFileContents(base_path) ## get base file contents
    filler = next(iter(getFileContents(fill_path) or []), '') ## get filler string
    remove = next(iter(getFileContents(remove_path) or []), '') ## get remove string

    numLines = numEmptyLines = 0
    for i, line in enumerate(base_file_contents):
        # count number of lines
        numLines += 1
        
        # check if line is empty
        if line.isspace():
            numEmptyLines += 1
            # add filler
            base_file_contents[i] = filler + '\n'
            continue
        
        # check if remove word is present
        if remove != '':
            base_file_contents[i] = line.replace(remove, '')
        # base_file_contents[i] = line.replace(remove, '') if remove != '' else line
    
    output_file_contents = ['There are {} lines in base file\n'.format(numLines), 'There are {} empty lines in base file\n'.format(numEmptyLines)] + base_file_contents

    saveFile(output_path, output_file_contents)

