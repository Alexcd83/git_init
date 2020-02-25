# Metrics CPU and MEM

Script which prints basic information about your OS to console

## Getting Started

1) Install Python3 on the your Linux 
```
https://docs.python-guide.org/starting/install3/linux/
```
2) Install PSUtil
```
https://psutil.readthedocs.io/en/latest/
```
3) Copy 2 files in your Linux
```
metrics_cpu.py and metrics_mem.py
```

### Running scripts CPU

Open Linux CLI input full path to this files
For exampl:

```
home/localadmin/metrics_cpu/metrics_cpu.py
```
In result you can see 

```
CPU Metrics:
system.cpu.idle - 24310.59
system.cpu.user - 291.41
system.cpu.guest - 0.0
system.cpu.iowait - 82.57
system.cpu.steal - 0.0
system.cpu.system - 126.63

```
### Running scripts MEM

Open Linux CLI input full path to this files
For exampl:

```
home/localadmin/metrics_mem/metrics_mem.py
```
In result you can see 

```
Memory Metrics:
virtual total - 8339873792
virtual used - 642076672
virtual free - 6939963392
virtual shared - 757760
swap total - 0
swap used - 0
swap free - 0
```
