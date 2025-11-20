import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Just PAINT :)")
    clock = pygame.time.Clock()
    
    radius = 10
    x = 0
    y = 0
    mode = 'draw'  
    color = (255, 255, 255)  
    start_pos = None
    drawing = False
    points = []
    last_pos = None  

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                #to activate forms
                if event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_r:
                    mode = 'rect'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_s:
                    mode = 'square'
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'
                elif event.key == pygame.K_q:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    mode = 'rhombus'
                
                # Choose a colour
                elif event.key == pygame.K_1:
                    color = (255, 0, 0)  # Red
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)  # Green
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)  # Blue
                elif event.key == pygame.K_4:
                    color = (255, 255, 0)  # Yellow
                elif event.key == pygame.K_5:
                    color = (255, 255, 255)  # White
                elif event.key == pygame.K_6:
                    color = (0, 0, 0)  # Black

            # Mouse control
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    start_pos = event.pos
                    last_pos = start_pos  
                    drawing = True
                elif event.button == 3:  
                    radius = max(1, radius - 1)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    if mode == 'rect':
                        draw_rect(screen, start_pos, end_pos, color, radius)
                    elif mode == 'circle':
                        draw_circle_shape(screen, start_pos, end_pos, color, radius)
                    elif mode == 'square':
                        draw_square(screen, start_pos, end_pos, color, radius)
                    elif mode == 'right_triangle':
                        draw_right_triangle(screen, start_pos, end_pos, color, radius)
                    elif mode == 'equilateral_triangle':
                        draw_equilateral_triangle(screen, start_pos, end_pos, color, radius)
                    elif mode == 'rhombus':
                        draw_rhombus(screen, start_pos, end_pos, color, radius)

                    drawing = False
                    last_pos = None  

            elif event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                if mode == 'draw':
                    if last_pos is not None:
                        pygame.draw.line(screen, color, last_pos, position, radius * 2)
                    last_pos = position

                elif mode == 'erase':
                    if last_pos is not None:
                        pygame.draw.line(screen, (0, 0, 0), last_pos, position, radius * 2)
                    last_pos = position

        pygame.display.set_caption(f"Mode: {mode.upper()} | Color: {color} | Brush Size: {radius}")
        pygame.display.flip()
        clock.tick(60)

#functions for forms
def draw_rect(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                       abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, width)

def draw_circle_shape(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
    pygame.draw.circle(screen, color, start, radius, width)

def draw_square(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    side = max(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(screen, color, rect, width)

def draw_right_triangle(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x2, y1), (x1, y2)]
    pygame.draw.polygon(screen, color, points, width)

def draw_equilateral_triangle(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    side = abs(x2 - x1)
    h = (3**0.5 / 2) * side
    points = [
        (x1, y1),
        (x1 + side, y1),
        (x1 + side / 2, y1 - h)
    ]
    pygame.draw.polygon(screen, color, points, width)

def draw_rhombus(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]
    pygame.draw.polygon(screen, color, points, width)

main()