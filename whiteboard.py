# Don't give me five!
# In this kata you get the start number and the end number of a region and should 
# return the count of all numbers except numbers with a 5 in it. The start and the 
# end number are both inclusive!

# Examples:

# 1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
# The result may contain fives. ;-)
# The start number will always be smaller than the end number. Both numbers can be 
# also negative!

# input - 1st and last num in a range / output - count of ints in the list (after any num with 5 is taken out)
# given 2 int, find the range(x, y+1)
# loop thru int list
# create new list
# find any number with 5 in it - remove it / if no 5, add to new list
# count integers in new list 

def solution(x, y):
    z = range(x, y+1)
    new_list = []
    for i in z:
        if str(5) not in str(i):
            new_list.append(i)
    endcount = len(new_list)
    return endcount