from dataclasses import dataclass, field
from datetime import datetime

last_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@dataclass
class SystemInformation:
    cpu: float
    ram: float
    disk: float
    last_updated: str = None
    update_log: list = field(default_factory=list)
    
    def __post_init__(self):
        self.last_updated = last_time

system_info = SystemInformation(cpu=25.5, ram=60.2, disk=80.1)
system_info.update_log.append(f"Initial values set at {system_info.last_updated}")

print(f"CPU: {system_info.cpu}%, RAM: {system_info.ram}%, Disk: {system_info.disk}%")
print(f"Last Updated: {system_info.last_updated}")