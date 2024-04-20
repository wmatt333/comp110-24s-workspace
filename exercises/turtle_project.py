"""Builds a picture of space including the sun, stars, and planets.
For part 7 I broke my draw_planet function into a planet_color function
and broke my draw_sunrays function into a find_radius function.
For part 8 I used the circle function for most of my shapes and
also used the bgcolor function to change the color of my background."""


__author__ = "730544766"


from turtle import Turtle, colormode, done 
colormode(255)


def main(fred: Turtle) -> None:
    """Changes the speed and background color of my picture and then calls all of the functions below it to create the whole picture."""
    fred.speed(100)
    fred.hideturtle()
    fred.screen.bgcolor("black")
    draw_sun(fred, 400, -400)
    draw_sunrays(fred, 420, -400)
    draw_planet(fred, -500, 0, 45)
    draw_planet(fred, 300, 100, 100)
    draw_planet(fred, -50, 250, 9)
    draw_star(fred, -250, 300)
    draw_star(fred, 500, 75)
    done()


def draw_planet(fred: Turtle, x: float, y: float, radius: float) -> None:
    """Uses the circle function to create planets of different size and color and places them at different points in the picture."""
    fred.color("white")
    fred.fillcolor(planet_color(radius))  # uses the radius to determine the color
    fred.penup()
    fred.goto(x, y)
    fred.setheading(0.0)
    fred.pendown()
    fred.begin_fill()
    fred.circle(radius)
    fred.end_fill()


def planet_color(size: float) -> str:
    """Returns a color for the planet based on the planet's size."""
    if size < 10:
        return "red"
    elif size < 50:
        return "green"
    else:
        return "blue"


def draw_star(fred: Turtle, x: float, y: float) -> None:
    """Uses a while loop at specific angles to create a star at different places in my picture."""
    fred.color("white")
    fred.fillcolor("yellow")
    fred.penup()
    fred.goto(x, y)
    fred.setheading(0.0)
    fred.pendown()
    fred.begin_fill()
    idx: int = 0
    while idx < 5:
        fred.forward(75)
        fred.right(120)
        fred.forward(75)   
        fred.right(72 - 120)
        idx += 1
    fred.end_fill()


def draw_sun(fred: Turtle, x: float, y: float) -> None:
    """Makes a large yellow semi circle at the bottom of the screen."""
    fred.color(0, 0, 0)
    fred.fillcolor(255, 254, 19)
    fred.penup()
    fred.goto(x, y)
    fred.setheading(90)
    fred.pendown()
    fred.begin_fill()
    fred.circle(400, 180)  # create a circle of size 400 and stops after 180 degrees
    fred.end_fill()


def draw_sunrays(fred: Turtle, x: float, y: float) -> None:
    """Creates larger, hallow semi circles around my sun to act as rays  and uses the find_radius function to properly scale them."""
    fred.pencolor("yellow")
    fred.setheading(90)
    fred.width(3)
    n: int = 0
    while n < 3:
        fred.penup()
        fred.goto(x, y)
        fred.pendown()
        fred.circle(find_radius(n))  # finds the radius of the next ray
        n += 1
        x += 20


def find_radius(n: float) -> float:
    """Increases the radius of the next ray using recursion so they won't  overlap.""" 
    if n == 0:
        return 420
    else:
        return find_radius(n - 1) * 1.05


if __name__ == "__main__":
    fred: Turtle = Turtle()
    main(fred)