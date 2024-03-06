import random
import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

def waveFunc(loopNum):
    for loop in range(loopNum):
        # Get the mass, Planck's Constant, and etc...
        mass = random.randint(1, 500)
        v = random.randint(1, 500)
        x = random.randint(1, 500)
        t = random.randint(1, 360)
        i = int(0 + (-1 * 0.5))

        h = float(6.63)

        # Kentic and Potential engeries
        KE = float((-h ** 2 / 2 * mass) * v ** 2)
        PE = int(v * (x + t))

        # Add KE + PE
        step1 = float(KE + PE)

        step2 = float((i * h) * (2 / 2 * t))

        # Get the final value
        print(f"SE: {step1 - step2}\n")