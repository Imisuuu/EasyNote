from Functions import File
import os

class Editor:
    def __init__(self, instance=File()):
        self.instance = instance

    #First idea: Copy text from a file, paste it into an input,
    #so the file could be edited without 3rd party editors such as nano
    #maybe implement it later
    def edit(self, instance=File()):
        os.system(f"nano ./Notes/{instance.Get_Current_Date()}")




