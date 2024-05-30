from turtle import Turtle, Screen, colormode;
import random

jym = Turtle();
jym.shape("turtle"); #shape es el icono que va hacer tortuga
jym.color("navy");
colormode(255);

# generate random RGB colors
def random_color():
    r = random.randint(0, 255);
    g = random.randint(0, 255);
    b = random.randint(0, 255);
    return (r, g, b);

jym.speed("fastest");
for _ in range(360):
    jym.color(random_color());
    jym.circle(100);
    jym.setheading(jym.heading() + 1);



screen = Screen();
screen.exitonclick();