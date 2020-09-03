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


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here

    t.pendown()
    t.pencolor("red")
    #t.setpos(-100, -90)
    #t.forward(10)

    #print(t.heading())

    t.setpos(-30, 17)
    #t.right(math.degrees(math.atan(1)))
    print(t.pos())
    t.circle(10)

    t.radians()

    # read file
    with open('data/irma.csv') as reader_obj:
        csv_reader = reader(reader_obj)
        header = next(csv_reader)
        start_pos = next(csv_reader)

        t.setpos(float(start_pos[3]), float(start_pos[2]))

        print(t.START_ORIENTATION)

        prev_pos = start_pos
        for row in csv_reader:
            dx = float(row[3]) - float(prev_pos[3])
            dy = float(row[2]) - float(prev_pos[2])
            dist = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

            t.right(math.radians(270) - (math.atan(dy / dx)) + t.heading())
            t.forward(dist)
            print(t.pos())
            prev_pos = row

        print(t.pos())

if __name__ == "__main__":
    irma()
