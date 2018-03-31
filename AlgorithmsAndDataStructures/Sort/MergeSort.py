class MergeSort(object):
    """description of class"""
    def SortArray(arrayToSort):
        tempArray = arrayToSort[:]
        MergeSort.Sort(arrayToSort, tempArray, 0, len(arrayToSort) - 1)

    def Sort(arrayToSort, tempArray, startIndex, endIndex):
        if startIndex >= endIndex :
            return
        middle = (startIndex + endIndex) // 2
        MergeSort.Sort(arrayToSort, tempArray, startIndex, middle)
        MergeSort.Sort(arrayToSort, tempArray, middle + 1, endIndex)
        MergeSort.MergeHalve(arrayToSort,tempArray, startIndex, endIndex)

    def MergeHalve(arrayToSort, tempArray, startIndex, endIndex):
        leftStart = startIndex
        leftEnd = (startIndex + endIndex) // 2
        rightStart = leftEnd + 1
        rightEnd = endIndex
        index = startIndex
        while leftStart <= leftEnd and rightStart <= rightEnd:
            if arrayToSort[leftStart] < arrayToSort[rightStart]:
                tempArray[index] = arrayToSort[leftStart]
                leftStart = leftStart + 1
            else:
                tempArray[index] = arrayToSort[rightStart]
                rightStart = rightStart + 1
            index = index + 1
        
        while leftStart <= leftEnd:
            tempArray[index] = arrayToSort[leftStart]
            leftStart = leftStart + 1
            index = index + 1

        while rightStart <= rightEnd:
            tempArray[index] = arrayToSort[rightStart]
            rightStart = rightStart + 1
            index = index + 1