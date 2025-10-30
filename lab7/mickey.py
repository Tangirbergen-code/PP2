import pygame
import datetime
import math
import os


def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)


def main():
   
    pygame.init()

    
    try:
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        SCRIPT_DIR = os.getcwd() 

    BG_PATH = os.path.join(SCRIPT_DIR, 'base_micky.jpg')
    MIN_HAND_PATH = os.path.join(SCRIPT_DIR, 'minute.png')
    SEC_HAND_PATH = os.path.join(SCRIPT_DIR, 'second.png')

    
    try:
        bg_image_raw = pygame.image.load(BG_PATH)
        min_hand_raw = pygame.image.load(MIN_HAND_PATH)
        sec_hand_raw = pygame.image.load(SEC_HAND_PATH)
        
    except pygame.error as e:
        print(f"Не удалось загрузить изображение: {e}")
        return 

    
    screen_width, screen_height = bg_image_raw.get_size()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mickey Clock")

    bg_image = bg_image_raw.convert()
    min_hand_img = min_hand_raw.convert_alpha()
    sec_hand_img = sec_hand_raw.convert_alpha()

    
    clock_center = (screen_width // 2, screen_height // 2)

    
    sec_hand_rect = sec_hand_img.get_rect()
    
    originPos_sec = (sec_hand_rect.width // 2, sec_hand_rect.height // 2)
    
    min_hand_rect = min_hand_img.get_rect()
    
    originPos_min = (min_hand_rect.width // 2, min_hand_rect.height // 2)

    clock = pygame.time.Clock()

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        
        sec_angle = -seconds * 6
        min_angle = -(minutes * 6) - (seconds * 0.1)

        
        screen.blit(bg_image, (0, 0))
        blitRotate(screen, sec_hand_img, clock_center, originPos_sec, sec_angle)
        blitRotate(screen, min_hand_img, clock_center, originPos_min, min_angle)

        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()