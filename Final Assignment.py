#Final Vampire Game Jacky liu
#January 22 2019
#Jacky Liu

#imports Pygame
import pygame
from random import randint
pygame.init()
#imports keyboard stuff
pygame.event.get()

#-------------[window Variables]-------------[-][◻][x]
#Window size
WIDTH = 1200
HEIGHT = 600
#sets up the window
game_window = pygame.display.set_mode((WIDTH,HEIGHT))

BACKGROUND_X = 0
BACKGROUND_Y = 0


#----------------------------------------------------#


#∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞[Loop]∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞#
#Game Loop Variables
#starting loop
starting_loop = True
#main loop
in_play = False
game = True
#used for the game over loop
game_over = False
#∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞#


#\/\/\/\/\/\/\/\/\/\/\/\/\/\/COLOURING\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
BLACK = (0,0,0)
PURPLE = (128,0,128)
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

#~~~~~~~~~~~~~~~~~~~~~~~~~~[COUNTERS]~~~~~~~~~~~~~~~~~~~~~~~~~~#
#animation counter
animation_counter = 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
vampire_health = 3

#@@@@@@@@@@@@@@@@@@@@@@@@@@[Vampire Variables]@@@@@@@@@@@@@@@@@@@@@@@@@@#
# Character location vertical, horitzontal axis/locations (x,y)
vampire_x, vampire_y = 0,25
# the speed of the character
vampire_speed_x, vampire_speed_y = 1,1

#^^^^^^^^^^^^^^^^^^^^^^^^^^[ SUN/MOON ]^^^^^^^^^^^^^^^^^^^^^^
# the moon's location vertical, horitzontal axis/locations (x,y)
sun_moon_x, sun_moon_y = 0, 150
# the speed of the moon
sun_moon_speed_y, sun_moon_speed_x = 1,1

# Checks if it is night or not, false = night, true = day
day = False

#--------------------------[ Location of the tree ]-------------------------#
TREE_ONE_X = 900
TREE_ONE_Y = 52
TREE_TWO_X = 50
TREE_TWO_Y = 252


# I M A G I N G ################################################## IMAGING
#[IDLE DOWN IMAGE]
vampire_down_idle_wake = pygame.image.load("vampire_down_idle_wake.png")
vampire_down_idle_blink = pygame.image.load("vampire_down_idle_blink.png")
#[IDLE RIGHT IMAGE]
vampire_right_idle_wake = pygame.image.load("vampire_right_idle_wake.png")
vampire_right_idle_blink = pygame.image.load("vampire_right_idle_blink.png")
#[IDLE LEFT IMAGE]
vampire_left_idle_wake = pygame.image.load("vampire_left_idle_wake.png")
vampire_left_idle_blink = pygame.image.load("vampire_left_idle_blink.png")

#[IDLE UP IMAGE]
vampire_up_idle = pygame.image.load("vampire_up_idle.png")
#[RIGHT IMAGING]
vampire_right_one_blink = pygame.image.load("vampire_right_one_blink.png")
vampire_right_one_wake = pygame.image.load ("vampire_right_one_wake.png")
vampire_right_two_blink = pygame.image.load ("vampire_right_two_blink.png")
vampire_right_two_wake = pygame.image.load ("vampire_right_two_wake.png")
#[LEFT IMAGING]
vampire_left_one_blink = pygame.image.load("vampire_left_one_blink.png")
vampire_left_one_wake = pygame.image.load ("vampire_left_one_wake.png")
vampire_left_two_blink = pygame.image.load ("vampire_left_two_blink.png")
vampire_left_two_wake = pygame.image.load ("vampire_left_two_wake.png")
#[UP IMAGING]
vampire_up_one = pygame.image.load ("vampire_up_one.png")
vampire_up_two = pygame.image.load ("vampire_up_two.png")
# Vampire sizing, Since all the vmapire images are the same dimension I only need to collect the dimesion from only one instead of all the imaging
vampire_rect = vampire_up_one.get_rect()
vampire_width = vampire_rect.width
vampire_height = vampire_rect.height

