import pygame
import random
import os

pygame.mixer.init()
pygame.font.init()
pygame.init()
display_font = pygame.font.SysFont("comicsans", 30)
# Colors
white = (255, 255, 255)
red = (200, 0, 0)
black = (0, 0, 0)
yellow =(12, 59, 125)
light_green=(255, 255, 255)
green=(37, 224, 4)
purple=(231, 235, 16)
voilet=(245, 245, 162)
light_red = (255,0,0)
peach =(249, 149, 136)
cnt =0
# Creating window
screen_width = 600
screen_height = 400
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pause=False


#icon
gameIcon = pygame.image.load('snake.ico')
pygame.display.set_icon(gameIcon)


#background image
pause1 =pygame.image.load("images/pause.jpg")
pause1 = pygame.transform.scale(pause1, (screen_width, screen_height)).convert_alpha()
intro =pygame.image.load("images/intro11.jpg")
intro = pygame.transform.scale(intro, (screen_width, screen_height)).convert_alpha()
img = pygame.image.load("images/pic1.jpg")
img = pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
img1 = pygame.image.load("images/pic.png")
img1 = pygame.transform.scale(img1, (screen_width, screen_height)).convert_alpha()
img2 = pygame.image.load("images/over.jpg")
img2 = pygame.transform.scale(img2, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# text fumctions

def quitgame():
    pygame.quit()
    quit()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def message_display_pause(text):
    largeText = pygame.font.SysFont('Comicsansms',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    gameWindow.blit(TextSurf, TextRect)

def message_display(text):
    largeText = pygame.font.SysFont('Comicsansms',15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    gameWindow.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
#Snake Function

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, yellow, [x, y, snake_size, snake_size])




#Button Function

def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameWindow, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            pygame.mixer.music.load("images/back.mp3")
            pygame.mixer.music.play(-1)
            action()
    else:
        pygame.draw.rect(gameWindow, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameWindow.blit(textSurf, textRect)

#Pause Function

def paused():
    pygame.mixer.music.load("images/first.mp3")
    pygame.mixer.music.play(-1)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c or pygame.K_SPACE:
                    pygame.mixer.music.load("images/back.mp3")
                    pygame.mixer.music.play(-1)
                    unpause()
                if event.key == pygame.K_ESCAPE:
                    quitgame()


        gameWindow.blit(pause1, (0, 0))
        message_display_pause("PAUSED")

        button("Continue", 130, 350, 120, 35, green, light_green, unpause)
        button("Quit",screen_width-200, 350, 100, 35, purple, voilet,quitgame)

        pygame.display.update()
        clock.tick(30)

def unpause():
    global pause
    pause=False

#Instruction menu

def instruction():
    pygame.mixer.music.load("images/first.mp3")
    pygame.mixer.music.play(-1)
    exit_game = False
    while not exit_game:

        gameWindow.blit(intro, (0, 0))
        text_screen("Right arrow - move snake to Right", light_green, 50, 20)
        text_screen("Left arrow - move snake to Left", light_green, 50, 40)
        text_screen("UP arrow - move snake in upward direction ", light_green, 50, 60)
        text_screen("Down arrow - move snake in Downward direction", light_green, 50, 80)
        text_screen("N Button - play next song", light_green, 50, 100)
        text_screen("Enter Button = Start the game!!", light_green, 50, 120)
        text_screen("space Button = Pause and Unpause the game!!", light_green, 50, 140)
        text_screen("Escape Button = Exit the game!!", light_green, 50, 160)
        text_screen("C Button = Continue the game!!", light_green, 50, 180)
        text_screen("R Button = Rules of the game!!", light_green, 50,200)
        text_screen("Tip = You can add your favorite songs in playlist folder ", light_green, 50,220)
        text_screen("          to enjoy this game.But if playlist folder is empty", light_green, 50, 240)
        text_screen("          it will play default system generated song", light_green, 50, 260)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("images/back.mp3")
                    pygame.mixer.music.play(-1)
                    gameloop()
        button("START", screen_width/2-70, 300, 120, 35, green, light_green, gameloop)
        pygame.display.update()
        clock.tick(60)

# Starting Screen
def welcome():
    pygame.mixer.music.load("images/first.mp3")
    pygame.mixer.music.play(-1)
    exit_game =False
    while not exit_game:

        gameWindow.blit(img1, (0,0))
        text_screen("WELCOME TO SNAKES BY ADITYA",red,120,20)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("images/back.mp3")
                    pygame.mixer.music.play(-1)
                    gameloop()
                if event.key == pygame.K_r:
                    instruction()
        button("START", screen_width/2-70, 350, 120, 35, green, light_green,gameloop)
        button("CONTROLS", screen_width-550, 350, 120, 35, red, light_red,instruction)
        button("Quit",screen_width-200, 350, 100, 35, purple, voilet,quitgame)

        pygame.display.update()
        clock.tick(60)
# Main Game Loop
def gameloop():

    # Game specific variables
    global pause
    global cnt
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y =55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    highscore = 0
    snk_length = 1

    if(not os.path.exists("highscore.txt")):
         with open ("highscore.txt", "w")as f:
             f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)

    food_size = 10
    score = 0
    init_velocity = 4
    snake_size = 12
    fps = 30
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.blit(img2, (0, 0))
            score_label = display_font.render(f"Your Score: {score} ", 1, white)
            gameWindow.blit(score_label, ((screen_width / 2) - score_label.get_width() / 2, 10))
            text_screen("Game Over!!! Press Enter To replay", (234,120,2), 140, 50)
            button("QUIT",screen_width-200, 350, 100, 35, purple, voilet,quitgame)
            button("REPLAY", 100, 350, 120, 35, green, light_green, gameloop)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN:
                        if cnt%2==0:
                            pygame.mixer.music.load("images/song.mp3")
                            pygame.mixer.music.play(-1)
                            cnt=cnt+1
                        else:
                            pygame.mixer.music.load("images/back.mp3")
                            pygame.mixer.music.play(-1)
                            cnt = cnt + 1
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                    if event.key == pygame.K_SPACE:
                        pause = True
                        paused()


                    if event.key ==pygame.K_n:
                        try:
                            a = os.listdir(r"playlist")
                            d = random.choice(a)
                            ab = "playlist/" + d
                            pygame.mixer.music.load(ab)
                            pygame.mixer.music.play(-1)
                        except Exception as e:
                            pygame.mixer.music.load("images/song.mp3")
                            pygame.mixer.music.play(-1)

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                snk_length +=5
            if int(score) > int(highscore):
                highscore = score
            gameWindow.blit(img, (0,0))
            score_label = display_font.render(f"score: {score} ", 1, white)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])
            gameWindow.blit(score_label, (10, 10))
            hscore_label = display_font.render(f"Highscore: {highscore} ", 1, white)
            gameWindow.blit(hscore_label, (screen_width -hscore_label.get_width() -10, 10))
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("images/start.mp3")
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("images/start.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
