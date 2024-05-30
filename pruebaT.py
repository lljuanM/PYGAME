import turtle
window = turtle.Screen()
window.title("Tortuga Dibujando Círculos")
window.bgcolor("white")

tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(0.2)  # Velocidad máxima
def dibujar_circulos():
    velocidad_x = 50  # Distancia horizontal entre círculos
    incremento_y = 40  # Distancia vertical entre filas
    radio = 15  # Radio de los círculos
    limite_derecho = window.window_width() // 2 - 15  # Límite derecho
    limite_izquierdo = -limite_derecho  # Límite izquierdo
    limite_superior = window.window_height() // 2 - 15  # Límite superior
    limite_inferior = -limite_superior  # Límite inferior

    direccion = "derecha"  # Dirección inicial

    tortuga.penup()
    tortuga.goto(limite_izquierdo, limite_inferior)  # Posiciona la tortuga en la esquina inferior izquierda
    tortuga.pendown()

    while True:
        x, y = tortuga.position()  # Obtiene la posición actual de la tortuga

        # Dibuja un círculo en la posición actual
        tortuga.circle(radio)
        tortuga.penup()

        if direccion == "derecha":
            if x + velocidad_x >= limite_derecho:
                if y + incremento_y >= limite_superior:
                    break  # Detiene si alcanza el límite superior
                y += incremento_y
                direccion = "izquierda"
            else:
                x += velocidad_x

        elif direccion == "izquierda":
            if x - velocidad_x <= limite_izquierdo:
                if y + incremento_y >= limite_superior:
                    break  # Detiene si alcanza el límite superior
                y += incremento_y
                direccion = "derecha"
            else:
                x -= velocidad_x

        tortuga.goto(x, y)  # Actualiza la posición de la tortuga
        tortuga.pendown()

        window.update()  # Actualiza la ventana

dibujar_circulos()
window.mainloop()
