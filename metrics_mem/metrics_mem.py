#!/usr/bin/env python3

import psutil
m=psutil.virtual_memory()
print("Memory Metrics:")
print("virtual total - %r" % m.total)
print("virtual used - %r" % m.used)
print("virtual free - %r" % m.free)
print("virtual shared - %r" % m.shared)

w=psutil.swap_memory()
print("swap total - %r" % w.total)
print("swap used - %r" % w.used)
print("swap free - %r" % w.free)
