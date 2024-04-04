import time
import psutil
import platform
#Libraries imported telling stuffs like cpu information and monitoring of cpu , memory usage
print("")

print("CPU USAGE AND BENCHMARK MONITOR")

print("")

print("CPU Brand Currently Used by the Computer :\n" + platform.processor())

print()

print("CPU AND MEMORY USAGE OF THE COMPUTER")

print()
print()

#printing cpu names and other related stuffs for a neat layout in command prompt

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '|' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '|' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage:  |{cpu_bar}| {cpu_usage:.2f}% ", end="")
    print(f"MEM Usage:  |{mem_bar}| {mem_usage:.2f}%  ", end="\r")

#created a class and multiplied | bars as a loading format , and everytime the memory usage goes up the string will multiply , basically to make a interactive loading screen



while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)
