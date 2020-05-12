#! usr/bin/python python3

import sys
import re


# Gets user input
# def GetFilePath():
#    print('Enter a file path:')
#    filePath = input()
#    OpenFile(filePath)
#    return

# Tries to open specified file in read mode
def OpenFile(filePath):
    try:
        file = open(filePath, 'r')
        print('Opening file \"' + file.name + '\"...')
        IndexWords(file)
    except:
        print('ERROR: Couldn\'t open file \"' + filePath + '\"... Check your spelling and try again.')
#        GetFilePath()
    return

# Splits text by non-word chars and store in set
def IndexWords(file):
    try:
        print('Reading contents of ' + file.name + '...')
        fileContents = file.read()
        fileContents = fileContents.lower() # Make lowercase
        file.close()
        print('Indexing words in ' + file.name + '...')
        tokens = list(re.split('\W+', fileContents)) # Create a list of every word in text (tokens)
        types = set(re.split('\W+', fileContents)) # Create a set of only unique words in text (types)
        CountWords(types, tokens)
    except:
        print('ERROR: Something went wrong during indexing...')
#        GetFilePath()
    return

# Counts occurrences of each word
def CountWords(types, tokens):
    print('Words in text: d')
    typesTokensDict = {}
    for type in types:
        typesTokensDict[type] = tokens.count(type)
    OrderTypesByTokens(typesTokensDict)
    return

# Orders set by no. of occurrences of each word
def OrderTypesByTokens(typesTokensDict):
    print('Ordering types by number of tokens...')
    orderedTypes = {type: tokens for type, tokens in sorted(typesTokensDict.items(), key=lambda item: item[1], reverse=True)}
    for type in orderedTypes:
        print(type, ':' , orderedTypes[type])
    return







# 5. Print output


# print('This program reads a text file and outputs how many times each word occurs in the text.')

# GetFilePath()

sys.argv
if len(sys.argv) > 1:
    filePath = str(sys.argv[1])
    OpenFile(filePath)
else:
    print('Specify a text file name like so: word-frequency.py file_name.txt')

