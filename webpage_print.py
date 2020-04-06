import urllib.request

try:
    webpage = urllib.request.urlopen('http://www.cnn.com')
except:
    print('Could not access webpage')

else:
    
    for line in webpage:
        print (line)
