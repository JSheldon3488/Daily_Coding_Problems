"""
Date: 8/24/20
14.1: Compute Flight Itinerary
"""

'''
Problem Statement: Given an unordered list of flights taken by someone,ach represented as (origin, destination) pairs,
and a starting airport, compute a possible itinerary. If no such itinerary exists, return None. All flights must be used
in the itinerary.

Example: [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] starting = 'YUL'
    :returns ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

Example2: [('SFO', 'COM'), ('COM', 'YYZ')] starting = 'COM'
    :returns None

'''

'''                             My Solution                              '''


'''                             Book Solution                            '''


'''                             Test Cases                               '''
def main():
    return

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Raising an exception is better than returning None! Can have messages in exceptions as well. Usually not a good
        idea to let things fail silently.
    * Wouldn't this be a better example of backtracking if a starting airport like say 'SFO' had more than one destination
        airport so that if it doesnt find a path moving forward it can back track and try a new path?
'''

