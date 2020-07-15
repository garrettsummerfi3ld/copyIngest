import os.path as path
import shutil
import os
import datetime
from colorama import init, Fore, Back, Style
from termcolor import colored

### VARS
sourcePath = "G:\\Ingest"
destPath = "E:\\Videos\\Ingest"
currentDateTime = datetime.datetime

### COLOR LOGGING
init()

# Green
def success(args): print(Fore.GREEN + args)

# Normal
def info(args): print(Style.RESET_ALL + args)

# Yellow
def warn(args): print(Fore.YELLOW + args)

# Red
def err(args): print(Fore.RED + args)

# Cyan
def debug(args): print(Fore.CYAN + args)

### FUNCTIONS

# Checks location of sourcePath if it is a real location
def sourcePathCheck():
    debug("Started sourcePathCheck()")
    info("Checking source path...")
    if (path.exists(sourcePath) == False):
        debug("Path exists bool =" + str(path.exists(sourcePath)))
        warn("Source location does not exist!")
        info("Creating source location...")
        os.mkdir(sourcePath)
        success("Created source location!")
        pass
    else:
        debug("Path exists bool =" + str(path.exists(sourcePath)))
        info("Source location exists!")
        pass

# Checks location of destPath if it is a real location
def destPathCheck():
    info("Checking destination path...")
    if (path.exists(destPath) == False):
        warn("Destination location does not exist!")
        info("Creating destination location")
        os.mkdir(destPath)
        success("Created destination location")
        pass
    else:
        info("Destination location exists!")

# File checking
def checkFiles():
    debug

# Main function
def main():
    debug("Started main()")
    try:
        sourcePathCheck()
        destPathCheck()
    except Exception as ex:
        err("Something really bad just happened. Printing stacktrace...")
        err(ex)
        SystemExit(1)

# Init function
if __name__ == "__main__":
    debug("Starting up...")
    main()