from rich.console import Console
from rich.tree import Tree 
import time
import importlib.util
from importlib.metadata import metadata, version, PackageNotFoundError

console = Console()


class TerminalControllerDependency: 
    def __init__(self):
        self.controllers = []
        
    def terminal_clear(self):
        def wrapper(func):
            def inner(*args, **kwargs):
                console.print("[green] [+] [red]Clearing terminal...[/red]")
                time.sleep(0.4)
                console.clear()
                time.sleep(1.2)
                return func(*args, **kwargs)
            return inner
        return wrapper
    
    def terminal_print(self, message):
        console.print(message)

TerminalTools = TerminalControllerDependency()

class ModuleScanner:
    def __init__(self, module_name):
        self.module_name = module_name
    
    def get_full_package_info(self):
        
        def module_exists(module_name) -> bool:
            spec = importlib.util.find_spec(module_name)
            return spec is not None
        
        if not module_exists(self.module_name):
            TerminalTools.terminal_print(f"[green] [+] [red]Module '{self.module_name}' not found.[/red]")
            return None
        
        if module_exists(self.module_name):
            try:
                module_metadata = metadata(self.module_name)
                tree = Tree(f"[green] [+] [red]Module '{self.module_name}' found![/red]")
                tree.add(f"[bold]Name:[/bold] {module_metadata.get('Name', 'N/A')}")
                tree.add(f"[bold]Version:[/bold] {module_metadata.get('Version', 'N/A')}")
                tree.add(f"[bold]Summary:[/bold] {module_metadata.get('Summary', 'N/A')}")
                tree.add(f"[bold]Author:[/bold] {module_metadata.get('Author', 'N/A')}")
                tree.add(f"[bold]License:[/bold] {module_metadata.get('License', 'N/A')}")
                return tree
            except PackageNotFoundError:
                TerminalTools.terminal_print(f"[green] [+] [red]Module '{self.module_name}' not found.[/red]")
                return None
            
            except Exception as e:
                TerminalTools.terminal_print(f"[green] [+] [red]An error occurred: {e}[/red]")
                return None
        

if __name__ == "__main__":
    console.print("[green] [+] [red]Welcome to the Module Scanner![/red]")
    module_name = console.input("Enter the module name to scan: ")
    scanner = ModuleScanner(module_name)
    info = scanner.get_full_package_info()
    if info:
        TerminalTools.terminal_print("[green]Module Information:[/green]")
        console.print(info)
            