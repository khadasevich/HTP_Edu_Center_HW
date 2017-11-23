#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creation of unittest for autocomplete function"""

import unittest
import Third_task


class TestAutocompleteFunction(unittest.TestCase):
    """Unittest class for autocomplete function testing"""

    def setUp(self):
        """Setting up input data for test case"""
        self.pattern = 'C1o#'
        self.input_data = {1: 'cold', 2: 'ColdWorld', 3: 'call', 4: 'cockTail', 5: 'escort', 6: 'co-existence',
                           7: 'correspond',
                           8: 'core'}
        self.limit = 6
        self.case_sensitive_check = 'ColdWorld'
        self.checking_array = (Third_task.autocomplete(self.pattern, self.input_data, self.limit))
        self.stereotype = ['cold', 'ColdWorld', 'cockTail', 'co-existence', 'correspond', 'core']
        self.wrong_word = 'escort'

    def test_autocomplete(self):
        """Testing ability of imported module to autocomplete inputted dictionary
        and don't record not suitable items"""
        for element in self.stereotype:
            self.assertIn(element, self.checking_array, "Function didn't complete all words")
        self.assertNotIn(self.wrong_word, self.checking_array)

    def test_check_len_limit(self):
        """Checks whether function uses limitation"""
        length = len(self.checking_array)
        self.assertEqual(length, self.limit, "Limitation doesn't work")

    def test_check_case_sensitive(self):
        """Checks whether all cases appears in the result array"""
        self.assertIn(self.case_sensitive_check, self.checking_array)

    def tearDown(self):
        """Cleaning environment"""
        pass


if __name__ == '__main__':
    unittest.main()
