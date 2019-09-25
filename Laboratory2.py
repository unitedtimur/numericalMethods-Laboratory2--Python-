import numpy
import matplotlib.pyplot as plt

def Atkins(xMain, yMain, x, indexes):
    if len(indexes) == 1:
        return yMain[indexes[0]]
    else:
        xTail = xMain[indexes[-1]]
        xHead = xMain[indexes[0]]
        value = (Atkins(xMain, yMain, x, indexes[:-1]) * (xTail - x) - Atkins(xMain, yMain, x, indexes[1:]) * (xHead - x)) / (xTail - xHead)
        return value

#Original Function 
def originalFunc(x):
    return (numpy.sin(x) + 3 * numpy.cos(3 * x))

x = [0.000, 1.250, 2.350, 3.000, 5.500] 
y = [3.000, -1.513, 2.872, -2.592, -2.813]
pointX = 1.963

origX = numpy.linspace(numpy.min(x), numpy.max(x), 1000)
origY = [Atkins(x, y, i, [j for j in range(len(x))]) for i in numpy.linspace(numpy.min(x), numpy.max(x), 1000)]

#Print Atkins
plt.plot(x, y, 'o', origX, origY, color = 'green')

origY = [originalFunc(x) for x in numpy.linspace(numpy.min(x), numpy.max(x), 1000)]

#Print original function
plt.plot(origX, origY, color = 'red')

#Print point 'x'
plt.scatter(pointX, Atkins(x, y, pointX, [j for j in range(len(x))]), marker = 'x', color = 'black')

plt.legend(['Points', 'Atkins function', 'Original function', 'Point X'])
plt.title("My laboratory work")
plt.xlabel("Axis X")
plt.ylabel("Axis Y")

plt.grid(True)
plt.show()