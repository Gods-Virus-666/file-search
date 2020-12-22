### FILE READER *needs work*
#Extract data into a text file & extract specific pieces of data
filetype = input('Enter the file type; ')
if filetype in ['t', 'te', 'tex', 'text', '.t', '.te', '.tex', '.text' ]:
    filetype = '.txt'
filename = input('Enter the file name; ') + filetype
data = input('Enter 1 word related to the information you are looking for:  ')
data2 =input('Enter additional word if no additional word(s) press the enter key:  ')
data3 =input('Enter additional word if no additional word(s) press the enter key:  ')
data4 =input('Enter additional word if no additional word(s) press the enter key:  ')
data5 =input('Enter additional word if no additional word(s) press the enter key:  ')
filehandle = open(filename)
for line in filehandle:
    line = line.rstrip()
    if line.find(data) == -1: continue
    print(line)
    for line in filehandle:
        line = line.rstrip()
        if line.find(data2) == -1: continue
        print(line)
        for line in filehandle:
            line = line.rstrip()
            if line.find(data3) == -1: continue
            print(line)
            for line in filehandle:
                line = line.rstrip()
                if line.find(data4) == -1: continue
                print(line)
                for line in filehandle:
                    line = line.rstrip()
                    if line.find(data5) == -1: continue
                    print(line)
