__author__ = 'Anton'

import sys
import time
from listclass import List
from sort import Quicksort
from sort import Bubblesort
from sort import Shellsort
from sort import Quicksort2

def create_list(low, high, size):

    L = List(size)
    L.fill_list(low, high)
    return L

# Timestamps sorting of the array.
# Needs to have an argument sort class
# return: time
def testSort(sort, arr, size):

    start = time.time()
    b = sort.sort(arr, 0, size-1)
    end = time.time()
    return end-start

def program(_n, _size):

    n = _n     # Number of tests to be made on every sort.
    low = 0     # Lowest number possible in the randomized lists
    high = 100  # Highest number possible in the randomized lists
    size = _size  # Size of the lists

    qTime = 0
    q2Time = 0
    bTime = 0
    sTime = 0

    c = 0
    # Quicksort recursive
    while(c < n):
        L = create_list(low, high, size)
        a = Quicksort()
        qTime += testSort(a, L._list, L._size)
        c+=1
    c = 0
    # Quicksort iterative
    while(c < n):
        L = create_list(low, high, size)
        a = Quicksort2()
        q2Time += testSort(a, L._list, L._size)
        c+=1
    c = 0
    #Bubblesort
    while(c < n):
        L = create_list(low, high, size)
        a = Bubblesort()
        bTime += testSort(a, L._list, L._size)
        c+=1
    c = 0
    # Shellsort
    while(c < n):
        L = create_list(low, high, size)
        a = Shellsort()
        sTime += testSort(a, L._list, L._size)
        c+=1

    print("Quicksort\trank[",podium(qTime, q2Time, bTime, sTime),"]\ttime[",qTime,"]")
    print("Quicksort2\trank[",podium(q2Time, qTime, bTime, sTime),"]\ttime[",q2Time,"]")
    print("Bubblesort\trank[",podium(bTime, qTime, sTime, q2Time),"]\ttime[",bTime,"]")
    print("Shellsort\trank[",podium(sTime, bTime, qTime, q2Time),"]\ttime[",sTime,"]")

## If a want to take a high rank on the podium the score should be low
## In choosing the variable names I thought that "me" is the one you want
## to know the rank of. "opp1", "opp2" etc, is your opponents.
## return: rank or None if something wrong.
def podium(me, opp1, opp2, opp3):

    size = 4
    pod = [me, opp1, opp2, opp3]

    # Sort the array
    k = size - 1
    i = 0
    r = 0 # rank
    while ( i < k ):
        if( pod[i] > pod[i+1]):
            r = r + 1
        i = i + 1

    return r

def printWinner(q, b, s):

    if(q < b and q < s):
        print("WINNER: QUICKSORT")
    if(b < q and b < s):
        print("WINNER: BUBBLESORT")
    if(s < q and s < b):
        print("WINNER: SHELLSORT")


def main():

    print("Tests[100]   Size[305]")
    program(100, 305)
    print("")
    print("Tests[100]   Size[200]")
    program(100, 200)
    print("")
    print("Tests[100]   Size[100]")
    program(100, 100)
    print("")
    print("Tests[100]   Size[50]")
    program(100, 50)
    print("")
    print("Tests[100]   Size[10]")
    program(100, 10)

    ## Next sort is Mergesort. Progressing in sort file.
    return

if __name__ == "__main__":
    sys.exit(main())