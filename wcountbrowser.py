import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count=dict()
for words in fhand:
    word = words.decode().split()
    for name in word:
     count[name]=count.get(name,0)+1
print(count)