"""
Date: 8/4/19
4.2 Determine whether brackets are balanced
"""
from Stack import Stack

'''
Problem Statement: Given a string of round, curly, and square opening and closing brackets, returns whether the brackets are balanced.

Ex1. Input: "([])[]({})" returns true
Ex2. Input: "([)]" returns false
Ex3. Input: "((()" returns false

'''

'''                             My Solution                              '''
def is_balanced(String):
    """
    Given a string of round, curly, and square opening and closing brackets, returns whether the brackets are balanced.
    Arguements:
        String -- an string of round curly or square brackets
    Returns:
        True if String has balanced brackets, False otherwise.
    """
    LEFTS = ["(","[","{"]
    RIGHTS = [")","]","}"]
    PAIRS = ["()", "[]", "{}"]
    stack = Stack()

    for char in String:
        if char in LEFTS:
            stack.push(char)
        if char in RIGHTS:
            #Right with no left so cannot be balanced
            if stack.size == 0:
                return False
            else:
                test = str(stack.pop()) + char
                #Not a matching pair between right and left so cannot be balanced
                if test not in PAIRS:
                    return False
    #Stack must be empty to be balanced otherwise we have too many lefts
    return stack.size == 0

'''                             Book Solution                            '''
def balance(s):
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            if  (char == ")" and stack[-1] != "(") or \
                (char == "]" and stack[-1] != "[") or \
                (char == "}" and stack[-1] != "{"):
                return False
            stack.pop()
    return len(stack) == 0
""" Notes:
    * We used the same method but I think mine is cleaner.
    * I could have not had a RIGHTS list because if its not a left then it has to be a right    
"""

'''                             Test Cases                               '''
def main():
    print(is_balanced("([])[]({})") == True)
    print(is_balanced("([)]") == False)
    print(is_balanced("((()") == False)
    help(is_balanced)

if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Can save a little space in memory if you have a disjoint set of inputs where if its not in one it has to be in other
        Then all you have to have is one of the sets covered and the other can be implied.
'''
