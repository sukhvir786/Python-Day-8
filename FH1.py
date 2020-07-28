"""
File Handling

File : It's a collection of records
Record : Group of Related Data Items
Data Items : Information related to students, employees etc.

File Operations:
Creation, Opening, Reading, Writing, Closing

1 : Writing some text in file
2 : Write Numbers in the file
"""
def FH1():
    F1 = open("File1.txt","w")
    F1.write("Hello Everyone\n")
    F1.write("Let us learn File Handling in Python")
    F1.close()
FH1()

