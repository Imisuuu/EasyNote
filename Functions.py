from os.path import exists
from Module import File
import os
import datetime
from Editor import Editor

class Functions:
    def __init__(self, instance=File(), editor=Editor()):
        self.instance = instance
        self.editor = editor

    def if_exists(self, instance=File()):
        print("1. Read the file\n2. Edit the file\n3. Clear the file\n4. Open historical note")
        choice = 0
        try:
            choice = int(input("Choice: "))
        except:
            self.if_exists()

        if choice == 1:
            print(f"\nToday is {instance.current_date}!\n")
            print(instance.Read_File().read())

        elif choice == 2:
            #Zamiana na editor
            self.editor.edit()


        elif choice == 3:
            instance.Clear_File()

        elif choice == 4:
            self.Get_Historical_Data()

        else:
            self.if_exists()

    def Count(self, directory):
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
                if (file.startswith("20") and f != ""):
                    date.append(file)
        return sorted(date)

    def Get_Historical_Data(self):
        history = self.Count('./Notes/')
        print("")
        for i in range(len(history)):
            print(f"{i}. {history[i]}")
        try:
            choose = int(input('Choose: '))
            var = File(current_date=history[choose])
            print(f"\nToday is {var.current_date}!")
            print(var.Read_File().read())
            return 0
        except:
            self.Get_Historical_Data()

    def create_file(self):
        instance = File()
        print(f"\nToday is {instance.current_date}!")
        instance.Create_File()
        self.if_exists()

    def check_if_file_exists(self, path):
        return exists(path)

    def run(self):
        if self.check_if_file_exists(f"./{datetime.date.today()}"):
            self.if_exists()
        else:
            self.create_file()
