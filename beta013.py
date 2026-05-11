import os
import sys
import time
import rich.console
console = rich.console.Console()

class SysBot:
    def __init__(self, name, version, author, commands=None):
        self.__name = name
        self.__version = version
        self.__author = author
        self.__tasks = []
        self.__commands = {}
        self.register_commands({
            "1": {"description": "View Tasks", "function": self.view_tasks},
            "2": {"description": "Add Task", "function": self.add_task},
            "3": {"description": "Display Bot Info", "function": self.display_info},
            "4": {"description": "Exit", "function": self.exit_bot}
        })
    
    def register_commands(self, commands):
        for key, command_info in commands.items():
            self.__commands[key] = {
                "description": command_info["description"],
                "function": command_info["function"]
            }
    
    def display_info(self):
        console.print(f"[green]Bot Name:[/green] {self.__name}")
        time.sleep(0.2)
        console.print(f"[blue]Version:[/blue] {self.__version}")
        time.sleep(0.2)
        console.print(f"[magenta]Author:[/magenta] {self.__author}")
        time.sleep(0.2)
        console.print(f"[yellow]Tasks:[/yellow] {len(self.__tasks)}")
        
    def add_task(self):
        new_task = input("Enter the new task: ")
        self.__tasks.append(new_task)
        console.print(
            f"[bold green]Task "
            f"'{new_task}' added successfully![/bold green]"
        )
        
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def view_tasks(self):
        console.print("\n[bold cyan]TASKS:[/bold cyan]")
        if not self.__tasks:
            console.print("[yellow]No tasks available.[/yellow]")
        else:
            for idx, task in enumerate(self.__tasks, 1):
                console.print(f"[green]{idx}. {task}[/green]")
        
    def welcome_message(self):
        console.print(
            f"[bold green]Welcome to "
            f"{self.__name} v{self.__version} "
            f"by {self.__author}![/bold green]"
        )
        self.clear_screen()
        
    def exit_bot(self):
        console.print("[bold red]Exiting...[/bold red]")
        time.sleep(1)
        exit()
        
    def run(self):
        self.welcome_message()
        while True:
            console.print("\n[bold cyan]Main Menu:[/bold cyan]")
            for key, command_info in self.__commands.items():
                console.print(f"[green]{key}. {command_info['description']}[/green]")
            choice = input("\nSELECT OPTION: ")
            if choice in self.__commands:
                self.__commands[choice]["function"]()
            else:
                console.print("[red]Invalid option. Please try again.[/red]")
                
if __name__ == "__main__":
    bot = SysBot(name="SysBot", version="1.0", author="Your Name")
    bot.run()
    