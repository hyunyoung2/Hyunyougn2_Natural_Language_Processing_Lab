# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 15:28:41 2017

@author: hyunyoung2
"""

# -- the version of python : 3.5 --

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
    
def argparse_test_introducing_positional_arguments_useful () :
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    print (args.echo)

# this function throw error message, TypeError
# Basically, the value of the option is the type of str
def argparse_test_introducing_positional_arguments_more_useful () :
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number")
    args = parser.parse_args()
    print (args.square**2)
    
# the below is function after fixing the above error, TypeError as specify the type of input
def argparse_test_introducing_positional_arguments_more_useful_after_fixing_error () :  
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number", type=int)
    args = parser.parse_args()
    print (args.square**2)
    
def argparse_test_introducing_optional_arguments () :
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    args = parser.parse_args()
    if args.verbosity:
        print ("verbosity turned on")
    
def argparse_test_introducing_optional_arguments_more_useful () :   
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print ("verbosity turned on")

def argparse_test_introducing_optional_arguments_with_short_option () :
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print ("verbosity turned on")

def argparse_test_introducing_optional_arguments_combining_positional_n_optional_arguments () :
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print ("the square of {} equals {}".format(args.square, answer))
    else:
        print (answer)

# a bit tuning of the above code. 
def argparse_test_introducing_optional_arguments_mutiple_verbose_value () :

    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print ("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity == 1:
        print ("{}^2 == {}".format(args.square, answer))
    else:
        print (answer)

# revising the above code a bit 
def argparse_test_introducing_optional_arguments_revising_mutiple_verbose_value () :
    
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print ("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity == 1:
        print ("{}^2 == {}".format(args.square, answer))
    else:
        print (answer)

# get a different approach of the verbose from the above code with count keyword 
def argparse_test_introducing_optional_arguments_a_different_approach_of_mutiple_verbose_value () :
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display the square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print ("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity == 1:
        print ("{}^2 == {}".format(args.square, answer))
    else:
        print (answer)

# change the above code a bit about not informative 
def argparse_test_introducing_optional_arguments_a_different_approach_revised_a_bit () :
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2

    # bugfix: replace == with >=
    if args.verbosity >= 2:
        print ("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity >= 1:
        print ("{}^2 == {}".format(args.square, answer))
    else:
        print (answer)

def argparse_test_introducing_optional_arguments_a_different_approach_informative () :
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity >= 2:
        print ("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity >= 1:
        print ("{}^2 == {}".format(args.square, answer))
    else:
        print (answer)
        
def argparse_test_advanced_mode () :
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent") 
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    answer = args.x**args.y
    if args.verbosity >= 2:
        print ("{} to the power {} equals {}".format(args.x, args.y, answer))
    elif args.verbosity >= 1:
        print ("{}^{} == {}".format(args.x, args.y, answer))
    else:
        print (answer)
        
def argparse_test_advanced_mode_tuned () :

    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    answer = args.x**args.y
    if args.verbosity >= 2:
        print ("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print ("{}^{} ==".format(args.x, args.y), answer)
    else :
        print (answer)
        
# conflicting between --quiet and --verbose
# their functionality is opposite to each other
def argparse_test_advanced_mode_about_conflicting_arguments() :
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")    
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x**args.y

    if args.quiet:
        print (answer)
    elif args.verbose:
        print ("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print ("{}^{} == {}".format(args.x, args.y, answer))

def argparse_test_advanced_mode_about_main_purpose_of_your_program () :
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x**args.y

    if args.quiet:
        print (answer)
    elif args.verbose:
        print ("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print ("{}^{} == {}".format(args.x, args.y, answer))
        
if __name__ == "__main__" :
    #sys_test()
    #argparse_test_the_basic()
    #argparse_test_introducing_positional_arguments_useful ()
    #argparse_test_introducing_positional_arguments () 
    #argparse_test_introducing_positional_arguments_more_useful_after_fixing_error()
    #argparse_test_introducing_optional_arguments()
    #argparse_test_introducing_optional_arguments_more_useful ()
    #argparse_test_introducing_optional_arguments_with_short_option ()
    #argparse_test_introducing_optional_arguments_combining_positional_n_optional_arguments()
    #argparse_test_introducing_optional_arguments_mutiple_verbose_value ()
    #argparse_test_introducing_optional_arguments_revising_mutiple_verbose_value () 
    #argparse_test_introducing_optional_arguments_a_different_approach_of_mutiple_verbose_value()
    #argparse_test_introducing_optional_arguments_a_different_approach_revised_a_bit ()
    #argparse_test_introducing_optional_arguments_a_different_approach_informative ()
    #argparse_test_advanced_mode ()
    #argparse_test_advanced_mode_tuned()
    #argparse_test_advanced_mode_about_conflicting_arguments ()
    argparse_test_advanced_mode_about_main_purpose_of_your_program ()
