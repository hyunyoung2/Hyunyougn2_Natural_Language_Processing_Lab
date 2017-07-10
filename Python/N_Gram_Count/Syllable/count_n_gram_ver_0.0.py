# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:02:34 2017

@author: hyunyoung2
"""

# -- The current version of python :  3.5

# count_n_gram version : 0.0

# for regular expression
import re

# for the location of the current directory you're working with python
import os

# for command line arguments
import argparse

# @ function : Read a File line by line
# input : A file like, "hellow spm\n I'm fine\n" in a file
# output : A list consisting of lines, i.e. a factor of lists is line of a file.
#         like this, ["hellow spm\n", "I'm fine\n"]
#--- this function has '\n', new line character. ---
def readAFileLinebyLine(a_file_path) :
    f = open(a_file_path, "r")
    whole_lines = f.readlines()
    f.close()
    return whole_lines 
    
# @ function : write pairs of tuple like ("letter of n gram", conunt of the letter)
#              if it is 2 gram, ("he", 1) and so on
# input : file path to write with pairs of seqeunce data of tuple. 
# output : True, later on, I will fix it
def writeAFlieWithData(a_file_path, pairs_of_sequence_data) :
    default_file_name = "/output_of_counting_n_gram.csv"
    flag = False
    
    if a_file_path == None :
        flag = True
        # To get the location of the current dicrectory 
        # from https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory       
        cwd = os.getcwd()
        a_file_path = cwd + default_file_name
   
    f = open(a_file_path,"w")
           
    # the type of var is tuple    
    for idx, var in enumerate(pairs_of_sequence_data) :
        if type(var) is not tuple :
            print ("your data is unstable")
            return None
        data = "\t".join(var)
        data += "\n"
        f.write(data)
        
    f.close()
    
    if flag == True :
        print ("\nThe location of your output is under", cwd+"/")
        print ("If you don't name output, the file name is", default_file_name)
    
    print ("So, the final location is", a_file_path)
    return True
    
# @ function :  remove sapce like " ", "\t".
# input : A string like "hellow, I'm fine\n"
# output : A string like "helow,I'mfine\n"
def removeWhiteSpace(a_temp_string) :
    white_space = "[ \t]" #  " ", "\t"
    
    a_temp_string = re.sub(white_space,"", a_temp_string)
    
    return a_temp_string
 
# @ function : remove space and new line like ' ', '\t' and '\n' 
# input : A string including ' ' , '\t' and '\n'
# output : A new string without ' ', '\t' and '\n'
def removeNewLineNwhiteSpace(a_string) :
    white_space = "[ \t]" #  " ", "\t"
    # To remove '\n' line by line
    new_string = a_string[0:-1] 
    
    new_string = re.sub(white_space,"", new_string)
    
    return new_string
    
# @ function : make the total index set of the features apart from duplication. 
# input : A list of sentences and what you want to make like uni_gram, bi_gram and so on
#        for example ["hellow spm\n", "I'm fine\n"] or ["hellow spm", "I'm fine"]
#        like whatever doesn't matter whether including "\n" or not
# output : A fearture set or list in n_gram_of_syllable unit, for ["hellow spm\n", "I'm fine\n"]
#         if n_gram_of_syllable is 1 {h, e, l, o, w, ' ', s, p, m, '\n', 'I', "'", 'f', 'i', 'n'} 
def makeIndexSetOfFeaturesWithAListOfSentences(list_of_sentences, n_gram_of_syllable, set_or_list) :
    if set_or_list == 'set' :
        syllable_of_features = set ()
    elif set_or_list == 'list' :
        syllable_of_features = list ()
    
    for idx, var in enumerate(list_of_sentences) :
        temp_str = removeNewLineNwhiteSpace(var)
        temp_len = len(temp_str)
        for i in range(0, temp_len) : # len function include '\n'
            if i+n_gram_of_syllable <= temp_len : 
                if type(syllable_of_features) is list :
                    syllable_of_features.append(temp_str[i:i+n_gram_of_syllable])        
                elif type(syllable_of_features) is set :    
                    syllable_of_features.add(temp_str[i:i+n_gram_of_syllable])        
                else :
                    print ("you're now making wrong type of n gram")
           
    return syllable_of_features   
    
# @ function : coll function to the above makeIndexSetOfFeaturesWithAListOfSentences function 
# input : A list of sentences including "\n" and n_gram you want to make
# output : A set of n_garm of syllable without duplication
def makeSetIndexOfNGramOfSentences(list_of_sentences, n_gram) :
    
    return makeIndexSetOfFeaturesWithAListOfSentences(list_of_sentences, n_gram, 'set')
    
# @ function : call function to the above makeIndexSetOfFeaturesWithAListOfSentences function   
# input : A list of sentences including "\n" and n_gram
# ouput : A list of n_gram of syllable
def makeListOfNGramOfSentences(list_of_sentences, n_gram) :
    
    return makeIndexSetOfFeaturesWithAListOfSentences(list_of_sentences, n_gram, 'list') 
    
# @ function : prepare to count n gram of syllable  
# input : A Set after call to makeSetIndexOfNGramOfSentences 
# output : A Dinctionary except for duplication from the same n gram 
def makeIndexDictionary(a_set_of_list) :
    dict_index = {}
    
    temp_list = list(a_set_of_list)
    for idx, var in enumerate(temp_list) :
        if dict_index.get(var) == None :
            dict_index[var] = 0
        else :
            print ("you set has a problem that it has duplication in the set")
            
    return dict_index

# @ fucntion : count word with the above dictionary and a list of n gram in sentences.
# input : A dictionary after call the above function, makeIndexDictionary
#        and a list that seperates setences into n gram line by line
#        i.e the list, a_list_of_ngram is list after function, makeListOfNGramOfSentences
# output : A dictionary since counting of n gram is complete
def countingWords(a_dict_of_index, a_list_of_ngram) :
    
    for idx, var in enumerate(a_list_of_ngram) :
        if a_dict_of_index.get(var) != None :
            a_dict_of_index[var] += 1
        else :
            print ("you counting has a problem")
            
    return a_dict_of_index
    
# @ function : prepare to write the pair("str", count) into a file
# input : the last dict after countingWords functions.
# output : A new list having pairs of tuple. for example,
#           [("he", 1), ("el", 3), ("ll", 2), ("lo", 7), ("ow", 2)]
def makePairsOfTupleFromDict(final_dict) :
    new_sequence_of_list = list ()
    
    for key, val in final_dict.items() :
        new_sequence_of_list.append((key,str(val)))
        
    return new_sequence_of_list
    
def test(n_gram_from_commandLine) :
    test_file_path = []    
    
    test = list ()
    
    if test_file_path == None :
        print ("set up path of yourtest file in variable, test_file_path")
        print ("till doing that, test is doesn't work")
        return 
    
    print ("\nthis code is implemented with three lines in a file stored internlly")    
    
    if n_gram_from_commandLine == 2 : 
        print ("\nfrom now no, by deault, n gram is 2")
        print ("this test is executed with 2 gram")
    
    for idx, var in enumerate(test_file_path) :
        test.extend(readAFileLinebyLine(var))
        
    print ()
    print(test[0])
    test_dic = makeSetIndexOfNGramOfSentences(test[0:3], n_gram_from_commandLine)
    
    print ("the type of test_dict :", type(test_dic), "count :", len(list(test_dic)))
    print (test_dic)
    
    index_dict = makeIndexDictionary(test_dic)
        
    test_list = makeListOfNGramOfSentences(test[0:3], n_gram_from_commandLine)
   
    print ("\nthe type of test_list :", type(test_list), "count :", len(test_list))
    print (test_list)
    
    test_dict_of_counting = countingWords(index_dict, test_list)
   
    print ("\ncounting is done")
    print (test_dict_of_counting)
    
    temp_test = makePairsOfTupleFromDict(test_dict_of_counting)
    
    print ("\nchange of dict to list including tuple and len of the pairs of tuple :", len (temp_test))
    print (temp_test)
    
    temp_test.sort()
    
    print ("\nAfter sorting...", len(temp_test))
    print (temp_test)
    
    if writeAFlieWithData(None, temp_test) == None :
        print ("error happened during writing your data into a file")
    else :
        print ("The total process is completely done\n")


def main (a_list_file_path, n_gram, output_path) :
    a_list_of_sentences = list()    
    
    for idx, var in enumerate(a_list_file_path) :
        print ("reading", var)
        a_list_of_sentences.extend(readAFileLinebyLine(var))
    
    print ("\n--- the one of a list of sentences ---")    
    print (a_list_of_sentences[0:2])
    
    print ("\nmaking dictionary......")
    dict_of_index = makeSetIndexOfNGramOfSentences(a_list_of_sentences, n_gram)   
    
    print ("\nIn order to check index")
    print ("the type of index set :", type(dict_of_index), "the number of index set :", len(list(dict_of_index)))
    
    index_dict = makeIndexDictionary(dict_of_index)
    
    print ("the type of index_dict :", type(index_dict), "the number of index dict :", len(list(index_dict)))
   
    
    print ("\nmaking list of n gram line by line")
    
    a_list_of_n_gram_line_by_line =  makeListOfNGramOfSentences(a_list_of_sentences, n_gram)  
    
    print ("\nthe type of a list of n gram line by line :", type(a_list_of_n_gram_line_by_line), "the number of a list of n gram line by line :", len(a_list_of_n_gram_line_by_line))
    print (a_list_of_n_gram_line_by_line[0:10]) 
    
    print ("\ncounting....")
    dict_of_counting =  countingWords(index_dict, a_list_of_n_gram_line_by_line)
    print ("counting is complete")
    
    print ("\nchang the type from dict to a list of pairs of tuple")
    temp_tuple = makePairsOfTupleFromDict(dict_of_counting)
    print ("the type of a list incluing pairs of tuple :", type(temp_tuple), "the number of a list including pairs of tuple :", len(temp_tuple))
    print (temp_tuple[0:10])
    
    print ("\nsorting...")
    temp_tuple.sort()
    
    print ("sorting is done")
    print ("the number of a list including pairs of tuple :", len(temp_tuple))
    print (temp_tuple[0:10])
    
    if output_path != None :
        after_writing = writeAFlieWithData(output_path, temp_tuple)
    else :
        after_writing = writeAFlieWithData(None, temp_tuple)
        
    if after_writing == None :
        print ("error happened during writing your data into a file")
    else :
        print ("The total process is completely done\n")    

if __name__ == "__main__" :
    #test(2)
    parser = argparse.ArgumentParser(description="this program count N gram in syllable unit in a file.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--test", action="store_true", help="implement test code")
    group.add_argument("-f", "--file", nargs="+", help="your file name with path")
    parser.add_argument("-o", "--output", help="your file name of output wit path")
    parser.add_argument("-n", "--ngram", type=int, choices=[1,2,3,4,5], help="N gram you want to make")
    args = parser.parse_args()
    
    if args.test : 
        if args.ngram : 
            test(args.ngram)
        else : 
            test(2)
    elif args.file :
        if args.ngram and args.output: 
            main(args.file, args.ngram, args.output)
        elif args.ngram : 
            main(args.file, args.ngram)
        else : 
            print ("enter n gram you want to make again")
    else :
        print ("you're missing some options, So look at how to use this tool one more time......")
