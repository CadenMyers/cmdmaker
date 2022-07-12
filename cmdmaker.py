#!/usr/bin/env python3

import subprocess
import time

subprocess.call(["figlet", "-f", "big", "cmdmaker"])

file_name = input("[+] What is the name of your python file?:\n")
new_name = input("[+] What would you like to name your executable?\n")


subprocess.call(["chmod", "+x", file_name])
subprocess.call(["cp", file_name, f"/bin/{new_name}"])
