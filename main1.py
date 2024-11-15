import pgzrun
from pgzhelper import *
import random




WIDTH = 1200
HEIGHT = 700

player_idle = [
    "player/right/idle/tile000",
    "player/right/idle/tile001",
    "player/right/idle/tile002",
    "player/right/idle/tile003"
]

player_attack = [
    "player/right/attack/tile004",
    "player/right/attack/tile005",
    "player/right/attack/tile006",
    "player/right/attack/tile007",
    "player/right/attack/tile008",
    "player/right/attack/tile009",
    "player/right/attack/tile010"
]

player_attack2 = [
    "player/right/attack2/tile011",
    "player/right/attack2/tile012",
    "player/right/attack2/tile013",
    "player/right/attack2/tile014",
    "player/right/attack2/tile015",
    "player/right/attack2/tile016",
    "player/right/attack2/tile017",
    "player/right/attack2/tile018",
    "player/right/attack2/tile019",
]

player_death = [
    "player/right/death/tile020",
    "player/right/death/tile021",
    "player/right/death/tile022",
    "player/right/death/tile023",
    "player/right/death/tile024",
    "player/right/death/tile025",
    "player/right/death/tile026",
    "player/right/death/tile027",
]

enemy_idle = [
    "enemy/idle/tile000",
    "enemy/idle/tile001",
    "enemy/idle/tile002",
    "enemy/idle/tile003"
]

enemy_attack = [
    "enemy/attack/tile004",
    "enemy/attack/tile005",
    "enemy/attack/tile006",
    "enemy/attack/tile007",
    "enemy/attack/tile008",
    "enemy/attack/tile009"
]

enemy_attack2 = [
    "enemy/attack2/tile009",
    "enemy/attack2/tile010",
    "enemy/attack2/tile011",
    "enemy/attack2/tile012",
    "enemy/attack2/tile013",
    "enemy/attack2/tile014"
]

enemy_death = [
    "enemy/death/tile015",
    "enemy/death/tile016",
    "enemy/death/tile017",
    "enemy/death/tile018",
    "enemy/death/tile019",
    "enemy/death/tile020"
]




player = Actor(player_idle[0])
player.images = player_idle
player.left = -35
player.bottom = HEIGHT + 90 
player.scale = 0.8
player.fps = 6
player.hp = 100

enemy = Actor(enemy_idle [0])
enemy.images = enemy_idle
enemy.right = WIDTH - 30
enemy.bottom = HEIGHT - 30
enemy.scale = 1.3
enemy.fps = 8


questionBank = (['attack', 'spell', 'slash','defeat','slay'])
question = random.choice(questionBank)
typed = ''
typed_status = 'incomplete'





def update():
    global typed, question, typed_status
    if player.image != player_death [-1]:
        player.animate()
    enemy.animate()
    if player.hp <= 0 and player.image not in player_death:
        player.images = player_death
    # elif player.hp <= 0 and player.image == player_death [-1]:
    #     player.image = player_death [-1]




    if enemy.collide_pixel(player):
        enemy.images = enemy_death
    if player_attack[-1] == player.image:
        player.images = player_idle
        player.left = -35
        player.fps = 6
    if player_attack2[-1] == player.image:
        player.images = player_idle
    if enemy_death [-1] == enemy.image:
        enemy.images = enemy_idle
        enemy.right = WIDTH - 30
        enemy.bottom = HEIGHT - 30
    if enemy_attack [-1] == enemy.image:
        enemy.images = enemy_idle





    
    
def on_key_down(key):
    global typed, question, typed_status
    
    if key in range(97, 123):
        #print(chr(key))
        typed += chr(key)
    
    if key == 13:
        typed_status = 'complete'

    if key == 32:
        typed += ' '

    if key == 8:
        typed = typed[0:-1]



    if typed_status == 'complete':
        if typed == question:
            typed_status = 'incomplete'
            typed = ''
            player.images = player_attack
            player.x = enemy.left + 70
            player.fps = 8
            enemy.images = enemy_death
            question = random.choice(questionBank)
        elif typed != question:
            enemy.images = enemy_attack
            typed = ''
            typed_status = 'incomplete'
            player.hp -= 5
        


        
def draw():
    screen.clear()
    screen.draw.filled_rect(Rect(player.x - 30, player.top, 100, 20), 'red')
    screen.draw.filled_rect(Rect(player.x-30, player.top, player.hp, 20), 'green')
    screen.draw.text(question, (20, 100), fontsize=60)
    screen.draw.text(typed, (20, 100), fontsize=60, color='orange')
    enemy.draw()
    player.draw()

pgzrun.go()