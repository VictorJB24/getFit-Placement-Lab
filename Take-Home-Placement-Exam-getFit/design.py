"""
	Description: This program creates a sizable graphics display to help users
 			track the number of steps that they walk in a week by generating
 			a series of graphs based off of the number of steps they walked
 			during the week and their step goal for the week.

Author: Victor Joulin - Batejat
Date: Spring 2021
"""

from random import *
from graphics import *


# --------------------------------------------------------- #

def getUserData():
    """
    Purpose: To obtain the filename of type string and the step goal, width, and height of type int from user.
    Parameters:  None
    Returns: The filename of type string, and the positive int values for step goal, width, and height.
    """
    print("In getData()")
    filename = "week1.data"
    stepGoal = 10000
    width = 400
    height = 400
    return filename, stepGoal, width, height


# --------------------------------------------------------- #

def getWeekStepData(filename):
    """
    Purpose: To extract the user's weekly step data from the file they specified in getUserData().
    Parameters: The filename specified in getUserData()
    Returns: A list of floats representing the number of steps the
            user took on a certain day
    """
    print("In getWeekStepData()")
    weekStepData = [12345, 5671, 10975, 8909, 4655, 11412, 10402]
    return weekStepData


# --------------------------------------------------------- #

def calculateAverageAndTotal(stepList):
    """
    Purpose: To calculate the total and average number of steps the user did throughout the week.
    Parameters: A list of integers representing the number of steps the
                user took on a certain day
    Returns: One float representing  total steps the user took, and one
            int representing the average number of steps the user took
    """
    print("In calculateAverageAndTotal()")
    total = sum(stepList)
    avg = total / len(stepList)
    return total, int(avg)


# --------------------------------------------------------- #

def getTopPartHeight(height):
    """
    Purpose: To calculate the height of the top part of the graphic.
    Parameters: An integer representing the height the user previously inputted.
    Returns: A float representing the height of the top part of the graphic.
    """
    print("In getTopPartHeight()")
    topPartHeight = height * .1  # calculates the height to be ten percent of the total graphic height
    return topPartHeight


# --------------------------------------------------------- #

def calculateBarSize(stepsInWeekList, height, width):
    """
    Purpose: To calculate the width and heights of the bars
    Parameters: The list of steps the user took each day of the week, and the height and width the user
                previously inputted.
    Returns: A float representing the width of the bars, and a list of floats representing the heights
            of the bars.
    """
    print("In calculateBarSize()")
    barHeights = calculateBarHeight(stepsInWeekList, height)
    barWidth = width / 7  # calculating the pixels per day
    return barHeights, barWidth


# --------------------------------------------------------- #

def calculateBarHeight(stepsInWeekList, height):
    """
    Purpose: To calculate the height of all the bars.
    Parameters: The list of steps the user walked every day throughout a previously specified week, and
                the total height of the graphic the user previously inputted.
    Returns: A list of floats representing the heights of each bar.
    """
    print("In calculateBarHeight()")
    bottomPartHeight = height * .9  # calculates the height to be the remaining ninety percent of the graphic
    maxStepCount = max(stepsInWeekList)  # calculates the maximum amount of steps the user took in one day of the week
    pixelsPerStep = bottomPartHeight / maxStepCount  # calculates the amount of pixels per step
    barHeights = calculateHeightOfOneBar(stepsInWeekList, pixelsPerStep)
    return barHeights


# --------------------------------------------------------- #

def calculateHeightOfOneBar(stepsInWeekList, pixelsPerStep):
    """
    Purpose: To calculate the height of one bar of the graphic.
    Parameters:  The list of steps the user walked every day throughout a previously specified week, and
                a float representing the pixels per step that was previously calculated in
                calculateBarHeight().
    Returns: A list of floats representing the heights of each individual bar.
    """
    print("In calculateHeightOfOneBar")
    barHeights = []
    for stepsInOneDay in stepsInWeekList:
        heightOfOneBar = pixelsPerStep * stepsInOneDay  # calculating the height of each bar individually
        barHeights.append(heightOfOneBar)
    return barHeights


# --------------------------------------------------------- #

def calculateTextSize(width):
    """
    Purpose: To calculate the size of the text displayed on the graphic.
    Parameters: The width of the total graphic inputted by the user.
    Returns: A float representing the size of the text.
    """
    print("In calculateTextSize()")
    textSize = width * .1  # calculating text size as ten percent of total width
    return textSize


# --------------------------------------------------------- #

def generateGraphic(stepGoal, width, height, totalSteps, avgOfSteps, topPartHeight, heightsOfBars, widthOfBars,
                    textSize):
    """
    Purpose: To generate the final graphic.
    Parameters: The step goal, total steps, average of steps, width and height of the graphic, individual heights of
                each bar, widths of all the bars, the height of the top part of the graphic, and the
                text size.
    Returns: None
    """
    print("In generateGraphic()")
    graphicWindow = GraphWin("Get Fit!", width, height)  # creates new GraphWin object
    graphicWindow.setCoords(0, 0, graphicWindow.getWidth(), graphicWindow.getHeight())
    graphicWindow.setBackground("silver")
    createTopPartOfGraphic(graphicWindow)
    # createBottomPartOfGraphic()
    graphicWindow.getMouse()  # Pause to view result
    graphicWindow.close()
    return 1


# --------------------------------------------------------- #

def createTopPartOfGraphic(graphicWindow):
    """
    Purpose: To create the top part of the graphic.
    Parameters: The previously created instance of the GraphicWin object.
    Returns: The modified GraphicWin object.
    """
    print("In createTopPartOfGraphic()")
    roll = 1  # will use the random library to simulate a die roll
    return roll


# --------------------------------------------------------- #

def rollOne():
    """
    Purpose: Randomly roll one die.
    Parameters:  None
    Returns: An integer representing the die value between 1 and 6.
    """
    print("In rollOne()")
    roll = 1  # will use the random library to simulate a die roll
    return roll


# --------------------------------------------------------- #


def main():
    # get the filename, step goal, width of window, and height of window
    filename, stepGoal, width, height = getUserData()

    # get the user's weekly step data from the file specified in getUserData()
    stepsInWeekList = getWeekStepData(filename)

    # calculate the average and total number of steps
    totalSteps, avgOfSteps = calculateAverageAndTotal(stepsInWeekList)

    # calculate the size of the top part of the graphic
    topPartHeight = getTopPartHeight(int(height))

    # calculate the size of the bars
    heightsOfBars, widthOfBars = calculateBarSize(stepsInWeekList, int(height), int(width))
    print(f"Heights: {heightsOfBars}\nWidth: {widthOfBars}")

    # calculate the size of the text
    textSize = calculateTextSize(int(width))
    print("Text size:", textSize)

    # generate the graphic
    generateGraphic(stepGoal, width, height, totalSteps, avgOfSteps, topPartHeight, heightsOfBars, widthOfBars,
                    textSize)

    # compute probability of rolling five of a kind with six-sided dice, & display probability & average
    print("The average is: %f" % 1)
    print("The probability is: %f" % (1 / 2))


main()
