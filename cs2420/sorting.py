import random
def get_random_numbers():
    randomlist = []
    for i in range(0,random.randint(5,10)):
        n = random.randint(1,30)
        randomlist.append(n)
    return randomlist

def bubble_sort(randomlist):

    for i in range(0, len(randomlist)-1):
        for j in range(0,len(randomlist)-i-1):
            if randomlist[j+1] < randomlist[j]:
                temp = randomlist[j+1]
                randomlist[j] = temp
    return randomlist

def selection_sort(randomlist):
    for i in range(0,len(randomlist)-1):
        smallest = i
        for j in range(i,len(randomlist)):
            if randomlist[j] < randomlist[smallest]:
                smallest = j
                temp = randomlist[smallest]
                randomlist[smallest] = randomlist[i]
                randomlist[i] = temp
    return randomlist

def shaker_sort(randomlist):
    n = len(randomlist)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range(start,end):
            if (randomlist[i] > randomlist[i+1]):
                randomlist[i], randomlist[i+1] = randomlist[i+1], randomlist[i]
                swapped = True
            if (swapped == False):
                break
            swapped = False
            end = end-1
            for i in range(end-1, start-1, -1):
                if (randomlist[i] > randomlist[i +1]):
                    randomlist[i], a[i + 1] = randomlist[i + 1], randomlist[i]
                    swapped = True
                    start = start + 1
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

    
         




def main():
    print("How many times would you like to test?")
    number = int(input( ))
    for i in range(0,number):
        randomlist = get_random_numbers()
        bubble_sort_list = bubble_sort(randomlist)
        selection_sort_list = selection_sort(randomlist)
        shaker_sort_list = shaker_sort(randomlist)
        print("Random Numbers List:" , randomlist)
        print("Bubble Sort Result:", randomlist)
        print("Selection Sort Result:", randomlist)
        print("Shaker Sort Result:", randomlist)
        randomlist.sort()
        print("Random List VS Bubble Sort Result:", randomlist == bubble_sort_list)
        print("Random List Vs Selection Sort Result:", randomlist == selection_sort_list)
        print("Random List Vs Shaker Sort Result:", randomlist == shaker_sort_list)

main()
