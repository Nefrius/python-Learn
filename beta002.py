import os
import time
from rich.console import Console
import sys
console = Console()

class SysBot: 
    def __init__(self, bot_name):
        self.bot_name = bot_name
        console.print(f"[bold green]{self.bot_name} initialized successfully![/bold green]")

    def os_check(self):
        os.system("cls" if os.name == "nt" else "clear")

        if os.name == "nt":
            console.print("[bold green]Windows detected[/bold green]")
            os_name = "Windows"
        else:
            console.print("[bold green]Unix/Linux detected[/bold green]")
            os_name = "Unix/Linux"

        os_info = [
            f"Operating System: {os_name}",
            f"Platform: {sys.platform}",
            f"Python Version: {sys.version}",
        ]

        console.print("\n[bold cyan]OS INFORMATION:[/bold cyan]")

        for info in os_info:
            console.print(f"[green]{info}[/green]")
            
    def clear_screen(self):
            os.system("cls" if os.name == "nt" else "clear")

console.print("[bold yellow]Welcome to SysBot![/bold yellow]")
bot_NAME = input("Enter Your Bot Name: ")
bot = SysBot(bot_NAME)
bot.os_check()
time.sleep(3)
bot.clear_screen()
sys.exit()