import datetime
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