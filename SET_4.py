"""
  remove and discard method in sets
"""
A = set()
A.add(7)
A.add(3)
A.add(1)
A.add(9)
print("A:",A)
#A.remove(11)
A.discard(11)
print("A:",A)
A.discard(1)
print("A:",A)