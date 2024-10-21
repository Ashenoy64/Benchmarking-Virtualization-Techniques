#!/bin/python3
import psutil
import sys
import time
pid=int(sys.argv[1])
file=sys.argv[2]
p=psutil.Process(pid)

start = time.time()

with open (file, "w") as f:
	f.write("time,cpu_percent,virtual_memory_percent,rss(MB),vms(MB),shared(MB),text(MB),lib(MB),data(MB), dirty(MB)"+"\n")
	while p.is_running():
		
		f.write(str(time.time()-start)+","+str(p.cpu_percent(interval=0.1))+","+str(p.memory_percent())+","+",".join(map(lambda a:(str(a/1024**2)), p.memory_info()))+"\n")
		f.flush()

