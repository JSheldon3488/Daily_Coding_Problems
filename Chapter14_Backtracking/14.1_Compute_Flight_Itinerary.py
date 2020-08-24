"""
Date: 8/24/20
14.1: Compute Flight Itinerary
"""

'''
Problem Statement: Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute a possible itinerary. If no such itinerary exists, return None. All flights must be used
in the itinerary.

Example: [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] starting = 'YUL'
    :returns ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

Example2: [('SFO', 'COM'), ('COM', 'YYZ')] starting = 'COM'
    :returns None

'''

'''                             My Solution                              '''
""" I am confused how this is a backtracking problem. Wouldn't I just start at the starting airport, go to its destination,
and pop that tuple out of the list, then repeat until there is no match for starting airport or the list is empty in which
case we are done? I do not see how I backtrack here? """
from typing import List
def itinerary(starting: str, org_dest: List[tuple], result=[]) -> List[str]:
    try:
        # Base Case
        if not org_dest:
            return result + [starting]

        # Recursive Case
        for org, dest in org_dest:
            if org == starting:
                org_dest.remove((org, dest))
                return itinerary(dest, org_dest, result + [org])

        # starting not any origin so can not complete itinerary
        raise NoPossibleItinerary(starting, result)

    except NoPossibleItinerary as e:
        print("No possible itinerary exists.")
        print(f"Current trip: {e.result_so_far}")
        print(f'Got stuck in {e.current}')

class NoPossibleItinerary(Exception):
    def __init__(self, start: str, result: List[str]):
        self.current = start
        self.result_so_far = result + [start]


'''                             Book Solution                            '''
def get_itinerary(flights, current_itinerary):
    if not flights:
        return current_itinerary

    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        flights_minus_current = flights[:i] + flights[i+1:]
        current_itinerary.append(destination)
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinerary)
        current_itinerary.pop()

    return None

'''                             Test Cases                               '''
def main():
    i1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    starting = 'YUL'
    assert itinerary(starting, i1) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

    i2 = [('SFO', 'COM'), ('COM', 'YYZ')]
    starting = 'COM'
    itinerary(starting, i2)

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Raising an exception is better than returning None! Can have messages in exceptions as well. Usually not a good
        idea to let things fail silently.
    * Wouldn't this be a better example of backtracking if a starting airport like say 'SFO' had more than one destination
        airport so that if it doesnt find a path moving forward it can back track and try a new path?
            No becuase all flights must be used...
    * Create a class that inherits from Exception, then you can pass variables to it by using the dunder init
        then use the try block on your code and raise this exception if needed and catch it in the except block
        and print out whatever message you want.
    * This felt like a real stretch for them to turn this problem into a backtracking problem. I just do not think this
        is a good example of when to use backtracking.
'''

