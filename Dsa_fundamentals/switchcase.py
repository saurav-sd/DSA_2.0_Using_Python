class SwitchCase:
    def whichDay(self, day):
        match day:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
            case _:
                return "Invalid day"
            


day = int(input("Enter the day number (1-7): "))
switch_case = SwitchCase()
day_name = switch_case.whichDay(day)
print(f"The day is: {day_name}")

