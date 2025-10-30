import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_DIR = "music"

try:
    playlist_files = [
        os.path.join(MUSIC_DIR, f) 
        for f in os.listdir(MUSIC_DIR) 
        if f.endswith(('.mp3', '.ogg', '.wav'))
    ]
except FileNotFoundError:
    print(f"Ошибка: Папка '{MUSIC_DIR}' не найдена.")
    print("Пожалуйста, создайте папку 'music' и добавьте в нее аудиофайлы.")
    exit()

if not playlist_files:
    print(f"В папке '{MUSIC_DIR}' не найдено .mp3, .ogg или .wav файлов.")
    exit()

current_song_index = 0
is_paused = False

SONG_END_EVENT = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END_EVENT)

def play_song(index):
    global current_song_index, is_paused
    
    current_song_index = index % len(playlist_files)
    
    try:
        pygame.mixer.music.load(playlist_files[current_song_index])
        pygame.mixer.music.play()
        is_paused = False
        print(f"Playing: {os.path.basename(playlist_files[current_song_index])}")
    except pygame.error as e:
        print(f"Ошибка загрузки файла: {playlist_files[current_song_index]}")
        print(e)
        next_song()

def next_song():
    play_song(current_song_index + 1)

def prev_song():
    play_song(current_song_index - 1)

def stop_song():
    global is_paused
    pygame.mixer.music.stop()
    is_paused = False

def toggle_pause():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        print("Resumed")
    else:
        pygame.mixer.music.pause()
        is_paused = True
        print("Paused")

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Pygame Music Player")

font = pygame.font.Font(None, 28)
controls_text = "SPACE: Play/Pause | S: Stop | →: Next | ←: Prev | Q: Quit"
text_render = font.render(controls_text, True, (200, 200, 200))

print("--- Pygame Music Player ---")
print(controls_text)
play_song(current_song_index)

running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == SONG_END_EVENT:
            print("Song finished, playing next...")
            next_song()
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    toggle_pause()
                else:
                    play_song(current_song_index)
            
            if event.key == pygame.K_s:
                print("Stopped")
                stop_song()
                
            if event.key == pygame.K_RIGHT:
                print("Next track")
                next_song()
                
            if event.key == pygame.K_LEFT:
                print("Previous track")
                prev_song()
            
            if event.key == pygame.K_q:
                running = False

    screen.fill((30, 30, 30))
    
    song_name = os.path.basename(playlist_files[current_song_index])
    status = "Paused" if is_paused else "Playing"
    if not pygame.mixer.music.get_busy() and not is_paused:
        status = "Stopped"
        
    song_text = font.render(f"{status}: {song_name}", True, (255, 255, 255))
    
    screen.blit(song_text, (20, 50))
    screen.blit(text_render, (20, 150))
    
    pygame.display.flip()
    
    clock.tick(30)

print("Shutting down...")
pygame.quit()