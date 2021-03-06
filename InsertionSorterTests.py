import unittest
import random
from InsertionSorter import InsertionSorter


class ArrayGenerationTests(unittest.TestCase):
    NUMBER_OF_NUMBERS = 10

    def setUp(self):
        self.randomNumbers = [0] * self.NUMBER_OF_NUMBERS
        self.sorter = InsertionSorter()

        for index, number in enumerate(self.randomNumbers):
            self.randomNumbers[index] = random.randint(0, 100)

    @unittest.skip('Skipped generation of numbers test')
    def test_number_of_random_numbers_generated(self):
        self.assertEqual(len(self.randomNumbers), self.NUMBER_OF_NUMBERS, "Number of elements in array was not correct.")

    @unittest.skip('Skipped unsigned numbers test')
    def test_numbers_all_unsigned(self):
        for n in self.randomNumbers:
            self.assertTrue(n >= 0)

    def print(self, message):
        print(message)
        print(*self.randomNumbers, sep='\n')

    @unittest.skip('Skipped print numbers test')
    def test_print_all_numbers(self):
        self.print('Print Numbers:')
        self.assertTrue(True)

    def test_sort_numbers(self):
        # self.print("Unsorted Numbers:")
        self.sorter.sort(self.randomNumbers)
        # self.print("Sorted Numbers:")
        previousNumber = 0

        for i, n in enumerate(self.randomNumbers):
            self.assertTrue(n >= previousNumber, "Number " + str(n) + " at index " + str(i) + " is not > " + str(previousNumber))
            previousNumber = n

if __name__ == '__main__':
    unittest.main()
