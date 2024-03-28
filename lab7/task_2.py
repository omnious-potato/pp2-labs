import pygame, os, random, math
from PIL import Image



local_gif_counter = 0

def split_into_frame(file):
    gif = Image.open(file)

    frames = []

    while True:
        try:
            gif.seek(gif.tell() + 1)
        except EOFError: 
            break
        
        
        frame = gif.copy()

        if frame.mode != 'RGBA':
            frame = frame.convert('RGBA')

        frames.append(frame)
    
    return frames

class AudioPlayer:
    def __init__(self, playlist):
        pygame.init()
        self.jam_cat = pygame.image.load('images/cat-jam-cat.gif')
        
        global frame_counter
        frame_counter = 0
        
        self.playlist = playlist 
        self.current_track = 0 #track index
        
        self.paused = False
        self.playing = False
        
        self.load_track()
        self.windows_color = (0, 0, 0)
        self.init_window()
        
    def init_window(self):
        self.window_width = 1280
        self.window_height = 600
        
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        
        global frames
        frames = split_into_frame('images/cat-jam-cat.gif')
        pygame.display.set_caption('Audio Player')
        
        self.font = pygame.font.SysFont(None, 36)
        self.clock = pygame.time.Clock()

        

        
        
    def load_track(self):
        pygame.mixer.music.load(self.playlist[self.current_track])
        
    def play_pause(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True
            
    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.load_track()
        if self.playing:
            pygame.mixer.music.play()
    
    def prev_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.load_track()
        if self.playing:
            pygame.mixer.music.play()
    
    def run(self):
        global frame_counter
        
        done  = False
        while not done:
            frame_counter = (frame_counter + 1) % 60
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.play_pause()
                    elif event.key == pygame.K_RIGHT:
                        self.next_track()
                    elif event.key == pygame.K_LEFT:
                        self.prev_track()
                        
            self.draw_window()
            self.clock.tick(60)
        

    def draw_window(self):

        self.window.fill(self.windows_color)

        
        global local_gif_counter

        
        if not self.playing or self.paused:
            local_gif_counter = 0
        frame = frames[local_gif_counter]
        jam_surf = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode).convert_alpha()
        self.window.blit(jam_surf, (0, 0))
            
        if self.playing:
            local_gif_counter = (local_gif_counter + 1) % len(frames)
    

        status_text = f"Paused: {playlist[self.current_track]}" if self.paused else f"Now playing: {playlist[self.current_track]}" if self.playing else "Stopped"
        text_surface = self.font.render(status_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.window_width/2, self.window_height/2))
        self.window.blit(text_surface, text_rect)
        
        pygame.display.update()


if __name__ == "__main__":
    playlist = ["audio/" + x for x in os.listdir("audio") if x.endswith(".mp3")]
    
    player = AudioPlayer(playlist)
    player.run()
