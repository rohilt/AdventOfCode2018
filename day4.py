class Guard:
    def __init__(self, id):
        self.id = id
        self.minutesAsleep = {}
        for x in range(60):
            self.minutesAsleep[x] = 0
    def getMinuteMostAsleep():
        maxMinute = -1
        max = 0
        for x in minutesAsleep:
            if minutesAsleep[x] > max:
                max = minutesAsleep[x]
                maxMinute = x
        return maxMinute

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
