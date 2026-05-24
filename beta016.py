import os
import platform
import psutil
import GPUtil

from rich.console import Console
from rich.tree import Tree

print = Console().print

gpus = GPUtil.getGPUs()


class OsInfo():
    def __init__(
        self,
        os_name=os.name,
        version=platform.platform(),
        architecture=platform.architecture()[0]
    ):
        self.os_name = os_name
        self.version = version
        self.architecture = architecture

    def get_os_info(self):
        tree = Tree("[green][+] [red]Operating System Information[/red]")

        if self.os_name == 'nt':
            tree.add("[bold blue]OS: Windows")

        elif self.os_name == 'posix':
            tree.add("[bold blue]OS: Unix/Linux")

        else:
            tree.add(f"[bold blue]OS: {self.os_name}")

        tree.add(f"[bold blue]Version: {self.version}")
        tree.add(f"[bold blue]Architecture: {self.architecture}")

        print(tree)


class PcInfo():
    def __init__(
        self,
        cpu=psutil.cpu_percent(interval=1),
        ram=psutil.virtual_memory().percent,
        gpu=gpus[0].name if gpus else None,
        disk=psutil.disk_usage('/').percent
    ):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.disk = disk

    def get_pc_info(self):
        tree = Tree("[green][+] [red]PC Information[/red]")

        # CPU
        if self.cpu > 80:
            tree.add(f"[bold red]CPU Usage: {self.cpu}% (High)")

        elif self.cpu > 50:
            tree.add(f"[bold yellow]CPU Usage: {self.cpu}% (Moderate)")

        else:
            tree.add(f"[bold green]CPU Usage: {self.cpu}% (Low)")

        # RAM
        if self.ram > 80:
            tree.add(f"[bold red]RAM Usage: {self.ram}% (High)")

        elif self.ram > 50:
            tree.add(f"[bold yellow]RAM Usage: {self.ram}% (Moderate)")

        else:
            tree.add(f"[bold green]RAM Usage: {self.ram}% (Low)")

        # Disk
        if self.disk > 80:
            tree.add(f"[bold red]Disk Usage: {self.disk}% (High)")

        elif self.disk > 50:
            tree.add(f"[bold yellow]Disk Usage: {self.disk}% (Moderate)")

        else:
            tree.add(f"[bold green]Disk Usage: {self.disk}% (Low)")

        # GPU
        if self.gpu:
            tree.add(f"[bold cyan]GPU: {self.gpu}")

        else:
            tree.add("[bold red]GPU: Not Detected")

        print(tree)


os_info = OsInfo()
os_info.get_os_info()

pc_info = PcInfo()
pc_info.get_pc_info()