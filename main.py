import datetime
from os.path import exists
import os
class File:
    def __init__(self, text="", current_date=datetime.date.today()):
        self.text = text
        self.current_date = current_date

    def Create_File(self):
        file = open(f"./Notes/{self.current_date}", "a")
        return file

    def Read_File(self):
        file = open(f"./Notes/{self.current_date}", "r")
        print(file.read())
        return file.read()

    def Write_File(self, text):
        with open(f"./Notes/{self.current_date}", "a") as f:
            f.write(text + "\n")

    def Clear_File(self):
        with open(f"./Notes/{self.current_date}", "w") as f:
            f.write("")

def Check_If_File_Exists(path):
    return exists(path)

def Primera():
    print("1. Read the file\n2. Edit the file\n3. Clear the file\n4. Open historical note")
    choice = int(input("Choice: "))
    instance = File()

    if choice == 1:
        print(f"\nToday is {instance.current_date}!\n")
        instance.Read_File()

    elif choice == 2:
        text = input("Write sum: ")
        instance = File(text=text)
        instance.Write_File(text)
        instance.Read_File()

    elif choice==3:
        instance.Clear_File()

    elif choice==4:
        history = Count('./Notes/')
        print("")
        for i in range(len(history)):
            print(f"{i}. {history[i]}")
        choose = int(input('Choose: '))
        var = File(current_date=history[choose])
        print(f"\nToday is {var.current_date}!")
        var.Read_File()

def Segunda():
    instance = File()
    print(f"\nToday is {instance.current_date}!")
    instance.Create_File()
    Primera()

def Main():
    if Check_If_File_Exists(f"./{datetime.date.today()}"):
        Primera()
    else:
        Segunda()

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
    return date


Main()
