import RPi.GPIO as GPIO
#useless edit so I can push again

red_front = 13
green_front = 6
blue_front = 27

red_back = 22
green_back = 5
blue_back = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_back,GPIO.OUT)
GPIO.setup(green_back,GPIO.OUT)
GPIO.setup(blue_back,GPIO.OUT)
GPIO.setup(red_front,GPIO.OUT)
GPIO.setup(green_front,GPIO.OUT)
GPIO.setup(blue_front,GPIO.OUT)

#color functions----------------------------------------
def white(red,blue,green):
    GPIO.output(red,GPIO.HIGH)
    GPIO.output(blue,GPIO.HIGH)
    GPIO.output(green,GPIO.HIGH)
def red(red,blue,green):
    GPIO.output(red,GPIO.HIGH)
    GPIO.output(blue,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
def blue(red,blue,green):
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(blue,GPIO.HIGH)
def green(red,blue,green):
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.HIGH)
    GPIO.output(blue,GPIO.LOW)
def yellow(red,blue,green):
    GPIO.output(red,GPIO.HIGH)
    GPIO.output(green,GPIO.HIGH)
    GPIO.output(blue,GPIO.LOW)
def off(location):
	if location == "Front":
		red = red_front
		blue = blue_front
		green = green_front
	if location == "Back":
		red = red_back
		blue = blue_back
		green = green_back
	if location == "Both":
		GPIO.output(red_front,GPIO.LOW)
	    	GPIO.output(green_front,GPIO.LOW)
		GPIO.output(blue_front,GPIO.LOW)
		red = red_back
		blue = blue_back
		green = green_back

	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.LOW)
	GPIO.output(blue,GPIO.LOW)

def set(location,color):
    if location == "Front":
        red = red_front
        blue = blue_front
        green = green_front
    if location == "Back":
        red = red_back
        blue = blue_back
        green = green_back
    if location == "Both":
        GPIO.output(red_front, GPIO.LOW)
        GPIO.output(green_front, GPIO.LOW)
        GPIO.output(blue_front, GPIO.LOW)
        red = red_back
        blue = blue_back
        green = green_back
    GPIO.output(red, GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(blue,GPIO.LOW)

def purple(red,blue,green):
    GPIO.output(red,GPIO.HIGH)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(blue,GPIO.HIGH)
def teal(red,blue,green):
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.HIGH)
    GPIO.output(blue,GPIO.HIGH)


def set(location, color):
    if location == "Front":
        if color == "red":
            red(red_front, blue_front, green_front)
        elif color == "blue":
            blue(red_front, blue_front, green_front)
        elif color == "green":
            green(red_front, blue_front, green_front)
        elif color == "purple":
            purple(red_front, blue_front, green_front)
        elif color == "white":
            white(red_front, blue_front, green_front)
        elif color == "yellow":
            yellow(red_front, blue_front, green_front)
        elif color == "teal":
            teal(red_front, blue_front, green_front)
    elif location == "Back":
        if color == "red":
            red(red_back, blue_back, green_back)
        elif color == "blue":
            blue(red_back, blue_back, green_back)
        elif color == "green":
            green(red_back, blue_back, green_back)
        elif color == "purple":
            purple(red_back, blue_back, green_back)
        elif color == "white":
            white(red_back, blue_back, green_back)
        elif color == "yellow":
            yellow(red_back, blue_back, green_back)
        elif color == "teal":
            teal(red_back, blue_back, green_back)
    elif location == "Both":
        if color == "red":
            red(red_front, blue_front, green_front)
            red(red_back, blue_back, green_back)
        elif color == "blue":
            blue(red_front, blue_front, green_front)
            blue(red_back, blue_back, green_back)
        elif color == "green":
            green(red_front, blue_front, green_front)
            green(red_back, blue_back, green_back)
        elif color == "purple":
            purple(red_front, blue_front, green_front)
            purple(red_back, blue_back, green_back)
        elif color == "white":
            white(red_front, blue_front, green_front)
            white(red_back, blue_back, green_back)
        elif color == "yellow":
            yellow(red_front, blue_front, green_front)
            yellow(red_back, blue_back, green_back)
        elif color == "teal":
            teal(red_front, blue_front, green_front)
            teal(red_back, blue_back, green_back)
