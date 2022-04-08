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
    stepGoal = 7000
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
    daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return weekStepData, daysOfWeek


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
    print("In calculateHeightOfOneBar()")
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
    textSize = int(width * .02)  # calculating text size as five percent of total width
    if textSize > 36:  # making sure size is between legal constraints
        textSize = 36
    if textSize < 5:
        textSize = 5
    return textSize


# --------------------------------------------------------- #

def generateGraphic(stepGoal, width, height, topPartHeight, heightsOfBars, widthOfBars,
                    textSize, stepsInWeekList, daysOfWeek):
    """
    Purpose: To generate the final graphic.
    Parameters: The step goal, width and height of the graphic, individual heights of
                each bar, widths of all the bars, the height of the top part of the graphic, the
                text size, the list of steps the user walked throughout a given week, and the
                names of the days of the week.
    Returns: None
    """
    print("In generateGraphic()")
    graphicWindow = GraphWin("Get Fit!", width, height)  # creates new GraphWin object
    graphicWindow.setCoords(0, 0, graphicWindow.getWidth(), graphicWindow.getHeight())
    graphicWindow.setBackground("silver")
    graphicWindow, totalSteps = createTopPartOfGraphic(graphicWindow, stepsInWeekList, stepGoal, textSize)
    createBottomPartOfGraphic(graphicWindow, daysOfWeek, heightsOfBars, widthOfBars, stepGoal,
                              stepsInWeekList, height, width)
    graphicWindow.getMouse()  # Pause to view result
    graphicWindow.close()


# --------------------------------------------------------- #

def createTopPartOfGraphic(graphicWindow, stepsInWeekList, stepGoal, textSize):
    """
    Purpose: To create the top part of the graphic.
    Parameters: The previously created instance of the GraphicWin object, the list of steps the
                user walked throughout a given week, the step goal, and the text size.
    Returns: The modified GraphicWin object.
    """
    print("In createTopPartOfGraphic()")
    topLeftCoordinate = Point(0, graphicWindow.getHeight())
    rightSideCoordinate = Point(graphicWindow.getWidth(), graphicWindow.getHeight() * .9)
    topPartRectangle = Rectangle(topLeftCoordinate, rightSideCoordinate)
    topPartRectangle.draw(graphicWindow)
    topPartRectangle.setFill("white")
    topPartRectangle.setOutline("white")
    graphicWindow, totalSteps = setTopPartText(graphicWindow, stepsInWeekList, stepGoal, textSize)
    return graphicWindow, totalSteps


# --------------------------------------------------------- #

def setTopPartText(graphicWindow, stepsInWeekList, stepGoal, textSize):
    """
    Purpose: To set the text for the top part of the graphic.
    Parameters: The previously created GraphicWin object, list of steps the user
                walked throughout a given week, the step goal, and the text size.
    Returns: The new GraphicWin object, and the total steps the person took.
    """
    print("In setTopPartText()")
    totalSteps, avgOfSteps = calculateAverageAndTotal(stepsInWeekList)
    stepGoalLabel = Text(Point(graphicWindow.getWidth() * 1 / 4, graphicWindow.getHeight() * .95),
                         'Daily goal: ' + str(stepGoal))
    averageLabel = Text(Point(graphicWindow.getWidth() * 1 / 2, graphicWindow.getHeight() * .95),
                        'Average: ' + str(avgOfSteps))
    totalLabel = Text(Point(graphicWindow.getWidth() * 3 / 4, graphicWindow.getHeight() * .95),
                      'Total steps: ' + str(totalSteps))
    stepGoalLabel.draw(graphicWindow).setSize(textSize)
    averageLabel.draw(graphicWindow).setSize(textSize)
    totalLabel.draw(graphicWindow).setSize(textSize)
    return graphicWindow, totalSteps


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

def createBottomPartOfGraphic(graphicWindow, daysOfWeek, heightsOfBars, widthOfBars, stepGoal,
                              stepsInWeekList, height, width):
    """
    Purpose: To create the bottom part of the graphic.
    Parameters: The previously created GraphicWin object, a list containing the days of the week, the
                list with the heights of the bars, the width of the bars, the step goal previously
                inputted by the user, the list with the number of steps the user took throughout
                the week, the height of the graphic, and the width of the graphic.
    Returns: None
    """
    print("In createBottomPartOfGraphic()")
    generateBars(heightsOfBars, graphicWindow, widthOfBars, stepGoal, stepsInWeekList, height, width,
                 daysOfWeek)


