Your home assignment for Class 6, Python will be as follows

by 17:00PM Monday, 10/30/17:

 

Read about the “os” module, particularly “walk” function and “path” module.

https://docs.python.org/2/library/os.html#os.walk

https://docs.python.org/2/library/os.path.html

 

Write a wrapper for the os.walk() function that returns a generator.

The generator should give me all the files (and only files, excluding directories!) with their absolute path.

Example:

 

import os

 

files_lazy_lister = your_wrapper(os.walk("c:\\"))
list(files_lazy_lister)

=>

["C:\\Development\\ARM Embedded Toolchain\\5.4 2016q3\\uninstall.exe",
"C:\\Development\\ARM Embedded Toolchain\\5.4 2016q3\\arm-none-eabi\\bin\\ar.exe",
"C:\\Development\\ARM Embedded Toolchain\\5.4 2016q3\\arm-none-eabi\\bin\\as.exe",
"C:\\Windows\\bfsvc.exe",
"C:\\Windows\\explorer.exe", ...]

 

P.S.

Below is repeating generator example from the classes:

 

def counter_generator(max_count=10):
    count = 0
    while count < max_count:
        yield count
        count += 1


def counter_repeater(generator_to_repeat):
    last = 0
    while True:
        current = next(generator_to_repeat)
        yield last, current
        last = current


counter_to_10 = counter_generator(10)
repeater_generator = counter_repeater(counter_to_10)

for _ in repeater_generator:
    print(_)
