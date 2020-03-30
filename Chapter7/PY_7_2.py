#7.1 Write a program that prompts for a file name,
#then opens that file and reads through the file,
#and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

fname = input("Enter file name: ")
fh = open (fname)
spamcnt = 0
spamtot = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    spam = float(line[line.find(":")+1:].strip())
    spamcnt = spamcnt+1
    spamtot = spamtot + spam
spamavg = spamtot/spamcnt

print ("Average spam confidence:", spamtot/spamcnt)
