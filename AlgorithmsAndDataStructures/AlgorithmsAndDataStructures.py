
if __name__ == "__main__":
   #from BubbleSort import BubbleSort
   #from MergeSort import MergeSort
   #from QuickSort import QuickSort
   #numberList = [11, 4, 36, 8, 1, -1, 18, 0, 24, 3]
   #print('Before Sorting')
   ##print('Applying Bubble Sort on lists')
   #print('Applying Quick Sort on list')
   #print(numberList)
   ##BubbleSort.Sort(numberList)
   ##MergeSort.SortArray(numberList)
   #QuickSort.SortArray(numberList)
   #print('Sorted list')
   #print(numberList)

   from PaymentBuilder import PaymentBuilder
   payments = PaymentBuilder()
   for line in payments.liabilities():
       print(line)

    #from BinarySearch import BinarySearch;

    #numberList = [1, 4, 6, 8, 11, 13, 18, 22, 24, 30]
    #item = int(input("What number are you looking for? "))
    #isItFound = BinarySearch.doBinarySearch(item, numberList)
    #if isItFound:
    #    print("Your number is in the list!")
    #else:   
    #    print("Your number is not in the list!")