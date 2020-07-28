"""
SET:
    A well defined collection of objects
    Repeatition is not allowed in a set
    Elements are unordered while we display set
    Set is always written in curly brackets {}
    Set is mutable:
        we can add or delete elements in a set
    Union:
        Representation of two or more sets in single
        condition is that repeatition is not allowed
    Intersection:
        Representation of common elements
        if there is no element common
        then sets are known as disjoint sets
TOPICS:
    1. Declaration of SET
    2. How to add elements in a set
    3. How to check whether it's a set or not
    4. use of in and not in operator
    5. How to delete an element from a set
    6. Copy all the elements of one set into another
    7. How to delete all elements from set
"""
A = set()
A.add(1)
A.add(2)
A.add(31)
A.add(10)
A.add(27)
print("A:->",A)
print(type(A))
print("2 in A:",2 in A)
print("9 in A:",9 in A)
print("9 not in A:",9 not in A)
A.remove(1)
print("After removing 1 from A:")
print("A:->",A)
B = A.copy()
print("B:->",B)
B.clear()
print("B:->",B)
C = {1,3,5,2,5,6}
print("C:->",C)
print(type(C))