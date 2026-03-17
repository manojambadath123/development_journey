


from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class Vscode(Editor):

    def open(self):
        print("vscode open method")

    def execute(self):
        print("vscode execute method")

    def debug(self):
        print("vscode debug method")

vscode_instance = Vscode()

vscode_instance.open()
vscode_instance.execute()
vscode_instance.debug()