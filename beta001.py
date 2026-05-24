import os
import time
import sys
from rich.console import Console

console = Console()


def os_check():
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


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def create_file(file_name, content=""):
    if os.path.exists(file_name):
        return False

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

    return True


# Login Screen
while True:
    console.print("[bold blue]TYPE PASSWORD TO CONTINUE[/bold blue]")
    password = input("PASSWORD: ")
    if password == "ee":
        console.print("[bold green]ACCESS GRANTED[/bold green]")
        time.sleep(1)
        clear_screen()
        break
    else:
        console.print("[bold red]ACCESS DENIED[/bold red]")
        time.sleep(2)
        sys.exit()


# Main Menu
while True:
    console.print("\n[bold magenta]=== MAIN MENU ===[/bold magenta]")
    console.print("[yellow]1.[/yellow] Show OS Information")
    console.print("[yellow]2.[/yellow] Clear Screen")
    console.print("[yellow]3.[/yellow] Check File Existence")
    console.print("[yellow]4.[/yellow] Create File")
    console.print("[yellow]Q.[/yellow] Exit")
    
    choice = input("\nSELECT OPTION: ").lower()
    
    if choice == "1":
        os_check()
        time.sleep(2)
    elif choice == "2":
        clear_screen()
    elif choice == "3":
        console.print("[bold cyan]Enter file path to check:[/bold cyan]")
        file_path = input("FILE PATH: ")
        if os.path.exists(file_path):
            console.print(f"[bold green]File exists: {file_path}[/bold green]")
        else:
            console.print(f"[bold red]File does not exist: {file_path}[/bold red]")
    elif choice == "4":
        console.print("[bold cyan]Enter file name to create:[/bold cyan]")
        file_name = input("FILE NAME: ")
        if file_name.strip() == "":
            console.print("[bold red]File name cannot be empty[/bold red]")
            time.sleep(1)
            continue
        if os.path.exists(file_name):
            console.print(f"[bold red]File already exists: {file_name}[/bold red]")
            time.sleep(1)
            continue
        file_content = input("Enter content for the file: ")
        console.print("[bold cyan]Creating file...[/bold cyan]")
        success = create_file(file_name, file_content)
        time.sleep(0.5)
        if success:
            console.print(f"[bold green]File created: {file_name}[/bold green]")
        else:
            console.print(f"[bold red]Failed to create file: {file_name}[/bold red]")
    elif choice == "q":
        console.print("[red]Exiting...[/red]")
        time.sleep(1)
        sys.exit()
    else:
        console.print("[bold red]Invalid option[/bold red]")