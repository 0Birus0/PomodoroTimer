import tkinter as tk
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        
        # Initial time set for the Pomodoro timer (25 minutes)
        self.minutes = 0
        self.seconds = 5
        self.running = False
        self.is_paused = False
        
        # Label to display the time
        self.timer_label = tk.Label(root, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 48))
        self.timer_label.pack(pady=20)
        
        # Start Button
        self.start_button = tk.Button(root, text="Start", font=("Arial", 14), command=self.start_timer)
        self.start_button.pack(pady=20)
        
        #Stop Button
        self.stop_button = tk.Button(root, text="Pause", font=("Arial", 14), command=self.stop_timer)
        self.stop_button.pack(pady=20)

    
    def stop_timer(self):
        self.running = False

            




    def start_timer(self):
        if self.running == False:
            self.running = True     
            if self.running:
                if self.seconds == 0:
                    if self.minutes > 0:
                        self.minutes -= 1
                        self.seconds = 59

                    else: 
                        self.running = False
            
                else:
                    if self.minutes >= 0:
                        self.seconds -= 1


              

    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.timer_label.config(text=f"{self.minutes:02d}:{self.seconds:02d}")
        self.root.after(1000, self.start_timer)
    

    


if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = PomodoroTimer(root)
    root.mainloop()
