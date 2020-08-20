"""
Date: 8/20/20
13.2: Number of ways to decode a string
"""

'''
Problem Statement: Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be
decoded.
Example: "111" returns 3
                'aaa', 'ka', 'ak'
                [1,1,1], [11,1], [1,11]
Assume that all inputs are valid and decodable.
'''

'''                             My Solution                              '''
""" The recurrence relationship that I came up with is that when you look at the current number it is a combination of 
all the ways you can get to the previous number plus all the ways you could get to the previous previous number if this number
and the previous number can also be decoded. The base can be there are 1 way to get to 0 and 1 numbers and then start with the
second number (1st index) and solve from there. This is much easier to explain with examples than words
Example: '111' start at decoding '11' = all ways you can get to '1' + all ways you can get to '' if '11' is decoded
            therefore '11' = 2.
            Then go to '111' = all ways you can get to '11' + all ways you can get to '1' if '11' is decoded.
            '111' = 3
        The important part here is that if the chunk of 2 (this number and prev number) can not be decoded then the solution
        for this number is just the solution for the previous number because all you will do is add the single decoded number
        to the solution which results in the same number of ways to decode. """
from typing import Dict

def decode_combos(message: str, mappings: Dict) -> int:
    prev_prev = 1
    prev = 1

    for i in range(1, len(message)):
        curr = prev + prev_prev if (message[i-1]+message[i]) in mappings else prev
        prev_prev = prev
        prev = curr

    return prev


'''                             Book Solution                            '''
from _collections import defaultdict

def num_encodings(s):
    cache = defaultdict(int)
    cache[len(s)] = 1

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            cache[i] += cache[i+1]
            if int(s[i:i+2]) <= 26:
                cache[i] = cache[i+2]

    return cache[0]



'''                             Test Cases                               '''
def main():
    alphabet = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
                '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't',
                '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}
    assert decode_combos('111', alphabet) == 3
    assert decode_combos('131', alphabet) == 2
    assert decode_combos('1313', alphabet) == 4
    assert decode_combos('13131', alphabet) == 4
    assert decode_combos('1111', alphabet) == 5
    assert decode_combos('11111', alphabet) == 8



if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * If you can find the correct recurrence relationship for these problems they become very easy to code and very elegent.
    * Always ask yourself how is this piece a combination of previously solved pieces. Here it had to do with whether this
        piece (this number and the previous number) could be decoded or not, if it could not be then all we could do was add
        the single letter to the solutions we already had which does not create any more combinations. If it could be then
        we could also decode this piece two ways which would be the sum off the single way and the double way which is a
        combination of the previous count and the previous previous count.
    * Drawing things out on paper or a white board help a lot!
    * Their solution is bad. First off you said it takes in two arguments and your solution only has one... second off its much
        more confusing and memory intensive. If you only need the previous two values then why would you store an entire cache
        dictionary. Space inefficient. Lazy coding.
    * Also inefficient because you can go forward in the string you do not need to call the reversed function on range
    * The <= 26 makes this solution more efficient BUT it is a hard coded magic number which means that if the mapping changes
        this solution breaks. Using in mappings is slower but it allows for more versatility and if the mapping changes then
        the solution will still work..
        ** Actually key in dict is O(1) amortized so its almost as fast as the <= check (still need to hash the key which takes time)
'''

