import os
import time
from rich.console import Console
import sys
console = Console()

class SysBot:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        console.print(f"[bold green]{self.bot_name} initialized successfully![/bold green]")
    
    def list_Packages(self):
        
        global package_List
        package_List = ["os", "time", "sys", "rich"]
        console.print("[bold cyan]Available Packages:[/bold cyan]")
        for package in package_List:
            console.print(f"[green]{package}[/green]")
    
    def get_Package(self, object_NAME):
        get_packageNAME = input(f"Enter the package name for {object_NAME}: ")
        
        if get_packageNAME in ["os", "time", "sys", "rich"]:
            console.print(f"[bold green]{get_packageNAME} package found for {object_NAME}![/bold green]")
            try:
                global package_List
                package_List.append(get_packageNAME)
            except:
                console.print(f"[bold red]Failed to add {get_packageNAME} to package list[/bold red]")
        else:
            console.print(f"[bold red]{get_packageNAME} package not found for {object_NAME}![/bold red]")
            
            
            

console.print("[bold yellow]Welcome to SysBot![/bold yellow]")
bot_NAME = input("Enter Your Bot Name: ")
bot = SysBot(bot_NAME)
bot.list_Packages()
bot.get_Package("your project")
time.sleep(3)
