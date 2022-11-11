from random import choice, randint
import pygame
from sys import exit


pygame.init()
screen=pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
game_active=False
score=0
lagre_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',40) 
medium_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',20)
small_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',10)

#intro
logo_game=pygame.image.load('Millionair_Images/pngtree-gold-ringing-christmas-bells-with-red-bow-png-image_6037900.jpg').convert_alpha()
logo_game_rect=logo_game.get_rect(center=(400,150))
intro_mes=lagre_font.render('Who want to be millionare!!!',True,('#0066FF'))
intro_mes_rect=intro_mes.get_rect(center=(400,300))
play=medium_font.render('Press space to begin.',True,('#0066FF'),)
play_rect=intro_mes.get_rect(center=(550,350))

#in game
#achievement
achievement_0=pygame.image.load('Millionair_Images/Picture0.png').convert_alpha()
achievement_1=pygame.image.load('Millionair_Images/Picture1.png').convert_alpha()
achievement_2=pygame.image.load('Millionair_Images/Picture2.png').convert_alpha()
achievement_3=pygame.image.load('Millionair_Images/Picture3.png').convert_alpha()
achievement_4=pygame.image.load('Millionair_Images/Picture4.png').convert_alpha()
achievement_5=pygame.image.load('Millionair_Images/Picture5.png').convert_alpha()
achievement_6=pygame.image.load('Millionair_Images/Picture6.png').convert_alpha()
achievement_7=pygame.image.load('Millionair_Images/Picture7.png').convert_alpha()
achievement_8=pygame.image.load('Millionair_Images/Picture8.png').convert_alpha()
achievement_9=pygame.image.load('Millionair_Images/Picture9.png').convert_alpha()
achievement_10=pygame.image.load('Millionair_Images/Picture10.png').convert_alpha()
achievement_11=pygame.image.load('Millionair_Images/Picture11.png').convert_alpha()
achievement_12=pygame.image.load('Millionair_Images/Picture12.png').convert_alpha()
achievement_13=pygame.image.load('Millionair_Images/Picture13.png').convert_alpha()
achievement_14=pygame.image.load('Millionair_Images/Picture14.png').convert_alpha()
achievement_15=pygame.image.load('Millionair_Images/Picture15.png').convert_alpha()
achievement_lst=[achievement_0,achievement_1,achievement_2,achievement_3,achievement_4,achievement_5,achievement_6,achievement_7,achievement_8,achievement_9,achievement_10,achievement_11,achievement_12,achievement_13,achievement_14,achievement_15]
achievement_index=0
achievement_img=achievement_lst[achievement_index]
achievement_img=pygame.transform.rotozoom(achievement_img,0,0.6)
achievement_rect=achievement_img.get_rect(center=(675,200))

#support
half=pygame.image.load('Millionair_Images/jpge50.jpg').convert_alpha()
halfX=pygame.image.load('Millionair_Images/jpge50X.jpg')
half_lst=[half,halfX]
half_index=0
half_img=half_lst[half_index]
half_rect=half_img.get_rect(center=(150,50))

people=pygame.image.load('Millionair_Images/jpgePeople.jpg').convert_alpha()
peopleX=pygame.image.load('Millionair_Images/jpgePeopleX.jpg').convert_alpha()
people_lst=[people,peopleX]
people_index=0
people_img=people_lst[people_index]
people_rect=people_img.get_rect(center=(300,50))

phone=pygame.image.load('Millionair_Images/jpgePhone.jpg').convert_alpha()
phoneX=pygame.image.load('Millionair_Images/jpgePhoneX.jpg').convert_alpha()
phone_lst=[phone,phoneX]
phone_index=0
phone_img=phone_lst[phone_index]
phone_rect=phone_img.get_rect(center=(450,50))

#play
decor=pygame.image.load('Millionair_Images/pngtree-gold-ringing-christmas-bells-with-red-bow-png-image_6037900.jpg').convert_alpha()
decor=pygame.transform.rotozoom(decor,0,0.25)
decor_rect=decor.get_rect(center=(300,150))

#question
question=medium_font.render('What is 5*5 ?',True,('#FFFFFF'))
question_rect=question.get_rect(center=(175,225))

#answer
answer_A=medium_font.render('A: 15',True,'#FFFFFF')
answer_B=medium_font.render('B: 20',True,'#FFFFFF')
answer_C=medium_font.render('C: 25',True,'#FFFFFF')
answer_D=medium_font.render('D: 30',True,'#FFFFFF')
answer_A_rect=answer_A.get_rect(center=(125,300))
answer_B_rect=answer_B.get_rect(center=(330,300))
answer_C_rect=answer_C.get_rect(center=(125,360))
answer_D_rect=answer_D.get_rect(center=(330,360))

while True:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            
            
            exit()
        if game_active:    
            if event.type== pygame.MOUSEBUTTONDOWN:
                if half_rect.collidepoint(event.pos) and half_index==0:
                    half_index+=1
                    half_img=half_lst[half_index]
                if people_rect.collidepoint(event.pos) and people_index==0:
                    people_index+=1
                    people_img=people_lst[people_index]
                if phone_rect.collidepoint(event.pos) and phone_index==0:
                    phone_index+=1
                    phone_img=phone_lst[phone_index]
                
                    
            # if event.type== obstacle_timer:
            #     obstancle_group.add(obstancle(choice(['fly','snail'])))
        else:
            if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_SPACE:
                        game_active=True
                        phone_index=0
                        half_index=0
                        people_index=0
                        # obstancle_group.empty()
                        # start_time=round(pygame.time.get_ticks()/1000) 
    if game_active:
        
        screen.blit(achievement_img,achievement_rect)
        screen.blit(half_img,half_rect)
        screen.blit(people_img,people_rect)
        screen.blit(phone_img,phone_rect)
        screen.blit(decor,decor_rect)
        pygame.draw.rect(screen,'#0066FF',pygame.Rect(100,200,400,50))
        screen.blit(question,question_rect)
        pygame.draw.rect(screen,'#0066FF',pygame.Rect(100,275,195,50))
        pygame.draw.rect(screen,'#0066FF',pygame.Rect(305,275,195,50))
        pygame.draw.rect(screen,'#0066FF',pygame.Rect(100,335,195,50))
        pygame.draw.rect(screen,'#0066FF',pygame.Rect(305,335,195,50))
        screen.blit(answer_A,answer_A_rect)
        screen.blit(answer_B,answer_B_rect)
        screen.blit(answer_C,answer_C_rect)
        screen.blit(answer_D,answer_D_rect)
        
    else:
        
        screen.blit(logo_game,logo_game_rect)
        screen.blit(intro_mes,intro_mes_rect)
        score_mes=medium_font.render(f'Your score: {score}',True,'#0066FF')
        score_mes_rect=score_mes.get_rect(center=(550,350))
        if score==0:
            screen.blit(play,play_rect)  
        else:
            screen.blit(score_mes,score_mes_rect)
        
    pygame.display.update() 
    clock.tick(60)