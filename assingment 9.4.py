# Write a program to read through the mbox-short.txt and figure out who
# has sent the greatest number of mail messages. The program looks for
# 'From ' lines and takes the second word of those lines as the
# person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of
# times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

sender = dict()  # set sender as an empty dictionary
for lines in handle:  # for the lines in mbox-short.txt
    if not lines.startswith('From:'): continue  # ignore if word doesn't start with From:
    lines = lines.split()  # split the words in the line into individual words
    lines = lines[1]  # takes the word after 'From:'
    sender[lines] = sender.get(lines, 0) + 1  # If not found add 0, if found add 1
    # print(lines)  # prints out every email in the list

Bigcomment = None  # Key
Bignum = None  # value
for comment, num in sender.items():  # for the key and its value in items()
    if Bignum is None or num > Bignum:  # if value() is none or bigger than the replaced value()
        Bigcomment = comment
        Bignum = num

print(Bigcomment, Bignum)
