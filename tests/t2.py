import psutil

percpu = psutil.cpu_percent(interval=None, percpu=True)

for i in range(len(percpu)):
    print(i+1,"-" ,percpu[i])