#[DOWN IMAGING]
vampire_down_blink_two = pygame.image.load ("vampire_down_blink_two.png")
vampire_down_blink_one = pygame.image.load ("vampire_down_blink_one.png")
vampire_down_wake_two = pygame.image.load ("vampire_down_wake_two.png")
vampire_down_wake_one = pygame.image.load ("vampire_down_wake_one.png")
#[Background Screens]
day_time = pygame.image.load ("day_time.png")
night_time = pygame.image.load ("night_time.png")
#[SUN AND MOON]
sun_pic = pygame.image.load("sun.png")
moon_pic = pygame.image.load("moon.png")
#[Load Screen]
start_screen = pygame.image.load("start.png")
how_to_play_one = pygame.image.load("how_to_play_one.png")
how_to_play_two = pygame.image.load("how_to_play_two.png")
how_to_play_three = pygame.image.load("how_to_play_three.png")
how_to_play_four = pygame.image.load("how_to_play_four.png")
#[Game over]
game_over_image = pygame.image.load("game_over.png")
#[TREE]
tree_left = pygame.image.load ("tree_left.png")
# tree sizing stuff
tree_one_rect = tree_left.get_rect()
tree_two_rect = tree_left.get_rect()
tree_width = tree_one_rect.width
tree_height = tree_one_rect.height

# [ HEALTH BAR ]
health_bar = pygame.image.load ("health_bar.png")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
# HUMANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNn

human_right_one = pygame.image.load ("human_right_one.png")
human_right_two = pygame.image.load ("human_right_two.png")
human_right_three = pygame.image.load ("human_right_three.png")


human_left_one = pygame.image.load ("human_left_one.png")
human_left_two = pygame.image.load ("human_left_two.png")
human_left_three = pygame.image.load ("human_left_three.png")


# HUMANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNn

hunter_right_one = pygame.image.load ("hunter_right_one.png")
hunter_right_two = pygame.image.load ("hunter_right_two.png")
hunter_right_three = pygame.image.load ("hunter_right_three.png")


hunter_left_one = pygame.image.load ("hunter_left_one.png")
hunter_left_two = pygame.image.load ("hunter_left_two.png")
hunter_left_three = pygame.image.load ("hunter_left_three.png")

hunter_rect = hunter_right_one.get_rect()
hunter_width = hunter_rect.width
hunter_height = hunter_rect.height

#music
game_music = pygame.mixer.Sound("game_music.wav")
##human hit box sizing stuff

# collision boxing of fthe humans
human_one_rect = human_right_one.get_rect()
human_two_rect = human_right_one.get_rect()
# the width and height of the image
human_width = human_one_rect.width
human_height = human_one_rect.height

#the font and size
font = pygame.font.SysFont("Courier New Bold",36)

#`````````````````````````[facing location]`````````````````````````#
NOTHING = 0
#Used for the direction that vampire will be facing
#Used to check if vampire went up
UP = 1
#used to check if vampire went right
RIGHT = 2
#Used to check if vampire went down
DOWN = 3
#Used to check if vampire went left
LEFT = 4

#Human Variables
# the human's & and hunters location vertical, horitzontal axis/locations (x,y)
human_one_x, human_one_y = 5,250

human_two_x , human_two_y = 1100, 500

hunter_x , hunter_y = 10, 400

# the humans and hunter's speed
human_one_speed_x, human_one_speed_y, human_two_speed_x, human_two_speed_y, hunter_speed_x, hunter_speed_y  = 1,1,1,1,1,1

#used to check to spawn the humans + hunter
human_one = False
human_two = False
hunter = True
#sets the location to face for the animation
human_one_location, human_two_location, hunter_location = RIGHT, RIGHT, RIGHT
#sets the lcoation to starting position for the vampire to face
vampire_location = DOWN
#used to check if the vampire is idle/not movin
idle = True
# health bar location
HEALTH_X, HEALTH_Y = 0,0

#---------[Colour variables]---------
GREEN = (125,225,0)
YELLOW = (225,225,0)
RED = (225,0,0)



#score counter and day
score_counter, day_counter = 0,0

#Used for random spawn or random eat
spawn, eat_scam = 0, 0
#no = False, yes = True (yes and no used so that it is not confused with the built in true and false)
NO = 0
YES = 1

start_screen_counter = 0 
#```````````````````````````````````````````````````````````````````#

#..........................Subprograms..........................#

#Moon/Sun subprogram
#this subprogram "rises up" the sun/moon till about 1/4 of the playing area
#and continues to add 1 from the very start until it reaches the outside of the windows
#as well as it "moon/sun sets" the sun/moon around 3/4 of the playing area until it reaches the outside of the rightside of the windows
#then goes to the right till it reaches to the outside of the rightside of the screen
#and resets back to the outside of the left side of the screen and continues again and again
def sun_moon():
    #imports variable
    global sun_moon_x, sun_moon_y, sun_moon_speed_y, sun_moon_speed_x, day
    #Moving to the right
    sun_moon_x = sun_moon_x + sun_moon_speed_x
    #as long as the sun/moon is on 1/4ish of the screen it will rise
    if sun_moon_x <= 150:
        #subtracts from the y making it rise
        sun_moon_y = sun_moon_y - sun_moon_speed_y
    #as long as the sun/moon is on 3/4ish of the screen it will set down
    elif sun_moon_x >= 1050:
        #adds 1 to lower it
        sun_moon_y = sun_moon_y + sun_moon_speed_y
    #if the sun/moon is outof the screen on the rightside, it will reset to outside of the left side
    #as well as when it reaches to the outside it will turn to night or day
    if sun_moon_x >= WIDTH+50:
        #sets it out of the screen on the left
        sun_moon_x = 0
        #sets it in the sky
        sun_moon_y = 150
        #if it is day time
        if day == True:
            #it will go to night
            day = False
        #if it night then it will become day
        else:
            day = True
