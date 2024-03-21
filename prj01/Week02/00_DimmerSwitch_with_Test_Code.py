class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
        
    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)

    def micOn(self):
        print('mic is on')
        self.micIsOn = True
    
    def micOff(self):
        print('mic is off')
        self.micIsOn = False
    
oDimmer = DimmerSwitch() 
oDimmer2 = DimmerSwitch()
oDimmer3 = DimmerSwitch()

oDimmer.micOn()

oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.show()

oDimmer3.turnOn()
oDimmer3.raiseLevel()
oDimmer3.show()

oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

oDimmer.turnOn()

oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()

oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

oDimmer.micOff()
