import pygame
import random
import sys
import os

pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
GRIS = (100, 100, 100)

ANCHO = 800
ALTO = 600
TAMANO_BLOQUE = 20
VELOCIDAD = 10

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Snake con Sonido')
reloj = pygame.time.Clock()

try:
    
    pygame.mixer.music.load("menu_music.mp3") 
    pygame.mixer.music.set_volume(0.5)
    
    
    sonido_comer = pygame.mixer.Sound("comer.wav")  
    sonido_comer.set_volume(0.7)
    
    
    sonido_game_over = pygame.mixer.Sound("game_over.wav")  
    sonido_game_over.set_volume(0.7)
    
    sonidos_disponibles = True
except:
    print("Advertencia: No se pudieron cargar los archivos de sonido.")
    print("El juego funcionará sin sonido.")
    sonidos_disponibles = False

def mostrar_texto(texto, tamaño, x, y, color=BLANCO):
    fuente = pygame.font.SysFont(None, tamaño)
    texto_surface = fuente.render(texto, True, color)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    pantalla.blit(texto_surface, texto_rect)
    return texto_rect

def menu_principal():
    if sonidos_disponibles:
        pygame.mixer.music.play(-1)  
    
    esperar = True
    while esperar:
        pantalla.fill(NEGRO)
        mostrar_texto("SNAKE GAME", 50, ANCHO//2, ALTO//4)
        mostrar_texto("Presiona cualquier tecla para jugar", 20, ANCHO//2, ALTO//2)
        mostrar_texto("Controles: Flechas para mover", 20, ANCHO//2, ALTO//2 + 30)
        mostrar_texto("Pulsa ESC durante el juego para salir", 20, ANCHO//2, ALTO//2 + 60)
        mostrar_texto("Pulsa P para pausar", 20, ANCHO//2, ALTO//2 + 90)
        
        pygame.display.update()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                if sonidos_disponibles:
                    pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if sonidos_disponibles:
                        pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                
                if sonidos_disponibles:
                    pygame.mixer.music.stop()
                esperar = False  
        reloj.tick(15)

def mostrar_puntuacion(puntos):
    fuente = pygame.font.SysFont(None, 30)
    texto = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    pantalla.blit(texto, [10, 10])

def juego():
    x_serpiente = ANCHO // 2
    y_serpiente = ALTO // 2
    x_cambio = 0
    y_cambio = 0
    cuerpo_serpiente = []
    largo_serpiente = 1

    
    comida_x = round(random.randrange(TAMANO_BLOQUE, ANCHO - TAMANO_BLOQUE) / TAMANO_BLOQUE) * TAMANO_BLOQUE
    comida_y = round(random.randrange(TAMANO_BLOQUE, ALTO - TAMANO_BLOQUE) / TAMANO_BLOQUE) * TAMANO_BLOQUE

    game_over = False
    pausa = False

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    game_over = True
                if evento.key == pygame.K_p:
                    pausa = not pausa
                if not pausa:
                    if evento.key == pygame.K_LEFT and x_cambio != TAMANO_BLOQUE:
                        x_cambio = -TAMANO_BLOQUE
                        y_cambio = 0
                    elif evento.key == pygame.K_RIGHT and x_cambio != -TAMANO_BLOQUE:
                        x_cambio = TAMANO_BLOQUE
                        y_cambio = 0
                    elif evento.key == pygame.K_UP and y_cambio != TAMANO_BLOQUE:
                        y_cambio = -TAMANO_BLOQUE
                        x_cambio = 0
                    elif evento.key == pygame.K_DOWN and y_cambio != -TAMANO_BLOQUE:
                        y_cambio = TAMANO_BLOQUE
                        x_cambio = 0
        
        if pausa:
            mostrar_texto("PAUSA", 50, ANCHO//2, ALTO//2)
            pygame.display.update()
            continue
            
        x_serpiente += x_cambio
        y_serpiente += y_cambio
        
        if x_serpiente >= ANCHO or x_serpiente < 0 or y_serpiente >= ALTO or y_serpiente < 0:
            if sonidos_disponibles:
                sonido_game_over.play()
            game_over = True
            
        pantalla.fill(NEGRO)
        
        pygame.draw.rect(pantalla, GRIS, [0, 0, ANCHO, ALTO], 2)
        
        pygame.draw.rect(pantalla, ROJO, [comida_x, comida_y, TAMANO_BLOQUE, TAMANO_BLOQUE])

        cabeza_serpiente = [x_serpiente, y_serpiente]
        cuerpo_serpiente.append(cabeza_serpiente)
        
        if len(cuerpo_serpiente) > largo_serpiente:
            del cuerpo_serpiente[0]

        for bloque in cuerpo_serpiente[:-1]:
            if bloque == cabeza_serpiente:
                if sonidos_disponibles:
                    sonido_game_over.play()
                game_over = True

        for bloque in cuerpo_serpiente:
            pygame.draw.rect(pantalla, VERDE, [bloque[0], bloque[1], TAMANO_BLOQUE, TAMANO_BLOQUE])

        mostrar_puntuacion(largo_serpiente - 1)
        pygame.display.update()

        if x_serpiente == comida_x and y_serpiente == comida_y:

            if sonidos_disponibles:
                sonido_comer.play()
                
            comida_x = round(random.randrange(TAMANO_BLOQUE, ANCHO - TAMANO_BLOQUE) / TAMANO_BLOQUE) * TAMANO_BLOQUE
            comida_y = round(random.randrange(TAMANO_BLOQUE, ALTO - TAMANO_BLOQUE) / TAMANO_BLOQUE) * TAMANO_BLOQUE
            largo_serpiente += 1

        reloj.tick(VELOCIDAD)
    
    pantalla.fill(NEGRO)
    mostrar_texto("GAME OVER", 50, ANCHO//2, ALTO//2 - 50)
    mostrar_texto(f"Puntuación: {largo_serpiente - 1}", 30, ANCHO//2, ALTO//2)
    mostrar_texto("Presiona cualquier tecla para volver al menú", 20, ANCHO//2, ALTO//2 + 50)
    pygame.display.update()
    
    esperar = True
    while esperar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                esperar = False

while True:
    menu_principal()
    juego()