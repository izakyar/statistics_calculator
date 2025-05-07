from rich.console import Console
import time

console = Console()

def solution(msg: str) -> None:
    console.log(f"[bold green](Solution)[/] {msg}")

def succsess(msg: str) -> None:
    console.log(f"[bold green](Succsess)[/] {msg}")

def error(msg: str) -> None:
    console.log(f"[bold red](Error)[/] {msg}")

def warning(msg: str) -> None:
    console.log(f"[bold yellow](Warning)[/] {msg}")

