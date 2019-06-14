"""
Date: 6/14/19
2.2: Generate Palindrome Pairs
"""

'''
Problem Statement: Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.
    A palindrome is a word that reads the same backwards as forwards
    Ex1. ["code", "edoc", "da", "d"] returns [(0,1), (1,0), (2,3)]

'''

'''                             My Solution                              '''
# Simple solution where you combine the two strings in question and move in from both ends as long as the characters are equivalent to eachother
        ## if the left,right indices cross then you know you have a palindrome
def palidrome_pairs(strings):
    result = []

    for i in range(len(strings)):
        for j in range(len(strings)):
            if i != j:
                temp = strings[i] + strings[j]
                left,right = 0, len(temp)-1
                while left <= right and temp[left] == temp[right]:
                    left += 1
                    right -= 1
                if left > right:
                    result.append((i,j))

    return result
'''Notes: This works but seems like the run time would be terrible and there is probably a better way. Run time would be O(n^2 *(len(temp)/2))
        * Can't think of any way we are duplicating work or a way to use a different data structure like a dictionary to help.
'''

'''                             Book Solution                            '''
def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    result = []

    for i,word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                result.append((i,j))

    return result
'''Notes:
        * I need to remember when you need and index and the actual item from a list use enumerate
        * I think the if i == j continue is more confusing then i != j like I did
        * word[::-1] will reverse the word for you
        * Can extract out functionality like is_palindrome so that code looks a little clearner (i prefer to have the helper functions below)
            ** Try to keep one function doing one job, having is_palindrome seperate accomplishes that
'''

def fast_palindrome_pairs(words):
    #Create a dictionary of (word,index) pairs
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    result = []
    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if is_palindrome(suffix) and reversed_prefix in d:
                if i != d[reversed_prefix]:
                    result.append((i,d[reversed_prefix]))
            if is_palindrome(prefix) and reversed_suffix in d:
                if i != d[reversed_suffix]:
                    result.append(d[reversed_suffix], i)
    return result
'''Notes:
        * I feel like the added code complexity in this solution is not worth the improvement in run time.
        ** It would be worth it if you really needed a faster method and no one was ever going to work on this method again so the
                complexity doesnt really hurt anyone but the first person writing the code. 
'''

'''                             Test Cases                               '''
def main():
    Ex1 = ["code", "edoc", "da", "d"]
    print(palidrome_pairs(Ex1) == [(0,1), (1,0), (2,3)])

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Remember to use enumerate when you need an index and the item from the list
    * Keep functions doing one job and use helper functions to extract away seperate tasks
    * word[::-1] will reverse a string for you
    * Remember there is usually a trade off between speed and comlexity. More complex code my be faster but it will be harder to 
        maintain in the future. Just keep that in consideration.
    * Also keep in mind that O() is not the only metric that matters. My original solution O() notation is not great but most words
        are not actually palandromes and therefore will short and finish way before checking the entire string. 
'''