# make 0 constant and 1
    
    #drawing the sun/moon
    #if is day time it will draw the sun image
    #if it is night time it will draw the moon image
    if day == True:
        
        game_window.blit(sun_pic, (sun_moon_x, sun_moon_y))

    elif day == False:
        game_window.blit(moon_pic, (sun_moon_x, sun_moon_y))
        

   
        
#Subprogram for moving the vampire
def controls():
    global vampire_location, vampire_x, vampire_y, idle
    
    #if user presses W the main character will go up by subtracting the y
    #as well as set the vampire_location to up so that it is used for drawing the proper direction
    #sets the idle to false
    if keys[pygame.K_UP]:
        idle = False        
        vampire_y = vampire_y - vampire_speed_y
        vampire_location = UP
    #if user presses s the main character will go down by adding the y
    #as well as set the vampire_location to up so that it is used for drawing the proper direction
    #sets the idle to false
    elif keys[pygame.K_DOWN]:
        vampire_y = vampire_y + vampire_speed_y
        vampire_location = DOWN
        idle = False
    #if user presses A the main character will go left by subtracting the x
    #as well as set the location to up so that it is used for drawing the proper direction
    #sets the idle to false
    elif keys[pygame.K_LEFT]:
        vampire_x = vampire_x - vampire_speed_x
        vampire_location = LEFT
        idle = False
    #if user presses d the main character will go down by adding the x
    #as well as set the location to up so that it is used for drawing the proper direction
    #sets the idle to false
    elif keys[pygame.K_RIGHT]:
        vampire_x = vampire_x + vampire_speed_x
        vampire_location = RIGHT
        idle = False
    #Used for the character's idle animation
    else:
        ##if no keys are pressed than idle will be true
        idle = True

#Subprogram for the vampire to die
def dying():
    #imports variables
    global vampire_health, day, sun_moon_x, vampire_rect, game_over, in_play
    #draws the health bar template thing (The gray thing)
    game_window.blit(health_bar,(HEALTH_X,HEALTH_Y))

    #collects the 'hitbox'/ the sizing of the box
    tree_one_rect = pygame.Rect(TREE_ONE_X,TREE_ONE_Y,tree_width,tree_height)
    tree_two_rect = pygame.Rect(TREE_TWO_X,TREE_TWO_Y,tree_width,tree_height)
    vampire_rect = pygame.Rect(vampire_x,vampire_y,vampire_width,vampire_height)
    
    #if it is day and the vampire is not under the tree the vampire will be set to 0 and will instantly die
    if day == True and vampire_rect.colliderect(tree_two_rect) == False and vampire_rect.colliderect(tree_one_rect) == False:
        vampire_health = 0
    #if it is night/ day is false and the moon is at the left side it will lose a health
    if day == False and sun_moon_x == 0:
        vampire_health = vampire_health - 1
    #checks iif the vampire health is 0 the game loop will stop and the game over screen will be shown
    if vampire_health <= 0:
        in_play = False
        game_over = True
    #if the vampire is at 3 health it will draw 3 green squares to show that it is full on healh
    elif vampire_health == 3:
        pygame.draw.rect(game_window, GREEN, (HEALTH_X+75,HEALTH_Y+7,30, 30), 0)
        pygame.draw.rect(game_window, GREEN, (HEALTH_X+15,HEALTH_Y+7,30, 30), 0)
        pygame.draw.rect(game_window, GREEN, (HEALTH_X+45,HEALTH_Y+7,30, 30), 0)
    #if the vampire is at 2 healht it will draw 2 yellow squares to indicate it is medium health
    elif vampire_health == 2:
        pygame.draw.rect(game_window, YELLOW, (HEALTH_X+15,HEALTH_Y+7,30, 30), 0)
        pygame.draw.rect(game_window, YELLOW, (HEALTH_X+45,HEALTH_Y+7,30, 30), 0)
    #if the vampire is at 1 health it will draw 1 red square to indicate it is low on health
    elif vampire_health == 1:
        pygame.draw.rect(game_window, RED, (HEALTH_X+15,HEALTH_Y+7,30, 30), 0)

