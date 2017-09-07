# If you start the python setting 
# help(os-python keyword)

# -- the version of python : 3.5 --

# In order to check the version of python 
import sys
print ("python :" , sys.version)
print () # for newline 

# In order to Create Directory to store material
import os 

name_dir = ["MNIST_Dataset", "CIFAR_10_Dataset", "CIRFAR_100_Dataset"]

# Get current Directory from "https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory"
current_dir = os.getcwd()
print ("The location of current Directory :", current_dir)
print () # for nweline

# Checking Whether all the Directory exist already
for i in range(3) :
    new_dir = current_dir+"/"+name_dir[i]
    if not os.path.isdir(new_dir) :
        print ("Currently, (%s) doesn't exist" % new_dir)
print () # for nweline

# Create new Directory from "https://stackoverflow.com/questions/1274405/how-to-create-new-folder"
for i in range(3) :
    new_dir = current_dir+"/"+name_dir[i]
    print("The location for New Directory :", new_dir)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
print () # for nweline
        
# Finally, Checking whether the directories is made or not
for i in range(3) :
    new_dir = current_dir+"/"+name_dir[i]
    if os.path.isdir(new_dir) :
        print ("Currently, (%s) exist" % new_dir)    
print () # for nweline
