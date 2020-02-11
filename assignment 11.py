# using the file regex_sum_357298.txt
# find the sum of all the values within it


# import re
#
# file = open('regex_sum_357298.txt', 'r')
#
# sum = 0
#
# for val in file:
#     value = re.findall('[0-9]+', val)
#     for va in value:
#         sum = sum + int(va)
#
# print(sum)



import re

file = open('regex_sum_357298.txt', 'r')

sum = 0

for values in file:
    numbers = re.findall('[0-9]+', values)
    for integer in numbers:
        sum = sum + int(integer)

print(sum)