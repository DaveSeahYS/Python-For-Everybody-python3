# Welcome Dave Seah Yong Sheng from Using Python to Access Web Data
#
# Exploring the HyperText Transport Protocol
#
# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#
# http://data.pr4e.org/intro-short.txt

# There are three ways that you might retrieve this web page and look at the response headers:
#
# Preferred: Modify the socket1.py(https://www.py4e.com/code3/socket1.py)
# program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
# Use the telnet program as shown in lecture to retrieve the headers and content.
# Enter the header values in each of the fields below and press "Submit".

# Last-Modified:
Sat, 13 May 2017 11:22:22 GMT
# Etag:
"1d3-54f6609240717"
# Content-Length:
467
#Cache-Control:
max-age=0, no-cache, no-store, must-revalidate
#Content-Type:
text/plain

# Note: To solve this problem, just go to http://data.pr4e.org/intro-short.txt
# and then click F12 and then refresh(F5)
# Afterwards, go to Network -> intro-short.txt -> Headers
# All the information you require are stored there