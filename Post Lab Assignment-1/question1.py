


from sense_hat import SenseHat
from time import sleep
import sys

sense=SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
x=3
y=5
temperature = sense.get_temperature()
sense.set_pixel(x,y,(255,0,0))

temperature = round(temperature,1)
msg = "temperature:" + str(temperature)
while True:
    for event in sense.stick.get_events():
        print(event.direction,event.action)
        if event.action =="pressed":
            if event.direction=="middle":
                #sense.show_message(msg,text_colour = blue,back_colour = yellow,scroll_speed = 0.05)
                #sleep(2)
                sense.clear()
                sys.exit()
                
            elif event.direction == "up":
                sense.clear()
                if y >0:
                    y-=1
                    sense.set_pixel(x,y,(255,0,0))
            
            elif event.direction == "down":
                sense.clear()
                if y <7:
                    y+=1
                    sense.set_pixel(x,y,(255,0,0))
            elif event.direction == "right":
                sense.clear()
                if x <7:
                    x+=1
                    sense.set_pixel(x,y,(255,0,0))
            
            elif event.direction == "left":
                sense.clear()
                if x >0:
                    x-=1
                    sense.set_pixel(x,y,(255,0,0))
            
         
         
            
