import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_throws_error_if_no_list_passed(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([4]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


    # test functions HAVE to start w the word 'test' otherwise they won't be run

    # def test_function_returns_True(self):
    #     self.assertTrue(even_number_of_evens([]))
# pass lets you run code if you don't have anything written. python expects an indent after the colon above.


if __name__ == '__main__':
    unittest.main()
