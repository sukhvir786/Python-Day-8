"""
    1. Add Elements using for loop
    2. Union & Intersection
    3. Difference of Sets
    4. Symmetric Difference
"""
A = set()
for i in range(1,6):
    A.add(i)
print("A:",A)

B = set()
for j in range(3,8):
    B.add(j)
print("B:",B)

print("Union:",A|B)
print(A.union(B))
print("Intersection:",A&B)
print(A.intersection(B))
print("A-B:",A-B)
print(A.difference(B))
print("B-A:",B-A)
print(B.difference(A))
print("Sym Diff:",A^B)
print(A.symmetric_difference(B))
