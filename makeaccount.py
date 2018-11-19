import os
import random
import urllib

counter = 0
names = []

print ("Reading names into Array")

with open("names.txt", "r") as flash:
	for line in flash:
		names.extend(line.split())

for item in names:
	print item
	email = item + "@gmail.com"
	print email
	password = item + str(random.randint(1000,9999))
	print password	
	urllib.urlopen('https://csgoxxmagic.pro/auth.php?doAuth=1&login='+email+'&password='+password)
