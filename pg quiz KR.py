import pyautogui as pg
import time
points = 0
# question 1

answer = pg.prompt (
    """
It's friday night, what are you doing?

a. traveling, of course
b. modeling in Milan
c.

"""
           )
#Give points

if answer == "a":
    points +=1
elif answer== "b":
    points +=2
elif answer == "c":
    points += 3

# question 2

answer = pg.prompt (
    """
What's your favorite social media platform?
a. snapchat
b. instaram
c. twitter 

"""
           )

#Give points

if answer == "a":
    points +=2
elif answer== "b":
    points +=1
elif answer == "c":
    points += 3

# question 3

answer = pg.prompt (
    """
What's your favorite thing to do?
a. be a queen
b. do your makeup
c. walk the world's greates runways
d. travel
e. just relax and live life
f. 


"""
           )

#Give points

if answer == "a":
    points +=1
elif answer== "b":
    points +=2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 3
elif answer == "e":
    points += 3
    
    # question 4

answer = pg.prompt (
    """
What's your favorite thing to do?
a. be a queen
b. do your makeup
c. walk the world's greates runways
d. travel
e. just relax and live life


"""
           )

#Give points

if answer == "a":
    points +=1
elif answer== "b":
    points +=2
elif answer == "c":
    points += 3

# question 5

answer = pg.prompt (
    """
How would you describe your personality?
a. relaxed, you just live life and go with the flow, and you always stay true to yourself. 
b. Your a queen and you know you are! You make the trends while others follow, and love being the center of attention(As long as its good).
c. Your really adventerous and love to try new things. You travel, try new foods, learn about different culture, and have fun with your friends. You are also the most private one and like to keep things to yourslef unless your sure of them. 
d. You love to take care of others, and you love being with family. You always have good intentions, but if someone hurts you friends or family, they should watch out,
e.


"""
           )

#Give points

if answer == "a":
    points +=1
elif answer== "b":
    points +=2
elif answer == "c":
    points += 3


#end of survey

if
    
