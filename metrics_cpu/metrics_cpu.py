import psutil
p=psutil.cpu_times()
print("CPU Metrics:")
print("system.cpu.idle - %s" % p.idle)
print("system.cpu.user - %s" % p.user)
print("system.cpu.guest - %s" % p.guest)
print("system.cpu.iowait - %s" % p.iowait)
print("system.cpu.steal - %s" % p.steal)
print("system.cpu.system - %s" % p.system)

