"""
Date: 6/17/19
2.4: Determine smallest rotated string
"""
from queue import Queue

'''
Problem Statement: You are given a string of length n and an integer k, The string can be manipulated by taking one of the 
    first k letters and moving it to the end of the string. Write a program to determine the lexicographically smallest string
    that can be created after an unlimited number of moved. 
    Ex1. "daily" k = 1, returns "ailyd"

'''

'''                             My Solution                              '''
def smallest_lexico_string(String, k):
    #Base Case: K = 0 so can not do anything
    if k == 0:
        return String

    #Seems easier to just deal with the rotations if the string is a list
    s = list(String)
    # When K = 1 just rotate until the lowest char is in the firs position
    if k == 1:
        while s[0] != min(s):
            rotate_firstele(s)
        return "".join(s)

    #K > 0 can rotate until sorted
    else:
        return "".join(sorted(s))


def rotate_firstele(s):
    ele = s.pop(0)
    s.append(ele)

'''                             Book Solution                            '''
def bubble_swap(string,i,j):
    string = list(string)

    # Rotate so that i is at the beginning.
    while i>0:
        string = string[1:] + string[:1]
        i -= 1

    #Move the first two letters to the end in reversed order.
    string = string[:1] + string[2:] + string[1:2]
    string = string[1:] + string[:1]

    # Rotate back to the initial position
    while len(string) > j + 1:
        string = string[1:] + string[:1]
        j += 1

    return "".join(string)

def get_best_word(string,k):
    string = list(string)

    if k == 1:
        best = string
        for i in range(1,len(string)):
            if string[i:] + string[:i] < best:
                best = string[i:] + string[:i]
        return "".join(best)
    else:
        return "".join(sorted(string))
'''Notes:
    *I don't like calling the string converted to list still string. I think that is confusing notation and can lead you to think
    ** you should be using string methods and not list methods
    * I think this problem was poorly done

'''

'''                             Test Cases                               '''
def main():
    Ex1 = "daily"
    print(smallest_lexico_string(Ex1,1) == "ailyd")
    print(smallest_lexico_string(Ex1,2))

if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Using proper names is extremely important! Name things what they are so that it just makes sense exactly what mehotds
        ** can and can not be used on the object. Also it just helps make the code easier to read and understand
    * Full explanation of the problem helps a lot. If you are unsure what the problem is asking make sure to clarify before you try to solve
    * "".join(list) is a nice way to turn a list into a string in Python
'''