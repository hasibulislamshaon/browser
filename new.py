import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen('https://www.dictionary.com/browse/what')#SSL: CERTIFICATE_VERIFY_FAILED
for line in fhand:
    print(line.decode().strip())