# Commandline arguments of python 

 I tested the tutorial of argparse module in python.
 
 So I arrange the test code in here for later. 
 
 In short, This code is Basic commandline argument code, So When I need it, I can looking for it fast.

 Basic Setting, as follows : 
 
```python
# for sys.argv
import sys

# To make usage associated with dealing with arguments of command-line
import argparse

def sys_test() :
    print ("the len of sys.argv :", len(sys.argv))
    print ("sys.argv[0] :", sys.argv[0])
    print ("sys.argv: ", sys.argv)

def argparse_test_the_basic() :
    parser = argparse.ArgumentParser()
    parser.parse_args()

def argparse_test_introducing_positional_arguments () :
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print (args.echo)

if __name__ == "__main__" :
    sys_test()
    argparse_test_the_basic()
    argparse_test_introducing_positional_arguments_useful ()
```
 
  The above things is three type of the very basic form About commandline argument
 
 # Reference
 
  - [the usage of argparse moduel](https://docs.python.org/2/howto/argparse.html#argparse-tutorial)
