import pgzrun
from random import randint

HEIGHT=400
WIDTH=400
TITLE="ALIEN GAME"

message=""
ufo=Actor("space")

def draw():
    screen.clear()
    screen.fill(color=(230 ,201 ,150 ))
    ufo.draw()
    screen.draw.text(message,
                     topleft=(175, 10),
                     fontsize=30)
    
def place_ufo():
 
 ufo.x=randint(50, 350)
 ufo.y=randint(50, 350)


def on_mouse_down(pos):
   global message
   if ufo.collidepoint(pos):
      message ="nice shot"
      place_ufo()
   else:
      message="try again"



pgzrun.go()