#human/hunter subprogram    
def human():
    #imports variables from aboe
    global human_one_x, human_one_y,human_two_x, human_two_y, human_one_speed_x, human_one_speed_y, human_one, human_two, day
    global human_one_location, human_two_location, RIGHT, LEFT, human_two_speed_x, human_two_speed_y, spawn, YES, NO
    global hunter_x, hunter_y, hunter_speed_y, hunter_speed_x, hunter_location, hunter

    #checks if the day is true and the sun is on the left
    if day == True and sun_moon_x == 0:
        #the hunters and both humans will respawn
        human_one = True
        human_two = True
        hunter = True
    #checks if it is night and the moon is at the start of the left part
    elif day == False and sun_moon_x == 1:
        #randomly sets the human two spawn
        spawn = randint (NO,YES)
        #if spawn is true human two will spanw and human one will be false
        if spawn == YES:
            human_one = False
            human_two = True
        #if the spawn is false both humans will be false
        else:
            human_one = False
            human_two = False

    if hunter == True:
        #Boundry stuff, if the human hits the top or bottom of the play area
        if hunter_y >= HEIGHT-50 or hunter_y <= 239:
            #the human will go backwards
            hunter_speed_y = -hunter_speed_y
        #Boundry if the human hits the sides of the playing area 
        if hunter_x >= WIDTH-20 or hunter_x <= 0:
            #the human will go backwards
            hunter_speed_x = -hunter_speed_x
            if hunter_location == RIGHT:
                hunter_location = LEFT
            else:
                hunter_location = RIGHT
            #Keeps the human moving
        hunter_x = hunter_x + hunter_speed_x
        hunter_y = hunter_y + hunter_speed_y
        
    #checks if the human is out
    if human_one == True:
        #Boundry stuff, if the human hits the top or bottom of the play area
        if human_one_y >= HEIGHT-50 or human_one_y <= 239:
            #the human will go backwards
            human_one_speed_y = -human_one_speed_y
        #Boundry if the human hits the sides of the playing area 
        if human_one_x >= WIDTH-20 or human_one_x <= 0:
            #the human will go backwards
            human_one_speed_x = -human_one_speed_x
            if human_one_location == RIGHT:
                human_one_location = LEFT
            else:
                human_one_location = RIGHT
            #Keeps the human moving
        human_one_x = human_one_x + human_one_speed_x
        human_one_y = human_one_y + human_one_speed_y
                
    #checks if the human is out
    if human_two == True:
        #Boundry stuff, if the human hits the top or bottom of the play area
        if human_two_y >= HEIGHT-50 or human_two_y <= 239:
            #the human will go backwards
            human_two_speed_y = -human_two_speed_y
        #Boundry if the human hits the sides of the playing area 
        if human_two_x >= WIDTH-20 or human_two_x <= 0:
            #the human will go backwards
            human_two_speed_x = -human_two_speed_x
            if human_two_location == LEFT:
                human_two_location = RIGHT
            else:
                human_two_location = LEFT     
        
        #Keeps the human moving
        human_two_x = human_two_x + human_two_speed_x
        human_two_y = human_two_y + human_two_speed_y
        
#Subprogram for when the vampire eats the hunters or human
def eating():
    #imports variables from above
    global human_one_x, human_one_y, vampire_health, keys, vampire_rect, score_counter, human_one, human_two, human_three, vampire_rect, eat_scam, YES, NO, hunter

    #collects the 'hitbox' rectangle sizing for the humans and hunter
    human_one_rect = pygame.Rect(human_one_x,human_one_y,human_width,human_height)
    human_two_rect = pygame.Rect(human_two_x,human_two_y,human_width,human_height)
    hunter_rect = pygame.Rect(hunter_x,hunter_y,hunter_width,hunter_height)

    #checks if the user presses space the vampire still hasless than 3 health
    if keys[pygame.K_SPACE] and vampire_health < 3:
        #checks if the vampire collides with the  1st human and the 1st human is true, or the vampires collides with the 2nd human and the 2human is true
        if vampire_rect.colliderect(human_one_rect) and human_one == True or vampire_rect.colliderect(human_two_rect) and human_two == True:
            #50 will be added to the score
            score_counter = score_counter + 50

        #chekcs if the vampire collides with the hunter and the hunter is true
        if vampire_rect.colliderect(hunter_rect) and hunter == True:
            #make the hunter 'run away' or 'die'
            hunter = False
            #random chance of the vampire eating or 
            eat_scam = randint (NO,YES)
            #Chekcs if the vampire gets scammed
            if eat_scam == NO:
                #if they the vampire doesnt get scammed they get 1 health added
                vampire_health = vampire_health + 1
                #adds 200 to the score for the succesful attempt
                score_counter = score_counter + 200
            #checks if the vampire does get scammed, if do get scammed they lose 1 health
            elif eat_scam == YES:
                vampire_health = vampire_health - 1
                #adds 100 to the score
                score_counter = score_counter + 100
                
        if vampire_rect.colliderect(human_one_rect) and human_one == True:
            human_one = False
            vampire_health = vampire_health + 1
        if vampire_rect.colliderect(human_two_rect) and human_two == True:
            human_two = False
            vampire_health = vampire_health + 1
            
