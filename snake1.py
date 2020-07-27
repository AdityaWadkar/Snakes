import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (200, 0, 0)
black = (0, 0, 0)
yellow =(12, 59, 125)
light_green=(153, 232, 74)
green=(37, 224, 4)
purple=(78, 24, 214)
light_red = (255,0,0)
cnt =0
# Creating window
screen_width = 600
screen_height = 400
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pause=False


#icon
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)


#background image
pause1 =pygame.image.load("pause.jpg")
pause1 = pygame.transform.scale(pause1, (screen_width, screen_height)).convert_alpha()
intro =pygame.image.load("intro11.jpg")
intro = pygame.transform.scale(intro, (screen_width, screen_height)).convert_alpha()
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
            pygame.mixer.music.load("back.mp3")
            pygame.mixer.music.play()
            action()
    else:
        pygame.draw.rect(gameWindow, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameWindow.blit(textSurf, textRect)

#PAuse Function

def paused():
    pygame.mixer.music.load("first.mp3")
    pygame.mixer.music.play()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    unpause()
                if event.key == pygame.K_ESCAPE:
                    quitgame()


        gameWindow.blit(pause1, (0, 0))
        message_display_pause("PAUSED")

        button("Continue", 130, 350, 120, 35, green, light_green, unpause)
        button("Quit", 350, 350, 120, 35, red, light_red, quitgame)

        pygame.display.update()
        clock.tick(30)

def unpause():
    global pause
    pause=False

#Instruction menu

def instruction():
    pygame.mixer.music.load("first.mp3")
    pygame.mixer.music.play()
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
        text_screen("Escape Button = Start the game!!", light_green, 50, 160)
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
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        button("START", 200, 300, 120, 35, green, light_green, gameloop)
        pygame.display.update()
        clock.tick(60)

# Starting Screen
def welcome():
    pygame.mixer.music.load("first.mp3")
    pygame.mixer.music.play()
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
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    gameloop()
                if event.key == pygame.K_RETURN:
                    instruction()
        button("START", 230, 350, 120, 35, green, light_green,gameloop)
        button("CONTROLS", 20, 350, 120, 35, red, light_red,instruction)
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
    snk_length = 1

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
            text_screen("Game Over!!! Press Enter To replay", (234,120,2), 140, 50)


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

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                    if event.key == pygame.K_SPACE:
                        pause = True
                        paused()


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
            text_screen("Score: " + str(score) + "     Highscore : "+str(highscore) , red, 5, 5)
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