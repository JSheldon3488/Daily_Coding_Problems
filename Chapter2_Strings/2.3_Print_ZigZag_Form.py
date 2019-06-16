"""
Date: 6/15/19
2.3: Print ZigZag Form
"""

'''
Problem Statement: Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed
    out diagonally from top left to bottom right until reaching the kth line, then back up to the top right, and so on.
    Ex. "thisisazigzag" k = 4
    t     a     g
     h   s z   a
      i i   i z
       s     g
'''


'''                             My Solution                              '''
# I can not think of any other way then hard coding everything depending on k.
# The middle gap patter is 0 1 3 5. The between char pattern is 5 3 1 0.
# I couldn't figure this one out. I was having trouble with the spacing and the indexing for the correct element in the string
# My solution was no where close. I need practice with these types of printing string problems
def print_zigzag_form(string, lines):
    left_padding = 0
    gaps = lines + 1
    mid_gap = 0
    up_downs = len(string)//lines
    while lines > 0:
        this_line = ""
        for i in range(up_downs):
            this_line += " "*left_padding + string[i*gaps] + " "*gaps
        print(this_line)
        lines -= 1
        left_padding += 1
        gaps -= 2
        mid_gap += 1


'''                             Book Solution                            '''
def get_spaces(row, desc, k):
    max_spaces = (k-1)*2 - 1
    if desc:
        spaces = max_spaces - row*2
    else:
        spaces = max_spaces - (k-1-row)*2
    return spaces

def is_descending(index,k):
    return index % (2 * (k-1)) < k -1

def zigzag(sentence, k):
    n = len(sentence)

    #Building the printouts row by row
    for row in range(k):
        i = row
        line = [" " for _ in range(n)] #list comprehension filled with n spaces

        #Creating the row with correct character and spaces for the entire row
        while i < n:
            line[i] = sentence[i]
            desc = is_descending(i,k)
            spaces = get_spaces(row, desc, k)
            i += spaces + 1

        #Join the list together to print it out like a string
        print("".join(line))
'''Notes:
    * Clever use of helper functions here to break the problem down into the correct questions and then it basically just becomes
        ** a problem of moving the index correctly depending on the row you are in and if you are descinding or ascending
    * while i < n: makes sure you never index out of range (problem i was worried about my solution)
    * Lists are mutable strings are not, using a list is faster then having to rewrite the string every single time if you were
        ** to use a string and update it the entire time.
'''


'''                             Test Cases                               '''
def main():
    print_zigzag_form("thisisazigzag", 4)
    zigzag("thisisazigzag", 4)

if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * To solve string printout type of problems the first thing you need to do is figure out the right questions to ask that
        ** effect how each row is printed out. Once you have the right questions then you can figure out a mathematical relationship
        ** for how the answers to these questions affect the printout.
    * Updateing a list and using .join(list) is more efficient then rewriting the list over and over
'''