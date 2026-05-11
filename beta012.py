import rich.console
import time
import os

console = rich.console.Console()


class SysBot:
    def __init__(self, name, version, author,commands=None):
        self.__name = name
        self.__version = version
        self.__author = author
        self.__commands = self.commands = {
        "1": self.view_tasks,
        "2": self.add_task,
        "3": self.display_info,
        "4": self.exit_bot
    }
        self.__tasks = [] 
    
    
    def exit_bot(self):
        console.print("[bold red]Exiting...[/bold red]")
        time.sleep(1)
        exit()
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def welcome_message(self):
        console.print(
            f"[bold green]Welcome to "
            f"{self.__name} v{self.__version} "
            f"by {self.__author}![/bold green]"
        )

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

    def view_tasks(self):
        console.print("\n[bold cyan]TASKS:[/bold cyan]")

        if not self.__tasks:
            console.print("[red]No tasks available.[/red]")
            return

        for index, task in enumerate(self.__tasks, start=1):
            console.print(f"[white]{index}. {task}[/white]")

    def run(self):
        console.print("\n[bold cyan]Main Menu:[/bold cyan]")
        console.print("[green]1. View Tasks[/green]")
        console.print("[green]2. Add Task[/green]")
        console.print("[green]3. Display Bot Info[/green]")
        console.print("[green]4. Exit[/green]")
        choice = input("\nEnter your choice: ")


        if choice in self.__commands:
            self.__commands[choice]()
        
my_bot = SysBot("SysBot", "0.1.2", "Nefrius")

my_bot.welcome_message()
time.sleep(1)

my_bot.run()