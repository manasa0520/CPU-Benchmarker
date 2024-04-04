import psutil

#CPU Calculator And Monitoring
print()
print("\t\t\t\t\t\t\tCPU Monitor Started and Recording")
print()

while True:
    cpu = psutil.cpu_percent(interval=1)
    print(cpu)
    if cpu > 90:
        print("Reached the Limit")
        break