#subprogram for score
def score():
    #Imports variables from above
    global day, score_counter, day_counter, sun_moon_x
    #checks if the day is true and the sun is at the very start of the left
    if day == True and sun_moon_x == 0:
        #adds 1 to the day counter
        day_counter = day_counter + 1
        #gives 10 score
        score_counter = score_counter + 10
    #sets the scores
    score_text = font.render("Score: " + str(score_counter) + "  Day: " + str(day_counter),1,PURPLE)
    #draws the score
    game_window.blit(score_text,(150,1))


# subrpgraom for Animation
def animation():
    #collects the variables from above
    global animation_counter, vampire_x, vampire_y, idle, human_one_location, human_one, human_one_x, human_one_y, human_two_x, human_two_y, vampire_location
    global LEFT,RIGHT,UP,DOWN
    #continuosly adds 1 to the animation counter
    animation_counter = animation_counter + 1
    #if the animation counter adds to 128 it will reset to 0
    if animation_counter == 128:
        animation_counter = 0
        
    #DRAWS THE HUNTER LEFT ANIMATION
    #checks if the hunter is facing left and the hunter is true then it will draw the image during the animation counter times
    if hunter_location == LEFT and hunter == True:
        if animation_counter >= 0 and animation_counter < 16:
            game_window.blit(hunter_left_two, (hunter_x, hunter_y))
        elif animation_counter >= 16 and animation_counter < 32:
            game_window.blit(hunter_left_one, (hunter_x, hunter_y))
        elif animation_counter >= 32 and animation_counter < 48:
            game_window.blit(hunter_left_two, (hunter_x, hunter_y))
        elif animation_counter >= 48 and animation_counter <= 64:
            game_window.blit(hunter_left_three, (hunter_x, hunter_y))
        elif animation_counter >= 64 and animation_counter < 80:
            game_window.blit(hunter_left_two, (hunter_x, hunter_y))
        elif animation_counter >= 80 and animation_counter < 96:
            game_window.blit(hunter_left_one, (hunter_x, hunter_y))
        elif animation_counter >= 96 and animation_counter < 112:
            game_window.blit(hunter_left_two, (hunter_x, hunter_y))
        elif animation_counter >= 112 and animation_counter <= 128:
            game_window.blit(hunter_left_three, (hunter_x, hunter_y))
            
    #HUNTER RIGHT WALKINTG ANIMATION
    if hunter_location == RIGHT and hunter == True:
        if animation_counter >= 0 and animation_counter < 16:
            game_window.blit(hunter_right_two, (hunter_x, hunter_y))
        elif animation_counter >= 16 and animation_counter < 32:
            game_window.blit(hunter_right_one, (hunter_x, hunter_y))
        elif animation_counter >= 32 and animation_counter < 48:
            game_window.blit(hunter_right_two, (hunter_x, hunter_y))
        elif animation_counter >= 48 and animation_counter <= 64:
            game_window.blit(hunter_right_three, (hunter_x, hunter_y))
        elif animation_counter >= 64 and animation_counter < 80:
            game_window.blit(hunter_right_two, (hunter_x, hunter_y))
        elif animation_counter >= 80 and animation_counter < 96:
            game_window.blit(hunter_right_one, (hunter_x, hunter_y))
        elif animation_counter >= 96 and animation_counter < 112:
            game_window.blit(hunter_right_two, (hunter_x, hunter_y))
        elif animation_counter >= 112 and animation_counter <= 128:
            game_window.blit(hunter_right_three, (hunter_x, hunter_y))

    #DRAWS THE HUMAN ONE left walking ANIMATIONNN
    if human_one_location == LEFT and human_one == True:
        if animation_counter >= 0 and animation_counter < 16:
            game_window.blit(human_left_two, (human_one_x, human_one_y))
        elif animation_counter >= 16 and animation_counter < 32:
            game_window.blit(human_left_one, (human_one_x, human_one_y))
        elif animation_counter >= 32 and animation_counter < 48:
            game_window.blit(human_left_two, (human_one_x, human_one_y))
        elif animation_counter >= 48 and animation_counter <= 64:
            game_window.blit(human_left_three, (human_one_x, human_one_y))
        elif animation_counter >= 64 and animation_counter < 80:
            game_window.blit(human_left_two, (human_one_x, human_one_y))
        elif animation_counter >= 80 and animation_counter < 96:
            game_window.blit(human_left_one, (human_one_x, human_one_y))
        elif animation_counter >= 96 and animation_counter < 112:
            game_window.blit(human_left_two, (human_one_x, human_one_y))
        elif animation_counter >= 112 and animation_counter <= 128:
            game_window.blit(human_left_three, (human_one_x, human_one_y))
    #HUman one RIGHT WLAKINTG ANIMATION
    if human_one_location == RIGHT and human_one == True:
        if animation_counter >= 0 and animation_counter < 16:
            game_window.blit(human_right_two, (human_one_x, human_one_y))
        elif animation_counter >= 16 and animation_counter < 32:
            game_window.blit(human_right_one, (human_one_x, human_one_y))
        elif animation_counter >= 32 and animation_counter < 48:
            game_window.blit(human_right_two, (human_one_x, human_one_y))
        elif animation_counter >= 48 and animation_counter <= 64:
            game_window.blit(human_right_three, (human_one_x, human_one_y))
        elif animation_counter >= 64 and animation_counter < 80:
            game_window.blit(human_right_two, (human_one_x, human_one_y))
        elif animation_counter >= 80 and animation_counter < 96:
            game_window.blit(human_right_one, (human_one_x, human_one_y))
        elif animation_counter >= 96 and animation_counter < 112:
            game_window.blit(human_right_two, (human_one_x, human_one_y))
        elif animation_counter >= 112 and animation_counter <= 128:
            game_window.blit(human_right_three, (human_one_x, human_one_y))   

            

    #DRAWS THE HUMAN two left walking ANIMATIONNN
    if human_two_location == LEFT and human_two == True:
        if animation_counter >= 0 and animation_counter < 16:
            game_window.blit(human_left_two, (human_two_x, human_two_y))
        elif animation_counter >= 16 and animation_counter < 32:
            game_window.blit(human_left_one, (human_two_x, human_two_y))
        elif animation_counter >= 32 and animation_counter < 48:
            game_window.blit(human_left_two, (human_two_x, human_two_y))
        elif animation_counter >= 48 and animation_counter <= 64:
            game_window.blit(human_left_three, (human_two_x, human_two_y))
        elif animation_counter >= 64 and animation_counter < 80:
            game_window.blit(human_left_two, (human_two_x, human_two_y))
        elif animation_counter >= 80 and animation_counter < 96:
            game_window.blit(human_left_one, (human_two_x, human_two_y))
        elif animation_counter >= 96 and animation_counter < 112:
            game_window.blit(human_left_two, (human_two_x, human_two_y))
        elif animation_counter >= 112 and animation_counter <= 128:
            game_window.blit(human_left_three, (human_two_x, human_two_y))
    #HUman two RIGHT WLAKINTG ANIMATION
    if human_two_location == RIGHT and human_two == True:
        if animation_counter >= 0 and animation_counter < 16:
            game_window.blit(human_right_two, (human_two_x, human_two_y))
        elif animation_counter >= 16 and animation_counter < 32:
            game_window.blit(human_right_one, (human_two_x, human_two_y))
        elif animation_counter >= 32 and animation_counter < 48:
            game_window.blit(human_right_two, (human_two_x, human_two_y))
        elif animation_counter >= 48 and animation_counter <= 64:
            game_window.blit(human_right_three, (human_two_x, human_two_y))
        elif animation_counter >= 64 and animation_counter < 80:
            game_window.blit(human_right_two, (human_two_x, human_two_y))
        elif animation_counter >= 80 and animation_counter < 96:
            game_window.blit(human_right_one, (human_two_x, human_two_y))
        elif animation_counter >= 96 and animation_counter < 112:
            game_window.blit(human_right_two, (human_two_x, human_two_y))
        elif animation_counter >= 112 and animation_counter <= 128:
            game_window.blit(human_right_three, (human_two_x, human_two_y))

            
    #$$$$$$$$$$$$$$$$$$$$$$$$$ [WALKING ANIMATION] $$$$$$$$$$$$$$$$$$$$
    # Used for the vampire walking down animation
    if vampire_location == DOWN and idle == False:
        if animation_counter >= 0 and animation_counter < 32:
            game_window.blit(vampire_down_wake_one, (vampire_x, vampire_y))
        elif animation_counter >= 32 and animation_counter < 64:
            game_window.blit(vampire_down_blink_two, (vampire_x, vampire_y))
        elif animation_counter >= 64 and animation_counter < 96:
            game_window.blit(vampire_down_wake_one, (vampire_x, vampire_y))
        elif animation_counter >= 96 and animation_counter <= 128:
            game_window.blit(vampire_down_blink_two, (vampire_x, vampire_y))
    # used for vampire walking right animation
    elif vampire_location == RIGHT and idle == False:
        if animation_counter >= 0 and animation_counter < 32:
            game_window.blit(vampire_right_one_blink, (vampire_x, vampire_y))
        elif animation_counter >= 32 and animation_counter < 64:
            game_window.blit(vampire_right_two_wake, (vampire_x, vampire_y))
        elif animation_counter >= 64 and animation_counter < 96:
            game_window.blit(vampire_right_two_blink, (vampire_x, vampire_y))
        elif animation_counter >= 96 and animation_counter <= 128:
            game_window.blit(vampire_right_one_wake, (vampire_x, vampire_y))
    # used for vampire walking left animaiton
    elif vampire_location == LEFT and idle == False:
        if animation_counter >= 0 and animation_counter < 32:
            game_window.blit(vampire_left_one_blink, (vampire_x, vampire_y))
        elif animation_counter >= 32 and animation_counter < 64:
            game_window.blit(vampire_left_one_wake, (vampire_x, vampire_y))
        elif animation_counter >= 64 and animation_counter < 96:
            game_window.blit(vampire_left_two_blink, (vampire_x, vampire_y))
        elif animation_counter >= 96 and animation_counter <= 128:
            game_window.blit(vampire_left_two_wake, (vampire_x, vampire_y))
    # used for vampire wlaking up animaion
    elif vampire_location == UP and idle == False:
        if animation_counter >= 0 and animation_counter < 32:
            game_window.blit(vampire_up_one, (vampire_x, vampire_y))
        elif animation_counter >= 32 and animation_counter < 64:
            game_window.blit(vampire_up_two, (vampire_x, vampire_y))
        elif animation_counter >= 64 and animation_counter < 96:
            game_window.blit(vampire_up_one, (vampire_x, vampire_y))
        elif animation_counter >= 96 and animation_counter <= 128:
            game_window.blit(vampire_up_two, (vampire_x, vampire_y))
            
    #$$$$$$$$$$$$$$$$$$$$$$$$$$[ IDLE IMAGING ]$$$$$$$$$$$$$$$$$$$$$$$$#
    #if the vampire is idling down it will make it blink
    elif vampire_location == DOWN and idle == True:
        if animation_counter >= 0 and animation_counter < 32:
            game_window.blit(vampire_down_idle_wake, (vampire_x, vampire_y))
        elif animation_counter >= 32 and animation_counter < 64:
            game_window.blit(vampire_down_idle_blink, (vampire_x, vampire_y))
        elif animation_counter >= 64 and animation_counter < 96:
            game_window.blit(vampire_down_idle_wake, (vampire_x, vampire_y))
        elif animation_counter >= 96 and animation_counter <= 128:
            game_window.blit(vampire_down_idle_blink, (vampire_x, vampire_y))
    #vampire right idle blink animation
    elif vampire_location == RIGHT and idle == True:
        if animation_counter >= 0 and animation_counter < 32:
            game_window.blit(vampire_right_idle_wake, (vampire_x, vampire_y))
        elif animation_counter >= 32 and animation_counter < 64:
            game_window.blit(vampire_right_idle_blink, (vampire_x, vampire_y))
        elif animation_counter >= 64 and animation_counter < 96:
            game_window.blit(vampire_right_idle_wake, (vampire_x, vampire_y))
        elif animation_counter >= 96 and animation_counter <= 128:
            game_window.blit(vampire_right_idle_blink, (vampire_x, vampire_y))
    #vampire left idle blink animation
    elif vampire_location == LEFT and idle == True:
        if animation_counter >= 0 and animation_counter < 32:
            game_window.blit(vampire_left_idle_blink, (vampire_x, vampire_y))
        elif animation_counter >= 32 and animation_counter < 64:
            game_window.blit(vampire_left_idle_wake, (vampire_x, vampire_y))
        elif animation_counter >= 64 and animation_counter < 96:
            game_window.blit(vampire_left_idle_blink, (vampire_x, vampire_y))
        elif animation_counter >= 96 and animation_counter <= 128:
            game_window.blit(vampire_left_idle_wake, (vampire_x, vampire_y))
        #vampire up idle
    elif vampire_location == UP and idle == True:
        game_window.blit(vampire_up_idle, (vampire_x, vampire_y))
    
