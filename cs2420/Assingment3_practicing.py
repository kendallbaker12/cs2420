import math
import random
import sys
class Counts:
    def __init__(self):
        self.Compares = 0
        self.Swaps = 0
        
def CreateRandomList(size):
    randomlist = []
    for i in range(size):
        r = random.randrange(0,size)
        randomlist.append(r)
    return randomlist
        
def bubble_sort(randomlist,C):
    switched=True
    while switched == True:
        switched = False
        for i in range(0,len(randomlist)-1):
            C.Compares += 1
            if randomlist[i] > randomlist[i+1]:
                C.Swaps += 1
                randomlist[i],randomlist[i+1] = randomlist[i+1],randomlist[i]
                switched = True
    return randomlist

def selection_sort(randomlist,C):
    for i in range(0,len(randomlist)-1):
        smallest = i
        smallestnum = randomlist[i]
        for j in range(i,len(randomlist)):
            C.Compares += 1
            if randomlist[j] < randomlist[smallest]:
                smallest = j
                smallestnum = randomlist[j]
        C.Swaps += 1
        randomlist[i],randomlist[smallest] = randomlist[smallest],randomlist[i]
    return randomlist

def shaker_sort(randomlist,C):
    switched=True
    while switched == True:
        switched = False
        for i in range(0,len(randomlist)-1):
            C.Compares += 1
            if randomlist[i] > randomlist[i+1]:
                C.Swaps += 1
                randomlist[i],randomlist[i+1] = randomlist[i+1],randomlist[i]
                switched = True
        for i in reversed(range(len(randomlist)-1)):
            C.Compares += 1
            if randomlist[i] > randomlist[i+1]:
                C.Swaps += 1
                randomlist[i],randomlist[i+1] = randomlist[i+1],randomlist[i]
                switched = True
    return randomlist

