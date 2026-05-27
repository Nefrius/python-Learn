from contextlib import contextmanager
import os
import time
import psutil
from rich.console import Console
import GPUtil


console = Console()
print = console.print

gpus = GPUtil.getGPUs()

class SystemInformation:
    def __init__(self):
        self.cpu = psutil.cpu_percent(interval=1)
        self.ram = psutil.virtual_memory().percent
        self.disk = psutil.disk_usage('/').percent
        
        if gpus:
            gpu = gpus[0]
            self.gpu_load = gpu.load * 100
            self.gpu_memory_used = gpu.memoryUsed
            self.gpu_memory_total = gpu.memoryTotal
            self.gpu_memory_percent = gpu.memoryUtil * 100
        else:
            self.gpu_load = 0
            self.gpu_memory_percent = 0

@contextmanager
def display_system_info():
    console.print("[bold green]Gathering System Information...[/bold green]")
    start_time = time.time()
    
    try:
        yield
    finally:
        console.print(f"[bold green]CPU Usage :[/bold green] {system_info.cpu:.1f}%")
        console.print(f"[bold green]RAM Usage :[/bold green] {system_info.ram:.1f}%")
        console.print(f"[bold green]Disk Usage:[/bold green] {system_info.disk:.1f}%")
        console.print(f"[bold green]GPU Load  :[/bold green] {system_info.gpu_load:.1f}%")
        console.print(f"[bold green]GPU Memory:[/bold green] {system_info.gpu_memory_percent:.1f}%")
        
        elapsed = time.time() - start_time
        console.print(f"[bold green]Completed in {elapsed:.2f} seconds[/bold green]")
        
with display_system_info():
    system_info = SystemInformation()
    console.print("[bold green]System Information gathered successfully![/bold green]")
