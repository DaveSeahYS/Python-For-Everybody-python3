# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from
# the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each
# hour, print out the counts, sorted by hour as shown below.

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
#
# hours = dict()
#
# for lines in handle:  # for all the lines in the file
#     lines.rstrip()  # strip the right spaces
#     if not lines.startswith("From "): continue  # if it doesnt start with From, continue
#     words = lines.split()  # split lines into words
#
#     hour = words[5].split(":")  # split the 6th word by : which is  09:14:16
#     hours[hour[0]] = hours.get(hour[0],0) + 1  # get only the first part which is the hours
#
# lst = []  # create an empty list
#
# for a,b in hours.items():  # for the key and value in key() and value()
#     lst.append((a,b))  # add the tuples together
#
# lst.sort()  # sort the list by the keys which is the hour
#
#
# for a,b in lst:  # for key and value in list
#     print (a,b)


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()
for lines in handle:
    lines.rstrip()
    if not lines.startswith('From '): continue
    words = lines.split()

    hour = words[5].split(":")
    hours[hour[0]] = hours.get(hour[0], 0) + 1

lst = []

for a,b in hours.items():
    lst.append((a,b))

lst.sort()

# for a,b in lst:
for a,b in lst:
    print(a,b)
