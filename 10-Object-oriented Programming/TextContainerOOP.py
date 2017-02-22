import webget
import string

class TextContainer():
	
	def __init__(self, container):
		self.container = container
		
	def counterWord(text):
		totalWords = 0
		for item in text:
			totalWords += len(item.split())
		print ("\n\nTotal amount of words: ",totalWords)
	
	def counterChar(text):
		totalChars = 0
		for chars in text:
			totalChars += len(text)
		print ("\n\nTotal amount of characters: ",totalChars)

	def counterAscii(text):
		totalAscii = 0
		for chars in text:
			for x in chars:
				totalAscii+= 1
		print(len([letter for letter in text if letter in string.ascii_letters]))
		print("\n\nTotal amount of ASCII-Letters: ", totalAscii)
		
url = 'http://www.gutenberg.org/cache/epub/27525/pg27525.txt'
webget.download(url)		
with open('./pg27525.txt') as f:
	content = f.readlines()

TextContainer.counterWord(content)
TextContainer.counterChar(content)
TextContainer.counterAscii(content)

# Counting the amount of letters, where letters are all ASCII letters, see
# import string
# string.ascii_letters  # returns 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Remove all punctuation characters, see
# import string
# string.punctuation  # returns '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
