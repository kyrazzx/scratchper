import os
import time
import shutil
import requests
from colorama import Fore, Style, init
from itertools import cycle

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art_with_animation():
    art = r"""
                                                                                                                                              
         ______        _____        _____         _____   _________________      _____    ____   ____      _____        ______        _____   
     ___|\     \   ___|\    \   ___|\    \    ___|\    \ /                 \ ___|\    \  |    | |    | ___|\    \   ___|\     \   ___|\    \  
    |    |\     \ /    /\    \ |    |\    \  /    /\    \\______     ______//    /\    \ |    | |    ||    |\    \ |     \     \ |    |\    \ 
    |    |/____/||    |  |    ||    | |    ||    |  |    |  \( /    /  )/  |    |  |    ||    |_|    ||    | |    ||     ,_____/||    | |    |
 ___|    \|   | ||    |  |____||    |/____/ |    |__|    |   ' |   |   '   |    |  |____||    .-.    ||    |/____/||     \--'\_|/|    |/____/ 
|    \    \___|/ |    |   ____ |    |\    \ |    .--.    |     |   |       |    |   ____ |    | |    ||    ||    |||     /___/|  |    |\    \ 
|    |\     \    |    |  |    ||    | |    ||    |  |    |    /   //       |    |  |    ||    | |    ||    ||____|/|     \____|\ |    | |    |
|\ ___\|_____|   |\ ___\/    /||____| |____||____|  |____|   /___//        |\ ___\/    /||____| |____||____|       |____ '     /||____| |____|
| |    |     |   | |   /____/ ||    | |    ||    |  |    |  |`   |         | |   /____/ ||    | |    ||    |       |    /_____/ ||    | |    |
 \|____|_____|    \|___|    | /|____| |____||____|  |____|  |____|          \|___|    | /|____| |____||____|       |____|     | /|____| |____|
    \(    )/        \( |____|/   \(     )/    \(      )/      \(              \( |____|/   \(     )/    \(           \( |_____|/   \(     )/  
     '    '          '   )/       '     '      '      '        '               '   )/       '     '      '            '    )/       '     '   
                         '                                                         '                                       '                     
    """
    console_width = shutil.get_terminal_size().columns
    colors = cycle([Fore.RED, Fore.LIGHTRED_EX])

    for _ in range(10):  # Animation cycle
        clear_console()
        color = next(colors)
        for line in art.splitlines():
            print(color + line.center(console_width))
        time.sleep(0.2)

    print(Fore.RED + "Made by Kyra".center(console_width))

def progress_bar(current, total, bar_length=40):
    percent = int(current / total * 100)
    bar = ('█' * int(bar_length * percent / 100)).ljust(bar_length)
    print(Fore.LIGHTRED_EX + f"[{bar}] {percent}% Complete", end="\r")

def interactive_menu():
    while True:
        clear_console()
        print(Fore.RED + "Main Menu".center(shutil.get_terminal_size().columns, "-"))
        print(Fore.LIGHTRED_EX + "[1] Start Username Check")
        print(Fore.LIGHTRED_EX + "[2] Change API Endpoint")
        print(Fore.LIGHTRED_EX + "[3] Exit")
        choice = input(Fore.RED + "Choose an option: ")
        if choice == "1":
            return
        elif choice == "2":
            change_endpoint()
        elif choice == "3":
            clear_console()
            print(Fore.RED + "Thanks for using my tool!".center(shutil.get_terminal_size().columns))
            time.sleep(2)
            exit()
        else:
            print(Fore.LIGHTRED_EX + "Invalid option!".center(shutil.get_terminal_size().columns))
            time.sleep(2)

def change_endpoint():
    global LINK
    clear_console()
    print(Fore.RED + "Current API Endpoint:".center(shutil.get_terminal_size().columns))
    print(Fore.LIGHTRED_EX + LINK.center(shutil.get_terminal_size().columns))
    LINK = input(Fore.RED + "Enter new API endpoint: ")
    print(Fore.LIGHTRED_EX + "Endpoint updated!".center(shutil.get_terminal_size().columns))
    time.sleep(2)

def main():
    global LINK
    LINK = 'https://api.scratch.mit.edu/accounts/checkusername/'
    with open("list.txt", "r") as file:
        words = file.read().strip().split("\n")
    free = []
    session = requests.Session()
    try:
        for count, word in enumerate(words, start=1):
            response = session.get(LINK + word)
            if response.json().get('msg') == 'valid username':
                print(Fore.LIGHTRED_EX + f"Line {count}: {word} is available")
                free.append(f"{word}\n")
            else:
                print(Fore.RED + f"Username {count}: {word} is unavailable")
            progress_bar(count, len(words))
            print(Fore.YELLOW + f"\nValid usernames: {len(free)}", end="\r")
        print()  # Ensure progress bar line is separate
    except KeyboardInterrupt:
        write_free(free)
        raise SystemExit
    write_free(free)
    print(Fore.LIGHTRED_EX + f"\nCheck complete! {len(free)} usernames available.")

def write_free(free):
    with open('output.txt', 'w') as file:
        file.writelines(free)

if __name__ == "__main__":
    clear_console()
    display_ascii_art_with_animation()
    time.sleep(1)
    interactive_menu()
    main()