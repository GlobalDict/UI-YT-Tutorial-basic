from Range import *

class Game(types.KX_PythonComponent):
    args = {}
    
    def awake(self, args):
        logic.addScene("GUI", 1)
    
    def start(self, args):
        pass
    
    def update(self):
        pass