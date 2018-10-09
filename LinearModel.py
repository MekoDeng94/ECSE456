import random
import matplotlib.pyplot as plt
import numpy as np
import csv

# Return one row of the X matrix (VanderMonde Matrix)
def getExponents(x, degree):

    myList = []

    for i in range(degree):
        myList.insert(i, x**i)

    return myList

# Return complete VanderMondeMatrix
def getVanderMondeMatrix(xData, degree):
    xMatrix = []
    for x in xData:
        xMatrix.append(getExponents(x, degree))

    return xMatrix

# Returns the parameter matrix 
def getParameterMatrix(xData, yData, degree):
        
    # Create VanderMondeMatrix
    xMatrix = np.array(getVanderMondeMatrix(xData, degree))

    # Take its transpose
    xT = np.matrix.transpose(xMatrix)
   
    # Multiply by the VanderMondeMatrix
    xTX = np.matmul(xT, xMatrix)

    # Take the inverse
    inv = np.linalg.inv(xTX)

    # Mutliply by the transpose
    invAndXt = np.matmul(inv, xT)

    # Multiply by the y Matrix to get the parameter vector
    parameters = np.matmul(invAndXt, yData)

    return parameters

# Reads the data from csv file and return two lists: x and y data
def getData(fileName):
    with open(fileName) as csvfile:
        xData = []
        yData = []
        for x, y in csv.reader(csvfile, delimiter= ','):
            xData.append(float(x))
            yData.append(float(y))
    
    return xData, yData

# Print the function's equation
def printEquation(parameters):
    equation = "f(x) = " 
    i = 0
    
    for p in parameters:
        temp = str(p)
        equation += "%sx^%s + " % (temp,i)
        i += 1

    print(equation[:-2])

# This method will apply f(x) on each x values
def myFunction(xValues, parameters):

    yValues = []

    for x in xValues:   
        y = 0
        i = 0

        for p in parameters:
            y += p*(x**i)
            i += 1

        yValues.append(y)

    return yValues

# Returns the mean square error between the 
# data provided and the experimental function
def getMSE(xFileData, yFileData, parameters):
    
    sum = 0

    # Get experimental y values
    yValues = myFunction(xFileData, parameters)
    
    # Calculate square error for each point
    for yData, yExp in zip(yFileData, yValues):
        sum += (yData - yExp)**2

    return sum/len(yFileData)

# This method will show the coordinate points contained 
# in the data file and plot f(x)
def plotPointsAndFunction(title, dataFileName, parameters):

    # Read values from file
    xFileData, yFileData = getData(dataFileName)
    xTestData, yTestData = getData('Data/AMD_Test_2.csv')

    # Get the mean square error
    mse = getMSE(xFileData, yFileData, parameters)

    # Get x values
    xValues = np.linspace(min(xFileData), max(xTestData), max(xFileData)-min(xFileData) + 1)

    # Get experimental y values
    yValues = myFunction(xValues, parameters)
    
    # Plot the function
    plt.plot(xValues, yValues)  
    plt.plot(xFileData, yFileData) 
    plt.scatter(xTestData, yTestData)

    plt.text(400, 10, "MSE = %s" % mse)
    plt.title(title)
    plt.show()

    # Zoom in the test points
    plt.plot(xValues, yValues)  
    plt.plot(xFileData, yFileData) 
    plt.scatter(xTestData, yTestData)
    plt.gca().set_xlim([1000,1260])
    plt.gca().set_ylim([5,16])
    plt.show()

def main():

    # Get the x and y train data
    trainFileName = 'Data/AMD_Train_2.csv'
    xTrainData, yTrainData = getData(trainFileName)
    
    # Get the parameters
    parameters = getParameterMatrix(xTrainData, np.matrix.transpose(np.array(yTrainData)), 9)

    # Plot training points
    plotPointsAndFunction('Polynomial Regression of Degree 9 Compared with Training Data', 'Data/AMD_Train_2.csv', parameters)

    # Print the equation found to the terminal
    printEquation(parameters)

main()