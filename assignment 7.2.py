# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating
# point values from each of the lines and
# compute the average of those values and
# produce an output as shown below. Do not
# use the sum() function or a variable named
# sum in your solution.
# You can download the sample data at
# http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter
# mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0 # set to 0 so that later can add
total = 0 # set to 0 so that later can add
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    va = line.find(" ")
    val = line[va:].rstrip() # for spaces starting from va in line, strip \n
    # print(val)
    val = float(val)
#    print(val) # for checking purposes
    count = count + 1
    total = total + val # set total as total. Slowly add all values
    average = total/count

print("Average spam confidence:", average)