# Variables for first part of task
python_zen = """Beautiful is better than ugly.
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
my_email = 'khadasevich.aleksey@gmail.com'

# Different ways to concatenate strings. Option 1:
print python_zen, my_email

# Option 2:
python_zen = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those! %s"""
my_email = 'khadasevich.aleksey@gmail.com'
print (python_zen % my_email)

# Option 3:
python_zen = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those! {0}"""
my_email = 'khadasevich.aleksey@gmail.com'
print (python_zen.format(my_email))

# Option 3:
zen_email_string = python_zen + my_email
# Next string prints length of concatenated string
print (len(zen_email_string))
# Length of zen string:
print (len(python_zen))


# Counter of vowels in the string. Option 1


def vowels(arg, vowelchars='aeiou', counter=0):
    for element in range(0, len(arg)):
        if arg[element].lower() in vowelchars:
            counter += 1
    print (counter)


# Counting of vowels in the string. Option 2 (Let's count quantity of every vowel):
vowel_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def vowels2(arg):
    for element in arg:
        if element.lower() in vowel_dict:
            vowel_dict[element.lower()] += 1
    print (vowel_dict)


# Next step of home task. Function returns each 18th symbol of the string with position and changes case of char


def case_changer(arg):
    for element in range(17, len(arg), 18):
        if arg[element].isalpha() and arg[element].isupper():
            print element + 1, arg[element].lower()
        elif arg[element].isalpha() and arg[element].islower():
            print element + 1, arg[element].upper()
        else:
            print element + 1, arg[element]


vowels2(python_zen)
case_changer(python_zen)
