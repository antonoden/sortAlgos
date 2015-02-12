__author__ = 'Anton'


class Mergesort(object):

    def __init__(self):
        self.a = []

    def string(self):
        print("Initialize mergesort class.")
        print("Use function sort(array, start, end) to sort.")
        print("Sort will return the a sorted array")

    # Method for swapping two elements in the class array.
    # Takes teh index of the elements to swap
    def swap(self, A, B):

        self.a[A], self.a[B] = self.a[B], self.a[A]

    # A method who checks if the arguments is correct.
    # return: True if
    def wrong_arguments(self, arr, start, end):

        if(type(arr) is not list
        or type(start) is not int
        or type(end) is not int):
            return True

        return False

    # The sort function works as an interface between caller
    # and mergesort function.
    # return: Sorted array or None if wrong arguments.
    def sort(self, arr, start, end):

        if(self.wrong_arguments(arr, start, end) == True):
            return None
        self.a = arr
        self.mergesort(start, end)
        return self.a

## Needs work
    def mergesort(self, start, end):

        i = 0
        k = 2

        while True:
            while True:
                if(self.a[i] > self.a[i+1]):
                    self.swap(i, i+1)
                i=i+k



class Shellsort(object):

    def __init__(self):
        self.a = []

    def string(self):
        print("Initialize shellsort class.")
        print("Use function sort(array, start, end) to sort.")
        print("Sort will return the a sorted array")

    # Method for swapping two elements in the class array.
    # Takes teh index of the elements to swap
    def swap(self, A, B):

        self.a[A], self.a[B] = self.a[B], self.a[A]

    # A method who checks if the arguments is correct.
    # return: True if
    def wrong_arguments(self, arr, start, end):

        if(type(arr) is not list
        or type(start) is not int
        or type(end) is not int):
            return True

        return False

    # The sort function works as an interface between caller
    # and shellsort function.
    # return: Sorted array or None if wrong arguments.
    def sort(self, arr, start, end):

        if(self.wrong_arguments(arr, start, end) == True):
            return None
        self.a = arr
        self.shellsort(start, end)
        return self.a

    def shellsort(self, start, end):

        k = (end+1) // 2

        while True:
            i = start
            j = k
            while True:
                if(self.a[i] > self.a[k]):
                    self.swap(i, k)
                    if(i-1 >= 0):
                        i, j = i-1, j-1
                else:
                    i, j = i+1, j+1
                    if(j >= end):
                        break;
            k = k // 2
            if(k <= 1):
                break


# The Bubblesort class. Used to bubblesort an array.
# Search for bubblesort on google/youtube
class Bubblesort(object):

    def __init__(self):
        self.a = []


    def string(self):
        return "Initialize bubblesort class.\n" \
                "Use function sort(array, start, end) to sort.\n" \
                "Sort will return the a sorted array"

    # The sort function works as an interface between caller
    # and bubblesort function.
    # return: Sorted array or None if wrong arguments.
    def sort(self, arr, start, end):

        if(self.wrong_arguments(arr, start, end) == True):
            return None
        self.a = arr
        self.bubblesort(start, end)
        return self.a

    # The bubblesort function. Google for explanation
    def bubblesort(self, start, end):

        k = end
        while(k>start):
            i = start
            while True:
                if(self.a[i] > self.a[i+1]):
                    self.swap(i, i+1)
                i+=1
                if(i == k):
                    break;
            k-=1


    # Method for swapping two elements in the class array.
    # Takes teh index of the elements to swap
    def swap(self, A, B):

        self.a[A], self.a[B] = self.a[B], self.a[A]

    # A method who checks if the arguments is correct.
    # return: True if
    def wrong_arguments(self, arr, start, end):

        if(type(arr) is not list
        or type(start) is not int
        or type(end) is not int):
            return True

        return False


# The Quicksort class. Used to quicksort an array.
# Search for quicksort on google/youtube
class Quicksort(object):

    # init function the quicksort. Takes nothing as argument.
    def __init__(self):
        self.a = []

    def string(self):
        print("Initialize quicksort class.")
        print("Use function sort(array, start, end) to sort.")
        print("Sort will return the a sorted array")

    # The sort function works as an interface between
    # caller and quicksort function
    # return: Sorted array or None if wrong arguments.
    def sort(self, arr, start, end):

        if(self.wrong_arguments(arr, start, end) == True):
            return None
        self.a = arr
        self.quicksort(start, end)
        return self.a

    # A method who checks if the arguments is correct.
    # return: True if
    def wrong_arguments(self, arr, start, end):

        if(type(arr) is not list
        or type(start) is not int
        or type(end) is not int):
            return True

        return False

    # A recursive quicksort which takes use of a partition function
    def quicksort(self, start, end):

        if(start < end):

            k = self.partition(start, end)
            self.quicksort(start, k-1)
            self.quicksort(k+1, end)

    # This partition function which is standard in quicksort, choose
    # a pivot at the start of the argument array
    def partition(self, start, end):

        pivot = self.a[start]
        i = start
        j = end+1

        while True:
            i, j = i+1, j-1
            while(self.a[i] <= pivot and i < end):
                i+=1
            while(self.a[j] > pivot):
                j-=1
            if(i < j):
                self.swap(i, j)
            else:
                break

        self.swap(start, j)
        return j

    # Method for swapping two elements in the class array.
    # Takes teh index of the elements to swap
    def swap(self, A, B):

        self.a[A], self.a[B] = self.a[B], self.a[A]

# The Quicksort class. Used to quicksort an array.
# Search for quicksort on google/youtube
class Quicksort2(object):

    # init function the quicksort. Takes nothing as argument.
    def __init__(self):
        self.a = []

    def string(self):
        print("Initialize quicksort class.")
        print("Use function sort(array, start, end) to sort.")
        print("Sort will return the a sorted array")

    # The sort function works as an interface between
    # caller and quicksort function
    # return: Sorted array or None if wrong arguments.
    def sort(self, arr, start, end):

        if(self.wrong_arguments(arr, start, end) == True):
            return None
        self.a = arr
        self.quicksort(end+1)
        return self.a

    # A method who checks if the arguments is correct.
    # return: True if
    def wrong_arguments(self, arr, start, end):

        if(type(arr) is not list
        or type(start) is not int
        or type(end) is not int):
            return True

        return False

    # A recursive quicksort which takes use of a partition function
    def quicksort(self, size):

        MAX_LEVELS = 300
        beg = [MAX_LEVELS]
        end = [MAX_LEVELS]
        i=0
        while (i >= 0):
            L = beg[i]
            R = end[i]-1
            if ( L < R):
                piv = self.a[L]
                while ( L < R):
                    while ( self.a[R] >= piv and L < R ):
                        R = R - 1
                        if ( L < R ):
                            self.a[L] = self.a[R]
                            L = L + 1
                    while ( self.a[L] <= piv and L < R ):
                        L = L + 1
                        if ( L < R ):
                            self.a[R] = self.a[L]
                            R = R + 1
                    self.a[L] = piv
                    beg[i+1] = L + 1
                    end[i+1] = end[i]
                    end[i] = L
                    i = i + 1
                    if ( end[i]-beg[i] > end[i-1]-beg[i-1]):
                        self.swap(beg[i], beg[i-1])
                        self.swap(end[i], end[i-1])
            else:
                i = i - 1




    # Method for swapping two elements in the class array.
    # Takes teh index of the elements to swap
    def swap(self, A, B):

        self.a[A], self.a[B] = self.a[B], self.a[A]