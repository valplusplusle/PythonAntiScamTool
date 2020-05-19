import os
import random
import urllib3

counter = 0
names = []
http = urllib3.PoolManager()

print ("Reading names into Array")

with open("names.txt", "r") as flash:
	for line in flash:
		names.extend(line.split())

for item in names:

    email = item + "@gmail.com"
    password = item + str(random.randint(1000,9999))
    response = http.request('POST', 'https://dopplers.club/auth.php?doAuth=1&login='+email+'&password='+password)
    print ("item: "+item+" email: "+email+" pass: "+password+" http_status: "+str(response.status))
