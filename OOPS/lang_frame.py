
#single level inheritance using constructor initialization

class Language:

    def __init__(self,lname):

        self.lname=lname

    def display_language(self):

        print(self.lname)

class Framework(Language):

    def __init__(self,lname,fname):

        super().__init__(lname)

        self.fname=fname

    def display_framework(self):

        super().display_language()

        print(self.fname)

fw_instance1 = Framework("python","django")
fw_instance1.display_framework()

fw_instance2 = Framework("python","flask")
fw_instance2.display_framework()