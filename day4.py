class Guard:
    def __init__(self, id):
        self.id = id
        self.minutesAsleep = {}
        for x in range(60):
            self.minutesAsleep[x] = 0
    def getMinuteMostAsleep(self):
        maxMinute = -1
        max = 0
        for x in self.minutesAsleep:
            if self.minutesAsleep[x] > max:
                max = self.minutesAsleep[x]
                maxMinute = x
        return maxMinute
    def getTotalMinutesAsleep(self):
        total = 0
        for x in self.minutesAsleep:
            total += self.minutesAsleep[x]
        return total

class Duration:
    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute
    def getMinutes():
        return (day * 24 * 60 + hour * 60 + minute)

class Time:
    def __init__(self, year, month, day, hour, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
    def printTime(self):
        print(self.year, end="")
        print("-", end="")
        print(self.month, end="")
        print("-", end="")
        print(self.day, end="")
        print(" ", end="")
        print(self.hour, end="")
        print(":", end="")
        print(self.minute)
    def __gt__(self, rhs):
        minDiff = self.minute - rhs.minute
        hourDiff = self.hour - rhs.hour
        dayDiff = self.day - rhs.day
        if minDiff < 0:
            minDiff += 60
            hourDiff -= 1
        if self.year > rhs.year:
            return True
        elif self.year < rhs.year:
            return False
        else:
            if self.month > rhs.month:
                return True
            elif self.month < rhs.month:
                return False
            else:
                if dayDiff > 0:
                    return True
                elif dayDiff < 0:
                    return False
                else:
                    if hourDiff > 0:
                        return True
                    elif hourDiff < 0:
                        return False
                    else:
                        if minDiff > 0:
                            return True
                        elif minDiff < 0:
                            return False
                        else:
                            print("same time")

input = {}
file = open("input/day4.txt")
for line in file:
    timeContent = line.split("] ")
    time = Time(int(timeContent[0][1:5]), int(timeContent[0][6:8]), int(timeContent[0][9:11]), int(timeContent[0][12:14]), int(timeContent[0][15:]))
    if timeContent[1][0:5] == "Guard":
        guardInfo = timeContent[1].split(" ")
        input[time] = int(guardInfo[1][1:])
    elif timeContent[1][0:5] == "wakes":
        input[time] = -1
    else:
        input[time] = -2
file.close()
guardsOnShift = []
guardsList = {}
timeBefore = 0
for key in sorted(input):
    if input[key] > 0:
        guardsOnShift.append(input[key])
        print("Added Guard ", end="")
        print(input[key])
    elif input[key] == -2:
        timeBefore = key.minute
        print("Fell asleep at ", end="")
        print(key.minute)
    else:
        guardOnDuty = guardsOnShift.pop()
        print(key.minute - timeBefore)
        if guardOnDuty in guardsList:
            for x in range(timeBefore, key.minute):
                guardsList[guardOnDuty].minutesAsleep[x] += 1
        else:
            guardsList[guardOnDuty] = Guard(guardOnDuty)
            for x in range(timeBefore, key.minute):
                guardsList[guardOnDuty].minutesAsleep[x] += 1
        guardsOnShift.append(guardOnDuty)
maxGuard = 0
maxMinutes = 0
for guardID in guardsList:
    if guardsList[guardID].getTotalMinutesAsleep() > maxMinutes:
        maxMinutes = guardsList[guardID].getTotalMinutesAsleep()
        maxGuard = guardID
minuteMostAsleepOfMax = guardsList[maxGuard].getMinuteMostAsleep()
print(maxGuard*minuteMostAsleepOfMax) # Part A
