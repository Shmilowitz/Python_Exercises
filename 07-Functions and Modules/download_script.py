import sys
import urllib.request
import os
#First Exercise 1
argList = sys.argv
count = 1

def download(url, counter):
	for i in range(len(argList) - 1):
		print ("\n")
		print ("Downloading Item Number: ", (counter))
		urlSplit = os.path.basename(url[counter])
		print ("File will be named: ",urlSplit)
		print("Download Path: ", os.path.abspath(urlSplit))
		urllib.request.urlretrieve(url[counter], urlSplit)
		print ("Item Number",counter, "Finished\n")
		counter += 1

download(argList, count)

# python download_script.py http://www.gutenberg.org/files/2701/2701-0.txt http://www.gutenberg.org/cache/epub/27525/pg27525.txt




