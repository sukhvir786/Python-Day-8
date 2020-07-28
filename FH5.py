"""
Random Numbers
10 random numbers between 100 and 150
"""
from random import randint
def FH5():
    F1 = open("File5.txt","w")
    for i in range(10):
        i = randint(100,150)
        i = str(i)
        F1.write(i+" ")
    F1.close()
FH5()
        