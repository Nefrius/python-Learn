from contextlib import contextmanager
import os
import time
import psutil
import rich as rich
from rich.console import Console

print = Console().print

class SystemInformation():
    def __init__(self, cpu=None, ram=None, disk=None):
        self.cpu = cpu if cpu is not None else psutil.cpu_percent(interval=1)
        self.ram = ram if ram is not None else psutil.virtual_memory().percent
        self.disk = disk if disk is not None else psutil.disk_usage('/').percent

class CpuInfo(SystemInformation):
    def __init__(self, cpu=None):
        super().__init__(cpu=cpu)

class RamInfo(SystemInformation):
    def __init__(self, ram=None):
        super().__init__(ram=ram)
        
class DiskInfo(SystemInformation):
    def __init__(self, disk=None):
        super().__init__(disk=disk)


@contextmanager
def display_system_info():
    print("[bold green]Gathering System Information...[/bold green]")
    start_time = time.time()
    try:
        yield
            
    finally:
        print(f"[bold green]CPU Usage:[/bold green] {cpu_info.cpu}%")
        print(f"[bold green]RAM Usage:[/bold green] {ram_info.ram}%")
        print(f"[bold green]Disk Usage:[/bold green] {disk_info.disk}%")
    
    elapsed = time.time() - start_time
    print(f"[bold green]System Information gathered in {elapsed:.2f} seconds[/bold green]")

with display_system_info():
    system_info = SystemInformation()
    cpu_info = CpuInfo()
    ram_info = RamInfo()
    disk_info = DiskInfo()


display_system_info()