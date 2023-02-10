
import unicodedata
import os
import sys
import time
import termcolor
def GenMap(mapSize):
    
    n = mapSize
    m = mapSize
    map = [0] * n
    for i in range(n):
        map[i] = [chr(9829)] * m
        
    #for x in range(20):
    #    for y in range(20):
    #        print(map)
    #        map[x][y] = chr(9674)
        

    return map

def Rendermap(map):
    import itertools
    flatten_list = list(itertools.chain.from_iterable(map))
    printMap = ""
    for x in range(len(flatten_list)):
        printMap += str(flatten_list[x])

    print(printMap)
    

def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

os.system('mode con: cols=20 lines=22')

MapSize = 20

map = GenMap(MapSize)

x = 0
y = 0  

while True:
    Rendermap(map)
    time.sleep(0.5)
    map[x][y] = 1
    x = x + 1 
    y = y + 1
      





