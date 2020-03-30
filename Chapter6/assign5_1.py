# P4E - Week 7 - Assignment 5.1

largest = None
smallest = None

while True:
    numstr = input('Enter a number: ')
    if numstr == "done": break
    try:
        number =  int(numstr)
    except:
        print('Invalid input')
        continue

    if largest is None : largest = number
    if smallest is None :
        smallest = number
        continue
    if number < smallest: smallest = number
    if number > largest: largest = number

if largest is not None : print('Maximum is', largest)
if smallest is not None : print('Minimum is', smallest)
