import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint by Tangirbergen")
    clock = pygame.time.Clock()
    
    screen.fill((0, 0, 0))

    radius = 15
    draw_mode = 'pen'
    current_color = (0, 0, 255)
    drawing = False
    start_pos = (0, 0)
    last_pos = (0, 0)

    while True:
        
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    current_color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    current_color = (0, 0, 255)
                elif event.key == pygame.K_w: 
                    current_color = (255, 255, 255)
                    
                elif event.key == pygame.K_p: 
                    draw_mode = 'pen'
                elif event.key == pygame.K_t: 
                    draw_mode = 'rectangle'
                elif event.key == pygame.K_c: 
                    draw_mode = 'circle'
                elif event.key == pygame.K_e: 
                    draw_mode = 'pen'
                    current_color = (0, 0, 0) 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                
                elif event.button == 4: 
                    radius = min(200, radius + 1)
                elif event.button == 5: 
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    drawing = False
                    end_pos = event.pos
                    
                    if draw_mode == 'rectangle':
                        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                        rect.normalize() 
                        pygame.draw.rect(screen, current_color, rect, 2)
                        
                    elif draw_mode == 'circle':
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        circle_radius = int((dx*dx + dy*dy)**0.5)
                        
                        if circle_radius > 0:
                            pygame.draw.circle(screen, current_color, start_pos, circle_radius, 2)

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if draw_mode == 'pen':
                        current_pos = event.pos
                        pygame.draw.line(screen, current_color, last_pos, current_pos, radius)
                        last_pos = current_pos
                        
        pygame.display.flip()
        
        clock.tick(60)

main()