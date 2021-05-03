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

def calculateBarSize():
    """
    Purpose: Calculate the width and heights of the bars
    Parameters: The list of steps the user took each day of the week, and the height and width the user
                previously inputted.
    Returns: A float representing the width of the bars, and a list of floats representing the heights
            of the bars.
    """
    print("In calculateBarSize()")
    height = calculateHeight()
    return numRolls


# --------------------------------------------------------- #

def calculateBarHeight(n):
    """
    Purpose: Randomly roll n dice.
    Parameters:  An integer n representing the number of dice to roll.
    Returns: A list containing the dice rolls of length n.
    """
    print("In rollDice()")
    roll = rollOne()  # will call rollOne() n times
    diceRolls = [1] * n
    return diceRolls


# --------------------------------------------------------- #

def allSame(L):
    """
    Purpose: Checks whether the values in a list are equal.
    Parameters:  A list of values.
    Returns: True if all the values in the list are the same.
                     Otherwise False.
    """
    print("In allSame()")
    ITEMS_EQUAL = True
    return ITEMS_EQUAL


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
    total, avg = calculateAverageAndTotal(stepsInWeekList)

    # calculate the size of the top part of the graphic
    topPartHeight = getTopPartHeight()

    # calculate the size of the bars
    heights, width = calculateBarSize()
    # mywin = GraphWin("ponies!!", 600, 500)
    # mywin.setBackground("lightblue")
    # key = mywin.getKey()  # will pause here until key pressed in graph win

    # run dice-roll simulations and compute the average number of rolls required to roll 5 of a kind
    # numTrials = getPositiveInteger("Enter number of simulations to run: ")
    # avg = simulate(numTrials)

    # compute probability of rolling five of a kind with six-sided dice, & display probability & average
    print("The average is: %f" % avg)
    print("The probability is: %f" % (1 / avg))


main()
