import time


startTimer = time.perf_counter()
startTimer2 = time.process_time()

userData = float(int(input("Enter value:\n")))
userData2 = float(int(input("Enter secound value:\n")))

addValues = float(int(userData + userData2))

print(addValues)

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}")