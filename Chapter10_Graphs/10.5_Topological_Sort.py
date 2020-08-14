"""
Date: 8/14/20
10.5: Topological Sort
"""

'''
Problem Statement: We are given a hashmap associating each courseID key with a list of courseID values, which tell us 
that the prerequisites of courseID key are courseIDs values. Return a sorted ordering of courses such that we can complete
the curriculum. Return None if there is no such ordering.
Example:
    { 'CSC300' : ['CSC100', 'CSC200'],
      'CSC200' : ['CSC100']
      'CSC100' : []
    }
    :returns ['CSC100', 'CSC200', 'CSC300']
'''

'''                             My Solution                              '''
from typing import Dict, List
from collections import deque, defaultdict

def top_sort(course_to_prereqs: Dict) -> List:
    course_to_prereqs = {course: set(prereqs) for course, prereqs in course_to_prereqs.items()}

    # Reverse dictionary to get all classes that require a given prereq
    prereq_to_courses = defaultdict(list)
    for course, prereqs in course_to_prereqs.items():
        for prereq in prereqs:
            prereq_to_courses[prereq].append(course)

    # Topological Sort Algorithm
    results = [course for course, prereqs in course_to_prereqs.items() if not prereqs]
    to_process = deque(results)

    while to_process:
        prereq = to_process.popleft()
        for course in prereq_to_courses[prereq]:
            course_to_prereqs[course].remove(prereq)
            if not course_to_prereqs[course]:    # Now empty prereqs list
                results.append(course)
                to_process.append(course)

    if len(results) < len(course_to_prereqs):
        return None
    return results

'''                             Test Cases                               '''
def main():
    data = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': [],
            'CSC400': ['CSC300'], 'CSC500' : ['CSC300'],
            'ENG101': [], 'ENG102': ['ENG101']}
    print(top_sort(data))

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Having a reverse lookup list can be very helpful so that you do not have to iterate through every single 
        item if you know you are going to need to go in and delete items in the first dictionary.
'''

