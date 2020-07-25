import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow =(12, 59, 125)
cnt =0
# Creating window
screen_width = 600
screen_height = 400
gameWindow = pygame.display.set_mode((screen_width, screen_height))
#background image
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)
img = pygame.image.load("pic1.jpg")
img = pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
img1 = pygame.image.load("pic.png")
img1 = pygame.transform.scale(img1, (screen_width, screen_height)).convert_alpha()
img2 = pygame.image.load("over.jpg")
img2 = pygame.transform.scale(img2, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("MY First Game-snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, yellow, [x, y, snake_size, snake_size])

def welcome():
    pygame.mixer.music.load("first.mp3")
    pygame.mixer.music.play()
    exit_game =False
    #pause=False
    while not exit_game:

        gameWindow.blit(img1, (0,0))
        text_screen("welcome to Snakes by Aditya", red, 215, 50)
        text_screen("Press space to continue", white, 215, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()

                    gameloop()
        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():

    # Game specific variables
    global cnt
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y =55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    global pause
    if(not os.path.exists("highscore.txt")):
        with open ("highscore.txt", "w")as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 8
    score = 0
    init_velocity = 4
    snake_size = 12
    fps = 30
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                highscore = f.write(str(score))
            gameWindow.blit(img2, (0, 0))
            text_screen("Game Over! Press Enter To Continue and replay", (234,120,2), 100, 50)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN:
                        if cnt%2==0:
                            pygame.mixer.music.load("song.mp3")
                            pygame.mixer.music.play()
                            cnt=cnt+1
                        else:
                            pygame.mixer.music.load("back.mp3")
                            pygame.mixer.music.play()
                            cnt = cnt + 1
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT :
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP :
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN :
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

                    if event.key ==pygame.K_n:
                        songcnt = random.randint(1, 10)
                        if songcnt == 1:
                            pygame.mixer.music.load("song1.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 2:
                            pygame.mixer.music.load("song2.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 3:
                            pygame.mixer.music.load("song3.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 4:
                            pygame.mixer.music.load("song4.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 5:
                            pygame.mixer.music.load("song5.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 6:
                            pygame.mixer.music.load("song6.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 7:
                            pygame.mixer.music.load("song7.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 8:
                            pygame.mixer.music.load("song8.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 9:
                            pygame.mixer.music.load("song9.mp3")
                            pygame.mixer.music.play()
                        if songcnt == 10:
                            pygame.mixer.music.load("song10.mp3")
                            pygame.mixer.music.play()

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if int(score) > int(highscore):
                    highscore = score
            gameWindow.fill(white)
            gameWindow.blit(img, (0,0))
            text_screen("Score: " + str(score) + "     Highscore : "+str(highscore) +"    Press N to change song   "   , red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("start.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("start.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
gameloop()