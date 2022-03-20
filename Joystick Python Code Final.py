import serial
import time
import random
import pygame


ser = serial.Serial(
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=.1)

print("connected to: " + ser.portstr)

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game - EECE520 R.Vyas, B.Upperla, J.Morrow')

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 30

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


def gameLoop():  # creating a function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    ScoreTotal = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    pygame.display.update()
    dx = 5                   #X direction is second digit in data (data[0] is 'S')
    dy = 5                   #Y direction is fourth digit in data
    JSButton = int(0)
    x = int(6)
    count = 0

    while not game_over:
        if count == 1:
            x1 += x1_change
            y1 += y1_change
            dis.fill(red)
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(ScoreTotal - 1)
            pygame.display.update()
            pygame.display.update()
            pygame.display.update()
            count = 1
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
                foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
                ScoreTotal += 20
                Length_of_snake += 1
                ser.isOpen()
                ser.write(str.encode('1'))

                count = 0

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        try:
            #time.sleep(.5)
            rawdata = ser.readline().strip()          #read serial data from arduino one line at a time
            data = str(rawdata.decode('utf-8'))
            data1 = str(data)
            #print(data)
            dx = int(data[1])                   #X direction is second digit in data (data[0] is 'S')
            dy = int(data[2])
            #print(dx,dy)
            #print(len(data))
        except:
            continue

                #decode the raw byte data into UTF-8
        if (data.startswith("D")) :               #make sure the read starts in the correct place
            #dx = int(data[3])                   #X direction is second digit in data (data[0] is 'S')
            #dy = int(data[4])                   #Y direction is fourth digit in data
            #JSButton = int(data[5]
            #print("left")

            try:
                #time.sleep(.5)
                rawdata = ser.readline().strip()          #read serial data from arduino one line at a time
                data = str(rawdata.decode('utf-8'))
                data1 = str(data)
                #print(data)
                dx = int(data[1])                   #X direction is second digit in data (data[0] is 'S')
                dy = int(data[2])
                #print(dx,dy)
                #print(len(data))
            except:
                continue

        if dx == 1: #left
            x1_change = -snake_block
            y1_change = 0
            #print(data)

        #decode the raw byte data into UTF-8
        if (data.startswith("D")) :               #make sure the read starts in the correct place
            #dx = int(data[3])                   #X direction is second digit in data (data[0] is 'S')
            #dy = int(data[4])                   #Y direction is fourth digit in data
            #JSButton = int(data[5])
            #print("right")

            try:
                #time.sleep(.5)
                rawdata = ser.readline().strip()          #read serial data from arduino one line at a time
                data = str(rawdata.decode('utf-8'))
                data1 = str(data)
                #print(data)
                dx = int(data[1])                   #X direction is second digit in data (data[0] is 'S')
                dy = int(data[2])
                #print(dx,dy)
                #print(len(data))
            except:
                continue


        if dx == 2: #right
            x1_change = snake_block
            y1_change = 0
            #print(data)

       #decode the raw byte data into UTF-8
        if (data.startswith("D")) :                #make sure the read starts in the correct place
            #dx = int(data[3])                   #X direction is second digit in data (data[0] is 'S')
            #dy = int(data[4])                   #Y direction is fourth digit in data
            #JSButton = int(data[5])
            #print("up")

            try:
                #time.sleep(.5)
                rawdata = ser.readline().strip()          #read serial data from arduino one line at a time
                data = str(rawdata.decode('utf-8'))
                data1 = str(data)
                #print(data)
                dx = int(data[1])                   #X direction is second digit in data (data[0] is 'S')
                dy = int(data[2])
                #print(dx,dy)
                #print(len(data))
            except:
                continue


        if dy == 1: #down
            y1_change = -snake_block
            x1_change = 0
            #print(data)

        #decode the raw byte data into UTF-8
        if (data.startswith("D")) :               #make sure the read starts in the correct place
            #dx = int(data[3])                   #X direction is second digit in data (data[0] is 'S')
            #dy = int(data[4])                   #Y direction is fourth digit in data
            #JSButton = int(data[5])
            #print("down")


            try:
                #time.sleep(.5)
                rawdata = ser.readline().strip()          #read serial data from arduino one line at a time
                data = str(rawdata.decode('utf-8'))
                data1 = str(data)
                #print(data)
                dx = int(data[1])                   #X direction is second digit in data (data[0] is 'S')
                dy = int(data[2])
                #print(dx,dy)
                #print(len(data))
            except:
                continue

        if dy == 2: #up
            y1_change = snake_block
            x1_change = 0
            #print(data)

###############################################################3
        if (data.startswith("D")) :               #make sure the read starts in the correct place
            #dx = int(data[3])                   #X direction is second digit in data (data[0] is 'S')
            #dy = int(data[4])                   #Y direction is fourth digit in data
            #JSButton = int(data[5])
            #print("down")


            try:
                #time.sleep(.5)
                rawdata = ser.readline().strip()          #read serial data from arduino one line at a time
                data = str(rawdata.decode('utf-8'))
                data1 = str(data)
                #print(data)
                JSButton = int(data[3])                   #X direction is second digit in data (data[0] is 'S')
                #print(dx,dy)
                #print(len(data))
            except:
                continue

        if JSButton == 0: #up
            x1 += x1_change
            y1 += y1_change
            dis.fill(red)
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
            pygame.display.update()
            pygame.display.update()
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            pygame.display.update()
            pygame.display.update()
            count = 1

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        if count == 0:
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            pygame.display.update()
            pygame.display.update()
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(ScoreTotal - 1)

            pygame.display.update()
            pygame.display.update()
            pygame.display.update()
            pygame.display.update()
            pygame.display.update()



            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
                foody = round(random.randrange(0, dis_height - snake_block) / 20.0) *20.0
                ScoreTotal += 10
                Length_of_snake += 1
                ser.isOpen()
                #buzzer = int(1)

                    #if(data == 1):
                ser.write(str.encode('1'))
                    #elif(data == 0):
                        #port.write(str.encode('0'))
                    #else:
                        #print('Invalid input!!!!')







        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()
