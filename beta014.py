from time import sleep
from rich.console import Console

console = Console()


def login_system(func):
    def wrapper(*args, **kwargs):
        username = console.input("Kullanıcı Adı: ")
        password = console.input("Şifre: ")
        if username == "admin" and password == "admin":
            return func(*args, **kwargs)
        else:
            console.print("Kullanıcı adı veya şifre yanlış")

    return wrapper


def clear_screen(func):
    def wrapper(*args, **kwargs):
        console.clear()
        sleep(1.2)
        return func(*args, **kwargs)

    return wrapper


@login_system
@clear_screen
def menu_system():
    console.print("Menu:")
    console.print("1. Giriş Yap")
    console.print("2. Çıkış Yap")
    choice = console.input("Seçiminiz: ")
    if choice == "1":
        print("qwe")
    elif choice == "2":
        console.print("Çıkış yapılıyor...")
    else:
        console.print("Geçersiz seçim")


menu_system()
