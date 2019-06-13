"""
Date: 6/13/19
2.1: Find anagram indices
"""
from collections import Counter
from collections import defaultdict
'''
Problem Statement: Given a word w and a string s, find all indices in s which are the starting locations of anagrams of w.
    Ex. w = ab and s = abxaba returns [0,3,4]
    By anagram they mean that letters in the word w are used to form other words in s. (kind of loose with the definition of a word)
'''

'''                         My Solution                             '''

def anagram_indices(w,s):
    start_indices = []
    s_copy = s.replace(" ", "").lower()

    #Iterate over all the characters in s and remove them from w as long as you still have a consecutive match
    for i in range(len(s)):
        w_copy = w.replace(" ", "").lower()
        j = i
        while len(w_copy) > 0 and j < len(s_copy) and s_copy[j] in w_copy:
            w_copy = w_copy.replace(s_copy[j], "", 1)
            j+=1
        # w_copy is empty so found anagram starting at i
        if len(w_copy) == 0:
            start_indices.append(i)

    return start_indices
'''Notes:
    * This solution works by deleting characters from w that are found in s in successive order. If w ends up being empty after the deletion then
        we know we found an anagram of w in s.
    * My original solution worked as long as there was no spcaes so i fixed that by removing all spaces from w and s.
    * Also my original solution was case sensitive so I removed that problem by changing both strings to lower case.
    * A lot of little adjustments can be made or not made depending on the problem statement and the definition of "anagrams"
    * My for loop is wasteful because only need to check range(len(s)-len(w)+1) because otherwise anagram not possible as len(w) > remaining len(s)
'''

'''                         Book Solutions                          '''

def is_anagram(s1,s2):
    return Counter(s1) == Counter(s2)

def book_anagram_indices(word, s):
    result = []
    for i in range(len(s) - len(word) + 1):
        window = s[i: i +len(word)]
        if is_anagram(window,word):
            result.append(i)
    return result
'''Notes:
    * Counter takes in a collection and turns it into a dictionary whos keys are characters and values are counts of that character in the string.
        So obviously if the two Counter dictionaries are equivalent then they are an anagram
'''

def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]

def book_fast_anagram_indices(word, s):
    result = []

    freq = defaultdict(int)     #This tells the dictionary the values will be ints

    #Build Dictionary for the word
    for char in word:
        freq[char] += 1

    #Delete entries from a given window size in the string s
    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq, char)

    #If the dictionary is empty then it was an anagram
    if not freq:
        result.append(0)

    #Do this same process for all possible windows but you only need to delete the left item no longer in the window
    ## and add the right item that now is in the window
    for i in range(len(word), len(s)):
        start_char, end_char = s[i - len(word)], s[i]
        freq[start_char] += 1
        del_if_zero(freq, start_char)

        freq[end_char] -= 1
        del_if_zero(freq, end_char)

        if not freq:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result
'''Notes:
    * Very similar to my original approach of deleteing matching items just using a dictionary and optimized
    ** The optimization they used is that you do not have to recheck every single window you just need to delete the char that is no
            longer in the window and add the new char that is in the window. This saves time not redoing work you already did.
'''

'''                         Test Cases                              '''
def main():
    ex_w1 = "ab"
    ex_s1 = "abxaba"
    print(anagram_indices(ex_w1,ex_s1) == [0,3,4])
    ex_w2 = "Stressed"
    ex_s2 = "Desserts"
    print(anagram_indices(ex_w2,ex_s2) == [0])
    ex_w3  = "Eleven plus two"
    ex_s3 = "Twelve plus one"
    print(anagram_indices(ex_w3,ex_s3) == [0])

if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Use string.replace("char", "with", count) to delete individual things from a string in Python
    * The problem statment is very important! The solution will be different depending on the definition of an "anagram".
        This will be common with most problems so make sure you completely understand the problem statement.
    * Always think hashtable first when solving problems with strings
    * Always try to think of places where you are doing work twice and see if you can just use the previous results
    * Using defaultdict allows you to specify the data type of the value field in the dictionary. So if you specifically want a list
        and not counts or vice versa you can specify that when you create the dictionary like we did above (freq = defaultdict(int))
    ** also defaultdict simplifies the code because you do not have to have the if not in dict then make a new entry else add stuff
'''

