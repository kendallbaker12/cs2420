import random
import sys
def get_random_numbers():
    randomlist = []
    for i in range(0,random.randint(5,10)):
        n = random.randint(1,30)
        randomlist.append(n)
    return randomlist

def bubble_sort(randomlist):
    switched=True
    while switched == True:
        switched = False
        for i in range(0,len(randomlist)-1):
            if randomlist[i] > randomlist[i+1]:
                randomlist[i],randomlist[i+1] = randomlist[i+1],randomlist[i]
                switched = True
    return randomlist

def shaker_sort(randomlist):
    switched=True
    while switched == True:
        switched = False
        for i in range(0,len(randomlist)-1):
            if randomlist[i] > randomlist[i+1]:
                randomlist[i],randomlist[i+1] = randomlist[i+1],randomlist[i]
                switched = True
        for i in reversed(range(len(randomlist)-1)):
            if randomlist[i] > randomlist[i+1]:
                randomlist[i],randomlist[i+1] = randomlist[i+1],randomlist[i]
                switched = True
    return randomlist

def countsort(randomlist):
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

def mergeSort(randomlist):
    if len(randomlist) <= 1:
        return  
        
    L = randomlist[0:len(randomlist)//2]
    R = randomlist[len(randomlist)//2:]
    mergeSort(L)
    mergeSort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            randomlist[k] = L[i]
            i += 1
            k += 1
        else:
            randomlist[k] = R[j]
            j+= 1
            k+=1
                
    while i < len(L):
        randomlist[k]=L[i]
        i+=1
        k+=1
    while j < len(R):
        randomlist[k] = R[j]
        j+=1
        k+=1
    return randomlist

def quicksort(randomlist,low,high):
    if high-low <=0:
        return 
       
    lmbt= low+1
    pivot = low
    for i in range (low+1,high+1):
        if randomlist[i] < randomlist[pivot]:
            randomlist[i],randomlist[lmbt]=randomlist[lmbt],randomlist[i]
            lmbt += 1
    pivot = lmbt-1
    randomlist[low],randomlist[pivot]=randomlist[pivot],randomlist[low]
    quicksort(randomlist,low,pivot-1)
    quicksort(randomlist,pivot+1,high)

def modquicksort(randomlist,low,high):
    if high-low <= 0:
        return
    mid = (low + high)//2
    randomlist[low],randomlist[mid] = randomlist[mid],randomlist[low]
    lmbt= low+1
    pivot = low
    for i in range (low+1,high+1):
        if randomlist[i] < randomlist[pivot]:
            randomlist[i],randomlist[lmbt]=randomlist[lmbt],randomlist[i]
            lmbt += 1
    pivot = lmbt-1
    randomlist[low],randomlist[pivot]=randomlist[pivot],randomlist[low]
    modquicksort(randomlist,low,pivot-1)
    modquicksort(randomlist,pivot+1,high)

def main():  
    print("How many times would you like to test?")
    number = int(input( ))
    for i in range(0,number):
        randomlist = get_random_numbers()
        bubble_sort_list = randomlist.copy()
        bubble_sort_list = bubble_sort(bubble_sort_list)
        shaker_sort_list= randomlist.copy()
        shaker_sort_list = shaker_sort(shaker_sort_list)
        count_sort_list = randomlist.copy()
        count_sort_list = countsort(count_sort_list)
        merge_sort_list = randomlist.copy()
        merge_sort_list = mergeSort(merge_sort_list)
        quick_sort_list = randomlist.copy()
        quicksort(quick_sort_list,0,len(randomlist)-1)
        mod_quick_sort_list = randomlist.copy()
        modquicksort(mod_quick_sort_list,0,len(randomlist)-1)
        print("Random Numbers List:" , randomlist)
        print("Bubble Sort Result:", bubble_sort_list)
        print("Shaker Sort Result:", shaker_sort_list)
        print("Count Sort Result:", count_sort_list)
        print("Merge Sort Result:",merge_sort_list)
        print("Quick Sort Result:", quick_sort_list)
        print("Modified Quick Sort Result:",mod_quick_sort_list)
        randomlist.sort()
        print("Random List VS Bubble Sort Result:", randomlist == bubble_sort_list)
        print("Random List Vs Shaker Sort Result:", randomlist == shaker_sort_list)
        print("Random List Vs Count sort Result:", randomlist == count_sort_list)
        print("Random List Vs Merge Sort Result:", randomlist == merge_sort_list)
        print("Random List Vs Quick sort Result:", randomlist == quick_sort_list)
        print("Random List Vs Mod Quick Sort Result:", randomlist == mod_quick_sort_list)
main()