# --------------------------------------------------------- #

def generateBars(heightsOfBars, graphicWindow, widthOfBars, stepGoal, stepsInWeekList, height, width, daysOfWeek):
    """
    Purpose: To generate the bars on the graphic.
    Parameters: The list with the heights of the bars, the previously created GraphicWin
                object, the width of the bars, the step goal, the list of steps the user took
                throughout the week, the height of the graphic, the width of the graphic, and the
                list of the days of the week.
    Returns: The new GraphicWin object.
    """
    print("In generateBars()")
    counter = 0
    for element in heightsOfBars:
        barUpperLeftCoord = Point(widthOfBars * counter, element)
        barLowerRightCoord = Point(widthOfBars * (counter + 1), 0)
        barRectangle = Rectangle(barUpperLeftCoord, barLowerRightCoord)
        barRectangle.draw(graphicWindow)
        graphicWindow = colorBars(graphicWindow, stepGoal, stepsInWeekList, barRectangle, element, height, width)
        graphicWindow = setBarText(graphicWindow, height, daysOfWeek, counter, widthOfBars, width)
        counter += 1
    return graphicWindow


# --------------------------------------------------------- #

def colorBars(graphicWindow, stepGoal, stepsInWeekList, barRectangle, heightOfBar, height, width):
    """
    Purpose: To color in the bars with the appropriate color.
    Parameters: The GraphicWin object, the step goal, the list of steps the user took throughout
                the week, the bar object, the height of the bar, the height of the graphic, and
                the width of the graphic.
    Returns: The new GraphicWin object.
    """
    print("In colorBars()")
    graphicWindow, goalLineHeight = generateGoalLine(graphicWindow, stepGoal, stepsInWeekList, height, width)
    if goalLineHeight > heightOfBar:
        barRectangle.setFill("red")
    else:
        barRectangle.setFill("green")
    return graphicWindow


# --------------------------------------------------------- #

def generateGoalLine(graphicWindow, stepGoal, stepsInWeekList, height, width):
    """
    Purpose: To generate the goal line representing the step goal previously inputted by the user.
    Parameters: The previously created GraphicWin object, the step goal, the list of steps the user
                took throughout the week, the height of the graphic, and the width of the graphic.
    Returns: The new GraphicWin object.
    """
    print("In generateGoalLine()")
    pixelsPerStep = height * .9 / max(stepsInWeekList)  # calculates the pixels per step
    heightOfGoalLine = pixelsPerStep * stepGoal  # calculates height of goal line
    goalLine = Line(Point(0, heightOfGoalLine), Point(width, heightOfGoalLine))
    goalLine.draw(graphicWindow)
    return graphicWindow, heightOfGoalLine


# --------------------------------------------------------- #

def setBarText(graphicWindow, height, daysOfWeek, counter, widthOfBars, width):
    """
    Purpose: To set the text of each bar with the correct day.
    Parameters: The GraphicWin object, the height of the graphic, the list of the days of the week,
                the previously used iteration counter, the width of the bars, and the width of the graphic.
    Returns: The new GraphicWin object.
    """
    print("In setBarText()")
    dayOfWeekLabel = Text(Point((counter * widthOfBars) + (widthOfBars * .5), height * .1), daysOfWeek[counter])
    dayOfWeekLabel.draw(graphicWindow).setSize(calculateTextSize(width))
    return graphicWindow


# --------------------------------------------------------- #

def main():
    # get the filename, step goal, width of window, and height of window
    filename, stepGoal, width, height = getUserData()

    # get the user's weekly step data from the file specified in getUserData()
    stepsInWeekList, daysOfWeek = getWeekStepData(filename)

    # calculate the size of the top part of the graphic
    topPartHeight = getTopPartHeight(int(height))

    # calculate the size of the bars
    heightsOfBars, widthOfBars = calculateBarSize(stepsInWeekList, int(height), int(width))

    # calculate the size of the text
    textSize = calculateTextSize(int(width))

    # generate the graphic
    generateGraphic(stepGoal, width, height, topPartHeight, heightsOfBars, widthOfBars,
                    textSize, stepsInWeekList, daysOfWeek)


main()
