from Range import *

class GUI(types.KX_PythonComponent):
    args = {}
    
    def awake(self, args):
        self.gameScene = logic.getSceneList()["Game"]
        self.gameObjects = self.gameScene.objects
        
        self.guiScene = logic.getSceneList()["GUI"]
        self.widgets = self.guiScene.objects
        
        self.move = self.widgets["Move"]
        self.rotate = self.widgets["Rotate"]
        self.destroy = self.widgets["Destroy"]
        
        self.mouse = logic.mouse
        self.l = self.mouse.inputs[events.LEFTMOUSE]
    
    def start(self, args):
        pass
    
    def update(self):
        s = 1.1
        self.pos = self.mouse.position
        self.over = self.object.getScreenRay(self.pos[0], self.pos[1], 10)
        #print(self.over)
        
        if self.over is not None:
            
            # MoveButton
            if self.over == self.move:
                self.move.worldScale = (s,s,s)
                
                if self.l.activated:
                    if "Player" in self.gameObjects:
                        self.gameObjects["Player"].applyMovement([0.2,0,0])
            
            # RotateButton
            if self.over == self.rotate:
                self.rotate.worldScale = (s,s,s)
                
                if self.l.activated:
                    if "Player" in self.gameObjects:
                        self.gameObjects["Player"].applyRotation([0,0,0.2])
            
            # DestroyButton
            if self.over == self.destroy:
                self.destroy.worldScale = (s,s,s)
                
                if self.l.activated:
                    if "Player" in self.gameObjects:
                        self.gameObjects["Player"].endObject()
            
        else:
            buttons = [self.move, self.rotate, self.destroy]
            for b in buttons:
                b.worldScale = (1,1,1)