def mergeSort(randomlist,C):
    if len(randomlist) <= 1:
        return  
        
    L = randomlist[0:len(randomlist)//2]
    R = randomlist[len(randomlist)//2:]
    C.Swaps += len(randomlist)
    mergeSort(L,C)
    mergeSort(R,C)
    i = j = k = 0
    while i < len(L) and j < len(R):
        C.Compares += 1
        if L[i] <= R[j]:
            randomlist[k] = L[i]
            i += 1
            k += 1
        else:
            randomlist[k] = R[j]
            j+= 1
            k+=1
                
    while i < len(L):
        C.Compares += 1
        randomlist[k]=L[i]
        i+=1
        k+=1
    while j < len(R):
        C.Compares += 1
        randomlist[k] = R[j]
        j+=1
        k+=1
    C.Swaps += len(randomlist)
    return randomlist
                   
def countsort(randomlist,C):
    C.Compares = len(randomlist)
    C.Swaps = len(randomlist)
    Mmax = int(max(randomlist))
    Mmin = int(min(randomlist))
    elements = Mmax - Mmin + 1
    count_randomlist = [0 for _ in range(elements)]
    output_randomlist = [0 for _ in range(len(randomlist))]
    for i in range(0,len(randomlist)):
        count_randomlist[randomlist[i]- Mmin] += 1
    for i in range(1, len(count_randomlist)):
        count_randomlist[i] += count_randomlist[i-1]
    for i in range(len(randomlist)-1,-1,-1):
        output_randomlist[count_randomlist[randomlist[i] - Mmin] -1] = randomlist[i]
        count_randomlist[randomlist[i] - Mmin] -= 1
    for i in range(0,len(randomlist)):
        randomlist[i] = output_randomlist[i]
    return randomlist

def quicksort(randomlist,C,low,high):
    if high-low <=0:
        return 
       
    lmbt= low+1
    pivot = low
    for i in range (low+1,high+1):
        C.Compares += 1
        if randomlist[i] < randomlist[pivot]:
            C.Swaps += 1
            randomlist[i],randomlist[lmbt]=randomlist[lmbt],randomlist[i]
            lmbt += 1
    pivot = lmbt-1
    C.Swaps += 1
    randomlist[low],randomlist[pivot]=randomlist[pivot],randomlist[low]
    quicksort(randomlist,C,low,pivot-1)
    quicksort(randomlist,C,pivot+1,high)
                   
def quicksortR(randomlist,C):
    quicksort(randomlist,C,0,len(randomlist)-1)
                   
def modquicksort(randomlist,C,low,high):
    if high-low <= 0:
        return
    mid = (low + high)//2
    C.Swaps += 1
    randomlist[low],randomlist[mid] = randomlist[mid],randomlist[low]
    lmbt= low+1
    pivot = low
    for i in range (low+1,high+1):
        C.Compares += 1
        if randomlist[i] < randomlist[pivot]:
            C.Swaps += 1
            randomlist[i],randomlist[lmbt]=randomlist[lmbt],randomlist[i]
            lmbt += 1
    pivot = lmbt-1
    C.Swaps += 1
    randomlist[low],randomlist[pivot]=randomlist[pivot],randomlist[low]
    modquicksort(randomlist,C,low,pivot-1)
    modquicksort(randomlist,C,pivot+1,high)

def modquicksortR(randomlist,C):
    modquicksort(randomlist,C,0,len(randomlist)-1)
                   
def main():
    startingSize = 8
    endingSize =  1024*4
    sys.setrecursionlimit(endingSize+10)
    Algorithims = [bubble_sort,shaker_sort,quicksort,modquicksort,mergeSort,countsort]
    SortNames = ["BubbleSort","ShakerSort","QuickSort","ModQuicksort","MergeSort","CountSort"]

    print("%5s" %(" "), end="")
    for name in SortNames:
        x = name.ljust(9," ")
        print(x,end="")
    print()

    # size = startingSize
    # while size <= endingSize:
    #     print ("02d  " %(format(size)),end="")

    #     for i in range (len(Algorithims)):
    #         A = CreateRandomList(size)
    #         copy = A[:]
    #         copy.sort()

    #         Counts = [0,0]
    #         Algorithims[i](A,Counts)

    #         if A != copy:
    #             print("ERROR! failed in", SortNames[i])
    #             print (A)
    #             print (copy)
    #             sys.exit(0)

    #         print ("%05.f   "% (format(Counts[0])),end="")

    #     print()

            
    # print('{:10}'.format(''),'{:10}'.format('BubbleSort'),'{:10}'.format('ShakerSort'),'{:10}'.format('QuickSort'),'{:10}'.format('ModQuickSort'),'{:10}'.format('MergeSort'),'{:10}'.format('CountingSort'))
    # for s in range(3,13):
    #     size = 2 ** s
    #     print (s, end=" ")
    #     for i in bubble:
    #         randomlist = CreateRandomList(size)
    #         C = Counts()
    #         i(randomlist,C)
    #         print("%10.2f" %(math.log(C.Compares,2)), end=" \n ")
            
    # shaker = [shaker_sort]
    # for s in range(3,13):
    #     size = 2 ** s
    #     print (s, end=" ")
    #     for i in shaker:
    #         randomlist = CreateRandomList(size)
    #         C = Counts()
    #         i(randomlist,C)
    #         print("%10.2f" %(math.log(C.Compares,2)), end=" \n ")
    # # selection = [selection_sort]
    # # for s in range(3,13):
    # #     size = 2 ** s
    # #     print (s, end=" ")
    # #     for i in selection:
    # #         randomlist = CreateRandomList(size)
    # #         C = Counts()
    # #         i(randomlist,C)
    # #         print("%10.2f" %(math.log(C.Compares,2)), end=" \n ")
    # quick = [quicksortR] 
    # for s in range(3,13):
    #     size = 2 ** s
    #     print (s, end=" ")
    #     for i in quick:
    #         randomlist = CreateRandomList(size)
    #         C = Counts()
    #         i(randomlist,C)
    #         print("%10.2f" %(math.log(C.Compares,2)), end=" \n ")
    # mod = [modquicksortR]
    # for s in range(3,13):
    #     size = 2 ** s
    #     print (s, end=" ")
    #     for i in mod:
    #         randomlist = CreateRandomList(size)
    #         C = Counts()
    #         i(randomlist,C)
    #         print("%10.2f" %(math.log(C.Compares,2)), end=" \n ")
    # merge = [mergeSort]
    # for s in range(3,13):
    #     size = 2 ** s
    #     print (s, end=" ")
    #     for i in merge:
    #         randomlist = CreateRandomList(size)
    #         C = Counts()
    #         i(randomlist,C)
    #         print("%10.2f" %(math.log(C.Compares,2)), end=" \n ")
    # counting = [countsort]
    # for s in range(3,13):
    #     size = 2 ** s
    #     print (s, end=" ")
    #     for i in counting:
    #         randomlist = CreateRandomList(size)
    #         C = Counts()
    #         i(randomlist,C)
    #         print("%10.2f" % (math.log(C.Compares,2)), end=" \n ")

            

main()