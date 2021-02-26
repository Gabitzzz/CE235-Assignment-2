import sys
import os


def reader():
    global txtLinesIn
    fin = open("sfs.py", "r")
    # txtLinesIn is an array
    txtLinesIn = fin.readlines()
    print("File was read")
    fin.close()

def writer():
    fout = open("sfs.py", "w")
    count = 0
    for txtLine in txtLinesIn:
        if count == 51:
            txtLine = txtLine.replace('\n', ';print("Virus") \n')
        fout.write(txtLine)
        count = count + 1
    fout.close()
    print("File was written")


if __name__ == '__main__':
    reader()
    writer()
