class QuickSort(object):
    """description of class"""
    def SortArray(arrayToSort):    
        QuickSort.Sort(arrayToSort, 0, len(arrayToSort) - 1)
    
    def Sort(arrayToSort, startIndex, endIndex):
        if startIndex >= endIndex :
            return
        pivot = arrayToSort[(startIndex + endIndex) // 2]
        paritionIndex = QuickSort.Parition(arrayToSort, startIndex, endIndex, pivot)
        QuickSort.Sort(arrayToSort , startIndex, paritionIndex - 1)
        QuickSort.Sort(arrayToSort, paritionIndex, endIndex)

    def Parition(arrayToSort, startIndex, endIndex, pivot):
        while startIndex <= endIndex:
            while arrayToSort[startIndex] < pivot :
                startIndex+=1
            while arrayToSort[endIndex] > pivot :
                endIndex-=1
            if startIndex <= endIndex:
                QuickSort.Swap(arrayToSort, startIndex, endIndex)
                startIndex+=1
                endIndex-=1
        return startIndex

    def Swap(arrayToSort, index1, index2):
        temp = arrayToSort[index1]
        arrayToSort[index1] = arrayToSort[index2]
        arrayToSort[index2] = temp