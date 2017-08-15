def CostFunction(theta0, theta1, points):
    calcPoints = []
    mseError = 0;
    for i in range(0, len(points)):
        calcPoints.append([points[i][0], points[i][0] * theta1 + theta0])
        mseError = (calcPoints[i][1] - points[i][1]) ** 2
    mseError = 0.5 * mseError / len(points)
    return mseError


def updateThetaOne(theta0, theta1, points, alpha):
    calcPoints = []
    result = 0;
    for i in range(0, len(points)):
        calcPoints.append([points[i][0], (points[i][0] * theta1) + theta0])
        result = result + (((calcPoints[i][1] - points[i][1])) * points[i][0])
    result = result / len(points)
    return theta1 - alpha * result


def updateThetaZero(theta0, theta1, points, alpha):
    calcPoints = []
    result = 0;
    for i in range(0, len(points)):
        calcPoints.append([points[i][0], points[i][0] * theta1 + theta0])
        result = result + ((calcPoints[i][1] - points[i][1]))
    result = result / len(points)
    return theta0 - alpha * result


data = []
data.append([0.0, 0.0])
data.append([1.0, 1.0])
data.append([2.0, 2.0])
data.append([3.0, 3.0])
data.append([4.0, 4.0])
data.append([5.0, 5.0])
data.append([6.0, 6.0])


theta0 = 7
theta1 = 4
stop = False

while not stop:
    initError = CostFunction(theta0, theta1, data)
    temp1 = updateThetaOne(theta0, theta1, data, 0.1)
    temp0 = updateThetaZero(theta0, theta1, data, 0.1)
    theta1 = temp1
    theta0 = temp0
    error = CostFunction(theta0, theta1, data)
    if initError == error:
        stop = True

print("theta 0 is ", theta0)
print("theta 1 is ", theta1)
