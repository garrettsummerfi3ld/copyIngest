import shutil
import os
import datetime
import sys
import json
import os.path as path
from colorama import init, Fore, Back, Style
from termcolor import colored

### VARS
with open("vars.json", "r") as vars:
    data = json.load(vars)
sourcePath = data["sourcePath"]
destPath = data["destPath"]
fileTypes = data["fileTypes"]
currentDateTime = datetime.datetime.now()
sourceFiles = []


### COLOR LOGGING
init(autoreset=True)

# Success -> green
def success(args): print(Fore.GREEN + args)

# Normal -> white
def info(args): print(args)

# Warning -> yellow
def warn(args): print(Fore.YELLOW + args)

# Error -> red
def err(args): print(Fore.RED + args)

# Critical -> red bg
def crit(args): print(Back.RED + Fore.WHITE + args)

# Debug -> Cyan
def debug(args): print(Fore.CYAN + args)

### FUNCTIONS

# Checks location of sourcePath if it is a real location
def sourcePathCheck():
    info("Checking source path...")
    if (sourcePath != ""):
        if (path.exists(sourcePath) == False):
            warn("Source location does not exist!")
            info("Creating source location...")
            os.mkdir(sourcePath)
            success("Created source location!")
            pass
        else:
            info("Source location exists!")
            pass
    else:
        raise FileNotFoundError("'sourcePath' in 'vars.json' is left blank. Edit the file to fix this issue")


# Checks location of destPath if it is a real location
def destPathCheck():
    info("Checking destination path...")
    if (destPath != ""):
        if (path.exists(destPath) == False):
            warn("Destination location does not exist!")
            info("Creating destination location")
            os.mkdir(destPath)
            success("Created destination location")
            pass
        else:
            info("Destination location exists!")
            pass
    else:
        raise FileNotFoundError("'destPath' in 'vars.json' is left blank. Edit the file to fix this issue")

# Checks for files in the sourcePath
def checkFiles():
    info("Checking files in sourcePath...")
    for r, d, f in os.walk(data["sourcePath"]):
        for file in f:
            if data["fileTypes"] in file:
                sourceFiles.append(path.join(r, file))

    for f in sourceFiles:
        info("Found {}".format(f))

    if len(sourceFiles) == 0:
        err("There are no files! Exiting as there is nothing to do...")
        SystemExit(1)

# Main function
def main():
    info("Started at {}".format(str(currentDateTime)))

    try:
        debug("Checking 'vars.json'...")
        debug(str(data))
        sourcePathCheck()
        destPathCheck()
        checkFiles()

    except Exception as ex:
        crit("Something really bad just happened. Printing stacktrace...")
        print(ex)
        print(sys.exc_info())
        vars.close()
        SystemExit(1)

# Init function
if __name__ == "__main__":
    info("Starting up...")
    main()