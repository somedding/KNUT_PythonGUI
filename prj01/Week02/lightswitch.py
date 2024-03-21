class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
         self.switchIsOn = True

    def turnOff(self):
         self.switchIsOn = False

    def show(self):  
        print(self.switchIsOn)
    
oLightSwitch = LightSwitch()  

oLightSwitch.show() 
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()