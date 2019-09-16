import urllib.request
from collections import Counter
web = input("enter url: ")
fp = urllib.request.urlopen("http://" + web)
mybytes = fp.read().split()
wordcount = Counter(mybytes)
fp.close()
for item in wordcount.items():
    print("{}\t{}".format(*item))