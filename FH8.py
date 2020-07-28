"""
Calculation of Total Marks and Percentage 
of Students as per data stored in the file
"""
F1 = open("FFF.txt","r")
N = int(F1.readline())
print("Total Number of Students:",N)
for i in range(N):
    print("Student Number :",i+1,":",end="")
    gr = (F1.readline().split())
    print(gr)
    sum = 0
    for j in range(len(gr)):
        sum = sum + int(gr[j])
        per = float((sum/500)*100)
    print("Total Marks:",sum)
    print("Percentage:",per)
    print("\n")