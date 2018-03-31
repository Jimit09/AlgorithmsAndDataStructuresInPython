class BubbleSort(object):
    """Sort array in Bubble Sort pattern"""
    def Sort(listToSort):
        isSorted = False
        sortOnListLength = len(listToSort) - 1
        while not isSorted:
            isSorted = True
            for element in range(sortOnListLength):
                if listToSort[element] > listToSort[element + 1]:
                    BubbleSort.Swap(element, (element + 1), listToSort)
                    isSorted = False
            sortOnListLength -= 1
        return listToSort

    def Swap(a, b, list): 
       temp = list[a]
       list[a] = list[b]
       list[b] = temp





