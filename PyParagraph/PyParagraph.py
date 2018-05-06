# -*- coding: utf-8 -*-
# python-challenge is on my desktop
# Specify the paragraph you are interested in
paragraph = 'paragraph_1.txt' # or 'paragraph_2.txt' 
# Assuming user has their current working directory on DESKTOP






import os
import codecs
import re

path = os.path.join(os.environ["HOMEPATH"], 'Desktop', 'python-challenge', 'PyParagraph', 'raw_data', paragraph)
# Read in text file
txt = codecs.open(path, mode = 'r', encoding='utf-8').read()

s = re.sub(r'[^\w\s]','',txt)
numWords = len(s.split())
numSent = txt.count('.') + txt.count('!') + txt.count('?')

# Get total number of characters
countLetter = len(re.sub(' ', '', s)) / numWords
countSent = numWords / numSent

print('Paragraph Analysis')
print('-'*18)
print('Approximate Word Count: '+str(numWords))
print('Approximate Sentence Count: '+str(numSent))
print('Average Letter Count: '+str(countLetter))
print('Average Sentence Length: '+str(countSent))




# =============================================================================
# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.56557377049
# Average Sentence Length: 24.4
# =============================================================================
