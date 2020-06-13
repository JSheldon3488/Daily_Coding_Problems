"""
Date: 6/13/20
5.3: Implement a sparse array
"""

'''
Problem Statement: You have a large array, most of whose elements are zero. Create a more space efficient data structure
called SparseArray, that implements the following interface.

    -init(arr,size): initialize with the original large array and size.
    -set(i,val): update index at i to be val
    -get(i): get the value at index i

'''

'''                             My Solution                              '''
""" I am unsure what they really want me to do here? Do we just ignore the elements that are 0? Do we map index to val
in a hash table and anything that was value 0 doesn't get mapped? This would lead to more space efficiency and allow us
to set and get values at a specific index. I assume this is what they want so I will implement that.
To improve space efficiency use dictionary where key is index value is original value in array, any 0 vals are not mapped. """

from typing import List

class SparseArray():
    """ Turn a sparse array into a more space efficient data structure """
    def __init__(self, arr: List[int], size: int):
        self.size = size

        # Initialize the new sparse container: dict(index -> value)
        self.sparse_container = {}
        for index, val in enumerate(arr):
            if val != 0:
                self.sparse_container[index] = val

    def set(self, i: int, val: int):
        self._check_boundary(i)
        if val != 0:
            self.sparse_container[i] = val
        elif i in self.sparse_container:
            del self.sparse_container[i]

    def get(self, i: int) -> int:
        self._check_boundary(i)
        if (val := self.sparse_container[i]):
            return val
        return 0
        # self.sparse_container.get(i,0) works better

    def _check_boundary(self, i):
        if 0 <= i < self.size-1:
            return
        raise IndexError("Index out of array range")

    def reconstruct(self) -> str:
        """ turns our SparseArray into a bitstring """
        return "".join([str(self.sparse_container.get(index,0)) for index in range(self.size)])


'''                             Book Solution                            '''
class SparseArray_book():
    def __init__(self, arr, n):
        self.n = n
        self._dict = {}
        for i,e in enumerate(arr):
            if e != 0:
                self._dict[i] = e

    def _check_bounds(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("Out of bounds")

    def set(self, i, val):
        self._check_bounds(i)
        if val != 0:
            self._dict[i] = val
            return
        # Delete from array if inserting a 0
        elif i in self._dict:
            del self._dict[i]

    def get(self, i):
        self._check_bounds(i)
        return self._dict.get(i, 0)

def main():
    bit_array = [1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0]
    sparse_array = SparseArray(bit_array,16)
    assert sparse_array.reconstruct() == "1010011010000000"

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * You need to ask what a default value should be or if you should throw an exception
    * Remember that you have to check the bounds of size if you are going to use dictionary instead of an array because
        a dictionary can have any key that is hashable (immutable) so -1,-10,size+1 will all work.
    * always use enumerate if you need the element value and the index for that element!
    * I think using _ before an attribute or method means this is private to the class and should be treated as such
        (although I do not think this is enforced by python)
    * If you implement the same functionality multiple times across the code its probably best to abstract that functionality
        into a helper function (like bounds checking here)
    * We needed to delete the value if you tried putting a 0 into the sparse array. Any index that has a value 0 should not
        be in the spare_array. ( I think this is for a bit array or something that you can assume 0 if not in array)
    * Dictionaries have a .get method where you can return a default if that index is not in the dictionary
    * When using .join on an iterable you must have a str instance as the thing you are joining
'''

