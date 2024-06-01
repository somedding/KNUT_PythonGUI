#  Timer
class Timer():
    """
    This class is used to create a very simple Timer.

    Typical use:

    1)  Create a Timer object:

        myTimer = pyghelpers.Timer(10)

    2)  When you want the timer to start running, make this call:

        myTimer.start()

        You can also call this method to restart the timer after it finishes.

    3)  In your big loop, check to see if the timer has finished:

        finished = myTimer.update()

        Normally returns False, but returns True when the timer is finished

    Parameters:
        | timeInSeconds - the duration of the timer, in seconds (integer or float)

    Optional keyword parameters:
        | nickname - an internal name to associate with this timer (defaults to None)
        | callback - a function or object.method to be called back when the timer is finished
        |            The nickname of the timer will be passed in if a callback is made (defaults to None)

    """

    def __init__(self, timeInSeconds, nickname=None, callBack=None):
        self.timeInSeconds = timeInSeconds
        self.nickname = nickname
        self.callBack = callBack
        self.savedSecondsElapsed = 0.0
        self.running = False
        self.paused = False
        self.pauseCounter = 0  # counts how many calls to pause without a resume

    def start(self, newTimeInSeconds=None):
        """Start the timer running (starts at zero).
        Allows you to optionally specify a different amount of time.

        Optional keyword parameter:
        | newTimeInSeconds - a new duration for the timer (integer or float, default None)

        """
        if newTimeInSeconds is not None:
            self.timeInSeconds = newTimeInSeconds
        self.running = True
        self.startTime = time.time()
        self.paused = False
        self.timePaused = None
        self.pauseCounter = 0

    def update(self):
        """Call this in every frame to update the timer

        Returns:
           |   False - most of the time
           |   True - when the timer is finished
           |          (you can use this indication, or set up a callback)

        """
        if not self.running:
            return False
        self.savedSecondsElapsed = time.time() - self.startTime
        if self.savedSecondsElapsed < self.timeInSeconds:
            return False  # running but hasn't reached limit

        else:  # timer has finished
            self.running = False
            if self.callBack is not None:
                self.callBack(self.nickname)

            return True  # True here means that the timer has ended

    def getTime(self):
        """ Call this if you want to know how much has elapsed

        Returns:
           |   0 - if the Timer is not running
           |   seconds elapsed since start, as a float

        """
        if self.running or self.paused:
            self.savedSecondsElapsed = time.time() - self.startTime

        return self.savedSecondsElapsed

    def pause(self):
        """Pauses the timer"""
        self.pauseCounter = self.pauseCounter + 1
        self.timePaused = time.time()
        self.paused = True

    def resume(self):
        """Resumes the timer after a pause"""
        if self.pauseCounter == 0:
            print('Warning - called resume timer but the timer is not paused ... ignored')
        else:
            self.pauseCounter = self.pauseCounter -1
        if self.pauseCounter != 0:
            return  # don't resume

        # OK to resume
        pauseTime = time.time() - self.timePaused
        self.secondsStart = self.secondsStart + pauseTime
        self.paused = False

    def stop(self):
        """Stops the timer"""
        self.getTime()  # remembers final self.savedSecondsElapsed
        self.running = False
        self.paused = False
        self.pauseCounter = 0
