#!/usr/bin/env python3
import subprocess
import os

p1 = subprocess.Popen(["/usr/local/bin/processing-java", "--sketch=/home/pi/pi_cube/main --run"])
os.chdir("/home/pi/pi_cube/sol")
p2 = subprocess.Popen(["python3", "sol.py"])
    
try:
    p1.wait()
    p2.wait()
except KeyboardInterrupt:
    try:
       p1.terminate()
       p2.terminate()
    except OSError:
       pass
    p1.wait()
    p2.wait()
