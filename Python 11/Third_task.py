#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Autocomplete function"""


def autocomplete(pattern, dictionary, limit=5):
    """Calls functions and returns results"""
    newpattern = input_check(pattern)
    search_res = search_dict(newpattern, dictionary, limit)
    return search_res


def input_check(pattern):
    """ Removes non alphabetical chars from input and changes case of pattern """
    pattern = filter(str.isalpha, pattern)
    return pattern.lower()


def search_dict(pattern, dictionary, limit):
    """ Creates resulting array """
    array_res = []
    for element in dictionary:
        if dictionary[element].lower().startswith(pattern) and len(array_res) < limit:
            array_res.append(dictionary[element])
    return array_res


if __name__ == '__main__':
    print (autocomplete('C1o#',
                        {1: 'cold', 2: 'ColdWorld', 3: 'call', 4: 'cockTail', 5: 'escort', 6: 'co-existence',
                         7: 'correspond',
                         8: 'core'}))
