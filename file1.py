# How to Import works In Python:----

import sklearn as sk
print(sk.__version__)


import sys
print(sys.path)

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier)


#  It is carry the value of file2.py:---

import file2
print(file2.a)
file2.printjoke("This is me") # access the file from file2.py

import sklearn as sk
print(sk.__version__)

import sys
print(sys.path)

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier)

# It is carry the value of file2.py:---

import file2
print(file2.a)
file2.printjoke("This is me") # It has been access the file from file2.py

