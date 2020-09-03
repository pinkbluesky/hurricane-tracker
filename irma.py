import turtle
from csv import reader
import math

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")


    return (t, wn, map_bg_img)

#todo: add category number; change map location based on hurricane location
# possibly interesting: scrape web and make csv files; scrape news articles for people affected
def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here

    t.radians()
    t.speed('fast')

    # read file
    with open('data/irma.csv') as reader_obj:
        csv_reader = reader(reader_obj)
        header = next(csv_reader)
        start_pos = next(csv_reader)

        t.setpos(float(start_pos[3]), float(start_pos[2]))

        t.left(math.radians(180))

        prev_pos = start_pos
        for row in csv_reader:
            strength = float(row[4])
            if strength >= 157:
                t.pencolor("red")
                t.pensize(5)
            elif strength >= 130:
                t.pencolor("orange")
                t.pensize(4)
            elif strength >= 111:
                t.pencolor("yellow")
                t.pensize(3)
            elif strength >= 96:
                t.pencolor("green")
                t.pensize(2)
            elif strength >= 74:
                t.pencolor("blue")
                t.pensize(1)
            else:
                t.pencolor("white")
                t.pensize(0.5)

            dlong = float(row[3]) - float(prev_pos[3])
            dlat = float(row[2]) - float(prev_pos[2])
            dist = math.sqrt(math.pow(dlong, 2) + math.pow(dlat, 2))

            # moving vertically; only dlat has a value
            if dlong == 0:
                # moving straight down (south)
                if dlat < 0:
                    t.left(t.heading() + math.radians(180))
                # moving north
                else:
                    t.left(t.heading())
            # moving towards quad 2 and 3
            elif dlong < 0:
                t.right(math.radians(270) - math.atan(dlat / dlong) + t.heading() + math.radians(180))
            # 'normal' movement to the right (since atan's range is 90 to -90)
            else:
                t.right(math.radians(270) - math.atan(dlat / dlong) + t.heading())

            t.forward(dist)
            prev_pos = row

if __name__ == "__main__":
    irma()
