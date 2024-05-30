import pygame

screen = pygame.display.set_mode((400,500))
clock= pygame.time.Clock()
activo=True

c_x=200
c_y=250

velocidad_x=2

while activo:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         activo= False
    
    if (c_x>400 or c_x<=0):
       velocidad_x*=-1




    c_x+=velocidad_x
#fill le dice dibuje
    screen.fill((255,255,255))
#dibuja una linea o circulo, surface donde voy a dibujar , color,centro,radio
    pygame.draw.circle(screen,(255,0,0),(c_x,c_y),40)
    pygame.draw.rect(screen,(0,255,0),(100,100,45,100))



    #flip refrescar la pantalla
    pygame.display.flip()
    #para manejar la velocidad de los frames
    clock.tick(180)