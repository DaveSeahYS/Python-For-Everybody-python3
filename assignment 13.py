# Given a link with values in xml
# Attempt to grab all the values under comments/comment/count and sum them all out
# Finally, print out the number of count found as well as the overall sum

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# link given: http ://py4e-data.dr-chuck.net/comments_357302.xml

url = input('Enter URL here')
html = urllib.request.urlopen(url).read().decode()  # open up the link, read it, and decode it
print('Retrieving', url)  # as requested by the qn to show link retrieved
print('Retrieved', len(html), 'characters')  # as requested by the qn to display characters found in link

count = 0
sum = 0

data = ET.fromstring(html)  # Element tree for sequencing html
tags = data.findall('comments/comment')  # find within comments, comment, later we will do count.txt for the number

for tag in tags:
    count = count + 1
    sum = sum + int(tag.find('count').text)

print('Count:', count)  # print number of times numbers were found
print('Sum:', sum)  # print overall sum of whats found



#
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# url = input('Enter your url')
# html = urllib.request.urlopen(url).read().decode()
#
# count = 0
# sum = 0
#
# data = ET.fromstring(html)
# tags = data.findall('comments/comment')
#
# for tag in tags:
#     count = count+1
#     sum = sum + int(tag.find('count').text)
#
# print(count)
# print(sum)
