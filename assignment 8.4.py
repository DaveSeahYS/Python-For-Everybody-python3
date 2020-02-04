# 8.4 Open the file romeo.txt and read
# it line by line. For each line, split
# the line into a list of words using
# the split() method. The program should
# build a list of words. For each word
# on each line check to see if the word
# is already in the list and if not
# append it to the list. When the program
# completes, sort and print the resulting
# words in alphabetical order.
# You can download the sample data at
# http://www.py4e.com/code3/romeo.txt

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

fname = input("Enter file name: ")
fh = open(fname)  # open up romeo.txt
lst = list()
for line in fh:
    line.rstrip()  # remove the right spaces
    words = line.split()  # split each word in the lines
    for word in words:
        if not (word in lst):  # if its not already a word in the list
            lst.append(word)  # add the word if not found
lst.sort()  # alphabetical order
print(lst)
