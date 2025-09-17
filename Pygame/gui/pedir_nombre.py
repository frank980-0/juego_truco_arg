import pygame
import constantes

def pedir_nombre (pantalla):
    fuente = pygame.font.SysFont("Arial", 28)
    
    input_box = pygame.Rect(constantes.ANCHO_PANTALLA//2 - 150, constantes.ALTO_PANTALLA//2 - 30, 300, 50)
    color_inactivo = (200,200,200)
    color_activo = constantes.BLANCO
    color_borde = (50, 150, 255)
    color_texto = constantes.NEGRO

    activo = False
    texto = ''
    

    while True:
        
        fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA)) #carga y redimensiona la imagen de fondo

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Activo el cuadro si hago click dentro
                if input_box.collidepoint(evento.pos):
                    activo = True
                else:
                    activo = False
            if evento.type == pygame.KEYDOWN and activo:
                if evento.key == pygame.K_RETURN:  # ENTER
                    return texto  # devuelve el nombre
                elif evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]  # borra último caracter
                else:
                    texto += evento.unicode  # agrega lo escrito

        pantalla.blit(fondo, (0, 0)) #dibuja el fondo en la pantalla
        
        # Colores según activo/inactivo
        color = color_activo if activo else color_inactivo

        # Dibujar caja con borde redondeado
        pygame.draw.rect(pantalla, color, input_box, border_radius=15)
        pygame.draw.rect(pantalla, color_borde, input_box, 3, border_radius=15)

        # Renderizar texto
        superficie_texto = fuente.render(texto, True, color_texto)
        pantalla.blit(superficie_texto, (input_box.x + 10, input_box.y + 10))

        # Texto indicativo
        if texto == "" and not activo:
            marca = fuente.render("Escribe tu nombre...", True, (180, 180, 180))
            pantalla.blit(marca, (input_box.x + 10, input_box.y + 10))

        pygame.display.flip()
        
