"""
Date: 7/30/20
9.2: Find most similar websites
"""

'''
Problem Statement: You are given a list of (website, user) tuples that represent users visiting websites. Come up with
a program that identifies the top k pairs of websites with the greatest similarity. To compute similarity between two websites
you should compute the number of users they have in common divided by the number of users who have visited either site in total.
Example:
    [("google.com", 1), ("google.com", 3), ("google.com", 5),
    ("pets.com", 1), ("pets.com", 2),
    ("yahoo.com", 6), ("yahoo.com", 2), ("yahoo.com", 3), ("yahoo.com", 4), ("yahoo.com", 5),
    ("wikipedia.com", 4), ("wikipedia.com", 5), ("wikipedia.com", 6), ("wikipedia.com", 7),
    ("bing.com", 1), ("bing.com", 3), ("bing.com", 5), ("bing.com", 6)]
    :returns ("google.com", "bing.com", 0.75)
'''

import heapq
from collections import defaultdict
'''                             My Solution                              '''
""" So we need to know all users that visited a given site and then compare them to every other site to be able to
report the similarity score, then for each pair insert into a max heap so that we can efficiently get the top k. 
To keep track of each sites set of users we could use a dictionary to map websites to sets of users. 
To compute the similarity score between two sites we can divide the intersection of the two sets by the union.
We need a way to not recompute the same similarity score because google/bing is the same as bing/google. I did this by using
nested loops. I think this is as efficient as you can do it because it only calculates each pair once.

"""
def create_sets(data: (str, int)):
    d = defaultdict(set)
    for website, user in data:
        d[website].add(user)
    return d

def calc_similarity(a: set, b: set) -> float:
    return len(a.intersection(b))/len(a.union(b))

def k_most_similar_websites(k: int, data: (str,int)) -> (str,str,float):
    # Set up necessary variables
    data_sets = create_sets(data)
    sites = list(data_sets.keys())
    heap = []

    # Compute each pair of similarity scores and put into a max heap (using *-1 to get max heap)
    for i in range(len(sites)):
        for j in range(i+1,len(sites)):
            score = calc_similarity(data_sets[sites[i]], data_sets[sites[j]])
            heapq.heappush(heap, [-1*score, sites[i], sites[j]])

    # Get top k similar websites
    solution = []
    for _ in range(k):
        res = heapq.heappop(heap)
        res[0] = -1*res[0]
        solution.append(res)

    return solution

'''                             Book Solution                            '''
def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])

def top_pairs(log, k):
    visitors = defaultdict(set)
    for site, user in log:
        visitors[site].add(user)

    pairs = []
    sites = list(visitors.keys())

    for _ in range(k):
        heapq.heappush(pairs, (0, ('', '')))

    for i in range(len(sites) - 1):
        for j in range(i+1, len(sites)):
            score = compute_similarity(sites[i], sites[j], visitors)
            heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

    return [pair[1] for pair in pairs]

'''                             Test Cases                               '''
def main():
    data = [("google.com", 1), ("google.com", 3), ("google.com", 5),
            ("pets.com", 1), ("pets.com", 2),
            ("yahoo.com", 6), ("yahoo.com", 2), ("yahoo.com", 3), ("yahoo.com", 4), ("yahoo.com", 5),
            ("wikipedia.com", 4), ("wikipedia.com", 5), ("wikipedia.com", 6), ("wikipedia.com", 7),
            ("bing.com", 1), ("bing.com", 3), ("bing.com", 5), ("bing.com", 6)]

    print(k_most_similar_websites(1,data))
    print(k_most_similar_websites(2,data))
    print(k_most_similar_websites(3,data))
    print(k_most_similar_websites(4,data))

    print(top_pairs(data, 3))


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * I think my solution was a pretty good use of multiple data structures.
    * & and | are great ways to get intersections and unions as well
    * If you know you only need k elements you can make sure that you never store more than k elements to save memory
    * pushpop allows you to only keep k items and if its a min heap each time the smallest item will be poped off just keep the 
    k max items (but out of order)
'''

