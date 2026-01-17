import psutil

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the cpu threshold (%):"))
    current_cpu_usage = psutil.cpu_percent(interval=1)
    print("current cpu threshold: " ,current_cpu_usage)
    
    if current_cpu_usage > cpu_threshold:
        print("cpu alert email sent...")
    else:
        print("cpu in safe state")

check_cpu_threshold()

def check_memory_threshold():
    memory_threshold = int(input("Enter Memory usage threshold (%): "))
    current_memory_usage = psutil.virtual_memory().percent
    print("current memory threshold: " ,current_memory_usage)

    if current_memory_usage > memory_threshold:
        print("memory alert email sent...")
    else:
        print("memory in safe state")
check_memory_threshold()

def check_disk_threshold():
    disk_threshold = int(input("Enter Disk usage threshold (%): "))
    current_disk_usage = psutil.disk_usage("/").percent
    print("current disk threshold: " ,current_disk_usage)

    if current_disk_usage > disk_threshold:
        print("disk alert email sent...")
    else:
        print("disk in safe state")
check_disk_threshold()
