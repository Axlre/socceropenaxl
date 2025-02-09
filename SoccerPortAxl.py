#control de ingenieria para porterias by Axelinsano
import sensor, image, time, math, lcd

#Definir valores para calculos por tamano de camara para obtener el centro de la misma
x1=160
y1=120
x2=65
y2=0

#Esto no le muevas o te lleva la verga:
lcd.init(freq=15000000)
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)

angle = 0 #Iicializa angulo

#Variables de deteccion de Color Amarillo y Azul:
Dazul = [(32, 100, -128, -8, 27, 125)]
Damarillo = [(32, 100, -128, -8, 27, 125)]

#Funcion de limite de valores de motores
def constrain(val, min_val, max_val) =>
    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

while(True):
    img = sensor.snapshot()
    amarillo = img.find_blobs(Damarillo,pixels_threshold=20)
    amarillo = img.find_blobs(Damarillo,pixels_threshold=20)

    #Calculos de Control
    anguloPorteria = angle;
    convertedAngle = (anguloPorteria + 180) % 360 - 180;
    errorPorteria = -convertedAngle;
    kp = 6;
    up = errorPorteria * kp;


    #Calculos de simulacion de movimientos
    a = constrain(255-up, -255, 255);
    b = constrain(255+up, -255, 255);
    c = constrain(255+up, -255, 255);
    d = constrain(255-up, -255, 255);

    #Ver simulacion de movimientos de motores
    print("a: "+ (str(a)))
    print("b: "+ (str(b)))
    print("c: "+ (str(c)))
    print("d: "+ (str(d)))

    #BUSQUEDA DE PORTERIAS; COMENTAR LA QUE NO SE VAYA A USAR
    #Busqueda de porteria amarilla
    if amarillo:
        amarillo = max(amarillo, key=lambda b: b.pixels())
        img.draw_cross(amarillo.cx(),amarillo.cy(),(255,255,255),25,1)
        img.draw_rectangle(amarillo.x(), amarillo.y(), amarillo.w(), amarillo.h(), (255,0,0), 4, False)
        x2 = amarillo.cx()
        y2 = amarillo.cy()
        img.draw_arrow(x1, y1, x2, y2, (255, 255, 255), 25, 1)
        img.draw_string(x2 + int(amarillo.w()/2),y2, str(angle), color=(255,0,0), scale = 3)
        angle= int(math.degrees(math.atan2( x1-x2,y1-y2 )))

    #Busqueda de porteria azul (Sin probar xd)
    if azul:
        azul = max(azul, key=lambda b: b.pixels())
        img.draw_cross(azul.cx(),azul.cy(),(255,255,255),25,1)
        img.draw_rectangle(azul.x(), azul.y(), azul.w(), azul.h(), (255,0,0), 4, False)
        x2 = azul.cx()
        y2 = azul.cy()
        img.draw_arrow(x1, y1, x2, y2, (255, 255, 255), 25, 1)
        img.draw_string(x2 + int(azul.w()/2),y2, str(angle), color=(255,0,0), scale = 3)
        angle= int(math.degrees(math.atan2( x1-x2,y1-y2 )))



    #print(angle)
    #print(dist)
    #uart.write(str(angle)+ "," +(str(dist)+ "\n"))




