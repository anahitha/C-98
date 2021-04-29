def swap():
    file1 = input("Enter file name: ")
    file2 = input("Enter another file name: ")
    f = open(file1, 'r')
    data1 = f.read()
    fi = open(file2, 'r')
    data2 = fi.read()
    f = open(file1, 'w')
    f.write(data2)
    fi = open(file2, 'w')
    fi.write(data1)

swap()