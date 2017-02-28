import webget
import string
from string import ascii_lowercase
from collections import Counter

class TextContainer():
	
	def __init__(self, container):
		self.container = container
		
	def counterWord(text):
		totalWords = 0
		for item in text:
			totalWords += len(item.split())
		print ("\n\nTotal amount of words: ",totalWords)
	
	def counterChar(text):
		print ("\n\nTotal amount of characters: ",sum([len(i) for i in text]))

	def counterAscii(text):
		totalAscii = 0
		print ("\n\nTotal amount of ASCII-Letters: ", sum(Counter(letter for line in text for letter in line.lower() if letter in ascii_lowercase).values()))
	
	def removePunctuation(text):
		noPunctuation = [''.join(c for c in s if c not in string.punctuation) for s in text]
		TextContainer.counterChar(noPunctuation)
		
#Generating text while with webget
url = 'http://www.gutenberg.org/cache/epub/27525/pg27525.txt'
webget.download(url)		
with open('./pg27525.txt') as f:
	content = f.readlines()

#Calling all the different methods	
TextContainer.counterWord(content)
TextContainer.counterChar(content)
TextContainer.counterAscii(content)
TextContainer.removePunctuation(content)

