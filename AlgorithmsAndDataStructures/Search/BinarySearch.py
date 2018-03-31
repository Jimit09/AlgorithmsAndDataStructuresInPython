class BinarySearch:

    def doBinarySearch(itemToSearch, myList):
        found = False
        bottom = 0
        top = len(myList) - 1
        while bottom <= top and not found:
            midpoint = (bottom + top) // 2
            if myList[midpoint] == itemToSearch:
                found = True
            elif  myList[midpoint] < itemToSearch:
                bottom = midpoint + 1
            elif myList[midpoint] > itemToSearch:
                top = midpoint - 1
        return found


