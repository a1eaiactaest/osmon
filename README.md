# osmon

Are You tired of having to one of these speedtest websites every time you want to check you internet connection?
We've got solution designed specially for You!
<br>
Introducing... osmon!
<br>
Minimal weight and easy in use system monitor.

### Installation

```bash

pip3 install osmon

```
### Examples

If You get stuck:

```bash

$ osmon -h
usage: osmon [-h] [--cpu] [--gpu] [--ram] [--down] [--up] [--ping] [--net] [--all]

Get some stats.

optional arguments:
  -h, --help  show this help message and exit
  --cpu, -c   Check CPU parameters
  --gpu, -g   Check GPU parameters
  --ram, -r   Check RAM paramters
  --down, -d  Check download speed
  --up, -u    Check upload speed
  --ping, -p  Check download speed
  --net, -n   Check all network parameters
  --all, -a   Check all possible parameters

```

To get output off all possible measurements run:


```bash

$ osmon -a

CPU usage: 2.1%
Usage by Threads: 12
1  -  [3.3%]
2  -  [2.5%]
3  -  [3.3%]
4  -  [1.7%]
5  -  [1.6%]
6  -  [0.0%]
7  -  [0.0%]
8  -  [1.6%]
9  -  [2.5%]
10  -  [0.0%]
11  -  [3.3%]
12  -  [4.1%]
VRAM:
1  -  [592]MB Used
GPU Usage: 
 [1]
RAM usage: 27.2%
Available: 72.8%
Retrieving speedtest.net configuration...
Testing from Skynet sp. z o.o. ($IP)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by Orange Polska S.A. (Warsaw) [14.84 km]: 3.898 ms
Testing download speed................................................................................
Download: 495.75 Mbit/s
Testing upload speed......................................................................................................
Upload: 60.53 Mbit/s


```

### Why?
To gather Your data.
And but mostly to learn new things and have fun.

