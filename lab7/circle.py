import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
MOVE_SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

clock = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if (ball_y - MOVE_SPEED) >= BALL_RADIUS:
                    ball_y -= MOVE_SPEED
                    
            if event.key == pygame.K_DOWN:
                if (ball_y + MOVE_SPEED) <= (SCREEN_HEIGHT - BALL_RADIUS):
                    ball_y += MOVE_SPEED
                    
            if event.key == pygame.K_LEFT:
                if (ball_x - MOVE_SPEED) >= BALL_RADIUS:
                    ball_x -= MOVE_SPEED
                    
            if event.key == pygame.K_RIGHT:
                if (ball_x + MOVE_SPEED) <= (SCREEN_WIDTH - BALL_RADIUS):
                    ball_x += MOVE_SPEED

    screen.fill(WHITE)
    
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()