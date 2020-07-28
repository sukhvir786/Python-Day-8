"""
    Subset, superset and disjoint sets
"""
A = set()
for i in range(1,10,2):
    A.add(i)
print("A:",A)

B = set()
for j in range(1,10):
    B.add(j)
print("B:",B)

C = set()
for k in range(2,11,2):
    C.add(k)
print("C:",C)

print("A is a subset of B:",A.issubset(B))
print("A is superset of B:",A.issuperset(B))
print("B is a superset of A:",B.issuperset(A))
print("A and C are disjoint sets:",A.isdisjoint(C))
print("A and B are disjoint sets:",A.isdisjoint(B))