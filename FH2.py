"""
How to write numbers in file
"""
def FH2():
    F1 = open("File2.txt","w")
    for i in range(1,21):
        i = str(i)
        F1.write(i+"\n")
    F1.close()
FH2()
