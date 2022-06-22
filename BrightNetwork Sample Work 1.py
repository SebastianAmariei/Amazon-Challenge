import random
#Variables
current = [0, 0] #Start from Here and current location
end = [9, 9] #Need to End Here
difference = [end[0]-current[0], end[1]-current[1]]

obstacles = [[9,7],[8,7],[7,7],[7,8]] #Obstacles

for i in range(100):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    obstacles.append([num1, num2])

table = []
moves =[]

def createTable():
    arr = []
    tempArr = []
    flag = True
    for i in range(10):
        for j in range(10):
            for k in range(4):
                if((i == obstacles[k][0]) & (j == obstacles[k][1])):
                    tempArr.append([i, j, "X"])
                    flag = False
                    
            if ((i == current[0]) & (j == current[1])):
                tempArr.append([i, j, "C"])
            
            elif ((i == end[0]) & (j == end[1])):
                tempArr.append([i, j,"E"])
                  
            else:
                if(flag == True):
                    tempArr.append([i, j])
                flag = True
                    
        arr.append(tempArr)
        tempArr=[]
    return arr

def checkX(): # checks if at border
    return (current[0] < 9) & (current[0] >= 0)

def checkY():
    return (current[1] < 9) & (current[1] >= 0)

def checkObstacle(x, y): # checks for obstacle down
    try:
        if (table[current[0]+x][current[1]+y][2] == "X"):
            return False
        else:
            return True
    except:
        return True
    

def makeMove():
    if((checkX()) & (checkY() & checkObstacle(1,1))):
        tempCurrent = addCord("DownRight")
    elif (checkY() & checkObstacle(0,1)):
        tempCurrent = addCord("Down")
    elif (checkX() & checkObstacle(1,0)):
        tempCurrent = addCord("Right")
    else:
        tempCurrent = current
    return tempCurrent


def addCord(Move): #movesin specified direction
    if (Move == "Down"):
        move = [current[0], current[1]+1]
    elif (Move == "Right"):
        move = [current[0]+1, current[1]]
    elif (Move == "Up"):
        move = [current[0], current[1]-1]
    elif (Move == "Left"):
        move = [current[0]-1, current[1]]
    elif(Move == "DownRight"):
        move = [current[0]+1, current[1]+1]
    elif(Move == "DownLeft"):
        move = [current[0]+1, current[1]-1]
    elif(Move == "UpRight"):
        move = [current[0]-1, current[1]+1]
    elif(Move == "UpLeft"):
        move = [current[0]-1, current[1]-1]
        
    return move
    
count = 0
while(current != end):
    moves.append("(" + str(current[0]) + "," + str(current[1]) + ")")
    table = createTable()
    
    if (current == makeMove()):
        count = count + 1
        
    current = makeMove()

    if(count == 3):
        print("Unable To Reach")
        break
    #for i in range(10):
        #print(table[i])

print(moves + end)
print(difference)
