#! /usr/bin/env python

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ArgParse - demo program for argument parsing',
        description='Demo program for argument parsing',
        epilog='Run "argparse -h" for help')

    parser.add_argument('-u', '--username', required=True)
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-r', '--rollno', required=True)
    parser.add_argument('-p', '--place', required=True)
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    
    if args.verbose:
        print ("Username: ", args.username)
        print ("Name: ", args.name)
        print ("Roll No.: ", args.rollno)
        print ("Place: ", args.place)
