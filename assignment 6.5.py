# Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below. Convert
# the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
num = text.find('0') # find the very beginning of the number
# numb = text.find(' ', num)  # find a space after 0, not required since it uses the last character
numbe = text[num:]  # cannot text[num:numb+1] since there is no character after that
number = float(numbe)
print(number)
