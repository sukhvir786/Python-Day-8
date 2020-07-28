"""
Max, Min and Range
"""
F1 = open ("FFF.txt","r")
N = int(F1.readline())
print("Total Rows:",N)
print("\n")
for i in range(N):
    print("Row No",i+1,":",end="")
    M = (F1.readline().split())
    print(M)
    print("Max Value:",max(M))
    print("Min Value:",min(M))
    print("Range:",int(max(M))-int(min(M)))
    print("\n")
    