#subprogram for the vampire's border
def border():
    #Declare Variable
    global vampire_x , vampire_y
    #borders
    #if vampire wants to go out of the screen on the left side, it will keep teleporting
    #it to 0 to prevent it from going over
    if vampire_x <= 0:
        vampire_x = 0
    #if vampire wants to go out of the playing area/ground on the top side, it will keep teleporting
    #it to 350 to prevent it from going over the ground/playing area
    if vampire_y <= 250:
        vampire_y = 250
    #if vampire wants to go under the playing area/ground on the bottom side, it will not allow vampire to do that
    #it will keep teleporting vampire the height and a little less so that the character image will stay in the window
    if vampire_y >= HEIGHT-99:
        vampire_y = HEIGHT-99
    
    #if vampire wants to go over the window on the right side, it will not allow vampire to do that
    #it will keep teleporting vampire the width and a little less so that the character image will stay in the window
    if vampire_x >= WIDTH-51:
        vampire_x = WIDTH-51
        
#Subprogram for drawing trees
def trees():
    #imports variables
    global TREE_ONE_X, TREE_ONE_Y,TREE_TWO_X, TREE_TWO_Y
    #drwas the trees
    game_window.blit(tree_left, (TREE_ONE_X, TREE_ONE_Y))
    game_window.blit(tree_left, (TREE_TWO_X, TREE_TWO_Y))             
            

            
    
