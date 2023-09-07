import unittest
from randomfactory import *

class TestRandomFactory(unittest.TestCase):
    def test_generate_integer(self):
        test_int = generate_integer(1, 10)
        self.assertTrue(test_int >= 1 and test_int <= 10)
        self.assertIsInstance(test_int, int)

    def test_generate_alphabet(self):
        test_char = generate_alphabet()
        self.assertTrue(test_char >= 'A' and test_char <= 'z')
        self.assertIsInstance(test_char, str)

    def test_generate_alphabet_2(self):
        test_char = generate_alphabet("Z", "d")
        self.assertTrue(test_char >= 'Z' and test_char <= 'd')
        self.assertIsInstance(test_char, str)

    def test_generate_string(self):
        test_str = generate_string(10)
        self.assertEqual(len(test_str), 10)
        self.assertIsInstance(test_str, str)

    def test_generate_string_2(self):
        char_list = ["A", "B", "c"]
        test_str = generate_string(10, char_list)
        self.assertEqual(len(test_str), 10)
        self.assertTrue(all((cha in char_list) for cha in test_str))

    def test_generate_word(self):
        test_word = generate_word(10)
        self.assertEqual(len(test_word), 10)
        self.assertIsInstance(test_word, str)
        self.assertTrue(all((cha >= 'A' and cha <= 'z') for cha in test_word))

    def test_generate_array(self):
        test_arr = generate_array(10, 1, 10)
        self.assertEqual(len(test_arr), 10)
        self.assertIsInstance(test_arr, list)
        self.assertTrue(all((num >= 1 and num <= 10) for num in test_arr))

    def test_generate_2d_array(self):
        test_arr = generate_2d_array(10, 9, 1, 10)
        self.assertEqual(len(test_arr), 10)
        self.assertEqual(len(test_arr[0]), 9)
        self.assertIsInstance(test_arr, list)
        self.assertIsInstance(test_arr[0], list)
        self.assertTrue(all((num >= 1 and num <= 10) for num in test_arr[0]))

    def test_generate_unique_array(self):
        test_arr = generate_unique_array(10, 1, 100)
        self.assertEqual(len(test_arr), 10)
        self.assertIsInstance(test_arr, list)
        self.assertTrue(all((num >= 1 and num <= 100) for num in test_arr))
        self.assertTrue(len(test_arr) == len(set(test_arr)))

    def test_generate_subseq(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_arr = generate_subseq(arr, 3)
        self.assertEqual(len(test_arr), 3)
        self.assertIsInstance(test_arr, list)

        for i in range(1, len(test_arr)):
            self.assertTrue(
                arr.index(test_arr[i]) > arr.index(test_arr[i - 1])
            )
        

if __name__ == '__main__':
    unittest.main()