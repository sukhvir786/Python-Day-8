"""
Even Numbers
"""
def FH4():
    F1 = open("File4.txt","w")
    for i in range(2,31,2):
        i = str(i)
        F1.write(i+" ")
    F1.close()
FH4()