
import unicodedata
import os
import sys
import time
import random

class FormatColors:
    def RED(text):
        newText = "\033[91m{}\033[00m".format(text)
        return newText
    def GREEN(text):
        newText = "\033[92m{}\033[00m".format(text)
        return newText
def GenMap(mapSize):
    
    n = mapSize
    m = mapSize
    map = [0] * n
    for i in range(n):
        map[i] = [FormatColors.RED(chr(9829))] * m
        
    #for x in range(20):
    #    for y in range(20):
    #        print(map)
    #        map[x][y] = chr(9674)
        

    return map

def Rendermap(map):
    os.system('cls')
    import itertools
    flatten_list = list(itertools.chain.from_iterable(map))
    printMap = ""
    for x in range(len(flatten_list)):
        printMap += str(flatten_list[x])

    print(printMap)
    



os.system('mode con: cols=20 lines=22')

MapSize = 20

map = GenMap(MapSize)

x = 0
y = 0  

snake = [(MapSize//2, MapSize//2)]
food = (random.randint(0, MapSize-1), random.randint(0, MapSize-1))

def move_snake(map, snake, food):
    for i in range(len(map)):
        for j in range(len(map[i])):
            map[i][j] = chr(9829)
    for body_part in snake:
        y, x = body_part
        map[y][x] = chr(9774)

    food_y, food_x = food
    map[food_y][food_x] = chr(36)

    head_x, head_y = snake[0]

    try: 
        key = ord(input().strip())

    except: 
        key = None
        pass

    if key == 97:
        new_head = (head_x, head_y -1)

    elif key == 100:
        new_head = (head_x, head_y +1)
    elif key == 69: 
        new_head = (head_x + 1, head_y)
    elif key == 83:
        new_head = (head_x -1, head_y)

    else:
        new_head = (head_x, head_y)

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            food = (random.randint(0, MapSize-1), random.randint(0, MapSize -1))
            if food in snake:
                food = None

    else: snake.pop()

    return snake, food, head_x, head_y

tick = 0
while True:
    tick = tick + 1
    Rendermap(map)
    snake, food, x, y = move_snake(map, snake, food)
    print("X: " + str(x) +" "+ "Y: " + str(y))
    time.sleep(1)
    print("Tick #" + str(tick))
    
      





