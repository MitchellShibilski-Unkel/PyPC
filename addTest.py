import random


# Getting numbers
fNum = random.randint(0, 9)
sNum = random.randint(0, 9)
    
# Add num
finalValue = int(fNum + sNum)
    
# Timer
time = 0
for i in range(1000000):
    if finalValue.bit_length():
        pass
