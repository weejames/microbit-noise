from microbit import *
import music
import math

# global vars - boo!
high_range = False
low_range = False
default_range = True

# for frequency range
upper_bound = 1000
lower_bound = -980

music_duration = 50
pause_duration = 50

max_duration = 200
min_duration = 100

while True:
    # handle inputs
    if button_a.is_pressed():
        low_range = True
        high_range = False
        default_range = False
    elif button_b.is_pressed():
        low_range = False
        high_range = True
        default_range = False
    else:
        low_range = False
        high_range = False
        default_range = True
     
    # hook up display to show current option
    if low_range == True:
        display.show(Image.CLOCK9)
    elif high_range == True:
        display.show(Image.CLOCK3)
    elif default_range == True:
        display.show(Image.CLOCK12)
    
    # get accelerometer position
    acc_x = accelerometer.get_x()
    
    # normalise accelerometer range
    if acc_x >= upper_bound:
        acc_x = upper_bound
    elif acc_x <= lower_bound:
        acc_x = lower_bound
    
    wide_frequency = acc_x + upper_bound
    
    range_factor = 2000 * 0.33
    
    low_range = True
    
    # move frquency into correct range
    if low_range == True:
        frequency = int( (wide_frequency * 0.33) + ( 0 * range_factor ) )
    elif high_range == True:
        frequency = int( (wide_frequency * 0.33) + ( 2 * range_factor ) )
    else:
        frequency = int( (wide_frequency * 0.33) + ( 1 * range_factor ) )
    
    
    # calculate a good duration
    acc_y = accelerometer.get_y()
    
    # normalise Y value (duration)
    if acc_y >= upper_bound:
        acc_y = upper_bound
    elif acc_y <= lower_bound:
        acc_y = lower_bound
    
    
    duration = acc_y + upper_bound
    div_factor = 2000 / max_duration
    
    duration = math.ceil(duration / div_factor)
    music_duration = max(duration, min_duration)
    
    
    gesture = accelerometer.current_gesture()
    
    if gesture == "face down":
        music.pitch(frequency, music_duration)
    
    