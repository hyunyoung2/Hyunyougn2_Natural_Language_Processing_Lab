# n gram of syllable

 This program is couting n gram of syllable in a file line by line.
 
# Usage 
 
 Let's see how to use it. If you want to use it, type in like this :
 
 > $ python3 the_name_of_program -h
 
```shell
# hyunyoung2 @ hyunyoung2-desktop in ~/git-hub/Natural_Language_Processing_Lab/Python/N_Gram_Count/Syllable on git:master o [20:53:42] 
$ python3 count_n_gram_ver_0.0.py -h
usage: count_n_gram_ver_0.0.py [-h] [-t | -f FILE [FILE ...]] [-o OUTPUT]
                               [-n {1,2,3,4,5}]

this program count N gram in syllable unit in a file.

optional arguments:
  -h, --help            show this help message and exit
  -t, --test            implement test code
  -f FILE [FILE ...], --file FILE [FILE ...]
                        your file name with path
  -o OUTPUT, --output OUTPUT
                        your file name of output wit path
  -n {1,2,3,4,5}, --ngram {1,2,3,4,5}
                        N gram you want to make
```
 
# Develop Environment

 - My environment is , when I developed this, like this :

    - OS : Linux 4.8.0-58-generic #63~16.04.1-Ubuntu 
 
    - python : 3.5
 
    - IDE : spyder3
 
# Way to work 

 let's see how for This to work 
 
 i.e. If you have a file like this :
 
```
hellow world!
I'm fine 
```
 
 This program seperates it depending on n gram of you choic like this :
 
```python
# First, This reads the file line by line 
["hellow world\n", "I'm fine\n"]

# Second, This get rid of "\n", new line and space like " ", "\t"
["hellowworld", "I'mfine"]

# Third, This seperates it into n gram of syllable you chose
# in here, let's say 2 gram
["he", "el", "ll", "lo", "ow", "ww", "wo", "or", "rl", "ld", "I'", "'m", "mf", "fi", "in", "ne"]

# Fourth, This count the 2 gram to check how many times this file have each of 2 gram.
[("he", 1), ("el", 1), ("ll", 1), ("lo", 1), ("ow", 1), ("ww", 1), ("wo", 1), ("or", 1), ("rl", 1), ("ld", 1), ("I'", ),  ("'m", 1), ("mf", 1), ("fi", 1), ("in", 1), ("ne", 1)]

# Finally, This makes a file to store the result counted 2 gram line by line as cvs file. 
# file name -> output.csv, The file is like this :
he\t1
el\t1
.......
```
