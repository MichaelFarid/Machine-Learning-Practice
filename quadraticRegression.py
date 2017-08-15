data=[]
data.append([0,1])
data.append([1,2])
data.append([2,5])
data.append([3,10])

def updateTheta(thetaValues, data, alpha):
    calcY=[]
    for i in range(0, len(data)):
        calcY.append(thetaValues[0]*data[i][0]*data[i][0]+thetaValues[1]*data[i][0]+thetaValues[2])
    newTheta=[]
    for i in range(len(thetaValues)):
        tempsum=0
        for j in range(0, len(data)):
            tempsum+=(calcY[j]-data[j][1])*(data[j][0]**(2-i))
        newTheta.append(thetaValues[i]-alpha*tempsum/len(data))
    return newTheta

def CostFunction(thetaValues, data):
    calcY=[]
    for i in range(0, len(data)):
        calcY.append(thetaValues[0]*data[i][0]*data[i][0]+thetaValues[1]*data[i][0]+thetaValues[2])
    error=0
    for i in range(0, len(calcY)):
        error+=(calcY[i]-data[i][len(data[0])-1])**2
    error=error/2/len(calcY)
    return error

thetas=[4,1,3]

for i in range(0,10000):
    thetas=updateTheta(thetas,data, 0.05)

for i in thetas:
    print(round(i), end=" ")

print()

print(CostFunction(thetas,data))


