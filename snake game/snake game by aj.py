import pygame
import random
import os
pygame.init()
screen_width = 900
screen_height = 600

#images used in game
image = pygame.image.load('snake.jpg')
image2 = pygame.image.load('game over.jpg')
image4 = pygame.image.load('background.jpg')

#resizing the images
image3 = pygame.transform.scale(image2,(screen_width, screen_height))
image5 = pygame.transform.scale(image4,(screen_width, screen_height))
image6 = pygame.transform.scale(image,(screen_width, screen_height))

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green=(255,100,100)
blue=(26, 32, 232)

# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))


# Game Title
pygame.display.set_caption("SnakesGame")
pygame.display.update()
clock = pygame.time.Clock()

#font used in 1st page and last page of game
font = pygame.font.Font('freesansbold.ttf', 35)
font2 = pygame.font.Font('freesansbold.ttf', 65)


#it will write text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


# it will plot snake reqularly
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

#1st page or the welcome window
def welcome():
    exit_game = False
    #game loop
    while not exit_game:
        #gameWindow.fill(blue)
        gameWindow.blit(image6, (0,0))
        text_screen("Welcome to the game",white,80,450)
        text_screen("Press Space bar to Start",white,110,500)
        text_screen("By : ARPIT JAIN",white,610,550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #now if user press tab it will call my game defined in gameloop
                    gameloop()
        pygame.display.update()
        clock.tick(40)
        
    
# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
            hyscore=0
    else:
         with open("highscore.txt","r") as f:
            hyscore = f.read()
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 8
    snake_size = 18
    fps = 60
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(hyscore))
            #gameWindow.fill(blue)
            gameWindow.blit(image3, (0,0))
            text_screen2(f"Your  Score {score}", red, 250, 220)
            text_screen("Press ENTER to play again!!!", red, 250, 550)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #if user want to play again he have to press enter
                        #it will call again the welcome page
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    #cheat codes
                    if event.key == pygame.K_q:
                        score+=5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score +=10
                food_x = random.randint(50, screen_width / 2 )
                food_y = random.randint(50, screen_height / 2)
                snk_length +=5
            if score> int(hyscore):
            	hyscore=score

           # gameWindow.fill(white)
            gameWindow.blit(image5, (0,0))
            text_screen("Score: " + str(score), red, 5, 5)
            text_screen("Highscore: "+str(hyscore), red,600,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size-5, snake_size-5])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

#it will call welcom page or the 1st page
welcome()
s
