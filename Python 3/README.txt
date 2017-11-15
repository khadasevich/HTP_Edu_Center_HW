Create an autocomplete function that will take in an input string and a dictionary array and return the values from the dictionary that start with the input string. If there are more than 5 matches, restrict your output to the first 5 results. If there are no matches, return an empty array. Any input that is NOT a letter should be treated as if it is not there. For example, an input of "$%^" should be treated as "" and an input of "ab*&1cd" should be treated as "abcd".
Example:

autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane', 'airport']
For this assignment, the dictionary will always be a valid array of strings. Please return all results in the order given in the dictionary, even if they're not always alphabetical. The search should NOT be case sensitive, but the case of the word should be preserved when it's returned. For example, "Apple" and "airport" would both return for an input of 'a'. However, they should return as "Apple" and "airport" in their original cases.

 

Send the response as a reply to this message, preserving the Subject.

 

 

P.S.

Below are solutions from the most recent assignment, mind looking into standard types methods, use dir() and help().

 

keyset = dict.fromkeys(string)

d = {x: string.count(x) for x in keyset}

 

letter_count = {letter: text.count(letter) for letter in text}
