import sensor, image, time, math
from pyb import UART
uart = UART(3, 9600)
x1=160
y1=120
x2=65
y2=0
dist = 0
arduino = 0
angle = 0
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

Drnaranja = [(0, 100, -4, 79, 15, 103)]

while(True):
    img = sensor.snapshot()
    naranja = img.find_blobs(DRojo,pixels_threshold=5)
    if rojo:
        rojo = max(naranja, key=lambda b: b.pixels())
        img.draw_cross(naranja.cx(),naranja.cy(),(255,255,255),25,1)
        img.draw_rectangle(naranja.x(), naranja.y(), naranja.w(), naranja.h(), (255,0,0), 4, False)
        x2=naranja.cx()
        y2=naranja.cy()
        img.draw_arrow(x1, y1, x2, y2, (0, 0, 255), 25, 4)
        img.draw_string(x2 + int(naranja.w()/2),y2, str(angle), color=(255,0,0), scale = 3)
        angle= int(math.degrees(math.atan2( x1-x2,y1-y2 )))+180
        dist=int(math.sqrt( (y2-y1)**2+(x2-x1)**2 ))



    #print(angle)
    #print(dist)
    uart.write(str(angle)+ "," +(str(dist)+ "\n"))




