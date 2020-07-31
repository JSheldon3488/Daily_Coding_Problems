"""
Date: 7/31/20
9.3: Generate Regular Numbers
"""

'''
Problem Statement: A regular number in mathematics is defined as one which evenly divides some power of 60.
Equivalently, we can say that a regular number is one whose only prime divisors are 2,3,5.
These numbers have had many applications, from helping ancient Babylonia's keep time to tuning instruments according to the diatonic scale.
Given an integer n, write a program that generates, in order, the first n regular numbers.
'''

'''                             My Solution                              '''
""" I am really bad at these find the math pattern problems. Also at first glance I do not see how a heap is necessary or useful here.
Lets see what we can do. First we know that we will need to use a generator to save us tons of memory for a problem like this.
Secondly my guess is that if we can generate these numbers somehow and put them into a heap then we can return them in 
ascending order...
After a quick read on wikipedia it seems like this is a famous problem. The first number is 1, then every number after that
is one of 2h, 3h, 5h, where h is any previous hamming number. So you could start with 1 and pop it off the heap and multiply 
it by 2, 3, and 5 and then put those on the heap. Then to generate the next round you would pop off 2 and do the same thing.
Little hiccup here is that we want to generate them in ascending order and if we returned all the results from 2 then that would be
incorrect because 2*5 is 10 and 3*3 is 9 so we cant just return all the results for 2. That should be fine if we are using a heap
and just return the result after we add all its children to the heap.
The second hiccup that comes to mind is repeats. 2*3 is 6 and so is 3*2.... We could keep a dictionary or set of values
we have already pushed onto the heap to prevent repeats on the heap. (Dictionary would have faster lookups here then checking 
the entire set). I think that plan will work. Obviously using in would work but that is linear every single time which is expensive."""

from collections import defaultdict
import heapq

def gen_regular_numbers(n: int):
    seen = defaultdict(int)
    heap = [1]

    for _ in range(n):
        res = heapq.heappop(heap)
        yield res
        for num in (2 * res, 3 * res, 5 * res):
            if not seen[num]:
                seen[num] = True
                heapq.heappush(heap, num)


'''                             Book Solution                            '''
def regular_numbers(n):
    solution = [1]
    last = 0; count = 0

    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x; count += 1
            heapq.heappush(solution, 2*x)
            heapq.heappush(solution, 3*x)
            heapq.heappush(solution, 5*x)


'''                             Test Cases                               '''


def main():
    assert list(gen_regular_numbers(20)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    assert list(gen_regular_numbers(15)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    assert list(gen_regular_numbers(10)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

    assert list(regular_numbers(20)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    assert list(regular_numbers(15)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    assert list(regular_numbers(10)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

    list(regular_numbers(100000))
    list(gen_regular_numbers(100000))

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Remember 0 is False 1 is True for default dicts so that you can easily check if key in dictionary
    * When it says that only prime divisors are 2,3,5 then we know that every single value has to be a multiple of one of these
        3 numbers that is why we can just pop off a previous regular number and multiply it by 2,3,5 and get the next round
        of regular numbers
    * There solution is very similar but they are pushing all the values on the heap and just keeping track of the last value
        they yielded to make sure they are not returning duplicates. This seems less time (and maybe space) efficient than
        my solution. I feel like the extra log(n) pushes are worse then the extra lookups. But its close. Both are so fast
        the profiler doesnt pick up a difference
        ** For input of n=100000 my solution is significantly faster. Theres runs in 456ms and mine in 260ms. I think this is
            due to all the additional heap pops and pushes they have to do because not only do they push duplicates onto the heap
            they also has to pop duplicates off and keep the heap invariant satisfied the entire time.
        ** Note that my solution does have the extra dictionary space (but slightly less space in the heap). Their solution
            is probably more space efficient overall which shows the space vs speed tradeoff.
'''
