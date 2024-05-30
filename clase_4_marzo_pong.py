import pygame #Importamos las librerias de pygame
pygame.init()

BLACK=(0,0,0) #Color negro 
WHITE=(255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
size=(800,500) #Tamaño de la pantalla ancho y alto

pantalla=pygame.display.set_mode(size)
clock = pygame.time.Clock() ##para modificar la cantidad de frames o velocidad de ejecucion
#Parametros iniciales del jugador 1

ancho_jugador1 = 20
alto_jugador1 = 100
x_jugador1 = 40
y_jugador1 = size[1]//2-alto_jugador1//2

p1_y_speed = 0

#Parametros iniciales del jugador 2

ancho_jugador2 = 20
alto_jugador2 = 100
x_jugador2 = size[0]-60
y_jugador2 = size[1]//2-alto_jugador2//2

p2_y_speed = 0

#parametros pelota
x_pelota = size[0]//2 -8 
y_pelota = size[1]//2 -6 

pelota_mov_x = 3 
pelota_mov_y = 3

##Terminar del juego
fin_juego=False
while not fin_juego:
    for evento in pygame.event.get(): #Recorre todos los eventos que sucede en la pantalla
        if evento.type==pygame.QUIT: #CAPTURA EL evento x para salir
            fin_juego=True
            
            
#para que se mueva procedemos a capturar los eventos
        if evento.type == pygame.KEYDOWN:
           if evento.key == pygame.K_w:
              p1_y_speed=-3
           if evento.key == pygame.K_s:
              p1_y_speed=3
              
        if evento.type == pygame.KEYUP:
           if evento.key == pygame.K_w:
              p1_y_speed=0
           if evento.key == pygame.K_s:
              p1_y_speed=0
              
        if evento.type == pygame.KEYDOWN:
           if evento.key == pygame.K_UP:
              p2_y_speed=-3
           if evento.key == pygame.K_DOWN:
              p2_y_speed=3
              
        if evento.type == pygame.KEYUP:
           if evento.key == pygame.K_UP:
              p2_y_speed=0
           if evento.key == pygame.K_DOWN:
              p2_y_speed=0
        
    ###animación 
    y_jugador1+= p1_y_speed
    y_jugador2+= p2_y_speed
    
    x_pelota+= pelota_mov_x
    y_pelota+= pelota_mov_y
    
    if x_pelota>size[0]-17 or x_pelota <17:  ###contar un jugador ganando
        pelota_mov_x=0
        pelota_mov_y=0
        
    if y_pelota>size[1]-17 or y_pelota <17:
        pelota_mov_y*=-1
        
    ##-------
    pantalla.fill(BLACK) #Dibujar en la pantalla esta de color negro
    
    ## Área de dibujo
    jugador1=pygame.draw.rect(pantalla,WHITE,(x_jugador1,y_jugador1,ancho_jugador1,alto_jugador1))
    jugador2=pygame.draw.rect(pantalla,BLUE,(x_jugador2,y_jugador2,ancho_jugador2,alto_jugador2))
    pelota=pygame.draw.circle(pantalla,RED,(x_pelota,y_pelota),15)
    #-------------------------
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_mov_x*=-1
    
    
    pygame.display.flip() #El flip lo que hace es refrescar la pantalla
    # y pintamos con lo que hay debajo
    clock.tick(160)
    
    
    
    
    
    
    
    