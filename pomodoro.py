# Simple Pomodoro Timer
# Written by Ben Smart

import time, math, winsound
from datetime import datetime


class Timer:
    #Work - the number of minutes spent working per hr
    #Breaks - the number of breaks per hr
    #Cycles - the number of pomodori (work/rest cycles) before a longer break
    #reward_multiplier - used to calculate how long a long break is
    #   long_break = ceil(rest time * reward_muliplier)
    def __init__(self, work=50, breaks=2, cycles=4, reward_multiplier=2):
        self.work = work
        self.rest = 60 - work
        self.breaks = breaks
        self.work_time = self.work / self.breaks
        self.rest_time = self.rest / self.breaks

        self.cycles = cycles
        self.long_break = math.ceil(self.rest_time * reward_multiplier)
        
    def timestamp(self):
        return datetime.now().strftime("%H:%M:%S")
    
    def start(self):
        c_major = (261*2, 329*2, 392*2, 523*2) #For the break time noise
        a_minor = (330, 260, 220) #for the work time noise
        print(f"[{self.timestamp()}] Timer Started.  Begin working")
        #first initial break outside of the loop
        #Main loop
        while True:
            for i in range(self.cycles):
                time.sleep(self.work_time * 60)

                #rest
                print(f"[{self.timestamp()}] Work timer completed. Take a break!")

                #Play a noise (C major chord)
                for freq in c_major:
                    winsound.Beep(freq, 250)
                #delay
                time.sleep(self.rest_time * 60)

                #work
                print(f"[{self.timestamp()}] Break timer completed. GET BACK TO WORK!")
                #Play a noise (A minor chord)
                for freq in a_minor:
                    winsound.Beep(freq, 250)  

                if i != self.cycles - 1:          
                    print(f"[{self.timestamp()}] {self.cycles - i - 1} more cycles until a {self.long_break} minute break")


            for freq in c_major:
                winsound.Beep(freq, 250)


            print(f"[{self.timestamp()}] Time for a {self.long_break} minute break!")
            time.sleep(self.long_break * 60)
            print(f"[{self.timestamp()}] Long break completed.  Back to work!")
    
def absint_input(prompt, default):
    #Check for invalid input
    valid = False
    while not valid:
        try:
            work_time = input(prompt)
            if work_time == '': return default
            valid = True
            return int(work_time)
        except ValueError:
            print('Invalid option, try again')


def main():
    print("=================================================")
    print("Welcome to Lock-In: a Pomodoro timer\n")
    print("Written by Ben Smart")

    work_time = absint_input("How many minutes per hour would you like to work (default 50)? ", 50)
    #Clamp value between 1 and 60
    work_time = 1 if work_time <= 0 else 60 if work_time > 60 else work_time

    #Collect number of breaks
    print()
    breaks = absint_input("How many breaks would you like per hour (default 2)? ", 2)
    
    cycles = absint_input("How many work/like cycles would you like until a longer break (default 4)? ", 4)

    timer = Timer(work_time, breaks, cycles)

    print(f"You will work for {timer.work_time:.2f} minutes at a time, followed by a {timer.rest_time:.2f} minute break")
    print(f"After {cycles} cycles you'll take a {timer.long_break} minute break")


    input("Press enter to start, press Ctrl+C to stop")
    try:
        timer.start()
    except KeyboardInterrupt:
        print("Thanks for using Lock-in, Have a great day!")

if __name__ == '__main__':
    main()
