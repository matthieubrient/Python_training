# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:17:27 2020

@author: matth
"""
#print element 2 by 2
Good="GsoAo+d"
print(Good[::2])

###edit and sort tuple
C_tuple=(-5, 1, -3)
C_tuple = sorted(C_tuple)
print(C_tuple)

###edit list
a_list = [1, 'hello', [1,2,3] and True]
print(a_list)

###combine list
A = [1, 'a']  
B = [2, 1, 'd']

list = A + B
print(list)

###add to a set
S = {'A','B','C'}
S.add('D')
print(S)

###find intersection between two sets
A={1,2,3,4,5}
B={1,3,9, 12}

C=A.intersection(B)
print(C)

###union two sets

S={'A','B','C'}

U={'A','Z','C'}

print(U.union(S))

###compare sum of list and set list
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

print("the sum of A is:", sum(A))
print("the sum of A is:", sum(B))

# Check if subset

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1.union(album_set2)
print(album_set3)
print(set(album_set1).issubset(album_set3))    