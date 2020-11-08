#!/usr/bin/env python3
import argparse
import sys
parser = argparse.ArgumentParser(description='test')
parser.add_argument('-t', action='store_true')
res = parser.parse_args()



def test():
    x = 1+1
    print(x)


print(res.t)


if res.t:
    test()
        
