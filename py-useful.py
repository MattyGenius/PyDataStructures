import sys
import os
import string
import random
import math
import numpy as np
import datetime
import calendar
import struct
import platform
import site
import subprocess
import multiprocessing
import cProfile
import socket
import time
import traceback
import glob
import json

print(True.real)
print(False.real)

# print(sys.argv)
# print(sys.version) 
# print(sys.byteorder) # Big/little endian
# print(sys.maxsize)
# print(sys.getrecursionlimit())
# print(os.name)
# print(os.environ)
# print(platform.system())
# print(platform.release())
# print(site.getsitepackages())
# print(multiprocessing.cpu_count())

# To determine if a Python shell is executing in 32-bit mode or 64-bit mode on OS.
# The reason this works is because a struct is custom sized to the mode. I.e. 4 bits in 32-bit mode and 8 bits in 64-bit mode.
print(struct.calcsize("P") * 8)

# Use subprocess for all system commands.
print(subprocess.Popen("ls", shell=True).wait())
# subprocess.Popen("clear", shell=True).wait()
print(glob.glob('*.py'))

# print(abs.__doc__)

# Genuinely a good function to learn. MAP.
x, y = map(int, input("Input the value of x & y: ").split())
print("The value of x & y are: ", x, y)

# print(datetime.datetime.now())
# print(calendar.month(2024, 10))

stringls = input("string: ")
# this logic works
if len(stringls) > 1 and stringls[:2] == 'Is':
    print(stringls)
else:
    print("Is" + stringls)

# Running times and call times
def multiply(a, b):
    return a*b
cProfile.run('multiply(54,123)')

# How you actually time something.
def sum_of_n_numers(n):
    start_time = time.time()

    s = 0
    for i in range(1, n+1):
        s = s + i
    
    end_time = time.time()
    return s, end_time - start_time

n = 5
sol, tim = sum_of_n_numers(n)
print("n = %s, solution is %s, time taken is %s" % (n, sol, tim))

# print(time.ctime())


# Size in bytes of each variable. Note how the size is the same between strings / integers that arent too far apart. Thanks to padding.
str1 = "four"
str2 = "fives"
int1 = 69
int2 = 420

print(str1 + ": " + str(sys.getsizeof(str1)))
print(str2 + ": " + str(sys.getsizeof(str1)))
print(str(int1) + ": " + str(sys.getsizeof(int1)))
print(str(int2) + ": " + str(sys.getsizeof(int2)))

x = 53
print("Identity: %s, Type: %s, Memory Address: %s" % (x, type(x), id(x)))


# open() opens a file and returns it as a file object. Default is 'r' read, also 'a' append, 'w' write, 'x' create.
# Actually a huge lesson here. I never use 'with'. I should use it more. Essentially allows for much more readable code
# as well as reusable exception handling. For example, look at the following:
# file = open('a.txt', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()

# That whole thing can be condensed into:
# with open('a.txt', 'w') as file:
#     file.write('hello world')

# Error checking isn't even necessary because 'with' handles most cases. You can of course implement your own where necessary.
# Very useful for improving the quality and cleanliness of your code.
# 
# After a bit more research. Basically any time you're working with files or threading, you probably want to use a 'with' statement.
# It's a context manager, which means that it cleans up and manages multiple files, processes or threads working at the same time.
# Besides that it won't get much use. Is essentially a better version of try: finally:, though.

# src = 'py-catchup.py'
# dest = 'py-catchup-short.py'
# with open(src, 'r') as f, open(dest, 'w') as d:
#     for line in f:
#         d.write(line)

'''
Hijacking this question to learn about the different types of String literals available through prefixes.
First we have f-strings, e.g. f'Example'. An f-string is actually just a longer version of string.format.
name = "Matty"
adjective = "Genius"
print("{} is {}".format(name, adjective))
is the same as 
print(f"{name} is {adjective}")
Other languages have these features more naturally, so f-strings are Python's version.
For clarity, this process is called string interpolation - interpolating variables into strings.

Next we have b-strings. A byte string is literally a sequence of bytes, and isn't actually human-readable.
byte_str = b'Byte string'
print(byte_str)
So how come we can print this successfully? Well, Python decodes them from UTF-8 when you print them.
That's actually exactly what the 'print' function does - it converts byte information from memory to UTF-8 characters
for human readability.

Then we have r-strings. An r-string is a raw string. A good way to think about it is that an f-string
is essentially a string with batteries included, i.e. extra features. Whereas an r-string is a string with all
extra features removed, completely minimalist. An r-string ignores escape characters. So the use case for it
might be a function that feeds a string with escape characters into another function to eventually print it.

Finally we have u-strings. U-strings are unicode literals. Python3 strings are unicode by default so you
probably don't need to worry about these unless you venture into Python2 for work. U-strings allow you to use
non-ASCII characters (i.e. UTF-8) such as emojis, accented characters, etc.
'''
