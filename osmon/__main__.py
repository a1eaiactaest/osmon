#!/usr/bin/env python3
import argparse
import psutil
import time

parser = argparse.ArgumentParser(description='Get some stats.')
parser.add_argument('--cpu','-c', action='store_true')
#parser.add_argument('--gpu','-g', action='store_true')
parser.add_argument('--ram','-r', action='store_true')
parser.add_argument('--net','-n', aciton='store_true')
parser.add_argument('--all','-a', action='store_true')
args = parser.parse_args() 

def loading(str,y):
    if y == None:
        y = 20
    else:
        y = y
    for i in range(0,y):
        b = f'{str}'+'.'*i
        print(b,end='\r')
        time.sleep(0.1)
    sys.stdout.write("\033[K")

def cpu():
    loading('Checking CPU Usage', 10)
    print(f'CPU usage: {psutil.cpu_percent(interval=None)}%')
    percpu = psutil.cpu_percent(interval=None, percpu=True)
    print(f'Thread by Thread: {psutil.cpu_count()}')
    for i in range(len(percpu)):
        print(i+1, ' - ', f'[{percpu[i]}%]')


def ram():
    loading('Checking RAM Usage', 10)
    print(f'RAM usage: {psutil.virtual_memory().percent}%')
    free = round(psutil.virtual_memory().available*100/psutil.virtual_memory().total ,1)
    print(f'Available: {free}%')


import speedtest
st = speedtest.Speedtest()
def down():
    loading('Checking Download Speed')
    print(round(st.download()/1000000, 3))

def up():
    loading('Checking Upload Speed')
    print(round(st.upload()/1000000,3))

def ping():
    loading('Tesing Ping')
    servers=[]
    st.get_servers(servers)
    print(st.results.ping)

def net():
    down()
    up()
    ping()


def run_all():
    cpu()
    ram()
    net()

def main():
    if args.cpu:
        cpu()
#    elif args.gpu:
#        gpu()
    elif args.ram:
        ram()
    elif args.all:
        run_all()

if __name__ == '__main__':
    main()
