import pygame
from turtle import *
color('red','yellow')
begin_fill()
speed(0.2)
while True:
    forward(200)
    left(160)
    if abs(pos()) < 1:
        break
    
right(180)
forward(300)

end_fill()
done()
