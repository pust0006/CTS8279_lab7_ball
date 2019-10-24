from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
from gfxhat import backlight
import gfxhat
import time
#backlight/ reset
backlight.set_all(140, 0, 0)
gfxhat.lcd.clear()
backlight.show()
gfxhat.lcd.show()
#erases the object
def eraseObject(obj,xx,yy):
    x = xx
    y = yy
    a = 0
    while a <= len(obj) - 1: 
        b = 0 
        while b <= len(obj[a]) - 1:
            p = obj[a][b]
            if p == 1:
                p = 0
            if x == 128 or x == 0 or y == 0 or y == 64:
                break
            lcd.set_pixel(x,y,p)
            x += 1
            b += 1
        x = xx
        y += 1
        a += 1
    lcd.show()
#adjusts the draw point by adding or subtracting the speed
def moveObject(obj,xx,yy,vx,vy):
    xx = xx + vx
    yy = yy + vy
    return xx,yy
#displays objext using the coordinates
def displayObject(obj,xx,yy):  
    x = xx
    y = yy
    a = 0
    while a <= len(obj) - 1: 
        b = 0 
        while b <= len(obj[a]) - 1:
            p = obj[a][b]
            lcd.set_pixel(x,y,p)
            x += 1
            b += 1
        x = xx
        y += 1
        a += 1
    lcd.show()
#checks for collision before drawing and adjusts the speed direction and pixels draw point accordingly
def checkCollision(obj,xx,yy,vx,vy):
    x = xx
    y = yy
    a = 0
    while a <= len(obj) - 1: 
        b = 0 
        while b <= len(obj[a]) - 1:
            x += 1
            b += 1
#changes directions and the coordinate to draw pixels at and returns them
            if y == 63:
                yy -= vy
                vy = vy * -1
                if x == 127:
                    xx -= vx
                    vx = vx * -1
                if x == 1:
                    xx -= vx
                    vx = vx * -1
                return xx,yy,vx,vy
            if y == 1:
                yy -= vy
                vy = vy * -1
                if x == 127:
                    xx -= vx
                    vx = vx * -1
                if x == 1:
                    xx -= vx
                    vx = vx * -1
                return xx,yy,vx,vy
            if x == 127:
                xx -= vx
                vx = vx * -1
                if y == 63:
                    yy -= vy
                    vy = vy * -1
                if y == 1:
                    yy -= vy
                    vy = vy * -1    
                return xx,yy,vx,vy
            if x == 1:
                xx -= vx
                vx = vx * -1
                if y == 63:
                    yy -= vy
                    vy = vy * -1
                if y == 1:
                    yy -= vy
                    vy = vy * -1
                return xx,yy,vx,vy
        x = xx
        y += 1
        a += 1
    return xx,yy,vx,vy
#the object that bounces
obj =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]
#variables for speed and starting coordinate
vx = 5
vy = 5
xx = 12
yy = 12
#draw starting point
displayObject(obj,xx,yy)
#bouncing function
while True:
    time.sleep(0.3)
    eraseObject(obj,xx,yy)
    xx,yy = moveObject(obj,xx,yy,vx,vy)
    xx,yy,vx,vy = checkCollision(obj,xx,yy,vx,vy)
    displayObject(obj,xx,yy)
