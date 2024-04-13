import os
import platform
import psutil
import numpy as np
import cpuinfo


# CPU Core Count
def cpuCoreCount():
    print(f"Core Count: {os.cpu_count()}")
    return os.cpu_count()

# Processor/CPU Type  
def processorType():
    print(f"Processor: {platform.processor()}")
    return platform.processor()

# OS Name
def OS():
    print(f"OS: {platform.system()}")
    return platform.system()
    
# Computer Architecture
def computerArchitecture():
    print(f"Architecture: {platform.architecture()}")
    return platform.architecture()
   
# Physcial CPU Cores 
def phyicalCoresCPU():
    print(psutil.cpu_count(True))
    return psutil.cpu_count(True)

# Logical CPU Cores 
def logicalCoresCPU():
    print(psutil.cpu_count(False))
    return psutil.cpu_count(False)
    
# CPU Info
def CPU():
    return cpuinfo.get_cpu_info()["brand_raw"]

# Overall CPU Usage
def CPUsage():
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    return psutil.cpu_percent()
 
# Overall RAM Usage   
def RAMUsage():
    ram = np.round(psutil.virtual_memory().used/1000000000, 1)
    totalRAM = np.round(psutil.virtual_memory().total/1000000000, 2)
    print(f"RAM Usage: {ram} GB / {totalRAM} GB")
    return ram 
    
def swapMemory():
    swap = np.round(psutil.swap_memory().used/1000000000, 1)
    print(f"Swap Memory: {swap} GB")
    return swap
    
def getCPUTemp():
    temp = np.round(psutil.sensors_temperatures()['coretemp'][0].current, 1)
    return temp

def runALl():  
    cpuCoreCount()
    processorType()
    OS()
    computerArchitecture()
    phyicalCoresCPU()
    logicalCoresCPU()
    CPUsage()
    RAMUsage()
    swapMemory()
    getCPUTemp()