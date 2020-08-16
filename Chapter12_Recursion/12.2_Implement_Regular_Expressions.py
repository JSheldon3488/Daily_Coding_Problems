"""
Date: 8/14/20
12.2: Implement Regular Expressions
"""

'''
Problem Statement: Implement regular expression matching with the following special characters
    1. .(period) which matches any single character
    2. *(asterisk) which matches zero or more of the preceding elements
That is, implement a function that takes in a string and a valid reg expressions and returns whether or not the string
matches the regular expression.
Example:
    input: ra. "ray"
    return: True
    input: ra. "raymond"
    return: False
    input: .*at "chat"
    return True
    input: .*at "chats"
    return False
'''

'''                             My Solution                              '''
""" My first thoughts are that you just eat characters from both regular expression and input string and if they do
not match you return false else you call it again on the substring with this character gone. If you get to a point where
the regular expression is gone or the string is gone but the other one still exists then return false. 
The tricky part of this will be dealing with char* and .*
char* we can just use a while too remove that char as many times as possible.
.* I think the way to go about this is to recursively call all possible combinations of what .* can remove and see if any
of those lead to a True and if not then its False. So .*at 'chats' would branch to regex at with '', 's', 'ts', 'ats', 'hats', 'chats'
all of which would return false which is why it is false"""

def reg_expression(regex: str, candidate: str) -> bool:
    # Base Cases
    if not regex and not candidate:
        return True
    if not regex or not candidate:
        return False
    if len(regex) == 1:
        if regex[0] == '.':
            return len(candidate) == 1
        elif regex[0] == candidate[0]:
            return len(candidate) == 1
        else:
            return False

    # Recursive char case
    if regex[0] != '.' and regex[1] != '*':
        if regex[0] != candidate[0]:
            return False
        return reg_expression(regex[1:], candidate[1:])

    # Recursive . case
    if regex[0] == '.' and regex[1] != '*':
        return reg_expression(regex[1:], candidate[1:])

    # Recursive char* case
    if regex[0] != '.' and regex[1] == '*':
        move = 0
        while regex[0] == candidate[move]:
            move += 1
        return reg_expression(regex[2:], candidate[move:])

    # Recursive .* case
    return any(reg_expression(regex[2:], candidate[i:]) for i in range(len(candidate)))

'''                             Book Solution                            '''
def matches_first_char(s,r):
    return s[0] == r[0] or (r[0] == '.' and len(s) > 0)

def matches(s,r):
    if r == '':
        return s == ''

    if len(r) == 1 or r[1] != '*':
        if matches_first_char(s,r):
            return matches(s[1:], r[1:])
        else:
            return False

    else:
        if matches(s, r[2:]):
            return True

        i = 0
        while matches_first_char(s[i:], r):
            if matches(s[i+1:], r[2:]):
                return True
            i += 1

'''                             Test Cases                               '''
def main():
    assert reg_expression('ra.', 'ray') == True
    assert reg_expression('ra.', 'raymond') == False
    assert reg_expression('.*at', 'chat') == True
    assert reg_expression('.*at', 'chats') == False
    assert reg_expression('a*zzz', 'aaazzz') == True
    assert reg_expression('a*zz', 'aaaazzz') == False

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Any time you are indexing make sure that that index exists!
    * Dont forget that char* is a case we have to think about
    * My solution is very dependent on the checks from before or else the code breaks which is kind of bad. Linear code
        like this can lead to a lot of problems and is typically difficult to understand and follow because you have to
        remember what came before to know that you can do or not do certain things.
    * Their solution will exit before mine I think, unless any call on a generator returns true as soon as it sees a true
    * I do think their code is a little harder to follow with the deeply disjoint if else. If you are going to do this if
        else structure where else is many lines below I think you need comments to break up what the cases are.
'''

