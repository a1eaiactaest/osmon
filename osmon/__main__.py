#!/usr/bin/env python3
import argparse
import psutil


parser = argparse.ArgumentParser(description='Get some stats.')
parser.add_argument('--cpu','-c', action='store_true')
parser.add_argument('--gpu','-g', action='store_true')
parser.add_argument('--ram','-r', action='store_true')
parser.add_argument('--all','-a', action='store_true')
args = parser.parse_args() 

def cpu():
    pass

def ram():
    pass

def gpu():
    pass

def run_all()
    pass

def main():
    if args.cpu or args.c:
        cpu()
    elif args.gpu or args.g:
        gpu()
    elif args.ram or args.r:
        ram()
    elif args.all or args.a:
        run_all()



if __name__ == '__main__':
    main()
