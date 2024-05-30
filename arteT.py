from turtle import *
from turtle import Turtle, Screen, colormode;
import random


tortuga = Turtle()
tortuga.shape("turtle") #shape es el icono que va hacer tortuga
tortuga.color("navy")
colormode(255)
Screen = tortuga.screen #pantalla


# Obtener el tamaño de la ventana
Screen.setup(width=800, height=600) 
ancho_pantalla = Screen.window_width()
alto_pantalla = Screen.window_height()
print(f"El tamaño actual de la ventana es: {ancho_pantalla} x {alto_pantalla} píxeles")


# generate random RGB colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tortuga.speed(10) #velocidad de dibujo

# Función para dibujar y rellenar un círculo
def dibujar_circulo_relleno(tortuga, radio):
    tortuga.begin_fill()
    tortuga.circle(radio)
    tortuga.fillcolor(random_color()) # Color del relleno
    tortuga.end_fill()


# parametros del circulo
radio = 10
espacio_entre_circulos = 20

#Partida inicial
def pinicio():
    tortuga.penup()       # Levantar el lápiz para mover la tortuga sin dibujar
    tortuga.goto(-380, -280)  # Mover la tortuga a la posición (-200, -200)
    tortuga.pendown()     # Bajar el lápiz para comenzar a dibujar    
    
pinicio()

#efecto de movimiento
def mover(x_m,y_m):
    tortuga.penup()       # Levantar el lápiz para mover la tortuga sin dibujar
    tortuga.goto(x_m,y_m)  # Mover la tortuga a la posición 
    tortuga.pendown()     # Bajar el lápiz para comenzar a dibujar 
      
#Movimientos y dibujo de los circulos
def adelante():
    tortuga.penup()  # Levantar el lápiz para no dibujar mientras se mueve
    tortuga.forward(2 * radio + espacio_entre_circulos)  # Mover a la siguiente posición de adelante
    tortuga.pendown()  # Bajar el lápiz para dibujar el siguiente círculo   
    
def haciatras():
    tortuga.penup()  # Levantar el lápiz para no dibujar mientras se mueve
    tortuga.backward(2 * radio + espacio_entre_circulos)  # Mover a la siguiente posición de atras
    tortuga.pendown()  # Bajar el lápiz para dibujar el siguiente círculo

#limites
limite_derecho = ancho_pantalla // 2 - 30 # Límite derecho
limite_izquierdo = -limite_derecho  # Límite izquierdo
limite_superior = alto_pantalla // 2 - 20  # Límite superior
limite_inferior = -limite_superior  # Límite inferior
direccion = "derecha"  # Dirección inicial
    
while True:
    x, y = tortuga.position()  # Obtiene la posición actual de la tortuga
    dibujar_circulo_relleno(tortuga, radio)
    
    if direccion == "derecha":
        
            adelante()
            
            if x  >= limite_derecho:
                if y  >= limite_superior:
                    break  # Detiene si alcanza el límite superior
                
                mover(x,y+40)
                y += y
                direccion = "izquierda"
                
            else:
                x += x

    elif direccion == "izquierda":
          
            haciatras()
            
            if x <= limite_izquierdo:
                if y >= limite_superior:
                    break  # Detiene si alcanza el límite superior
                
                mover(x,y+40)
                y += y
                direccion = "derecha"
            else:
                x -= x
                ##hola
                #c
    tortuga.pendown()
    Screen.update()  # Actualiza la ventana

Screen.mainloop()