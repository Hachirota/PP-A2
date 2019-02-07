class Clock:

    def __init__(self, hr=00, min=00, sec=00):
        self.hours = hr
        self.minutes = min
        self.seconds = sec

    def __str__(self):
        return "The time is {:02d}:{:02d}:{:02d}".format(self.hours,self.minutes,self.seconds)

    def __repr__(self):
        return self.__str__()

    def strUpdate(self, input):
        self.hours = int(input[:2])
        self.minutes = int(input[3:5])
        self.seconds = int(input[6:])

    def printClock(self):
        self.__str__()

    def addClocks(self, clockB):
        outputHours = 00
        outputMinutes = 00
        outputSeconds = 00

        outputSeconds = self.seconds + clockB.seconds
        if outputSeconds > 59:
            outputMinutes += 1
            outputSeconds = outputSeconds - 60

        outputMinutes = outputMinutes + self.minutes + clockB.minutes
        if outputMinutes > 59:
            outputHours += 1
            outputMinutes = outputMinutes - 60

        outputHours = outputHours + self.hours + clockB.hours
        if outputHours > 23:
            outputHours = 23

        return Clock(outputHours, outputMinutes, outputSeconds)

def main():
    clocka = Clock(23,22,12)
    clockb = Clock(23,55,55)
    clockb.strUpdate("00:00:60")

    clockc = clocka.addClocks(clockb)

    print(clockc.__str__())


if __name__ == '__main__':
    main()



