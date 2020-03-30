# Python Data Structures - Week 7 - Assignment 6.1

text = "X-DSPAM-Confidence:    0.8475"

pos = text.find(":")
num = float(text[pos+1:].strip())
print (num)
