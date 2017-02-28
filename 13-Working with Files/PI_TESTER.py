import webget
import time

# Download the file in case we do not have it already
url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv' 
webget.download(url)

with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
	pi_string += line.strip()

print('0 to 100: ', pi_string[0:100] + "...")
print('100 to 200: ',pi_string[100:200] + "...")
print('Length: ', len(pi_string) - 2)

#Writing to file
with open('msgtext.txt', 'w') as file_object:
	file_object.write(pi_string[:50] + '\n')
	time.sleep(5)
	file_object.write(pi_string[50:100] + '\n')