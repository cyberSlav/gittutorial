import sys
import urllib.request
import re

link = sys.argv[1]
print(link)
webpage = urllib.request.urlopen(link)
mojiBitovi = webpage.read()
trenutnaStranica = mojiBitovi.decode("utf8")
print(trenutnaStranica)

linkovi = re.findall('href="[^"]+"', trenutnaStranica)

print(linkovi)

host = {}

for link in linkovi:
    patt = re.match('http://(?P<host>[^/]+).*', link)
    if patt:
        if patt.group('host') not in host:
            host[patt.group('host')] = 0
        host[patt.group('host')] += 1
        

print "\nHostovi i broj referenci:"
for x in host:
    print "\t", x, host[x]


print("\n")
allEMail = re.findall(".+@.+\..+", trenutnaStranica)
if len(allEMail) == 0:
    print("no emails have been found")
else:
    for mail in allEMail:
        print(mail)

imageUrl = re.findall('<img[\s+]src=\"[^\"]+\"[\s+][^>]*/>',
                            trenutnaStranica)

print(imageUrl)
print("\n\n\nnumber of urls on pictures: " + str(len(imageUrl)))