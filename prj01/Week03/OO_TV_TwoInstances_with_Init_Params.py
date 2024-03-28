#49페이지 + TV 사이즈 추가
class TV():
    def __init__(self, brand, location, size):  
        self.brand = brand
        self.location = location
        self.size = size
        self.isOn = False
        self.isMuted = False
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]  
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0  # constant
        self.VOLUME_MAXIMUM = 10  
        self.volume = self.VOLUME_MAXIMUM // 2  
       
    def power(self):
        self.isOn = not self.isOn 

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while muted, unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while muted, unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1    # wrap around to the top channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel not in self.channelList:
            return  # not in our list of legal channel, don't do anything
        self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print('Status of TV:', self.brand)
        print('    Location:', self.location)
        print('    Size:', self.size)
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')

oTV1 = TV('Sony', 'Family room', '55 inch')  
oTV2 = TV('Samsung', 'Bedroom', '85 inch')  


oTV1.power()
oTV2.power()

oTV1.volumeUp()
oTV1.volumeUp()

oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()

oTV2.setChannel(44)
oTV2.mute()

oTV1.showInfo()
oTV2.showInfo()

oTV2.setChannel(44)
oTV2.mute()

oTV1.showInfo()
oTV2.showInfo()