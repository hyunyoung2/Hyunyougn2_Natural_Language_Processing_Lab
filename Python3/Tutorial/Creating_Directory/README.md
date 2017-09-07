# HOW TO : Check Whether The Directory already Exist or not

 This tutorial is just checking how to create some directory and checking whether those exist or not
 
 Also, later on This code helps me Make some code fast
 
 Basic flow of the code , as follows :
 
 
```python

# In order to Create Directory to store material
import os 

# Get current Directory from "https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory"
current_dir = os.getcwd()

...
    if not os.path.isdir(new_dir) :
        print ("Currently, (%s) doesn't exist" % new_dir)

....
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
```
 
# Reference 

  [1. StackOverflow](https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory)
  
  [2. StackOverflow](https://stackoverflow.com/questions/1274405/how-to-create-new-folder)
 
