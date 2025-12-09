# Simple Pomodoro Timer
# Written by Ben Smart

import time, math

class Timer:
    #Work - the number of minutes spent working per hr
    #Rest - the number of minutes spent resting per hr
    #Breaks - the number of breaks per hr
    def __init__(self, work, rest, breaks):
        self.work = work
        self.rest = rest
        self.breaks = breaks
        self.work_time = self.work / self.breaks
        self.rest_time = self.rest / self.breaks

    def start(self):
        print("Timer Started")
        while True:
            time.sleep(self.work_time * 60) 
            print("Work timer completed. BREAK TIME!")
            time.sleep(self.rest_time * 60)
            print("Break timer completed. GET BACK TO WORK!")
    

def main():
    
    work_time = -1    

    #Check for invalid input
    valid = False
    while not valid:
        try:
            work_time = int(input("How many minutes would you like to spend working per hour? "))
            valid = True
        except ValueError:
            print('Invalid option, try again')

    #Clamp value between 1 and 60
    work_time = 1 if work_time <= 0 else 60 if work_time > 60 else work_time

    #Collect number of breaks
    print()
    breaks = 0
    valid = False
    while not valid:
        breaks = input("How many breaks would you like per hour?")
        try:
            breaks = abs(int(breaks))
            valid = True
        except ValueError:
            print("Invalid input")
    
    break_time = 60 - work_time

    timer = Timer(work_time, break_time, breaks)

    print(f"You will work for {timer.work_time} minutes at a time, followed by a {timer.rest_time} minute break")

    input("Press enter to start")
    timer.start()

if __name__ == '__main__':
    main()