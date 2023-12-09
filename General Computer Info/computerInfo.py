import os
import platform


# CPU Core Count
def cpuCoreCount():
    print("Core Count: "+os.cpu_count())

# Processor/CPU Type  
def processorType():
    print("Processor: "+platform.processor())

# OS Name
def OS():
    print("OS: "+platform.system())
    
# Computer Architecture
def computerArchitecture():
    print("Architecture: "+platform.architecture())
    
cpuCoreCount()
processorType()
OS()
computerArchitecture()