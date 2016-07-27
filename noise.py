# Add your Python code here. E.g.
from microbit import *
import math
import music
import microbit

upper_bound = 1000
lower_bound = -980
max_duration = 200

button_a_upper_bound = 500

class NotePlayer:
    def __init__ (self, freq, duration):
        music.pitch(freq, duration)
        sleep(50)

while True:
    acc_x = accelerometer.get_x()
    acc_y = accelerometer.get_y()
    
    # normalise X value (frequency)
    if acc_x >= upper_bound:
        acc_x = upper_bound
    elif acc_x <= lower_bound:
        acc_x = lower_bound
    
    frequency = acc_x + upper_bound
    
    # normalise Y value (duration)
    if acc_y >= upper_bound:
        acc_y = upper_bound
    elif acc_y <= lower_bound:
        acc_y = lower_bound
    
    duration = acc_y + upper_bound
    
    div_factor = 2000 / max_duration
    
    duration = math.ceil(duration / div_factor)
    
    duration = max(duration, 100)

    
    # lower frequency range if a is pressed
    if microbit.button_a.is_pressed():
        frequency_factor = 2000 / button_a_upper_bound
        frequency = math.ceil(frequency / frequency_factor)
    # increased frequency range if b is pressed    
    elif microbit.button_b.is_pressed():
        frequency_factor = 2000 / button_a_upper_bound
        frequency = math.ceil(frequency / frequency_factor) + 1000
    
    
    frequency = (int(frequency / 100)) * 100
    
    duration = 200
    
    print ('freq: ', frequency, ' duration: ', duration)
    
    NotePlayer(frequency, duration)