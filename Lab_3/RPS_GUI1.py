#Works cited: https://realpython.com/pygame-a-primer/
#Photo: https://www.pinterest.com/pin/rock-paper-scissors-icon-set-on-white-background--1055883075115643949/
import paho.mqtt.client as mqtt
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

B_Size = 90
DEFAULT_IMAGE_SIZE = (B_Size, B_Size)
def button(img, x, y):
    button = pygame.image.load(img)
    button = pygame.transform.scale(button, DEFAULT_IMAGE_SIZE)
    button = button.convert()
    buttonR = button.get_rect(topleft=(x, y))
    return button, buttonR

def text(f_size, str, x, y):
    font = pygame.font.Font('freesansbold.ttf', f_size)
    txt = font.render(str, True, white)
    txtR = txt.get_rect()
    txtR.center = (x,y)
    return txt, txtR

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("EugeneMin2")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

opponent_choice = " "
# The default message callback.
# (won’t be used if only publishing, but can still exist)
def on_message(client, userdata, message):
    global opponent_choice
    opponent_choice = message.payload.decode()

if __name__ == "__main__":
    pygame.init()
    # Define constants for the screen width and height
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    r_w = SCREEN_WIDTH//2 - 300
    r_h = SCREEN_WIDTH//2
    p_w = SCREEN_WIDTH//2 - 200
    p_h = SCREEN_WIDTH//2
    s_w = SCREEN_WIDTH//2 - 100
    s_h = SCREEN_WIDTH//2 
    A_w = SCREEN_WIDTH//2 + 100
    A_h = SCREEN_WIDTH//2 
    white = (255,255,255)
    black = (0,0,0)
    #screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Rock, Paper, Scissors')
    title, titleRect = text(32, 'Rock, Paper, Scissors', SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 250)
    Inst, InstR = text(32, "Instructions:", 170,120)
    Inst1,InstR1 = text(24, "Click on the image or", 250, 160)
    Inst2,InstR2 = text(24, "type rock (r), paper (p), or scissors (s)", 280, 200)
    N1, N1R =  text(32, "r", r_w+40, r_h+120)
    N2, N2R =  text(32, "p", p_w+40, p_h+120)
    N3, N3R = text(32, "s", s_w+40, s_h+120)

    #images
    rock, rockR = button("rock.png", r_w, r_h)
    scis, scisR = button("scissors.png", s_w, s_h)
    paper, paperR = button("paper.png", p_w, p_h)

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message


    client.connect_async("mqtt.eclipseprojects.io")

    client.loop_start()
    running = True
    while(running):
        player_choice = " "
        selecting= True
        while selecting and running:
            screen.fill((255, 255, 0))
            screen.blit(title,  titleRect)
            screen.blit(Inst, InstR)
            screen.blit(Inst1, InstR1)
            screen.blit(Inst2, InstR2)
            screen.blit(N1, N1R)
            screen.blit(N2, N2R)
            screen.blit(N3, N3R)
            mouse = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if(event.key == K_ESCAPE):
                        running = False
                    elif(event.key == 'r'):
                        player_choice = 'r'
                        selecting = False
                    elif event.key == 'p':
                        player_choice = 'p'
                        selecting = False
                    elif event.key == 's':
                        player_choice = 's'
                        selecting = False
                elif event.type == QUIT:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if r_w <= mouse[0] <= r_w + B_Size and r_h <= mouse[1] <= r_h +B_Size: 
                        player_choice = 'r'
                        selecting = False
                    elif p_w <= mouse[0] <= p_w + B_Size and p_h <= mouse[1] <= p_h +B_Size: 
                        player_choice = 'p'
                        selecting = False
                    elif s_w <= mouse[0] <= s_w + B_Size and s_h <= mouse[1] <= s_h +B_Size: 
                        player_choice = 's'
                        selecting = False

            pygame.draw.rect(screen, black, (50,100,500,260), 2)
            screen.blit(rock, rockR)
            screen.blit(paper, paperR)
            screen.blit(scis, scisR)
            pygame.display.flip()
        
        client.publish("EugeneMin1", player_choice,1) 

        wait, waitR = text(32, "Waiting for the input from player 2", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 
        while(opponent_choice == " " and running):
            screen.fill((255, 255, 0))
            screen.blit(wait,waitR)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            pygame.display.flip()

        if(opponent_choice == player_choice):
            result, resultR = text(64, "Result: Tie", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 
        else:
            if((player_choice == 'r' and opponent_choice  == 's') or (player_choice == 'p' and opponent_choice  == 'r') or (player_choice == 's' and opponent_choice  == 'p')):
                result, resultR = text(64, "Result: You Win", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            else:
                result, resultR = text(64, "Result: You Lost", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        again = False
        ag, agR = text(32, "Again?", A_w+75, A_h+40)
        p1O, p1OR = text(32, "Player1 used: " + player_choice, A_w+100, A_h + 120)
        p2O, p2OR   = text(32,"Player2 used: " + opponent_choice, A_w+100, A_h + 180) 
        opponent_choice = " " 
        while(running and (not again)):
            screen.fill((255, 255, 0))
            screen.blit(result,  resultR)
            screen.blit(p1O,   p1OR)
            screen.blit(p2O,  p2OR)
            screen.blit(ag,  agR)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if A_w <= mouse[0] <= A_w + 150 and A_h <= mouse[1] <= A_h +80: 
                        again = True

            pygame.draw.rect(screen, black, ( SCREEN_WIDTH//2 - 300,A_h,250,180), 2)
            pygame.draw.rect(screen, black, (A_w,A_h,150,80), 2)
            pygame.display.flip()     
    client.loop_stop()
    client.disconnect() 
    pygame.quit()