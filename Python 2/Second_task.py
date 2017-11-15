zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Countihg of letters in the string:
zen = zen.replace('\n', ' ')
char_counters = {i.lower(): 0 for i in set(zen)}
for char in zen:
    if char.lower() in char_counters:
        char_counters[char.lower()] += 1
print char_counters

# Sorting elements by alphabet:
print sorted(char_counters.items(), key=lambda t: t[0])

# Sorting elements by quantity:
print sorted(char_counters.items(), reverse=True, key=lambda t: t[1])

# Reverted list of items sorted by quantity:
print sorted(char_counters.items(), key=lambda t: t[1])


# Optional task with some kind of interface:
def checking_data(dictarg, var, var_sec):
    # Checks whether suitable variables were input.
    options = ('1', '2', '3')
    if (var.isdigit() and var in options) and var_sec.isdigit():
        sorting_factory(dictarg, var, var_sec)
    elif (var.isdigit() and var in options) and var_sec.lower() == 'all':
        var_sec = len(dictarg)
        sorting_factory(dictarg, var, var_sec)
    else:
        print 'Something went wrong. Please, check your input.'


def sorting_factory(dictarg, var, var_sec):
    # Select of option for sorting.
    if var == '1':
        sorted_items = sorted(dictarg.items(), key=lambda t: t[0])
    elif var == '2':
        sorted_items = sorted(dictarg.items(), key=lambda t: t[1], reverse=True)
    else:
        sorted_items = sorted(dictarg.items(), key=lambda t: t[1])
    alphabet_sort(sorted_items, var_sec)


def alphabet_sort(s, var_sec):
    # Print of result.
    for idx, element in enumerate(s):
        print ('Char: {}, Quantity: {}.'.format(*element))
        if idx == abs(int(var_sec)):
            break


option = raw_input("""Input '1' if you want to sort list by alphabet.
Press '2' if you want to sort list by the frequency.
Press '3' if you want to revert the list sorted by the frequency.""")
option_two = raw_input("""Please input how many raws you want to return from the table.
Input 'all' if you want to return all results. 
""")

checking_data(char_counters, option, option_two)
