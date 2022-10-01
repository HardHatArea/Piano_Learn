import random
import turtle
import scales

screen = turtle.Screen()
image = "Piano.gif"
screen.addshape(image)
turtle.shape(image)

Y_FLOOR_WHITE_KEY = -182
Y_FLOOR_BLACK_KEY = -25
Y_CEILING = 180
Y_NOTENAME_LOCATION = 74

def get_mouse_click_coor_sharp_key(x, y):
    if -494 < x < -446 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-476, Y_NOTENAME_LOCATION, 'C', degree)
    if -443 < x < -411 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-435, Y_NOTENAME_LOCATION, 'C#', degree)
    if -407 < x < -377 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-397, Y_NOTENAME_LOCATION, 'D', degree)
    if -372 < x < -341 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-364, Y_NOTENAME_LOCATION, 'D#', degree)
    if -337 < x < -289 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-319, Y_NOTENAME_LOCATION, 'E', degree)
    if -283 < x < -236 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-261, Y_NOTENAME_LOCATION, 'F', degree)
    if -233 < x < -200 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-224, Y_NOTENAME_LOCATION, 'F#', degree)
    if -196 < x < -165 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-185, Y_NOTENAME_LOCATION, 'G', degree)
    if -161 < x < -131 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-153, Y_NOTENAME_LOCATION, 'G#', degree)
    if -127 < x < -94 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-115, Y_NOTENAME_LOCATION, 'A', degree)
    if -90 < x < -60 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-82, Y_NOTENAME_LOCATION, 'A#', degree)
    if -55 < x < 8 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-41, Y_NOTENAME_LOCATION, 'B', degree)

def get_mouse_click_coor_flat_key(x, y):
    if -494 < x < -446 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-476, Y_NOTENAME_LOCATION, 'C', degree)
    if -443 < x < -411 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-435, Y_NOTENAME_LOCATION, 'Db', degree)
    if -407 < x < -377 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-397, Y_NOTENAME_LOCATION, 'D', degree)
    if -372 < x < -341 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-364, Y_NOTENAME_LOCATION, 'Eb', degree)
    if -337 < x < -289 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-319, Y_NOTENAME_LOCATION, 'E', degree)
    if -283 < x < -236 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-261, Y_NOTENAME_LOCATION, 'F', degree)
    if -233 < x < -200 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-224, Y_NOTENAME_LOCATION, 'Gb', degree)
    if -196 < x < -165 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-185, Y_NOTENAME_LOCATION, 'G', degree)
    if -161 < x < -131 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-153, Y_NOTENAME_LOCATION, 'Ab', degree)
    if -127 < x < -94 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-115, Y_NOTENAME_LOCATION, 'A', degree)
    if -90 < x < -60 and Y_FLOOR_BLACK_KEY < y < Y_CEILING:
        write_notename(-82, Y_NOTENAME_LOCATION, 'Bb', degree)
    if -55 < x < 8 and Y_FLOOR_WHITE_KEY < y < Y_CEILING:
        write_notename(-41, Y_NOTENAME_LOCATION, 'B', degree)

def write_notename(x, y, notename, degree):
    if (notename == degree):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        if len(notename) > 1:
            t.color('white')
        t.write(notename, font=("Arial", 12, "bold"))
        screen.onclick(clear_screen)

def clear_screen(x,y):
    screen.clear()
    screen.addshape(image)
    turtle.shape(image)
    new_question()

def new_question():
    global degree
    random_key = random.choice(list(scales.keys)) #choose random key
    random_key_letter = random_key[0]
    mode_name, mode_number = random.choice(list(scales.mode.items())) #choose random mode and it's value (i.e ionian->0)
    degree = random.choice(list(random_key[mode_number]))
    degree_letter = random_key[mode_number]
    turtle.title(f"What is the {degree} of the {mode_name} mode in the key of {random_key_letter['first']}")
    degree = degree_letter[degree] #change degree from string to notename
    if '#' in degree:
        turtle.onscreenclick(get_mouse_click_coor_sharp_key)
    else:
        turtle.onscreenclick(get_mouse_click_coor_flat_key)

new_question()
turtle.mainloop()
