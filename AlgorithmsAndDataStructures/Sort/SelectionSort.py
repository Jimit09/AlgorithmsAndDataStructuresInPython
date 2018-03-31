class SelectionSort(object):
    """description of class"""
    def Sort(listToSort):
        for i in range(len(listToSort)):
            minIndex = SelectionSort.FindMinIndex(listToSort, i)
            SelectionSort.Swap(listToSort, i, minIndex)

    def Swap(listToSort, index1, index2):
        temp = listToSort[index1]
        listToSort[index2] = listToSort[index1]
        listToSort[index1] = temp

    def FindMinIndex(listToSort, startIndex):
        resultIndex = startIndex
        for i in range(startIndex, len(listToSort), 1):
            if listToSort[i] < listToSort[resultIndex]:
                resultIndex = i
        return resultIndex
