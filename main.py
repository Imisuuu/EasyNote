import datetime
from os.path import exists
import os
from Module import File
def Check_If_File_Exists(path):
    return exists(path)

def If_Exists():
    print("1. Read the file\n2. Edit the file\n3. Clear the file\n4. Open historical note")
    choice = 0
    try:
        choice = int(input("Choice: "))
    except:
        If_Exists()
    instance = File()

    if choice == 1:
        print(f"\nToday is {instance.current_date}!\n")
        instance.Read_File()

    elif choice == 2:
        text = input("Write sum: ")
        instance = File(text=text)
        instance.Write_File(text)
        instance.Read_File()

    elif choice == 3:
        instance.Clear_File()

    elif choice == 4:
        Get_Historical_Data()

    else:
        If_Exists()


def Get_Historical_Data():
    history = Count('./Notes/')
    print("")
    for i in range(len(history)):
        print(f"{i}. {history[i]}")
    try:
        choose = int(input('Choose: '))
        var = File(current_date=history[choose])
        print(f"\nToday is {var.current_date}!")
        var.Read_File()
        return 0
    except:
        Get_Historical_Data()

def Not_Existing():
    instance = File()
    print(f"\nToday is {instance.current_date}!")
    instance.Create_File()
    If_Exists()

def Main():
    if Check_If_File_Exists(f"./{datetime.date.today()}"):
        If_Exists()
    else:
        Not_Existing()

def Count(directory):
    # days = []
    date = []
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            # print(f)
            file = f.removeprefix('.').removeprefix('/').removeprefix('Notes/')
            if (file.startswith("20")and f != ""):
                date.append(file)
    return sorted(date)


Main()
