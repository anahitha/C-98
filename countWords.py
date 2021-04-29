def countWords(file):
    wordcount = 0
    f = open(file)
    for line in f:
        words = line.split()
        wordcount+=len(words)
        print(words)
        print(len(words))
    print("Number of words: ", wordcount)

fname = input("Enter file name: ")
countWords(fname)