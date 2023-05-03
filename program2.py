#create a class Time with validations. Create two instances and print them.
class Time:
    def __init__(self, hour, minute, second):
        self.hour = self.validate_hour(hour)
        self.minute = self.validate_minute(minute)
        self.second = self.validate_second(second)

    def validate_hour(self, hour):
        if hour < 0 or hour > 23:
            raise ValueError("Hour should be between 0 and 23")
        return hour

    def validate_minute(self, minute):
        if minute < 0 or minute > 59:
            raise ValueError("Minute should be between 0 and 59")
        return minute

    def validate_second(self, second):
        if second < 0 or second > 59:
            raise ValueError("Second should be between 0 and 59")
        return second

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"


# create two instances of the Time class
time1 = Time(12, 30, 45)
time2 = Time(23, 59, 59)

# print the instances
print(time1)  # output: 12:30:45
print(time2)  # output: 23:59:59
