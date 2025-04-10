import pygame
import random
import time

pygame.init()
blue=(0,0,255)
yellow = (255, 255, 102)
light_blue=(135, 206, 250)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

dis_width = 600
dis_height = 400
dis= pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game")

clock=pygame.time.Clock()
snake_speed=15
snake_block = 15
font=pygame.font.SysFont(None,25)
score_font=pygame.font.SysFont(None,35)
def draw_brick_background():
    brick_color = (178, 34, 34)  # reddish brick
    brick_width = 55
    brick_height = 30

    for y in range(0, dis_height, brick_height):
        offset = 0 if (y // brick_height) % 2 == 0 else brick_width // 2
        for x in range(-offset, dis_width, brick_width):
            pygame.draw.rect(dis, brick_color, [x, y, brick_width, brick_height])
            pygame.draw.rect(dis, black, [x, y, brick_width, brick_height], 1)  

def score(score,color):
   value=score_font.render("Your score:" +str(score), True, color)
   dis.blit(value, [0,0])

def snake_move(snake_block, snake_list):
   for value in snake_list:
      pygame.draw.rect(dis,black, [value[0],value[1], snake_block,snake_block])

def message(msg,color):
    mesg=font.render(msg,True,color)
    text = mesg.get_rect(center=(dis_width / 2, dis_height / 2))
    dis.blit(mesg, text)

def game():
    game_over=False
    game_close=False
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx=round(random.randrange(0, dis_width-snake_block)/10.0)*10
    foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10
    while not game_over:
        while game_close==True:
          dis.fill(blue)
          message("You Lost!, Press C-Play Again or Q-Quit", white)
          score(Length_of_snake-1, yellow)
          pygame.display.update()
         
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game()
          time.sleep(0.1) 
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
              game_over=True
           if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_LEFT:
                x1_change=-snake_block
                y1_change=0
             elif event.key==pygame.K_RIGHT:
                x1_change=snake_block
                y1_change=0
             elif event.key==pygame.K_UP:
                x1_change=0
                y1_change=-snake_block
             elif event.key==pygame.K_DOWN:
                x1_change=0
                y1_change=snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1+=x1_change
        y1+=y1_change
        draw_brick_background()
        #dis.fill(light_blue)
        pygame.draw.rect(dis, white, [foodx,foody,snake_block,snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List)>Length_of_snake:
           del snake_List[0]
        for x in snake_List[:-1]:
           if x==snake_head:
              game_close=True
        snake_move(snake_block,snake_List)
        score(Length_of_snake-1, yellow)
        pygame.display.update()

        if (abs(x1-foodx)<snake_block and abs(y1-foody)<snake_block):
           foodx=round(random.randrange(0, dis_width-snake_block)/10.0)*10
           foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10
           Length_of_snake+=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
game()