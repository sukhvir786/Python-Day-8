"""
How to write odd numbers 
even numbers
random numbers in the file
"""
def FH3():
    F1 = open("File3.txt","w")
    for i in range(1,31,2):
        i = str(i)
        F1.write(i+" ")
    F1.close()
FH3()