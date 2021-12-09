def main():
    sys.setrecursionlimit(5000)

    #print two title lines by hand
    Sorts = [BubbleSort,ShakerSor,...QuickSort, ModQuicksort]
    for s in range(3,13):
        size = 2 **  s
        #print s as a formatted integer, supressing the return
        for sort in Sorts:
            A = CreateRandomList(size)
            Compares = [0]
            sort(A, Compares)
            #print the log of compares,formatted, supressing the return
        print()
