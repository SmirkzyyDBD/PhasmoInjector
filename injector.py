import os
import sys
import time
import shutil
from pystyle import Colors, Colorate, Center

os.system("title Phasmo Injector")

print_logo = '''
  _____  _                                 _____       _           _             
 |  __ \| |                               |_   _|     (_)         | |            
 | |__) | |__   __ _ ___ _ __ ___   ___     | |  _ __  _  ___  ___| |_ ___  _ __ 
 |  ___/| '_ \ / _` / __| '_ ` _ \ / _ \    | | | '_ \| |/ _ \/ __| __/ _ \| '__|
 | |    | | | | (_| \__ \ | | | | | (_) |  _| |_| | | | |  __/ (__| || (_) | |   
 |_|    |_| |_|\__,_|___/_| |_| |_|\___/  |_____|_| |_| |\___|\___|\__\___/|_|   
                                                     _/ |                        
                                                    |__/  By Smirkzyy                     
'''

logo = Center.XCenter(print_logo)

appdata = os.getenv("USERPROFILE")

SaveFile = "SaveFile.txt"
InjectPath = f"{appdata}\\AppData\\LocalLow\\Kinetic Games\\Phasmophobia\\SaveFile.txt"
BackupLocation = f"{appdata}\\AppData\\LocalLow\\Kinetic Games\\Phasmophobia\\SaveFile.txt"

red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"
white = "\033[1;37m"

def timeloop():
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        yield current_time
        
timegen = timeloop()

def get_time():
    return next(timegen)

def printlogo():
    print(Colorate.Horizontal(Colors.blue_to_cyan, logo, 1))

def choice():
    while True:
        now = get_time()
        printlogo()
        print(Center.XCenter(f"""
        {cyan}[ 1 ]{white} Inject Full Save File
        {cyan}[ 2 ]{white} Inject Custom Save File
        {cyan}[ 3 ]{white} Backup Current Save File
        {cyan}[ 4 ]{white} Exit
        """))
        
        print()
        appchoice = input(f"{cyan}[ >> ]{white} ")
        
        if appchoice == "1":
            fullinject()
        if appchoice == "2":
            custominject()
        if appchoice == "3":
            backup()
        if appchoice == "4":
            sys.exit()
            
        else:
            print()
            input(f"{red}[ {now} ]{white} Invalid option, press ENTER to retry...")
            os.system("cls")
            choice()
        
def fullinject():
    os.system("cls")
    now = get_time()
    printlogo()
    print()
    try:
        print(f'{cyan}[ {now} ]{white} Attempting to inject...')
        if not os.path.exists(SaveFile):
            print(f'{red}[ {now} ]{white} Save file not found!')
            input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")
            os.system("cls")
            choice()
        try:
            shutil.copyfile(SaveFile, InjectPath)
            print(f'{green}[ {now} ]{white} Save file injected successfully!')
            input(f"{cyan}[ {now} ]{white} Press ENTER to return...")
            os.system("cls")
            choice()
        except Exception as e:
            print(f"{red}[ {now} ]{white} Failed to Inject! {e}")
            input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")
            os.system("cls")
            choice()
        
    except Exception as e:
        print(f"{red}[ {now} ]{white} Failed to Inject! {e}")
        input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")
        os.system("cls")
        choice()
        
def custominject():
    while True:
        os.system("cls")
        now = get_time()
        printlogo()
        print()
        print(f"{cyan}[ {now} ]{white} Enter path to custom Save File:")
        customFile = input(f"{cyan}[ >> ]{white} ")
        customSavePath = os.path.join(customFile, 'SaveFile.txt')
        if not os.path.exists(customSavePath):
            print(f"{red}[ {now} ]{white} Save file not found! {red}{customSavePath}{white}")
            input(f"{cyan}[ {now} ]{white} Press ENTER to retry...")
            custominject()
        try:
            print(f'{cyan}[ {now} ]{white} Attempting to inject custom save file...')
            shutil.copyfile(customSavePath, InjectPath)
            print(f"{green}[ {now} ]{white} Custom Save File injected!")
            input(f"{cyan}[ {now} ]{white} Press ENTER to continue...")
            os.system("cls")
            choice()
        except Exception as e:
            print(f"{red}[ {now} ]{white} Failed to Inject! {e}")
            input(f"{red}[ {now} ]{white} Press ENTER to retry...")
            os.system("cls")
            custominject()
        
def backup():
    os.system("cls")
    now = get_time()
    printlogo()
    print()
    try:
        print(f'{cyan}[ {now} ]{white} Attempting to backup save file...')
        if not os.path.exists(InjectPath):
            print(f'{red}[ {now} ]{white} Save File not found!')
            input(f"{cyan}[ {now} ]{white} Press ENTER to return...")
            os.system("cls")
            choice()
        script_dir = os.path.dirname(sys.executable)
        createFolder = os.path.join(script_dir, "SaveFileBackup")
        if not os.path.exists(createFolder):
            os.makedirs(createFolder, exist_ok=True)
        backupFilePath = os.path.join(createFolder, "SaveFile.txt")
        shutil.copyfile(BackupLocation, backupFilePath)
        print(f"{green}[ {now} ]{white} Save File backed up!")
        input(f"{cyan}[ {now} ]{white} Press ENTER to return...")
        os.system("cls")
        choice()
    except Exception as e:
        print(f"{red}[ {now} ]{white} Failed to backup! {e}")
        input(f"{red}[ {now} ]{white} Press ENTER to continue...")
        os.system("cls")
        choice() 

if __name__ == '__main__':
    choice()