################# GAME LOOPS #################
while starting_loop:
    
    #Clears the Screen
    pygame.event.clear()
   
    #Key storing
    keys = pygame.key.get_pressed()
    #Checks if the player pressed space, and if they did it will start the in_play loop where the actual
    #game stuff happens
    if keys[pygame.K_SPACE]:
        #checks if the counter is equal to 4/ on the last insturction slide, it will start the game
        if start_screen_counter == 4:
            in_play = True
            starting_loop = False            
    #If user presses the escape key they can quitt my horrible program by turning the starting loop to false and going to pygame.quit
    if keys[pygame.K_ESCAPE]:
        starting_loop = False

    #Checks if user press from 1-4, if they do it will set the counter correpsonding to the key they press
    if keys[pygame.K_1]:
        start_screen_counter = 1
    elif keys[pygame.K_2]:
        start_screen_counter = 2
    elif keys[pygame.K_3]:
        start_screen_counter = 3
    elif keys[pygame.K_4]:
        start_screen_counter = 4

    #if the screen counter is set to from 1-4 it will draw the corresponding key pressed
    if start_screen_counter == 0:
        game_window.blit(start_screen, (BACKGROUND_X, BACKGROUND_Y))
    elif start_screen_counter == 1:
        game_window.blit(how_to_play_one, (BACKGROUND_X, BACKGROUND_Y))
    elif start_screen_counter == 2:
        game_window.blit(how_to_play_two, (BACKGROUND_X, BACKGROUND_Y))
    elif start_screen_counter == 3:
        game_window.blit(how_to_play_three, (BACKGROUND_X, BACKGROUND_Y))
    elif start_screen_counter == 4:
        game_window.blit(how_to_play_four, (BACKGROUND_X, BACKGROUND_Y))
        
    
    #updates the screen
    pygame.display.update()

    
