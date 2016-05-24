class InsertionSorter(object):

    def sort(self, numbers):

        for i, n in enumerate(numbers):
            if i < len(numbers) - 1:
                self.insert(numbers, i, numbers[i + 1])


    def insert(self, numbers, indexOfLastSortedNumber, number):

        for i in range(0, indexOfLastSortedNumber + 1):
            iComp = indexOfLastSortedNumber - i

            if iComp >= 0:
                if numbers[iComp] > number:
                    numbers[iComp + 1] = numbers[iComp]
                    numbers[iComp] = number