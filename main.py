import os
import shutil
import time
import requests
import queue
from colorama import Fore, init
from itertools import cycle
import threading
from concurrent.futures import ThreadPoolExecutor
init(autoreset=True)
API_URL = 'https://api.scratch.mit.edu/accounts/checkusername/'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_animated_banner():
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
    for _ in range(10):
        clear_console()
        color = next(colors)
        for line in art.splitlines():
            print(color + line.center(console_width))
        time.sleep(0.2)
    print(Fore.RED + "Made by Kyra".center(console_width))

def show_main_menu():
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
            update_api_endpoint()
        elif choice == "3":
            clear_console()
            print(Fore.RED + "Thanks for using my tool!".center(shutil.get_terminal_size().columns))
            time.sleep(2)
            exit()
        else:
            print(Fore.LIGHTRED_EX + "Invalid option!".center(shutil.get_terminal_size().columns))
            time.sleep(2)

def update_api_endpoint():
    global API_URL
    clear_console()
    print(Fore.RED + "Current API Endpoint:".center(shutil.get_terminal_size().columns))
    print(Fore.LIGHTRED_EX + API_URL.center(shutil.get_terminal_size().columns))
    API_URL = input(Fore.RED + "Enter new API endpoint: ")
    print(Fore.GREEN + "Endpoint updated!".center(shutil.get_terminal_size().columns))
    time.sleep(2)

def check_username(username, session, file_lock, progress_lock, counters, results_queue):
    global API_URL
    rate_limiter = threading.Semaphore(10)
    with rate_limiter:
        try:
            response = session.get(API_URL + username, timeout=5)
            if response.status_code == 200 and response.json().get('msg') == 'valid username':
                results_queue.put((True, username))
                with file_lock:
                    with open('output.txt', 'a') as file:
                        file.write(f"{username}\n")
                    counters['valid'] += 1
            else:
                results_queue.put((False, username))
        except requests.RequestException:
            results_queue.put((None, username))
        finally:
            with progress_lock:
                counters['checked'] += 1

def run_checker():
    try:
        with open("list.txt", "r") as file:
            usernames = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "Error: list.txt not found. Please create it and add usernames to check.")
        time.sleep(3)
        return
    if not usernames:
        print(Fore.YELLOW + "Warning: list.txt is empty.")
        time.sleep(3)
        return
    open('output.txt', 'w').close()
    counters = {'checked': 0, 'valid': 0}
    total_usernames = len(usernames)
    file_lock = threading.Lock()
    progress_lock = threading.Lock()
    results_queue = queue.Queue()
    try:
        with requests.Session() as session:
            with ThreadPoolExecutor(max_workers=10) as executor:
                for name in usernames:
                    executor.submit(check_username, name, session, file_lock, progress_lock, counters, results_queue)
                clear_console()
                while counters['checked'] < total_usernames:
                    while not results_queue.empty():
                        try:
                            is_valid, username = results_queue.get_nowait()
                            print(" " * shutil.get_terminal_size().columns, end="\r")
                            if is_valid is True:
                                print(Fore.GREEN + f"Username found: {username}")
                            elif is_valid is False:
                                print(Fore.RED + f"Username unavailable: {username}")
                            else:
                                print(Fore.YELLOW + f"Error checking username: {username}")
                        except queue.Empty:
                            break
                    percent = int(counters['checked'] / total_usernames * 100)
                    bar_length = 40
                    bar = ('█' * int(bar_length * percent / 100)).ljust(bar_length)
                    status_line = f"{Fore.LIGHTRED_EX}[{bar}] {percent}% Complete {Fore.GREEN}| Valid: {counters['valid']}"
                    print(status_line.ljust(shutil.get_terminal_size().columns), end="\r")
                    time.sleep(0.1)
        print(" " * shutil.get_terminal_size().columns, end="\r")
        print(f"\n{Fore.GREEN}Check complete! {counters['valid']} available usernames found and saved to output.txt.")
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "Stopping the threads...")
        time.sleep(2)


if __name__ == "__main__":
    clear_console()
    display_animated_banner()
    time.sleep(1)
    show_main_menu()
    run_checker()