##########this is the loop where all the real stuff happnes###########
while in_play:
    #clears the screen
    pygame.event.clear()
    #plays music
    game_music.play()
    #checks if it is day
    if day == True:
        #Draws starting screen
        game_window.blit(day_time, (BACKGROUND_X, BACKGROUND_Y))
    #checks if it is night
    else:
        #Draws starting screen
        game_window.blit(night_time, (BACKGROUND_X, BACKGROUND_Y))
        

    #Key storing
    keys = pygame.key.get_pressed()
    #subprograms
    controls()
    sun_moon()
    border()
    dying()
    eating()
    animation()
    human()
    trees()
    score()
    #If user presses the escape key they can quitt my  program by turning the starting loop to false and going to pygame.quit
    if keys[pygame.K_ESCAPE]:
        #ends the loop
        in_play = False
    #delays the screen          
    pygame.time.delay(5)    
    #updates the screen
    pygame.display.update()

while game_over:
    #clears the screen
    pygame.event.clear()
    #draws the game over image
    game_window.blit(game_over_image, (BACKGROUND_X, BACKGROUND_Y))
        
    #Key storing
    keys = pygame.key.get_pressed()
    #writes the final score
    score_text = font.render("Final Score: " + str(score_counter) + " You Survived: " + str(day_counter) + " day(s)",1,PURPLE)
    #draws the score
    game_window.blit(score_text,(150,1))
    #checks if space is pressed
    if keys[pygame.K_SPACE]:
        #loop will end
        game_over = False
    #updates the screen
    pygame.display.update() 
    
#quits the program if the loops are false
pygame.quit()
