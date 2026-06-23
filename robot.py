from importlib.resources import path
import random
from collections import deque
size = 5
def create_grid(size): 
    m = []
    for i in range(size):
        m.append(["-"] * size)
    
    m[0][0] = "S"
    m[size-1][size-1] = "T"
    obs = 0
    
    while (obs < 3):
        l = random.randint(0, size-1)
        c = random.randint(0, size-1)
        if m[l][c] == "-" and (l != 0 or c != 1) and (l != 1 or c != 0) and (l!=4 or c!=3):
            m[l][c] = "O"
            obs += 1
            
    return m

def display_grid(m):
    for i in m:
        print(" ".join(i))
    print("                ")


def move_agent(m, start, target):
     
    x,y = start
    tx, ty = target
    newX, newY = x, y
    #def deplacement(x, y, tx, ty):
    if x < tx:   # x : start  et tx : target
        newX = x+1
    elif x > tx:
        newX = x-1
    elif y < ty:
        newY = y+1
    elif y > ty:
        newY = y-1
        
    if 0 <= newX < len(m) and  0 <= newY < len(m) :
        if m[newX][newY] != "O":
            return (newX, newY)
    
    if m[newX][newY] == "O":
        print("it's an obstacle cannot move.")
    
    direction = [(0,1), (0,-1), (1,0), (-1,0)] # right(0,j+1), left(0,j-1), down(i+1,0), up(i-1,0)
    for dx, dy in direction:
        new_X = x + dx
        new_Y = y + dy
        if 0 < new_X < len(m) and 0 < new_Y < len(m) :
            if m[new_X][new_Y] != "O":
                return (new_X, new_Y)
    
    return start

def simulation(m) :
    start = (0, 0)
    target = (size-1, size-1)
    current_position = start
    etap = 1
    while current_position != target:
        new_position = move_agent(m, current_position, target)
        x,y = current_position 
        nx,ny = new_position
        m[x][y] = "-"
        m[nx][ny] = "S"
        etap+=1
        print(etap)
        display_grid(m)
        if(current_position == new_position ):
            print("agent bloquer")
        current_position = new_position
        #print("Current position:", current_position)
    print("Target reached!")

""" 
def dynamic_move (m):
    file = []
    visited = []
    start = (0, 0)
    target = (size-1, size-1) 
    file.append(start)
    while file:
        x = file.pop(0)
        visited.append(x)
        if x == target:
            print("Target reached!")
        new_position = move_agent(m, x, target)
        if new_position not in visited and new_position not in file:
            file.append(new_position)
"""
#recherche en profondeur
def bfs(m,start, target):
    size = len(m)
    #File FiFO 
    queue = deque([start])
    #Etat visite 
    visited = set()
    visited.add(start)
    #construire le chemin
    permut = {}
    #directions possibles
    d = [(0,1), (0,-1), (1,0), (-1,0)]
    while queue:
        current = queue.popleft()
        if current == target:
            print("Path:", cont_path(permut, start, target))
            return cont_path(permut, start, target)
        x,y = current
        for dx, dy in d:
            nx,ny = x+dx, y+dy
            #verifier les limites de la grille
            if 0 <= nx < size and 0 <= ny < size and m[nx][ny] != "O" and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                permut[(nx, ny)] = current
    return None

#on remplace le file par pile  par un fct
def cont_path(permut, start, target):
    path = []
    current = target
    while current != start:
        path.append(current)
        current = permut[current]
    path.append(start)
    path.reverse()
    return path
    

m = create_grid(size)
display_grid(m)
#dynamic_move(m)
simulation(m)
bfs(m,(0,0), (size-1, size-1))


