import unittest
import random
from InsertionSorter import InsertionSorter


class ArrayGenerationTests(unittest.TestCase):
    NUMBER_OF_NUMBERS = 5

    def setUp(self):
        self.randomNumbers = [0] * self.NUMBER_OF_NUMBERS
        self.sorter = InsertionSorter()

        for index, number in enumerate(self.randomNumbers):
            self.randomNumbers[index] = random.randint(0, 100)

    def test_number_of_random_numbers_generated(self):
        self.assertEqual(len(self.randomNumbers), self.NUMBER_OF_NUMBERS, "Number of elements in array was not correct.")

    def test_numbers_all_unsigned(self):
        for n in self.randomNumbers:
            self.assertTrue(n >= 0)

    def print(self, message):
        print(message)
        print(*self.randomNumbers, sep='\n')

    def test_print_all_numbers(self):
        self.print("Numbers:")
        self.assertTrue(True)

    def test_sort_first_two_elements(self):
        self.randomNumbers[0] = 69
        self.randomNumbers[1] = 68

        self.print("Unsorted Numbers:")
        self.sorter.sort(self.randomNumbers)
        self.print("Sorted Numbers:")

        self.assertTrue(self.randomNumbers[1] >= self.randomNumbers[0])

    def test_sort_numbers(self):
        self.print("Unsorted Numbers:")
        self.sorter.sort(self.randomNumbers)
        self.print("Sorted Numbers:")
        previousNumber = 0

        for i, n in enumerate(self.randomNumbers):
            self.assertTrue(n >= previousNumber, "Number " + str(n) + " at index " + str(i) + " is not > " + str(previousNumber))
            previousNumber = n

if __name__ == '__main__':
    unittest.main()
