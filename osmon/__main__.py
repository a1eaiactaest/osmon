#!/usr/bin/env python3
import argparse
import psutil
import time

parser = argparse.ArgumentParser(description='Get some stats.')
parser.add_argument('--cpu','-c', action='store_true')
parser.add_argument('--gpu','-g', action='store_true')
parser.add_argument('--ram','-r', action='store_true')
parser.add_argument('--all','-a', action='store_true')
args = parser.parse_args() 

def cpu():
    print('Checking CPU usage...')
    time.sleep(1)
    print(f'CPU usage: {psutil.cpu_percent(interval=None)}')
    print(f'CPU usage per CPU, printing from {psutil.cpu_count()} CPUs: {psutil.cpu_percent(interval=None,percpu=True)}',end='\n')

def ram():
    print('Checking RAM usage...')
    time.sleep(1)
    print(f'RAM usage: {psutil.virtual_memory().percent}')
    free = round(psutil.virtual_memory().available*100/psutil.virtual_memory().total ,1)
    print(f'Available: {free}')

def gpu():
    pass

def run_all():
    pass

def main():
    if args.cpu:
        cpu()
    elif args.gpu:
        gpu()
    elif args.ram:
        ram()
    elif args.all:
        run_all()



if __name__ == '__main__':
    main()
