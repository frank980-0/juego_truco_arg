import pygame
import constantes

def mostrar_menu():
    
    fuente = pygame.font.SysFont("Arial", 24)

    boton_jugar = pygame.Rect(constantes.ANCHO_PANTALLA//2 - 100, constantes.ALTO_PANTALLA//2 - 60, 200, 60)
    boton_ranking = pygame.Rect(constantes.ANCHO_PANTALLA//2 - 100, constantes.ALTO_PANTALLA//2 + 20, 200, 60)
    boton_salir = pygame.Rect(constantes.ANCHO_PANTALLA//2 - 100, constantes.ALTO_PANTALLA//2 + 100, 200, 60)

    pygame.display.set_caption("TRUCO") #establece el título de la ventana

# FONDO
    fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA)) #carga y redimensiona la imagen de fondo
# FAVICON
    icono = pygame.transform.scale(constantes.FAVICON, (64, 64)) #redimensiona el icono
    pygame.display.set_icon(icono) #establece el icono de la ventana
# LOGO
    logo = pygame.image.load("pygame/assets/logo/TRUCO.png") #carga el logo
    logo = pygame.transform.scale(logo,(650, 650))
    

    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos() #obtiene la posición del mouse

        if boton_jugar.collidepoint(mouse_x, mouse_y):
            color_jugar = constantes.VERDE

        else:
            color_jugar = constantes.AZUL

        if boton_ranking.collidepoint(mouse_x, mouse_y):
            color_ranking = constantes.VERDE
        else:
            color_ranking = constantes.AZUL

        if boton_salir.collidepoint(mouse_x, mouse_y):
            color_salir = constantes.ROJO

        else:
            color_salir = constantes.AZUL

        constantes.PANTALLA.blit(fondo, (0, 0)) #dibuja el fondo en la pantalla
        constantes.PANTALLA.blit(logo, (constantes.ANCHO_PANTALLA//2 - 325, -160))

        pygame.draw.rect(constantes.PANTALLA, color_jugar, boton_jugar, border_radius= 20)
        pygame.draw.rect(constantes.PANTALLA, color_ranking, boton_ranking, border_radius= 20)
        pygame.draw.rect(constantes.PANTALLA, color_salir, boton_salir, border_radius= 20)

        texto_jugar = fuente.render("JUGAR", True, constantes.BLANCO)
        texto_ranking = fuente.render("RANKING", True, constantes.BLANCO)
        texto_salir = fuente.render("SALIR", True, constantes.BLANCO)
        
        constantes.PANTALLA.blit(texto_jugar, (boton_jugar.x + 67, boton_jugar.y + 15))
        constantes.PANTALLA.blit(texto_ranking, (boton_ranking.x + 60, boton_ranking.y + 18))
        constantes.PANTALLA.blit(texto_salir, (boton_salir.x + 72, boton_salir.y + 14))

        pygame.display.update()    

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    return "jugar"
                elif boton_ranking.collidepoint(evento.pos):
                    return "ranking"
                elif boton_salir.collidepoint(evento.pos):
                    return "salir"
