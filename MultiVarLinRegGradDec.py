data = []
data.append([1,3,7])
data.append([1,5,11])
data.append([1,7,15])


def CostFunction(thetaValues, data):
    calcy=[]
    tempsum=0;
    for i in range(0, len(data)):
        for j in range(0, len(thetaValues)):
            tempsum+= thetaValues[j]*data[i][j]
        calcy.append(tempsum)
        tempsum = 0
    for i in range(0, len(calcy)):
        tempsum+=(calcy[i]-data[i][len(data[0])-1])**2
    tempsum=tempsum/2/len(calcy)
    return tempsum

def updateThetas(thetaValues, data,alpha):
    calcy = []
    tempsum = 0;
    for i in range(0, len(data)):
        for j in range(0, len(thetaValues)):
            tempsum += thetaValues[j] * data[i][j]
        calcy.append(tempsum)
        tempsum = 0
    newTheta=[]
    for i in range(0, len(thetaValues)):
        tempAdjust=0;
        for j in range(0, len(data)):
            tempAdjust+=(calcy[j]-data[j][len(data[0])-1])*data[j][i]
        adjustedTheta=thetaValues[i]-tempAdjust*alpha/len(data)
        newTheta.append(adjustedTheta)
    return newTheta


thetav=[0,3]

for i in range(0,100000):
    thetav=updateThetas(thetav,data,0.05)

print(thetav)

print(CostFunction(thetav, data))


