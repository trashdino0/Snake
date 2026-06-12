import pygame
import sys
import random
import turtle as trtl
import time

# Initialize Pygame
pygame.init()

# Constants
width, height = 600, 400
gridSize = 20
fps = 10

# Colors
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
black = 0, 0, 0

leaderboardFileName = "leaderboard.txt"
#getting player name
playerName = input("Please enter your name:")

#setting up the font and the turtle that will write the leaderboard
fontSetup = "Arial", 20, "normal"
lbWriterSize = 100
lbWriterColor = 'pink'
lbWriterShape = "turtle"

lbWriter = trtl.Turtle() 
lbWriter.shape(lbWriterShape)
lbWriter.shapesize(lbWriterSize)
lbWriter.fillcolor(lbWriterColor)

#setting up the score system
score = 0
printScore = 'Score:' + str(score)

# Create the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Snake variables
snakeSize = 20
snakeSpeed = gridSize
snake = [(100, 100), (90, 100), (80, 100)]
snakeDirection = (1, 0)

numFood = int(input("How many apples would you like? If you say a number out of range it will default to 1. 1-5:"))

# Function to create food objects
def createFood(num):
    return [(random.randrange(0, width, gridSize), random.randrange(0, height, gridSize)) for _ in range(num)]

# Initialize food
food = createFood(numFood)

#gets the names of the leaderboard
def getNames(fileName):
    with open(fileName, "r") as leaderboardFile:
        names = [line.split(",")[0] for line in leaderboardFile]
    print("names:", names)
    return names

#gets the scores of each leaderboard position
def getScores(fileName):
    with open(fileName, "r") as leaderboardFile:
        scores = [int(line.split(",")[1]) for line in leaderboardFile]
    print("scores:", scores)
    return scores

#updates the leaderboard by finding the correct position then adding the player name and score
def updateLeaderboard(fileName, leaderNames, leaderScores, playerName, playerScore):
    for index, score in enumerate(leaderScores):
        if playerScore >= score:
            break
    else:
        index += 1

    leaderNames.insert(index, playerName)
    leaderScores.insert(index, playerScore)

    if len(leaderNames) > 5:
        leaderNames.pop()
        leaderScores.pop()

    with open(fileName, "w") as leaderboardFile:
        for name, score in zip(leaderNames, leaderScores):
            leaderboardFile.write(f"{name},{score}\n")

# writes leaderboard and then says if you made the leaderboard or not
def drawLeaderboard(highScorer, leaderNames, leaderScores, leaderboardWriter, playerScore):
    fontSetup = "Arial", 20, "normal"
    leaderboardWriter.clear()
    leaderboardWriter.penup()
    leaderboardWriter.goto(-160, 100)
    leaderboardWriter.hideturtle()
    leaderboardWriter.down()

    for index, (name, score) in enumerate(zip(leaderNames, leaderScores)):
        leaderboardWriter.write(f"{index + 1}\t{name}\t{score}", font=fontSetup)
        leaderboardWriter.penup()
        leaderboardWriter.goto(-160, int(leaderboardWriter.ycor()) - 50)
        leaderboardWriter.down()

    leaderboardWriter.penup()
    leaderboardWriter.goto(-160, int(leaderboardWriter.ycor()) - 50)
    leaderboardWriter.pendown()

    if highScorer:
        leaderboardWriter.write("Congratulations!\nYou made the leaderboard!", font=fontSetup)
    else:
        leaderboardWriter.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=fontSetup)

def manageLeaderboard():
    global score
    global lbWriter

    leaderNamesList = getNames(leaderboardFileName)
    leaderScoresList = getScores(leaderboardFileName)

    if len(leaderScoresList) < 5 or score >= leaderScoresList[4]:
        updateLeaderboard(leaderboardFileName, leaderNamesList, leaderScoresList, playerName, score)
        drawLeaderboard(True, leaderNamesList, leaderScoresList, lbWriter, score)
    else:
        drawLeaderboard(False, leaderNamesList, leaderScoresList, lbWriter, score)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snakeDirection != (0, 1):
                snakeDirection = (0, -1)
            if event.key == pygame.K_DOWN and snakeDirection != (0, -1):
                snakeDirection = (0, 1)
            if event.key == pygame.K_LEFT and snakeDirection != (1, 0):
                snakeDirection = (-1, 0)
            if event.key == pygame.K_RIGHT and snakeDirection != (-1, 0):
                snakeDirection = (1, 0)

    # Move the snake
    newHead = ((snake[0][0] + snakeDirection[0] * snakeSpeed) % width, (snake[0][1] + snakeDirection[1] * snakeSpeed) % height)
    snake.insert(0, newHead)

    # Check for collisions with food
    if newHead in food:
        food.remove(newHead)
        food.append((random.randrange(0, width, gridSize), random.randrange(0, height, gridSize)))
        score += 1
        printScore = 'Score:' + str(score)
    else:
        snake.pop()

    # Check for collisions with the snake's body
    if newHead in snake[1:]:
        print("Game Over")
        running = False
        time.sleep(5)

    # Draw background and score
    if running:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(printScore), 1, black)
        textRect = text.get_rect()
        textRect.center = (width - 100, height - 50)
        screen.fill(white)
        screen.blit(text, textRect)
    else:
        manageLeaderboard()
        while True:
            finalScore = 'Final Score: ' + str(score)
            deathFont = pygame.font.Font('freesansbold.ttf', 32)
            deathText = deathFont.render('GAMEOVER', 1, red)
            deathTextRect = deathText.get_rect()
            deathTextRect.center = (width // 2, height // 2)
            scoreText = deathFont.render(finalScore, 1, black)
            scoreTextRect = scoreText.get_rect()
            scoreTextRect.center = (width // 2, height // 3)
            leaveText = deathFont.render('To leave press x', 1, black)
            leaveTextRect = leaveText.get_rect()
            leaveTextRect.center = (width // 2, height // 4)
            screen.fill(white)
            screen.blit(deathText, deathTextRect)
            screen.blit(scoreText, scoreTextRect)
            screen.blit(leaveText, leaveTextRect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

    # Draw food
    for f in food:
        pygame.draw.rect(screen, red, (f[0], f[1], gridSize, gridSize))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], snakeSize, snakeSize))

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(fps)

wn = trtl.Screen()
wn.bgcolor("white")
wn.mainloop()