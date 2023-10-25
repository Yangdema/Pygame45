import turtle
import time
import random

delay = 0.3

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Catapillar Game by Lhamyang")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates