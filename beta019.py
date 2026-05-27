from dataclasses import dataclass, field
from datetime import datetime
import logging
from pathlib import Path

folder = Path(__file__).parent
log_folder = folder / "systemLog"
log_file = log_folder / "system_info.log"

log_folder.mkdir(parents=True, exist_ok=True)

if not log_file.exists():
    log_file.touch()

if log_folder.exists() and log_file.exists():
     logging.info("Log folder and file are ready.")

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers = [logging.FileHandler(log_file), logging.StreamHandler()]
)


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
        logging.info(f"System information initialized at {self.last_updated}")

try:
    system_info = SystemInformation(cpu=25.5, ram=60.2, disk=80.1)
    system_info.update_log.append(f"Initial values set at {system_info.last_updated}")
    logging.info(f"System information created: CPU={system_info.cpu}%, RAM={system_info.ram}%, Disk={system_info.disk}%")
    
    print(f"CPU: {system_info.cpu}%, RAM: {system_info.ram}%, Disk: {system_info.disk}%")
    print(f"Last Updated: {system_info.last_updated}")
except Exception as e:
    logging.error(f"An error occurred: {e}")