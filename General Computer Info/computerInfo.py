import os
import platform
import psutil
import numpy as np


# CPU Core Count
def cpuCoreCount():
    print(f"Core Count: {os.cpu_count()}")

# Processor/CPU Type  
def processorType():
    print(f"Processor: {platform.processor()}")

# OS Name
def OS():
    print(f"OS: {platform.system()}")
    
# Computer Architecture
def computerArchitecture():
    print(f"Architecture: {platform.architecture()}")
   
# Physcial CPU Cores 
def phyicalCoresCPU():
    print(psutil.cpu_count(True))

# Logical CPU Cores 
def logicalCoresCPU():
    print(psutil.cpu_count(False))

# Overall CPU Usage
def CPUsage():
    print(f"CPU Usage: {psutil.cpu_percent()}%")
 
# Overall RAM Usage   
def RAMUsage():
    ram = np.round(psutil.virtual_memory().used/1000000000, 1)
    totalRAM = np.round(psutil.virtual_memory().total/1000000000, 2)
    print(f"RAM Usage: {ram} GB / {totalRAM} GB")
    
cpuCoreCount()
processorType()
OS()
computerArchitecture()
phyicalCoresCPU()
logicalCoresCPU()
CPUsage()
RAMUsage()