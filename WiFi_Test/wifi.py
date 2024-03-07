import speedtest
import numpy as np


def speedTest():
    speed = speedtest.Speedtest()
    
    download = speed.download()
    upload = speed.upload()
    
    return np.average([download, upload])