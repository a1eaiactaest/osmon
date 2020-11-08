#!/usr/bin/env python3
import argparse
import sys

def test():
    x = 1+1
    print(x)

parser = argparse.ArgumentParser(description='test')
parser.add_argument('-t', action='store_true')
res = parser.parse_args()

print(res.t)


if res.t:
    test()
        
